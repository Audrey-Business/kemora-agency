const CACHE_NAME = 'kemora-v1';
const ASSETS = [
  '/assets/images/Accueil.webp',
  '/assets/images/apropos.webp',
  '/assets/images/businessosia.webp',
  '/assets/images/contact.webp',
  '/assets/images/coreosia.webp',
  '/assets/images/faq.webp',
  '/assets/images/fondations.webp',
  '/assets/images/kemoraosia.webp',
  '/assets/images/le_cadremental.webp',
  '/assets/images/lexecution.webp',
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(c => c.addAll(ASSETS)).catch(() => {})
  );
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  const isAsset = /\.(webp|jpg|jpeg|png|gif|svg|woff2?|ico)$/.test(url.pathname);
  const isHTML = e.request.headers.get('accept')?.includes('text/html');

  if (isAsset) {
    e.respondWith(
      caches.match(e.request).then(cached => cached || fetch(e.request).then(res => {
        const clone = res.clone();
        caches.open(CACHE_NAME).then(c => c.put(e.request, clone));
        return res;
      }))
    );
  } else if (isHTML) {
    e.respondWith(
      fetch(e.request).catch(() =>
        caches.match(e.request).then(cached => cached || caches.match('/404.html'))
      )
    );
  }
});
