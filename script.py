import sys
import os
import os.path


def startingNumber(fileName):
	ans = 0
	yra = 0
	for element in range(0, len(fileName)):
		x = fileName[element]
		if '0'<=x and x<='9':
			num = int(x)
			ans *= 10
			ans += num
			yra = 1
		else:
			break;
	return (ans, yra)

def howToRename(name, number, maxNumber):
	numberLength = len(str(number))
	maxNumberLength = len(str(maxNumber))
	zeroes = maxNumberLength - numberLength
	startingNumbersInName = 0
	for element in range(0, len(name)):
		x = name[element]
		if '0'<=x and x<='9':
			startingNumbersInName = startingNumbersInName + 1
		else:
			break

	ansString = "0" * zeroes  + str(number) + name[startingNumbersInName:]
	print(name, number, maxNumber, ansString)
	return ansString

def compareLength(item1, item2):
	if len(item1[0]) < len(item2[0]):
		return -1
	elif len(item1[1]) == len(item2[0]):
		return 0
	else:
		return 1


fileNames = os.listdir('.')
print(fileNames)

numbers = []
for name in fileNames:
	x, y = startingNumber(name)
	if y==0:
		numbers.append(-1)
	else:
		numbers.append(x)

print(numbers)

if len(numbers)==0:
	sys.exit(0)

maxNumber = max(numbers)

needToRenameTo = {}
needToRenameList = []
print(maxNumber)

for i in range(len(fileNames)):
	name = fileNames[i]
	number = numbers[i]
	if number == -1:
		continue

	newName = howToRename(name, number, maxNumber)
	needToRenameTo[name] = newName
	needToRenameList.append(name)

needToRenameList.sort(lambda x, y: len(x) < len(y))

print(needToRenameTo)
for a in needToRenameList:
	if os.path.exists(needToRenameTo[a]):
		print(needToRenameTo[a] + "already exist")
	else:
		os.rename(a, needToRenameTo[a])