(() => {
  const back = document.querySelector('.sr-reader-back');
  if (!back) return;

  back.addEventListener('click', event => {
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey ||
        history.length < 2 || !document.referrer) return;

    const previous = new URL(document.referrer);
    const current = new URL(location.href);
    const sites = new Set(['srinipresents.com', 'www.srinipresents.com',
      'health.srinipresents.com', 'bhakti.srinipresents.com']);
    const related = previous.origin === current.origin ||
      (sites.has(previous.hostname) && sites.has(current.hostname));
    if (!related || previous.origin + previous.pathname === current.origin + current.pathname) return;

    event.preventDefault();
    history.back();
  });
})();
