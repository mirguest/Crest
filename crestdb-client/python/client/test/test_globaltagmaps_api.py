# coding: utf-8

"""
    CrestDB REST API

    Crest Rest Api to manage data for calibration files.

    OpenAPI spec version: 2.0
    Contact: andrea.formica@cern.ch
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import crestapi
from crestapi.rest import ApiException
from crestapi.apis.globaltagmaps_api import GlobaltagmapsApi


class TestGlobaltagmapsApi(unittest.TestCase):
    """ GlobaltagmapsApi unit test stubs """

    def setUp(self):
        self.api = crestapi.apis.globaltagmaps_api.GlobaltagmapsApi()

    def tearDown(self):
        pass

    def test_create_global_tag_map(self):
        """
        Test case for create_global_tag_map

        Create a GlobalTagMap in the database.
        """
        pass

    def test_find_global_tag_map(self):
        """
        Test case for find_global_tag_map

        Find GlobalTagMapDto lists.
        """
        pass


if __name__ == '__main__':
    unittest.main()
