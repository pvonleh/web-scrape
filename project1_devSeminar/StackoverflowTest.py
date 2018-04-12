from tkinter import *
import re
import sys
import lxml
import unittest
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulStoneSoup
from beautifulsouptest import SoupTest


#######################
# File: StackoverflowJobs.py
# Author: Prince D. Vonleh
# Date: Feburary 2018


class Display(Frame):
    ''' Demonstrate python interpreter output in Tkinter Text widget

type python expression in the entry, hit DoIt and see the results
in the text pane.'''

    def __init__(self, parent=0):
        Frame.__init__(self, parent)

        self.doIt = Button(self, text="Click to view jobs", command=self.write)
        self.doIt.pack()
        self.output = Text(self)
        self.output.pack()
        sys.stdout = self.write
        self.pack()

    def fileHandling(self, error):

        return self.output.insert(END, str(error))

    def stripLXMLTags(self, lxml):
        """
           Strip HTML tags from any string and transfrom special entities
        """

        text = lxml

        rules = [
            {r'br': u'\n'},
            {r'>\s+': u'>'},  # remove spaces after a tag opens or closes
            {r'\s+': u' '},  # replace consecutive spaces
            {r'\s*<br\s*/?>\s*': u'\n'},  # newline after a <br>
            {r'</(div)\s*>\s*': u'\n'},  # newline after </p> and </div> and <h1/>...
            {r'</(p|h\d)\s*>\s*': u'\n\n'},  # newline after </p> and </div> and <h1/>...
            {r'<head>.*<\s*(/head|body)[^>]*>': u''},  # remove <head> to </head>
            {r'<a\s+href="([^"]+)"[^>]*>.*</a>': r'\1'},  # show links instead of texts
            {r'[ \t]*<[^<]*?/?>': u''},  # remove remaining tags
            {r'^\s+': u''}  # remove spaces at the beginning
        ]

        for rule in rules:
            for (k, v) in rule.items():
                regex = re.compile(k)
                text = regex.sub(v, text)

        #  replace special strings
        special = {
            '&nbsp;': '', '&amp;': '', '&quot;': '"',
            '&lt;': '<', '&gt;': '>', '&rsquo;': '''''',
            '&amp;ldquo;': '', 'ldquo;': '', '&amp;': '',
            '&rdquo;': '', '&': ''
        }

        for (k, v) in special.items():
            text = text.replace(k, v)

        return self.output.insert(END, str(text))  # outputs job descripition and title without tags

    def write(self):
        try:
            request = requests.get(
                'https://stackoverflow.com/jobs/feed?l=Bridgewater%2c+MA%2c+United+States&u=Miles&d=50')
            soup = BeautifulSoup(request.text, "lxml")

            items = soup.find_all('item')
            for item in items:
                title = item.find('title').text
                description = item.find('description').text

                txt = (title + '\n' + description + '\n\n')
                self.stripLXMLTags(txt)

                SoupTest(description)

                # self.testText(title)

        except requests.ConnectionError as e:
            err = ('\nConnection Error!\n Make sure you have an internet connection.\n')
            self.fileHandling(err)
            self.fileHandling(str(e))
        except requests.Timeout as e:
            err = ('\nTimeout Error!\n')
            self.fileHandling(err)
            self.fileHandling(str(e))
        except requests.RequestException as e:
            err = ('\nGeneral Error\n')
            self.fileHandling(err)
            self.fileHandling(str(e))
        except KeyboardInterrupt:
            self.fileHandling('\nProgram has been closed!\n')


if __name__ == '__main__':
    Display().mainloop()