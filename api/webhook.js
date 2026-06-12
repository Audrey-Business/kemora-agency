// Vercel serverless function — Stripe webhook → Systeme.io contact + tag
// bodyParser must be disabled to verify the Stripe signature on the raw body.

import Stripe from 'stripe';

const BASE_URL = 'https://api.systeme.io/api';

// Tag slugs must match tags created manually in Systeme.io.
// Keys must match the product name exactly as set in Stripe.
const PRODUCTS = {
  'Kemora OS IA':  { tagSlug: 'achat-kemora-os-ia' },
  'Business OS IA': { tagSlug: 'achat-business-os-ia' },
  'CORE OS IA':    { tagSlug: 'achat-core-os-ia' },
  "L'Exécution":  { tagSlug: 'achat-execution' },
  'Le Cadre Mental': { tagSlug: 'achat-cadre-mental' },
};

export const config = { api: { bodyParser: false } };

async function getRawBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    req.on('data', (chunk) => chunks.push(chunk));
    req.on('end', () => resolve(Buffer.concat(chunks)));
    req.on('error', reject);
  });
}

async function getOrCreateContact(apiKey, email, firstName, lastName) {
  const fields = [{ slug: 'first_name', value: firstName || '' }];
  if (lastName) fields.push({ slug: 'surname', value: lastName });

  const createRes = await fetch(`${BASE_URL}/contacts`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-API-Key': apiKey },
    body: JSON.stringify({ email, fields }),
  });

  if (createRes.status === 201 || createRes.status === 200) {
    return await createRes.json();
  }

  if (createRes.status === 422) {
    const getRes = await fetch(`${BASE_URL}/contacts?email=${encodeURIComponent(email)}`, {
      method: 'GET',
      headers: { 'X-API-Key': apiKey },
    });
    if (!getRes.ok) {
      throw new Error(`Systeme.io GET contact failed: ${getRes.status} ${await getRes.text()}`);
    }
    const getData = await getRes.json();
    const contact = getData.items?.[0];
    if (!contact) throw new Error('Contact not found after 422');
    return contact;
  }

  throw new Error(`Systeme.io create contact failed: ${createRes.status} ${await createRes.text()}`);
}

async function applyTag(apiKey, contactId, tagSlug) {
  // Resolve slug → numeric tag id
  const listRes = await fetch(`${BASE_URL}/tags?name=${encodeURIComponent(tagSlug)}`, {
    method: 'GET',
    headers: { 'X-API-Key': apiKey },
  });
  if (!listRes.ok) {
    throw new Error(`Systeme.io tag lookup failed: ${listRes.status} ${await listRes.text()}`);
  }
  const listData = await listRes.json();
  const tag = listData.items?.find((t) => t.name === tagSlug);
  if (!tag) {
    throw new Error(`Tag "${tagSlug}" not found in Systeme.io — create it first.`);
  }

  const tagRes = await fetch(`${BASE_URL}/contacts/${contactId}/tags`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-API-Key': apiKey },
    body: JSON.stringify({ tagId: tag.id }),
  });
  if (tagRes.status !== 204 && tagRes.status !== 200) {
    throw new Error(`Systeme.io apply tag failed: ${tagRes.status} ${await tagRes.text()}`);
  }
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;
  const systemeKey   = process.env.SYSTEME_API_KEY;

  if (!webhookSecret || !systemeKey) {
    console.error('Missing STRIPE_WEBHOOK_SECRET or SYSTEME_API_KEY');
    return res.status(500).json({ error: 'Server configuration error' });
  }

  const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, { apiVersion: '2024-04-10' });

  let event;
  try {
    const rawBody = await getRawBody(req);
    const sig = req.headers['stripe-signature'];
    event = stripe.webhooks.constructEvent(rawBody, sig, webhookSecret);
  } catch (err) {
    console.error('Webhook signature verification failed:', err.message);
    return res.status(400).json({ error: `Webhook Error: ${err.message}` });
  }

  if (event.type !== 'checkout.session.completed') {
    return res.status(200).json({ received: true });
  }

  const session = event.data.object;
  const customerEmail = session.customer_details?.email;
  const firstName     = session.customer_details?.name?.split(' ')[0] ?? '';
  const lastName      = session.customer_details?.name?.split(' ').slice(1).join(' ') ?? '';

  if (!customerEmail) {
    console.error('No customer email in session:', session.id);
    return res.status(200).json({ received: true });
  }

  let lineItems;
  try {
    const expanded = await stripe.checkout.sessions.retrieve(session.id, {
      expand: ['line_items.data.price.product'],
    });
    lineItems = expanded.line_items?.data ?? [];
  } catch (err) {
    console.error('Failed to retrieve line items:', err.message);
    return res.status(500).json({ error: 'Failed to retrieve line items' });
  }

  // Create/retrieve the contact once, then apply one tag per product purchased.
  let contact;
  try {
    contact = await getOrCreateContact(systemeKey, customerEmail, firstName, lastName);
  } catch (err) {
    console.error('Failed to get/create Systeme.io contact:', err.message);
    return res.status(502).json({ error: 'Failed to sync contact to Systeme.io' });
  }

  const errors = [];

  for (const item of lineItems) {
    const productName = item.price?.product?.name ?? '';
    const product = PRODUCTS[productName];

    if (!product) {
      console.warn(`Unknown product: "${productName}" — skipping tag.`);
      continue;
    }

    try {
      await applyTag(systemeKey, contact.id, product.tagSlug);
      console.log(`Tag "${product.tagSlug}" applied to ${customerEmail} for "${productName}"`);
    } catch (err) {
      console.error(`Failed to apply tag for "${productName}":`, err.message);
      errors.push(productName);
    }
  }

  if (errors.length > 0) {
    return res.status(500).json({ error: 'Some tags failed to apply', products: errors });
  }

  return res.status(200).json({ received: true });
}
