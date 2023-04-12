# 'max"
# 3 -> pda
# 5 -> rfc
# 7 -> the

# IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV
#  1 -> 0 words recognized
#  5 -> 3 words recognized
#  11 -> 7 words recognized
#  18-> 1 words recognized
#  11 -> 2 words recognized
import nltk
from nltk.corpus import words, names
import ssl
# https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

word_list = words.words()
namelist = names.words()

word = 'computerrr'

if word in word_list:
    print('it is here')
else:
    print('not here')
# Take encrypted string
# split the string to words
# compare each word to the nltk word list
# come up with % of numbers that make sense
