#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

__author__ = 'Yuta Hayashibe' 
__version__ = ""
__copyright__ = ""
__license__ = "GPL v3"

import random
import unittest

import corrcha.tool.ssgnc

class Test(unittest.TestCase):
    def setUp(self):
        import corrcha.tool.setting
        BIN_PATH = corrcha.tool.setting.val['ssgnc']['bin']
        INDEX_PATH = corrcha.tool.setting.val['ssgnc']['index']
        self.ssgnc = corrcha.tool.ssgnc.Ssgnc(BIN_PATH, INDEX_PATH)
    
    def tearDown(self):
        pass

    def test_search(self):
        self.assertEqual(self.ssgnc.search("orange"), [['orange', 9640000]])
        self.assertEqual(self.ssgnc.search(u"orange tea"), [['orange', 'tea', 1570]])
        self.assertEqual(self.ssgnc.search("orange tea"), [['orange', 'tea', 1570]])
        self.assertEqual(self.ssgnc.search(u"orange tea"), [['orange', 'tea', 1570]])
        self.assertEqual(self.ssgnc.search("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"), [])
        self.assertEqual(self.ssgnc.search(u"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"), [])

        self.assertEqual(self.ssgnc.get_frequency("orange"), 9640000)
        self.assertEqual(self.ssgnc.get_frequency(u"orange"), 9640000)
        self.assertEqual(self.ssgnc.get_frequency("orange tea"), 1570)
        self.assertEqual(self.ssgnc.get_frequency(u"orange tea"), 1570)
        self.assertEqual(self.ssgnc.get_frequency("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"), 0)
        self.assertEqual(self.ssgnc.get_frequency(u"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"), 0)


if __name__ == '__main__':
    unittest.main()
