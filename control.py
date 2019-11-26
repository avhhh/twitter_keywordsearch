WELCOME_MSG = "Welcome to the Twitter Keyword Search!\n"+\
				"---------------------------------------"
inv_index = dict()
# Checks whether the file path is valid
def validFile(filename):
	try:
		file = open(filename, "r")
		line = file.readline()
	except:
		print("ERROR: File \"" + filename + "\" does not exist!")
		return False
	return True

# DEBUGGING FUNCTION: Reads all the tweets held in the file
def readtweets(filename):
	tweetnum = 1
	file = open(filename, "r")
	line = file.readline()

	while line:
		print("[Tweet " + str(tweetnum) + "]", line)
		line = file.readline()
		tweetnum += 1
	file.close()

	return

# Build inverted index from file
def buildIndex(filename):
	tweetnum = 1
	file = open(filename, "r")
	line = file.readline().split()
	while line:
		tweetnum += 1
		for i in range(0, len(line)):
			word = line[i]
			if word not in inv_index:
				inv_index[word] = [(tweetnum, i)]
			else:
				inv_index[word].append((tweetnum, i))
		line = file.readline().split()
	file.close()
	return


def main():
	print(WELCOME_MSG)
	filename = input("Imported Tweets File: ")
	if(validFile(filename)):
		buildIndex(filename)
	print(inv_index)
	# query = input("Enter your query: ")


if __name__ == '__main__':
	main()
