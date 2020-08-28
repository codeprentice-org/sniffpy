""" This module should implement tests pertaining the match module in the package"""
import os

import pytest

import sniffpy.match as match
from sniffpy.mimetype import parse_mime_type
from tests.utils import mimetype_is_equal


TEST_FILES_PATH = os.path.dirname(os.path.realpath(__file__))
TEST_FILES_PATH = os.path.join(TEST_FILES_PATH, 'test_files')



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
        mimetype_is_equal(computed_type, actual_type)

    def test_match_image_pattern_wfile(self):
        images_folder_path = os.path.join(TEST_FILES_PATH, 'images')
        images = os.listdir(images_folder_path)
        for image_name in images:
            image_name = os.path.join(images_folder_path, image_name)
            _, extension = os.path.splitext(image_name)
            expected_mime = parse_mime_type('image/' + extension[1:])
            with open(image_name, 'rb') as f:
                resource = f.read()
                computed_type = match.match_image_type_pattern(resource)
                mimetype_is_equal(computed_type, expected_mime)


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

    def test_audio_with_match_video_audio_type_pattern(self):
        audio_folder_path = os.path.join(TEST_FILES_PATH, 'audio')
        audios = os.listdir(audio_folder_path)
        for audio_name in audios:
            filename = os.path.join(audio_folder_path, audio_name)
            name, _ = os.path.splitext(audio_name)
            expected_mime = parse_mime_type('audio/' + name)
            with open(filename, 'rb') as f:
                resource = f.read()
                computed_type = match.match_video_audio_type_pattern(resource)
                mimetype_is_equal(computed_type, expected_mime)

    def test_video_with_match_video_audio_type_pattern(self):
        video_folder_path = os.path.join(TEST_FILES_PATH, 'video')
        videos = os.listdir(video_folder_path)
        for video_name in videos:
            filename = os.path.join(video_folder_path, video_name)
            name, _ = os.path.splitext(video_name)
            expected_mime = parse_mime_type('video/' + name)
            with open(filename, 'rb') as f:
                resource = f.read()
                computed_type = match.match_video_audio_type_pattern(resource)
                mimetype_is_equal(computed_type, expected_mime)
