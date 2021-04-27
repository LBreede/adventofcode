# --- Day 4: The Ideal Stocking Stuffer ---

import hashlib, re

f = open("input.txt", "r").read()

def findSecretKey(file, match):
	i = 1
	while(True):
		secretKey = file + str(i)
		result = hashlib.md5(secretKey).hexdigest()
		found = re.search("^" + match, result)
		if found:
			break
		else:
			i += 1
	return i

print(findSecretKey(f, "00000"))
print(findSecretKey(f, "000000"))