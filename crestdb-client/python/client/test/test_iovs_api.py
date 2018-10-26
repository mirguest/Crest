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
from crestapi.apis.iovs_api import IovsApi


class TestIovsApi(unittest.TestCase):
    """ IovsApi unit test stubs """

    def setUp(self):
        self.api = crestapi.apis.iovs_api.IovsApi()

    def tearDown(self):
        pass

    def test_create_iov(self):
        """
        Test case for create_iov

        Create a Iov in the database.
        """
        pass

    def test_find_all_iovs(self):
        """
        Test case for find_all_iovs

        Finds a IovDtos lists.
        """
        pass

    def test_get_size(self):
        """
        Test case for get_size

        Get the number o iovs for the given tag.
        """
        pass

    def test_get_size_by_tag(self):
        """
        Test case for get_size_by_tag

        Get the number o iovs for tags matching pattern.
        """
        pass

    def test_select_groups(self):
        """
        Test case for select_groups

        Select groups for a given tagname.
        """
        pass

    def test_select_iovs(self):
        """
        Test case for select_iovs

        Select iovs for a given tagname and in a given range.
        """
        pass

    def test_select_snapshot(self):
        """
        Test case for select_snapshot

        Select snapshot for a given tagname and insertion time.
        """
        pass


if __name__ == '__main__':
    unittest.main()