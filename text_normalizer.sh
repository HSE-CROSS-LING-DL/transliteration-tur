#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
python3 ${DIR}/encodings_normalizer.py | python3 ${DIR}/1to1_transliteration.py
