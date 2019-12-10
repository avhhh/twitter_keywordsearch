inv_index = dict()
allTweets = []

# DEBUGGING FUNCTION: Reads all the tweets held in the file
def readtweets(filename):
	print("***********READING TWEETS***********")
	print("------------------------------------")
	tweetnum = 1
	file = open(filename, "r")
	line = file.readline()

	while line:
		print("[Tweet " + str(tweetnum) + "]", line)
		line = file.readline()
		tweetnum += 1
	file.close()

	return

# Checks whether the file path is valid
def validFile(filename):
	try:
		file = open(filename, "r")
		line = file.readline()
	except:
		return False
	return True

# Stores tweets in an array
def storeTweets(filename):
	file = open(filename, "r")
	line = file.readline()
	while line:
		allTweets.append(line)
		line = file.readline()
	allTweets[len(allTweets)-1] += "\n"	
	file.close()
	print("Stored " + str(len(allTweets)) + " tweets.")
	return

# Build inverted index from file (tweet number, word placement)
def buildIndex(filename):
	tweetnum = 0
	file = open(filename, "r")
	line = file.readline().split()
	while line:
		tweetnum += 1
		for i in range(0, len(line)):
			word = line[i].lower()
			if word not in inv_index:
				inv_index[word] = [(tweetnum, i)]
			else:
				inv_index[word].append((tweetnum, i))
		line = file.readline().split()
	file.close()
	return

# Finds & Prints tweets that at least matches one word in pattern
def scoreTweets(inv_index, pattern):
	# Prevents from reprinting tweets
	numMatches = 0
	wordMatches = [0]*len(allTweets)
	for word in pattern.split(" "):
		if word in inv_index:
			tweet_list = inv_index[word]
		else:
			continue
		for pair in tweet_list:
			index = pair[0]-1
			if wordMatches[index] == 0:
				numMatches += 1
				wordMatches[index] = 1
			else:
				wordMatches[index] += 1
	return wordMatches, numMatches

def positionScore(inv_index, pattern):
	return

def printRelevant(wordMatches, numMatches):
	# Find the indicies of top 10 values
	if numMatches == 0:
		print("There are no relevant tweets.")
		return
	sortedMatches = sorted(range(len(wordMatches)), key=lambda x: wordMatches[x])[::-1]
	printNum = 10
	if numMatches < printNum:
		printNum = numMatches
	
	print("There are", printNum, "Relevant Tweets")
	print("---------------------------------------")
	for i in range(printNum):
		tweetIdx = sortedMatches[i]
		print("[Tweet " + str(tweetIdx+1) + "]:", end=" ")
		print(allTweets[tweetIdx])

def derestrict(pattern):
	newpattern = ""
	for word in pattern.split(" "):
		newpattern += (word + " ")
		newpattern += (word +"s ")
		newpattern += (word + "ing ")
		newpattern += (word + "ed ")
	return newpattern

def getTweets(filename):	
	storeTweets(filename)	
	buildIndex(filename)
	
	query = input("Enter your query: ")
	query = derestrict(query)
	
	result = scoreTweets(inv_index, query)
	printRelevant(result[0], result[1])

	return