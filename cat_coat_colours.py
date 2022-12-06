import sys, itertools, collections

'''
My solution maps genes like so:

BB ->       B
bb ->       b
bB or Bb -> c

DD ->       D
d  ->       d
Dd or dD -> e

O  ->       O
o  ->       o
oo ->       r
OO ->       R
Oo or oO -> m

'''



MaleBlack = ['BDo', 'cDo', 'Beo', 'ceo']
FemaleBlack = ['BDr', 'cDr', 'Ber', 'cer']
MaleBlue = ['Bdo', 'cdo']
FemaleBlue = ['Bdr', 'cdr']
MaleChocolate = ['bDo', 'beo']
FemaleChocolate = ['bDr', 'ber']
MaleLilac = ['bdo']
FemaleLilac = ['bdr']
MaleRed = ['BDO', 'cDO', 'bDO', 'BeO', 'ceO', 'beO']
FemaleRed = ['BDR', 'cDR', 'bDR', 'BeR', 'ceR', 'beR']
MaleCream = ['BdO', 'cdO', 'bdO']
FemaleCream = ['BdR', 'cdR', 'bdR']
BlackRedTortie = ['BDm', 'cDm', 'Bem', 'cem']
BlueCreamTortie = ['Bdm', 'cdm']
ChocolateRedTortie = ['bDm', 'bem']
LilacCreamTortie = ['bdm']


def colour_to_sequences(gender, colour):
	if colour == 'Black':
		if gender == 'm':
			return MaleBlack
		else:
			return FemaleBlack
	elif colour == 'Blue':
		if gender == 'm':
			return MaleBlue
		else:
			return FemaleBlue
	elif colour == 'Chocolate':
		if gender == 'm':
			return MaleChocolate
		else:
			return FemaleChocolate
	elif colour == 'Lilac':
		if gender == 'm':
			return MaleLilac
		else:
			return FemaleLilac
	elif colour == 'Red':
		if gender == 'm':
			return MaleRed
		else:
			return FemaleRed
	elif colour == 'Cream':
		if gender == 'm':
			return MaleCream
		else:
			return FemaleCream
	elif colour == 'Black-Red Tortie':
		return BlackRedTortie
	elif colour == 'Blue-Cream Tortie':
		return BlueCreamTortie
	elif colour == 'Chocolate-Red Tortie':
		return ChocolateRedTortie
	elif colour == 'Lilac-Cream Tortie':
		return LilacCreamTortie
	else:
		raise NotImplementedError()


def g(g1, g2):
	'''Parents have genes g1 and g2. This function
	gives you the child possibilities.'''
	# Don't want to encode things more than once,
	# so sort incoming genes.
	# Will discard duplicates, but will be fine!
	# I am blatently misusing sets, but it seems
	# to work out.
	s = {g1, g2}

	# Black gene combinations
	if s == {'B', 'B'}:
		return ['B', 'B', 'B', 'B']
	elif s == {'B', 'b'}:
		return ['c', 'c', 'c', 'c']
	elif s == {'b', 'b'}:
		return ['b', 'b', 'b', 'b']
	elif s == {'c', 'c'}:
		return ['B', 'c', 'c', 'b']
	elif s == {'b', 'c'}:
		return ['c', 'b', 'c', 'b']
	elif s == {'B', 'c'}:
		return ['B', 'c', 'B', 'c']

	# Dilution gene combinations
	elif s == {'D', 'D'}:
		return ['D', 'D', 'D', 'D']
	elif s == {'D', 'd'}:
		return ['e', 'e', 'e', 'e']
	elif s == {'d', 'd'}:
		return ['d', 'd', 'd', 'd']
	elif s == {'e', 'e'}:
		return ['D', 'e', 'e', 'd']
	elif s == {'d', 'e'}:
		return ['d', 'e', 'd', 'e']
	elif s == {'D', 'e'}:
		return ['D', 'e', 'D', 'e']

	# Red gene combinations
	elif s == {'o', 'r'}:
		return ['o', 'o', 'r', 'r']
	elif s == {'o', 'R'}:
		return ['O', 'O', 'm', 'm']
	elif s == {'o', 'm'}:
		return ['O', 'o', 'm', 'r']
	elif s == {'O', 'r'}:
		return ['o', 'o', 'm', 'm']
	elif s == {'O', 'R'}:
		return ['O', 'O', 'R', 'R']
	elif s == {'O', 'm'}:
		return ['O', 'o', 'R', 'm']
	else:
		raise NotImplementedError()



def cross_sequences(p1, p2):
	'''Take possibility like Bdr, bDO and produce all possible kitties'''
	# Black gene possibilities
	black = g(p1[0], p2[0]) # [c, c, c, c]
	dilution = g(p1[1], p2[1]) # [e, e, e, e]
	red = g(p1[2], p2[2]) # [o, o, m, m]

	#print(f"p1: {p1}, p2: {p2}")
	#print(f"black: {black}, dil: {dilution}, red: {red}")

	p1_p2_sequences = list(itertools.product(black, dilution, red))

	# Convert to strings
	return [''.join(x) for x in p1_p2_sequences]


def sequences_to_colours(seqs):
	colours = []
	for s in seqs:
		if s in MaleBlack or s in FemaleBlack:
			colours.append("Black")
		elif s in MaleBlue or s in FemaleBlue:
			colours.append("Blue")
		elif s in MaleChocolate or s in FemaleChocolate:
			colours.append("Chocolate")
		elif s in MaleLilac or s in FemaleLilac:
			colours.append("Lilac")
		elif s in MaleRed or s in FemaleRed:
			colours.append("Red")
		elif s in MaleCream or s in FemaleCream:
			colours.append("Cream")
		elif s in BlackRedTortie:
			colours.append("Black-Red Tortie")
		elif s in BlueCreamTortie:
			colours.append("Blue-Cream Tortie")
		elif s in ChocolateRedTortie:
			colours.append("Chocolate-Red Tortie")
		elif s in LilacCreamTortie:
			colours.append("Lilac-Cream Tortie")
		else:
			return NotImplementedError()

	return colours



def main(female_parent_colour, male_parent_colour):
	female_sequences = colour_to_sequences('f', female_parent_colour)
	male_sequences = colour_to_sequences('m', male_parent_colour)

	female_p_male = list(itertools.product(female_sequences, male_sequences))

	kitten_sequences = []
	for s1, s2 in female_p_male:
		kitten_sequences.extend(cross_sequences(s1, s2))

	colours = sequences_to_colours(kitten_sequences)

	total = len(colours)

	counts = collections.Counter(colours)
	freqs = {k: v/total for k,v in counts.items()}

	for colour, freq in sorted(freqs.items(), key=lambda x: (-x[1], x[0])):
		print(f"{colour} {freq:.9f}")




if __name__ == "__main__":
	female_parent = sys.stdin.readline().rstrip('\n')
	male_parent = sys.stdin.readline().rstrip('\n')
	main(female_parent, male_parent)
