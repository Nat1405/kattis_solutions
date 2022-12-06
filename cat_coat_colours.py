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



MaleBlack = ['BDo', 'cDo', 'ceo', 'Beo']
FemaleBlack = ['BDr', 'cDr', 'cer', 'Ber']
MaleBlue = ['Bdo', 'cdo']
FemaleBlue = ['Bdr', 'cdr']
MaleChocolate = ['bDo', 'beo']
FemaleChocolate = ['bDr', 'ber']
MaleLilac = ['bdo']
FemaleLilac = ['bdr']
MaleRed = ['BDO', 'cDO', 'bDO', 'BeO', 'ceO', 'beO']
FemaleRed = ['BDR', 'cDR', 'bDR', 'BeR', 'ceR', 'beR']
MaleCream = ['BDO', 'cdO', 'bdO']
FemaleCream = ['BDR', 'cdR', 'bdR']
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


def main(female_parent_colour, male_parent_colour):
	female_sequences = colour_to_sequences('f', female_parent_colour)
	male_sequences = colour_to_sequences('m', male_parent_colour)

	print(female_sequences)
	print(male_sequences)









if __name__ == "__main__":
	female_parent = sys.stdin.readline().rstrip('\n')
	male_parent = sys.stdin.readline().rstrip('\n')
	main(female_parent, male_parent)
