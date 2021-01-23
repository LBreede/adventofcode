def createPassportStringList(input):
	lineList = [line.rstrip("\n") for line in open(input)]
	oneLine = ""
	for L in lineList:
		
		if L != "":
			oneLine += L + " "
		else:
			oneLine += "-"

	passportList = oneLine.split("-")
	return passportList

def createPassportDictList(pStringList):
	pDictList = []
	for p in pStringList:
		elem = p.split(" ")
		elem.pop()
		pDict = {}
		for e in elem:
			ee = e.split(":")
			pDict[ee[0]] = ee[1]
		pDictList.append(pDict)
	return pDictList

def removeInvalidPassportsFromList(pDictList):
	for p in pDictList:
		if len(p) < 7:
			pDictList.remove(p)
	return pDictList

def cidCheck(pDictList):
	postCheck = []
	for p in pDictList:
		if len(p) == 7 and "cid" not in p:
			postCheck.append(p)
		elif len(p) == 8:
			postCheck.append(p)
	return postCheck

def passportMasterCheck(pDictList):
	validPassports = []
	for p in pDictList:
		check = 0

		# BIRTH YEAR
		if "byr" in p:
			byr = int(p["byr"])
			if byr >= 1920 and byr <= 2002:
				check += 1

		# ISSUE YEAR
		if "iyr" in p:
			iyr = int(p["iyr"])
			if iyr >= 2010 and iyr <= 2020:
				check += 1 

		# EXPIRATION YEAR
		if "eyr" in p:
			eyr = int(p["eyr"])
			if eyr >= 2020 and eyr <= 2030:
				check += 1

		# HEIGHT
		if "hgt" in p:
			hgt = p["hgt"]
			sys = hgt[-2:]
			amt = hgt[:-2]
			if sys == "cm":
				amt = int(amt)
				if amt >= 150 and amt <= 193:
					check += 1
			elif sys == "in":
				amt = int(amt)
				if amt >= 59 and amt <= 76:
					check += 1

		# HAIR COLOR
		if "hcl" in p:
			hcl = p["hcl"]
			first = hcl[0]
			if first == "#":
				rest = hcl[1:]
				if len(rest) == 6:
					# check += 1
					chars = set("ghijklmnopqrstuvwxyz")
					if not any((c in chars) for c in rest):
						check += 1

		# EYE COLOR
		if "ecl" in p:
			ecl = p["ecl"]
			colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
			if ecl in colors:
				check += 1

		# PASSPORT ID
		if "pid" in p:
			pid = p["pid"]
			if pid[0] == "0" and len(pid) == 9:
				check += 1

		if check == 7:
			validPassports.append(p)

	return validPassports

def countValidPassports(pDictList):
	return len(pDictList)

raw_list = createPassportStringList("input.txt")
passports = createPassportDictList(raw_list)
removeInvalidPassportsFromList(passports)
aaa = cidCheck(passports)
valid_passports = passportMasterCheck(aaa)
num_valid = countValidPassports(valid_passports)
# print("The answer for part one is: " + str(num_valid) + " valid passports.") # 264
print("The answer for part two is: " + str(num_valid) + " valid passports.")