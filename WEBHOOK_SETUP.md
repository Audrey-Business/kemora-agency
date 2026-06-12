# Webhook Stripe — Guide de configuration

## Architecture

```
Stripe checkout.session.completed
        ↓
api/webhook.js (Vercel)
        ↓
Systeme.io — création/mise à jour du contact + tag produit
        ↓
Systeme.io Automation — envoi de l'email de livraison
```

---

## 1. Configurer Systeme.io

### Créer les tags produit

Dans **Systeme.io** → **Contacts** → **Tags** → **Nouveau tag**, créer les 5 tags suivants (noms exacts, respecter la casse) :

| Tag | Produit associé |
|---|---|
| `achat-kemora-os-ia` | Kemora OS IA |
| `achat-business-os-ia` | Business OS IA |
| `achat-core-os-ia` | CORE OS IA |
| `achat-execution` | L'Exécution |
| `achat-cadre-mental` | Le Cadre Mental |

### Créer les règles d'automatisation

Pour chaque produit, créer une automatisation :

1. **Systeme.io** → **Automatisations** → **Nouvelle règle**
2. **Déclencheur** : *Tag ajouté* → sélectionner le tag correspondant (ex. `achat-kemora-os-ia`)
3. **Action** : *Envoyer un email* → rédiger l'email de livraison avec le lien Google Drive
4. Activer la règle

Répéter pour chacun des 5 produits.

---

## 2. Configurer le webhook dans Stripe Dashboard

### Créer le webhook

1. [Stripe Dashboard](https://dashboard.stripe.com) → **Développeurs** → **Webhooks**
2. Cliquer **Ajouter un endpoint**
3. **URL de l'endpoint** :
   ```
   https://kemora-agency.vercel.app/api/webhook
   ```
4. **Événements à écouter** : sélectionner uniquement `checkout.session.completed`
5. Cliquer **Ajouter l'endpoint**

### Récupérer le Webhook Secret

1. Cliquer sur le webhook créé
2. Dans la section **Signing secret** → **Révéler**
3. Copier la valeur → format `whsec_xxxxxxxxxxxx`

### Vérifier les noms de produits Stripe

Les noms des produits dans Stripe doivent correspondre **exactement** à ceux définis dans `api/webhook.js` :

| Nom dans Stripe | Tag Systeme.io |
|---|---|
| `Kemora OS IA` | `achat-kemora-os-ia` |
| `Business OS IA` | `achat-business-os-ia` |
| `CORE OS IA` | `achat-core-os-ia` |
| `L'Exécution` | `achat-execution` |
| `Le Cadre Mental` | `achat-cadre-mental` |

Pour vérifier : **Stripe Dashboard** → **Catalogue** → **Produits** → colonne **Nom**.

---

## 3. Ajouter les variables d'environnement dans Vercel

1. [Vercel Dashboard](https://vercel.com) → projet **kemora-agency** → **Settings** → **Environment Variables**
2. Ajouter les trois variables suivantes (environnements : Production + Preview) :

| Nom | Valeur |
|---|---|
| `STRIPE_SECRET_KEY` | `sk_live_xxxxxxxxxxxx` |
| `STRIPE_WEBHOOK_SECRET` | `whsec_xxxxxxxxxxxx` |
| `SYSTEME_API_KEY` | *(déjà présente)* |

3. Cliquer **Save** pour chaque variable
4. **Redéployer** : onglet **Deployments** → **Redeploy** sur le dernier déploiement

---

## 4. Tester le webhook

### Test en production

1. Effectuer un achat test (carte Stripe `4242 4242 4242 4242` en mode test)
2. **Stripe Dashboard** → **Webhooks** → endpoint → onglet **Tentatives récentes** → vérifier statut `200`
3. **Systeme.io** → **Contacts** → chercher l'email → vérifier que le tag est bien appliqué
4. Vérifier la réception de l'email de livraison déclenché par l'automatisation

### Déboguer en cas d'erreur

| Code | Cause probable | Solution |
|---|---|---|
| `400` | Signature invalide | Vérifier `STRIPE_WEBHOOK_SECRET` ; le `bodyParser` est désactivé par défaut dans `webhook.js` |
| `502` | Echec Systeme.io | Vérifier `SYSTEME_API_KEY` dans Vercel |
| `500` | Tag introuvable | Le tag n'existe pas dans Systeme.io — le créer avec le nom exact |
| Email non reçu | Automatisation inactive | Vérifier que la règle Systeme.io est activée et que le déclencheur est bien "Tag ajouté" |

Logs détaillés : **Vercel Dashboard** → **Functions** → **Logs**

---

## Récapitulatif des variables d'environnement requises

```
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
SYSTEME_API_KEY=...         ← déjà présente dans Vercel
```
