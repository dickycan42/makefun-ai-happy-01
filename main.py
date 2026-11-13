# ai-happy-01 entry: puts the happy picture at the grader's output path.
#
# The picture lives in this repository as entry.png, next to this script.
# All this program does is copy that file into the output directory as
# entry.png, then verify the copy byte for byte by comparing SHA-256
# digests of the source and the copy. If anything does not match, it
# prints an error and exits non-zero.
#
# The output directory comes from MAKEFUN_OUTPUT_DIR; when that variable
# is unset it defaults to /output, the grader's writable directory.
# Outside the grader you can try it with:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Deterministic by design: it only copies bytes. No network, no random
# numbers, no timestamps, no reading of anything else, so two runs
# always write exactly the same bytes.

import hashlib
import os
import shutil
import sys
from pathlib import Path


def sha256_of(path):
    """Return the SHA-256 hex digest of a file's bytes."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(65536)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def main():
    script_dir = Path(__file__).resolve().parent
    source = script_dir / "entry.png"

    if not source.is_file():
        print(f"error: {source} is missing", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"

    shutil.copyfile(source, destination)

    if destination.stat().st_size != source.stat().st_size:
        print("error: output size differs from entry.png", file=sys.stderr)
        sys.exit(1)

    if sha256_of(source) != sha256_of(destination):
        print("error: output bytes differ from entry.png", file=sys.stderr)
        sys.exit(1)

    print(f"wrote {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
