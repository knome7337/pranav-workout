const CACHE = 'workout-v1';
const URLS = [
  '.',
  'index.html',
  'img/bench-press.png',
  'img/seated-row.png',
  'img/shoulder-press.png',
  'img/plank.png',
  'img/dead-bug.png',
  'img/squat.png',
  'img/deadlift.png',
  'img/glute-bridge.png',
  'img/thoracic-rotation.png'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(URLS)));
  self.skipWaiting();
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request))
  );
});
