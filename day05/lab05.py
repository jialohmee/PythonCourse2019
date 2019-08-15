import re

# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
	obama = f.readlines()

onetext = "".join(obama)

keyword = re.compile(r"the")

for i,line in enumerate(obama):
	if not keyword.search(line):
		print(i, line)

## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]

re.findall(r"\bs\S*e\b", onetext)

keyword2 = re.compile(r"\bs\S*e\b")
for i, line in enumerate(obama):
	if keyword2.search(line):
		print(i, line)

# TODO: print lines that contain a word of any length starting with s and ending with e




## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = input(r"Please enter a date in the format MM DD YY: ")
pattern = re.compile(r'(\d{2})\s(\d{2})\s(\d{2})')
date = pattern.search(date)
date.groups()






