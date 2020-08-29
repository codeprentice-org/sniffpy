""" This module should implement tests pertaining the match module in the package"""
import os

import pytest

import sniffpy.match as match
from sniffpy.mimetype import parse_mime_type
from tests.resources import TEST_FILES_PATH, get_resource_test_list

def test_match_pattern():
    """Tests whether match_pattern implementation works"""
    ignore = b'\x01\x02'
    sequence = b'\x01\x02\xff'
    mask = b'\xdd'
    pattern = b'\xdd'
    true_value = match.match_pattern(
        resource=sequence,
        ignored=ignore,
        mask=mask,
        pattern=pattern
    )
    sequence = b'\x01\x00\x02\xff'
    false_value = match.match_pattern(
        resource=sequence,
        ignored=ignore,
        mask=mask,
        pattern=pattern
    )
    assert not false_value
    assert true_value


class TestImageMatching:
    """ Class to test pattern matching of image Mimetypes"""

    mime_types = ['image/gif', 'image/png', 'image/jpeg', 'undefined/undefined']
    content = [
        b'\x47\x49\x46\x38\x39\x61\x32\xa4\x90',
        b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x43',
        b'\xff\xd8\xff\x78\x98\x23\x32\xfa\x89',
        b'\xfa\xd8\xff\x78\x98\x23\x32\xfa\x89'
    ]

    @pytest.mark.parametrize('mime, resource', list(zip(mime_types, content)))
    def test_match_image_pattern(self, mime, resource):
        """ Tests the most importnat image MIMEs with simulated content"""
        computed_type = match.match_image_type_pattern(resource)
        actual_type = parse_mime_type(mime)
        assert computed_type == actual_type

    @pytest.mark.parametrize('expected_type, resource', get_resource_test_list(["image"]))
    def test_match_image_pattern_wfile(self, expected_type, resource):
        computed_type = match.match_image_type_pattern(resource)
        assert computed_type == expected_type

class TestAudioVideoMatching:

    def test_is_mp4_pattern(self):
        mp4_file_path = os.path.join(TEST_FILES_PATH, 'video/mp4.mp4')
        with open(mp4_file_path, 'rb') as f:
            resource = f.read()
            assert match.is_mp4_pattern(resource)

    def test_is_webm_pattern(self):
        webm_file_path = os.path.join(TEST_FILES_PATH, 'video/webm.webm')
        with open(webm_file_path, 'rb') as f:
            resource = f.read()
            assert match.is_webm_pattern(resource)

    @pytest.mark.parametrize('expected_type, resource', get_resource_test_list(["audio", "video"]))
    def test_match_video_audio_type_pattern(self, expected_type, resource):
        computed_type = match.match_video_audio_type_pattern(resource)
        assert computed_type == expected_type
