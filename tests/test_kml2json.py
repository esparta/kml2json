#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_kml2json
----------------------------------

Tests for `kml2json` module.
"""

import unittest
from os import path, getcwd

from kml2json import kml2json, kmlobject
from lxml.etree import _ElementTree

class TestKml2json(unittest.TestCase):

    def setUp(self):
        self.kmlfile = path.join(getcwd(),"tests/ags.kml")
        self.kml = kmlobject(self.kmlfile)

    def tearDown(self):
        pass

    def test_kmloader(self):
        self.assertIsInstance(self.kml, kmlobject)

    def test_kmlobject_has_root(self):
        self.assertIsNotNone(self.kml.root)

if __name__ == '__main__':
    unittest.main()
