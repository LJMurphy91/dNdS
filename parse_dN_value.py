from sys import argv
codeml_file = open(argv[1], 'rU')
second_file = open(argv[2], 'rU')

title = argv[1].split("/")
title = title[0].replace(".codeml","")


name_list = []
def get_name(needle_file):
	for stuff in needle_file:
		if "# 2" in stuff:
			strip = stuff.strip()
			split = strip.split(":")
			#print split
			name = split[1]. replace(" ", "")
			name_list.append(name)

get_name(second_file)

#print name_list
#dnds_list = []
dnds_dict = dict()
for lines in codeml_file:
	for x in name_list:
		if x in lines:	
			if not lines.startswith("#") and not lines.startswith("2"):
				countingline = lines.strip()
				countingline = countingline.split(" ")
				index = range(len(countingline))
				for nums in index:
					if "(" in countingline[nums]:
#						print countingline[nums]
						print "yes"
						dN = countingline[nums].replace('(', '')
						dnds_dict[title] = dN
#print dnds_dict
results_file = open("dn_results.txt", 'a')
for key, value in dnds_dict.items():
	results_file.write(str(key) + "\t" + str(value) + "\n")

results_file.close()



