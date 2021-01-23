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
	newList = []
	for p in pDictList:
		if len(p) == 7 and "cid" not in p:
			newList.append(p)
		if len(p) == 8:
			newList.append(p)
	return newList

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
initCleanupList = removeInvalidPassportsFromList(passports)
num_valid_pt1 = countValidPassports(initCleanupList)

print("The answer for part one is: " + str(num_valid_pt1) + " valid passports.") # 264

valid_passports = passportMasterCheck(initCleanupList)
num_valid_pt2 = countValidPassports(valid_passports)

print("The answer for part two is: " + str(num_valid_pt2) + " valid passports.")