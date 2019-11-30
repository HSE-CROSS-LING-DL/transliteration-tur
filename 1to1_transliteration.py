import sys

lat2cyr_translit = {
  'a': 'а',
  'b': 'б',
#  'ç': 'ч',
  'd': 'д',
  'e': 'е',
  'f': 'ф',
  'g': 'г',
  'h': 'х',
  'i': 'и',
  'k': 'к',
  'l': 'л',
  'm': 'м',
  'n': 'н',
 # 'o': 'о',
  'p': 'п',
  'r': 'р',
  's': 'с',
#  'ş': 'ш',
  't': 'т',
#  'u': 'у',
  'v': 'в',
  'z': 'з',
  'i': 'і',
  'ҡ': 'қ',
  'ı': 'ы',
  'y': 'й'
}

for lat_c in list(lat2cyr_translit.keys()):
    lat2cyr_translit[lat_c.upper()] = lat2cyr_translit[lat_c].upper()

for line in sys.stdin:
    print(''.join([lat2cyr_translit.get(c,c) 
                   for c in line]), end = '')
