# -*- coding: utf-8 -*-
"""Unit tests for Beautiful Soup.

These tests make sure the Beautiful Soup works as it should. If you
find a bug in Beautiful Soup, the best way to express it is as a test
case like this that fails."""

import unittest
#from BeautifulSoup import *
from bs4 import BeautifulSoup, NavigableString,SoupStrainer
from bs4 import BeautifulStoneSoup
import re
from StackOverflow import Display


class SoupTest(unittest.TestCase):

    def assertSoupEquals(self, toParse, rep=None, c=BeautifulSoup):
        """Parse the given text and make sure its string rep is the other
        given text."""

        if rep == None:
            rep = toParse
        self.assertEqual(str(c(toParse)), rep)


class FollowThatTag(SoupTest):
    "Tests the various ways of fetching tags from a soup."

    def setUp(self):



        ml = Display.write(self)
        self.soup = BeautifulStoneSoup(ml)

    def testFindAllByName(self):
        matching = self.soup('https://stackoverflow.com/jobs/feed?l=Bridgewater%2c+MA%2c+United+States&u=Miles&d=50')
        self.assertEqual(len(matching), 2)
        self.assertEqual(matching[0].name, 'a')
        self.assertEqual(matching, self.soup.findAll('a'))
        self.assertEqual(matching, self.soup.findAll(SoupStrainer('a')))



    def testFindAllText(self):
        soup = BeautifulSoup("<html>\xbb</html>", "lxml")
        self.assertEqual(soup.findAll(text=re.compile('.*')),
                         [u'\xbb'])

    def testTextNavigation(self):
        soup = BeautifulSoup('<url>http://cdn.sstatic.net/Sites/stackoverflow/img/favicon.ico?v=4f32ecc8f43d</url><title>Small funded Boston start-up seeks Senior Python/Django Developer at Circulation (Boston, MA)</title>', "lxml")
        baz = soup.find(text='Small funded Boston start-up seeks Senior Python/Django Developer at Circulation (Boston, MA)')
        self.assertEquals(baz.findParent("url")['title'])




if __name__ == '__main__':
    unittest.main()
    #Display.main()