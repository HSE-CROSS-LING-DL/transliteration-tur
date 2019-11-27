import sys
from collections import defaultdict as dd

alphabet = dd(int)
for line in sys.stdin:
    for c in line:
        alphabet[c] += 1

for c, freq in sorted(alphabet.items(), key = lambda x: x[1], reverse=True):
    if not c.strip():
        continue
    print('\t'.join([c, str(freq)]))
