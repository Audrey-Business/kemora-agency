// Vercel serverless function — booking form proxy to Systeme.io
// Avoids CORS: browser POSTs here (same origin), this calls Systeme.io server-side.

const BASE_URL = 'https://api.systeme.io/api';
const TAG_ID   = 2049163; // "reservation-appel-kemora"

export default async function handler(req, res) {
  // Only accept POST
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const API_KEY = process.env.SYSTEME_API_KEY;
  if (!API_KEY) {
    console.error('SYSTEME_API_KEY is not set');
    return res.status(500).json({ error: 'Server configuration error' });
  }

  const { email, first_name, last_name, telephone, objectif, creneaux } = req.body || {};

  if (!email || !first_name) {
    return res.status(400).json({ error: 'email and first_name are required' });
  }

  // Systeme.io requires fields as an array of {slug, value} objects.
  const fields = [{ slug: 'first_name', value: first_name }];
  if (last_name) fields.push({ slug: 'surname', value: last_name });

  try {
    // Step 1: create (or update) the contact
    const createRes = await fetch(`${BASE_URL}/contacts`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': API_KEY,
      },
      body: JSON.stringify({ email, fields }),
    });

    // 201 = created, 200 = upsert, 422 = email déjà utilisé (contact existant)
    let contact;
    if (createRes.status === 201 || createRes.status === 200) {
      contact = await createRes.json();
    } else if (createRes.status === 422) {
      // Contact existant — on le récupère via GET par email
      const getRes = await fetch(`${BASE_URL}/contacts?email=${encodeURIComponent(email)}`, {
        method: 'GET',
        headers: { 'X-API-Key': API_KEY },
      });
      if (!getRes.ok) {
        console.error('Systeme.io get contact error:', getRes.status, await getRes.text());
        return res.status(502).json({ error: 'Failed to retrieve existing contact' });
      }
      const getData = await getRes.json();
      contact = getData.items?.[0];
      if (!contact) {
        return res.status(502).json({ error: 'Contact not found after 422' });
      }
    } else {
      const err = await createRes.text();
      console.error('Systeme.io create contact error:', createRes.status, err);
      return res.status(502).json({ error: 'Failed to create contact' });
    }

    // Step 2: attach the tag
    const tagRes = await fetch(`${BASE_URL}/contacts/${contact.id}/tags`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': API_KEY,
      },
      body: JSON.stringify({ tagId: TAG_ID }),
    });

    if (tagRes.status !== 204 && tagRes.status !== 200) {
      console.error('Systeme.io tag error:', tagRes.status, await tagRes.text());
    }

    // Log données supplémentaires
    if (telephone || objectif || creneaux) {
      console.log(`Réservation ${contact.id} — tél: ${telephone || 'N/A'} — objectif: ${objectif || 'N/A'} — créneaux: ${creneaux || 'N/A'}`);
    }

    return res.status(200).json({ success: true, id: contact.id });

  } catch (err) {
    console.error('Unexpected error in /api/book:', err);
    return res.status(500).json({ error: 'Internal server error' });
  }
}
