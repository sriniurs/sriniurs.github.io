import copy
import datetime as dt
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('publisher', Path(__file__).with_name('publish_due.py'))
pub = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pub)


class PublisherTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.page = ('<!doctype html><html><head><title>Keep</title></head><body>'
                     '<div class="page"><header class="hero">KEEP HERO</header>'
                     '<ul>\n<!-- KEEP COMMENT -->\n'
                     '<li class="story-card"><a href="/old/">Old</a></li>\n</ul>'
                     '<script id="theme-groups-js">keepScript()</script></div>'
                     '<script data-goatcounter="keep"></script></body></html>')
        (self.root / 'archive').mkdir()
        for name in ('index.html', 'archive/index.html'):
            (self.root / name).write_text(self.page, encoding='utf-8')
        self.queue = {'version': 1, 'time_zone': 'Asia/Kolkata', 'publish_time': '05:00',
                      'start_date': '2026-11-08', 'last_published_on': '2026-11-08', 'entries': []}
        for number, slug, date in ((2, 'first', '2026-11-09'), (3, 'second', '2026-11-10')):
            directory = self.root / slug
            directory.mkdir()
            (directory / 'index.html').write_text('<html>APPROVED ARTICLE</html>', encoding='utf-8')
            self.queue['entries'].append({
                'number': number, 'path': f'/{slug}/', 'url': f'https://sriniurs.github.io/{slug}/',
                'title': slug, 'not_before': date + 'T05:00:00+05:30', 'status': 'pending',
                'published_at': None,
                'card_html': f'<li class="story-card"><a href="/{slug}/">{slug}</a>'
                             '<span class="story-date">9 Nov 2026</span></li>'})

    def run_plan(self, time, queue=None):
        return pub.plan(self.root, queue or self.queue, dt.datetime.fromisoformat(time))

    def test_before_five(self):
        self.assertFalse(self.run_plan('2026-11-09T04:59:59+05:30')[0])

    def test_at_five_and_preserves_everything_outside_list(self):
        changes, _ = self.run_plan('2026-11-09T05:00:00+05:30')
        self.assertEqual(set(changes), {'index.html', 'archive/index.html', 'publishing-queue.json'})
        for name in ('index.html', 'archive/index.html'):
            actual = changes[name]
            self.assertEqual(actual.split('<ul>')[0], self.page.split('<ul>')[0])
            self.assertEqual(actual.split('</ul>')[1], self.page.split('</ul>')[1])
            self.assertIn('KEEP COMMENT', actual)
            self.assertIn('href="/old/"', actual)
            self.assertLess(actual.index('href="/first/"'), actual.index('href="/old/"'))
        self.assertEqual((self.root / 'first/index.html').read_text(), '<html>APPROVED ARTICLE</html>')

    def test_repeat_run_does_not_release_another_story(self):
        changes, _ = self.run_plan('2026-11-10T06:30:00+05:30')
        after = json.loads(changes['publishing-queue.json'])
        self.assertFalse(self.run_plan('2026-11-10T07:30:00+05:30', after)[0])
        self.assertEqual(after['entries'][1]['status'], 'pending')

    def test_record_also_prevents_duplicate_if_guard_is_stale(self):
        changes, _ = self.run_plan('2026-11-09T06:30:00+05:30')
        after = json.loads(changes['publishing-queue.json'])
        after['last_published_on'] = '2026-11-08'
        self.assertFalse(self.run_plan('2026-11-09T07:30:00+05:30', after)[0])

    def test_delayed_release_uses_today_and_only_one_entry(self):
        changes, _ = self.run_plan('2026-11-12T06:30:00+05:30')
        after = json.loads(changes['publishing-queue.json'])
        self.assertIn('12 Nov 2026', changes['index.html'])
        self.assertEqual(after['entries'][0]['status'], 'published')
        self.assertEqual(after['entries'][1]['status'], 'pending')
        self.assertEqual(self.queue['entries'][0]['status'], 'pending')

    def test_future_first_entry_is_not_skipped(self):
        self.queue['entries'][0]['not_before'] = '2026-11-13T05:00:00+05:30'
        self.assertFalse(self.run_plan('2026-11-12T06:30:00+05:30')[0])

    def test_empty_queue(self):
        self.queue['entries'] = []
        self.assertFalse(self.run_plan('2026-11-09T06:30:00+05:30')[0])

    def test_future_last_date_fails(self):
        self.queue['last_published_on'] = '2026-11-11'
        with self.assertRaises(ValueError):
            self.run_plan('2026-11-09T06:30:00+05:30')

    def test_missing_article_fails_before_writes(self):
        (self.root / 'first/index.html').unlink()
        with self.assertRaises(ValueError):
            self.run_plan('2026-11-09T06:30:00+05:30')
        self.assertEqual((self.root / 'index.html').read_text(), self.page)

    def test_duplicate_numbers_fail(self):
        self.queue['entries'][1]['number'] = 2
        with self.assertRaises(ValueError):
            self.run_plan('2026-11-09T06:30:00+05:30')

    def test_absolute_and_index_links_are_deduplicated(self):
        text = self.page.replace('<!-- KEEP COMMENT -->',
            '<li class="story-card"><a href="https://sriniurs.github.io/first/index.html">Duplicate</a></li>'
            '<li class="story-card"><a href="/first/">Duplicate 2</a></li>')
        for name in ('index.html', 'archive/index.html'):
            (self.root / name).write_text(text)
        changes, _ = self.run_plan('2026-11-09T06:30:00+05:30')
        self.assertEqual(changes['index.html'].count('href="/first/"'), 1)
        self.assertNotIn('Duplicate', changes['index.html'])

    def test_utc_clock_is_converted_to_ist(self):
        changes, _ = self.run_plan('2026-11-08T23:30:00+00:00')
        self.assertEqual(json.loads(changes['publishing-queue.json'])['last_published_on'], '2026-11-09')

    def test_bad_source_structure_fails(self):
        (self.root / 'archive/index.html').write_text('<html><body>No source list</body></html>')
        with self.assertRaises(ValueError):
            self.run_plan('2026-11-09T06:30:00+05:30')


if __name__ == '__main__':
    unittest.main()
