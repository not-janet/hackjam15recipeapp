import re

def formatInput(string):
	comma = ","
	junk = re.findall(r"[\w']+", string)
	result = []
	for item in junk:
		if item.isalpha():
			result.append(item)
	comma = comma.join(result)
	return comma


string = input('--->')
string = formatInput(string)
print(string)