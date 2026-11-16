const form = document.querySelector('#search');
const query = document.querySelector('#query');
const section = document.querySelector('#section');
const status = document.querySelector('#status');
const results = document.querySelector('#results');
const more = document.querySelector('#more');
const pageSize = 12;
let engine;
let currentSearch;

function loadEngine() {
  return import('/pagefind/pagefind.js');
}

function resultItem(result) {
  const item = document.createElement('li');
  const heading = document.createElement('h2');
  const link = document.createElement('a');
  const category = document.createElement('small');
  const excerpt = document.createElement('p');
  link.href = result.url;
  link.textContent = result.meta.title || 'Read article';
  heading.append(link);
  category.textContent = result.filters?.section?.[0] || '';
  // Pagefind escapes excerpt text and inserts only its own highlight markup.
  excerpt.innerHTML = result.excerpt;
  item.append(heading, category, excerpt);
  return item;
}

async function showPage(search) {
  more.disabled = true;
  const batch = search.matches.slice(search.shown, search.shown + pageSize);
  const articles = await Promise.all(batch.map(match => match.data()));
  if (search !== currentSearch) return;
  results.append(...articles.map(resultItem));
  search.shown += articles.length;
  const total = search.matches.length;
  status.textContent = total
    ? `Showing ${search.shown} of ${total} ${total === 1 ? 'article' : 'articles'}.`
    : 'No articles matched. Try a different search term or section.';
  more.hidden = search.shown >= total;
  more.disabled = false;
}

async function searchArticles() {
  const term = query.value.trim();
  const search = { matches: [], shown: 0 };
  currentSearch = search;
  more.hidden = true;
  results.replaceChildren();
  if (!term) {
    status.textContent = '';
    return;
  }
  status.textContent = 'Searching…';
  try {
    engine ??= loadEngine();
    const pagefind = await engine;
    if (search !== currentSearch) return;
    const options = section.value ? { filters: { section: section.value } } : {};
    const response = await pagefind.search(term, options);
    if (search !== currentSearch) return;
    search.matches = response.results;
    await showPage(search);
  } catch {
    engine = undefined;
    if (search === currentSearch) status.textContent = 'Search is temporarily unavailable. Please try again.';
  }
}

form.addEventListener('submit', event => {
  event.preventDefault();
  searchArticles();
});
section.addEventListener('change', searchArticles);
more.addEventListener('click', async () => {
  const search = currentSearch;
  try {
    await showPage(search);
  } catch {
    if (search !== currentSearch) return;
    more.disabled = false;
    status.textContent = 'More results could not be loaded. Please try again.';
  }
});
