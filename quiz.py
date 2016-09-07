
def has_teen(a,b,c):
	if (a == 13) or (a == 14) or (a == 15) or (a == 16) or (a == 17):
		return True
	if (a == 18) or (a == 19):
		return True
	if (b == 13) or (b == 14) or (b == 15) or (b == 16) or (b == 17):
		return True
	if (b == 18) or (b == 19):
		return True
	if (c == 13) or (c == 14) or (c == 15) or (c == 16) or (c == 17):
		return True
	if (c == 18) or (c == 19):
		return True
	return False

def not_string(s):
	if s[:3] == 'not':
		return s + 'not'
	a = 'not'+ s
	return a

def icy_hot(a,b):
	if a < 0 and b > 100 or a > 100 and b < 0:
		return True
	return False

def closer_to(t, g1, g2):
	if abs(t - g1) < abs(t - g2):
		return g1
	if abs(t - g2) < abs(t - g1):
		return g2
	if abs(t - g2) == abs(t - g1):
		return 0

def two_as_one(a,b,c):
	if (a + b) == c or (c + b) == a or (a + c) == b:
		return True
	return False

#def pig_latinify(st):
	#low = st.lower()
	#first = low.lstrip(None)
	#string = first.rstrip(None)
	#if string[:1] == 'a' or string[:1] == 'e' or string[:1] == 'i' or string[:1] == 'o' or string[:1] == 'u':
	#	return string + 'way'
	#else:
	#	return string + 'ay'

#print pig_latinify('   Apple   ')
#print pig_latinify('dank')
