CYRILLIC_CHARS = {c for c in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"}

alphabet_fns = {
  "bak": "bak_alphabet.txt",
  "kaz": "kaz_alphabet.txt",
  "tat": "tat_alphabet.txt",
  "crh": "crh_alphabet.txt",
  "kir": "kir_alphabet.txt",
  "tur": "tur_alphabet.txt",
  "krc": "krc_alphabet.txt"
}

langs = set(alphabet_fns.keys())

common_alphabet = set()

lang2alphabet = dict()

for lang, lang_fn in alphabet_fns.items():
    lang_f_alphabet = set([l.strip() for l in open(lang_fn, encoding="utf-8")])
    # print(lang, lang_fn, lang_f_alphabet)
    # input()
    common_alphabet.update(lang_f_alphabet)
    lang2alphabet[lang] = lang_f_alphabet


char2lang = {c: dict() for c in common_alphabet}

for c in common_alphabet:
    for lang in langs:
        char2lang[c][lang] = c in lang2alphabet[lang]

header = ["char"] + sorted(langs)

print('\t'.join(header))
for c in sorted(common_alphabet):
    if c not in CYRILLIC_CHARS:
        print('\t'.join([c] + [str(char2lang[c][lang]) for lang in sorted(langs)]))


# print(char2lang)

