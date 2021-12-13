chapters = {
	"1": "Report Repair", "2": "Password Philosophy",
	"3": "Toboggan Trajectory", "4": "Passport Processing"
}

with open("chapters.json", "w") as f:
	json.dump(chapters, f, indent=4)