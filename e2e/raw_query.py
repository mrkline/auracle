#!/usr/bin/env python

import auracle_e2e_test
import json


class TestE2ERawQuery(auracle_e2e_test.TestCase):

    def testRawInfo(self):
        p = self.Auracle(['rawinfo', 'auracle-git'])
        self.assertEqual(p.returncode, 0)

        parsed = json.loads(p.stdout)
        self.assertEqual(parsed['resultcount'], 1)

        names = (r['Name'] for r in parsed['results'])
        self.assertIn('auracle-git', names)

        self.assertCountEqual(self.requests_made,
                ['/rpc?type=info&v=5&arg[]=auracle-git'])


    def testRawSearch(self):
        p = self.Auracle(['rawsearch', 'aura'])
        self.assertEqual(p.returncode, 0)

        parsed = json.loads(p.stdout)
        self.assertGreater(parsed['resultcount'], 1)

        names = (r['Name'] for r in parsed['results'])
        self.assertIn('auracle-git', names)

        self.assertCountEqual(self.requests_made,
                ['/rpc?by=name-desc&type=search&v=5&arg=aura'])


    def testRawSearchBy(self):
        p = self.Auracle(
                ['rawsearch', '--searchby=maintainer', 'falconindy'])
        self.assertEqual(p.returncode, 0)

        parsed = json.loads(p.stdout)
        self.assertGreaterEqual(parsed['resultcount'], 1)

        names = (r['Name'] for r in parsed['results'])
        self.assertIn('auracle-git', names)

        self.assertCountEqual(self.requests_made,
                ['/rpc?by=maintainer&type=search&v=5&arg=falconindy'])


if __name__ == '__main__':
    auracle_e2e_test.main()
