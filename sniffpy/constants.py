# This document contains all of the tables specified in https://mimesniff.spec.whatwg.org/
# Each table is implemented as an Array and a comment before each
# table indicates title of the table and meaning of each column.
# pylint: disable=line-too-long
from sniffpy.mimetype import MIMEType

# URLs
RSS_PURL_URL = b'http://purl.org/rss/1.0/'
RDF_SYNTAX_URL = b'http://www.w3.org/1999/02/22-rdf-syntax-ns#'

# Bytes that the specification defines as whitespace
WHITESPACE = b'\x09\x0a\x0c\x0d\x20'
UNDEFINED = MIMEType('undefined', 'undefined')

# Apache Bug Flag Table
# Bytes as Bytes | Bytes as String
APACHE_BUG_FLAG_PATTERNS = [
    [b'text/plain', 'text/plain'],
    [b'text/plain; charset=ISO-8859-1', 'text/plain; charset=ISO-8859-1'],
    [b'text/plain; charset=iso-8859-1', 'text/plain; charset=iso-8859-1'],
    [b'text/plain; charset=UTF-8', b'text/plain; charset=UTF-8']
]

# Archive Pattern Table
# Bytes | Pattern Mask | Leading Bytes to Be Ignored | MIMETYPE
ARCHIVE_PATTERNS = [[b'\x1f\x8b\x08',
                     b'\xff\xff\xff',
                     b'',
                     'application/x-gzip'],
                    [b'PK\x03\x04',
                     b'\xff\xff\xff\xff',
                     b'',
                     'application/zip'],
                    [b'\x52\x61\x72\x20\x1A\x07\x00',
                     b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF',
                     b'',
                     'application/x-rar-compressed']]

# Patterns for Audio and video
# Bytes as Bytes |  Pattern Mask |  Leading BYTES TO Be Igonred | MIMETYPE
AUDIO_VIDEO_PATTERNS = [
    [b'.snd', b'\xFF\xFF\xFF\xFF', b'', 'audio/basic'],
    [b'FORM\x00\x00\x00\x00AIFF', b'\xFF\xFF\xFF\xFF\x00\x00\x00\x00\xFF\xFF\xFF\xFF', b'', 'audio/aiff'],
    [b'ID3', b'\xFF\xFF\xFF', b'', 'audio/mpeg'],
    [b'OggS\x00', b'\xFF\xFF\xFF\xFF\xFF', b'', 'application/ogg'],
    [b'MThd\x00\x00\x00\x06', b'\xff\xff\xff\xff\xff\xff\xff\xff', b'', 'audio/midi'],
    [b'RIFF\x00\x00\x00\x00AVI ', b'\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff', b'', 'video/avi'],
    [b'RIFF\x00\x00\x00\x00WAVE', b'\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff', b'', 'audio/wave']
    ]

# Patterns for Images
# Bytes as Bytes | Pattern Mask |  Leading BYTES TO Be Igonred | MIMETYPE
IMAGE_PATTERNS = [
    [b'\x00\x00\x01\x00', b'\xff\xff\xff\xff', b'', 'image/x-icon'],
    [b'\x00\x00\x02\x00', b'\xff\xff\xff\xff', b'', 'image/x-icon'],
    [b'BM', b'\xff\xff', b'', 'image/gif'],
    [b'GIF87a', b'\xff\xff\xff\xff\xff\xff', b'', 'image/gif'],
    [b'GIF89a', b'\xff\xff\xff\xff\xff\xff', b'', 'image/gif'],
    [b'RIFF\x00\x00\x00\x00WEBPVP', b'\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff', b'', 'image/webp'],
    [b'\x89PNG\x0d\x0a\x1a\x0a', b'\xff\xff\xff\xff\xff\xff\xff\xff', b'', 'image/png'],
    [b'\xff\xd8\xff', b'\xff\xff\xff', b'', 'image/jpeg']
]

# Patterns for Fonts
# Bytes as Bytes | Pattern Mask |  Leading BYTES TO Be Igonred | MIMETYPE
FONT_PATTERNS = [
    [b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' +
     b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00LP',
     b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' +
     b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff',
     b'', 'application/vnd.ms-fontobject'],
    [b'\x00\x01\x00\x00', b'\xff\xff\xff\xff', b'', 'font/ttf'],
    [b'OTTO', b'\xff\xff\xff\xff', b'', 'font/otf'],
    [b'ttcf', b'\xff\xff\xff\xff', b'', 'font/collection'],
    [b'wOFF', b'\xff\xff\xff\xff', b'', 'font/woff'],
    [b'wOF2', b'\xff\xff\xff\xff', b'', 'font/woff2']
]

