from random import choices
import string
import itertools

a = [a for a in string.ascii_lowercase]
b = [b for b in string.ascii_uppercase]
c = [c for c in string.digits]
d = [d for d in string.punctuation]


def generate(pl, length):
    pass_t = []
    res = choices(pl, weights=None, cum_weights=None, k=int(length))
    pass_t.append("".join([str(item) for item in res]))
    return pass_t


pass_length = input('How long would you like your new Password?: ')
contents = input('Choose more than one option or \'e\' for all, without spaces:\n\'a\' For lowercase, \'b\' for uppercase, \'c\' for digits, \'d\' for punctuation: ')


if contents == 'ab':
    pl = list(itertools.chain(a, b))
elif contents == 'ac':
    pl = list(itertools.chain(a, c))
elif contents == 'ad':
    pl = list(itertools.chain(a, d))
elif contents == 'bc':
    pl = list(itertools.chain(b, c))
elif contents == 'bd':
    pl = list(itertools.chain(b, d))
elif contents == 'cd':
    pl = list(itertools.chain(c, d))
elif contents == 'abc':
    pl = list(itertools.chain(a, b, c))
elif contents == 'abd':
    pl = list(itertools.chain(a, b, d))
elif contents == 'acd':
    pl = list(itertools.chain(a, c, d))
elif contents == 'bcd':
    pl = list(itertools.chain(b, c, d))
elif contents == ('e' or 'abcd'):
    pl = list(itertools.chain(a, b, c, d))

try:
    print(generate(pl, pass_length))
except NameError:
    print('Invalid selection')