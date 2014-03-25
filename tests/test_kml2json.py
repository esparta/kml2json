#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_kml2json
----------------------------------

Tests for `kml2json` module.
"""

import unittest
from os import path, getcwd

from kml2json import KMLobject
from lxml.etree import _ElementTree

class TestKmlObject(unittest.TestCase):
    """Test the KML"""
    def setUp(self):
        self.kmlfile = path.join(getcwd(),"tests/ags.kml")
        self.kml = KMLobject(self.kmlfile)

    def tearDown(self):
        pass

    def test_kmloader(self):
        """Can we create the Kmlobject"""
        self.assertIsInstance(self.kml, KMLobject)

    def test_kmlobject_has_root(self):
        """ The KMLObject has a root """
        self.assertIsNotNone(self.kml.root)

if __name__ == '__main__':
    unittest.main()
