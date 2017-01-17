# The one pad problem.

import string
from GF2 import one, zero
from collections import OrderedDict
from pprint import pprint

# Galois field integers.
gf2_tab = {'0': zero, '1':one}
gf2_tab_rev = {zero:'0', one:'1'}

# Galois field sequences for each character.
char_list = string.ascii_uppercase+' '
char_gf2_list = OrderedDict()
for i, char in enumerate(char_list):
	char_idx_bin = '{0:05b}'.format(i)
	char_idx_gf2 = [gf2_tab[x] for x in char_idx_bin]
	char_gf2_list[char] = char_idx_gf2

# Go through each cyphertext bit sequence,
# Test each character bit sequence with GF2 add and get the letters
# print letters

c_txt = '10101 00100 10101 01011 11001 00011 01011 10101 00100 11001 11010'
c_txt_list = c_txt.split(' ')

for char, char_gf2 in char_gf2_list.items():
	seq = []
	print 'Using:', char_gf2
	for c_txt in c_txt_list:
		c_txt_gf2 = [gf2_tab[x] for x in c_txt]
		comp_sym_gf2 = map(lambda a,b:a-b, c_txt_gf2, char_gf2)
		comp_sym_bin_list = [gf2_tab_rev[x] for x in comp_sym_gf2]
		comp_sym_bin = ''.join(comp_sym_bin_list)
		comp_sym_idx = int(comp_sym_bin, 2)
		if comp_sym_idx < 27:
			seq.append(char_list[comp_sym_idx])
		else:
			 continue
	if seq:
		orig_char_sequence = ' '.join(seq)
		print orig_char_sequence
	print


