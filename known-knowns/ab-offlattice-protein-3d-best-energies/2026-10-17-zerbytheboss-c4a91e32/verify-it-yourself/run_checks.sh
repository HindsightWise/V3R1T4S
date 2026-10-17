#!/bin/sh
set -eu
DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$DIR"
python3 verify-it-yourself/check_ab_protein.py object/1CRN_L46_negE95.720530.json