# Patterns corresponding to first table in section 7.1 of specification
# Bytes as Bytes | Pattern Mask | Leading Bytest To Be  Igonred | MIMETYPE
UNKNOWN_PATTERNS = [
    [b'<!DOCTYPE HTML ', b'\xff\xff\xdf\xdf\xdf\xdf\xdf\xdf\xdf\xff\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<!DOCTYPE HTML>', b'\xff\xff\xdf\xdf\xdf\xdf\xdf\xdf\xdf\xff\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<HTML ', b'\xff\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<HTML>', b'\xff\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<HEAD ', b'\xff\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<HEAD>', b'\xff\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<SCRIPT ', b'\xff\xdf\xdf\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<SCRIPT>', b'\xff\xdf\xdf\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<IFRAME ', b'\xff\xdf\xdf\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<IFRAME>', b'\xff\xdf\xdf\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<H1 ', b'\xff\xdf\xff\xff', WHITESPACE, 'text/html'],
    [b'<H1>', b'\xff\xdf\xff\xff', WHITESPACE, 'text/html'],
    [b'<DIV ', b'\xff\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<DIV>', b'\xff\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<FONT ', b'\xff\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<FONT>', b'\xff\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<TABLE ', b'\xff\xdf\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<TABLE>', b'\xff\xdf\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<A ', b'\xff\xdf\xff', WHITESPACE, 'text/html'],
    [b'<A>', b'\xff\xdf\xff', WHITESPACE, 'text/html'],
    [b'<STYLE ', b'\xff\xdf\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<STYLE>', b'\xff\xdf\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<TITLE ', b'\xff\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<TITLE>', b'\xff\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<B ', b'\xff\xdf\xff', WHITESPACE, 'text/html'],
    [b'<B>', b'\xff\xdf\xff', WHITESPACE, 'text/html'],
    [b'<BODY ', b'\xff\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<BODY>', b'\xff\xdf\xdf\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<BR ', b'\xff\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<BR>', b'\xff\xdf\xdf\xff', WHITESPACE, 'text/html'],
    [b'<P ', b'\xff\xdf\xff\xff', WHITESPACE, 'text/html'],
    [b'<P>', b'\xff\xdf\xff\xff', WHITESPACE, 'text/html'],
    [b'<!-- ', b'\xff\xff\xff\xff\xff', WHITESPACE, 'text/html'],
    [b'<!-->', b'\xff\xff\xff\xff\xff', WHITESPACE, 'text/html'],
    [b'<?xml', b'\xff\xff\xff\xff\xff', WHITESPACE, 'text/xml'],
    [b'%PDF-', b'\xff\xff\xff\xff\xff', b'', 'application/pdf']
]

# Patterns corresponding second table in section 7.1 of specification
# TODO: Add logic to allow user to extend this table safely
# Byte Pattern | PATTERN MASK | LEADING BYTES TO BE IGNORED | MIMETYPE
ADDITIONAL_PATTERNS = [[b'%!PS-Adobe-',
                        b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',
                        b'',
                        'application/postscript'],
                       [b'\xff\xff\x00\x00',
                        b'\xff\xff\x00\x00',
                        b'',
                        'text/plain'],
                       [b'\xef\xbb\xbf\x00',
                        b'\xff\xff\xff\x00',
                        b'',
                        'text/plain'],
                       [b'\xef\xbb\xbf\x00',
                        b'\xff\xff\xff\x00',
                        b'',
                        'text/plain']]

# mp25_rates
# index | mp2.5-rates
MP25_RATES = {
    0: 0,
    1: 8000,
    2: 16000,
    3: 24000,
    4: 32000,
    5: 40000,
    6: 48000,
    7: 56000,
    8: 64000,
    9: 80000,
    10: 96000,
    11: 112000,
    12: 128000,
    13: 144000,
    14: 160000,
}

# MP3 Rates table
# index | mp3-rates
MP3_RATES = {
    0: 0,
    1: 32000,
    2: 40000,
    3: 48000,
    4: 56000,
    5: 64000,
    6: 80000,
    7: 96000,
    8: 112000,
    9: 128000,
    10: 160000,
    11: 192000,
    12: 224000,
    13: 256000,
    14: 320000,
}


# Sample rates
# index | samplerate
SAMPLE_RATES = {
    0: 44100,
    1: 48000,
    2: 32000
}
