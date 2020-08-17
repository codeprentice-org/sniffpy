"""This module implements tests pertaining to the sniff module"""

import sniffpy
from sniffpy.mimetype import parse_mime_type
from tests.utils import mimetype_is_equal
import pytest


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
        """Test sniff_mislabeled_binary using manually constructed test plain text and binary strings"""
        computed_type = sniffpy.sniff_mislabeled_binary(resource)
        actual_type = parse_mime_type(mime)
        mimetype_is_equal(computed_type, actual_type)
