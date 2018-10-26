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
from crestapi.models.tag_summary_dto import TagSummaryDto


class TestTagSummaryDto(unittest.TestCase):
    """ TagSummaryDto unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTagSummaryDto(self):
        """
        Test TagSummaryDto
        """
        model = crestapi.models.tag_summary_dto.TagSummaryDto()


if __name__ == '__main__':
    unittest.main()