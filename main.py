#!/usr/bin/env python3
"""news-23 b63 front-page-dense: copy entry.png (1024x1024) to $MAKEFUN_OUTPUT_DIR/entry.png.

Stdlib only. Never writes next to itself: it writes only to MAKEFUN_OUTPUT_DIR,
so it also works from a read-only copy (with MAKEFUN_OUTPUT_DIR pointed elsewhere).
"""
import hashlib
import os
import struct
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
MAX_BYTES = 1024 * 1024
PNG_SIG = b"\x89PNG\r\n\x1a\n"
# IEND trailer: length 0, type "IEND", CRC 0xAE426082 (the fixed CRC of "IEND").
IEND_TRAILER = struct.pack(">I", 0) + b"IEND" + struct.pack(">I", 0xAE426082)


def fail(msg):
    print("error: " + msg, file=sys.stderr)
    sys.exit(1)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    if not out_dir:
        fail("MAKEFUN_OUTPUT_DIR is empty")
    out_dir_abs = os.path.abspath(out_dir)
    repo_abs = os.path.dirname(os.path.abspath(__file__))
    if out_dir_abs == repo_abs or out_dir_abs.startswith(repo_abs + os.sep):
        fail("MAKEFUN_OUTPUT_DIR must not be inside the repo (%s)" % repo_abs)

    with open(SRC, "rb") as f:
        data = f.read()

    if len(data) > MAX_BYTES:
        fail("entry.png is %d bytes, over the 1 MiB limit" % len(data))
    if data[:8] != PNG_SIG:
        fail("entry.png is not a PNG (bad signature)")
    if len(data) < 33 or data[12:16] != b"IHDR":
        fail("entry.png has no IHDR chunk")
    width, height, bit_depth, colour_type = struct.unpack(">IIBB", data[16:26])
    if (width, height) != (1024, 1024):
        fail("entry.png is %dx%d, expected 1024x1024" % (width, height))
    if bit_depth != 8 or colour_type not in (2, 6):
        fail("unexpected bit depth %d / colour type %d" % (bit_depth, colour_type))
    if data[-12:] != IEND_TRAILER:
        fail("entry.png has a malformed IEND trailer")

    os.makedirs(out_dir_abs, exist_ok=True)
    dst = os.path.join(out_dir_abs, "entry.png")
    with open(dst, "wb") as f:
        f.write(data)

    with open(dst, "rb") as f:
        written = f.read()
    if written != data:
        fail("output does not match source byte-for-byte")
    sha = hashlib.sha256(data).hexdigest()
    print("source: %s (%dx%d, %d bytes, sha256 %s)" % (SRC, width, height, len(data), sha))
    print("verified: PNG signature, IHDR 1024x1024, bit depth 8, colour type %d, IEND OK" % colour_type)
    print("wrote %s (byte-identical, sha256 %s)" % (dst, sha))


if __name__ == "__main__":
    main()
