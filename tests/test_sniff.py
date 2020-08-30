"""This module implements tests pertaining to the sniff module"""

import pytest

import sniffpy
from sniffpy.mimetype import parse_mime_type
from tests.resources import get_resource_test_list

class TestSniffing:
    mime_types = [
        'text/plain',
        'text/plain',
        'text/plain',
        'text/plain',
        'application/octet-stream']
    content = [
        b'\xfe\xffthis is a test string',
        b'\xff\xfethis is a test string',
        b'\xef\xbb\xbfthis is a test string',
        b'this is a string without binary data byte\x09',
        b'this is a string with binary data byte\x05'
    ]


    @pytest.mark.parametrize('mime, resource', list(zip(mime_types, content)))
    def test_sniff_mislabeled_binary(self, mime, resource):
        """Test sniff_mislabeled_binary using manually constructed
        test plain text and binary strings"""
        computed_type = sniffpy.sniff_mislabeled_binary(resource)
        actual_type = parse_mime_type(mime)
        assert computed_type == actual_type

    @pytest.mark.parametrize('expected_type, resource', get_resource_test_list(["sniff"]))
    def test_sniff(self, expected_type, resource):
        computed_type = sniffpy.sniff(resource)
        assert computed_type == expected_type

    @pytest.mark.parametrize('expected_type, resource', \
            get_resource_test_list(["sniff-mislabeled-html"]))
    def test_sniff_with_mislabeled_html(self, expected_type, resource):
        computed_type = sniffpy.sniff(resource, "text/html")
        assert computed_type == expected_type
