import os
import utility

WELCOME_MSG = "Welcome to the Twitter Keyword Search!\n"+\
				"---------------------------------------\n" +\
				"Choose an option for Twitter dataset:\n" +\
				"[1] basic.txt -- 3 Tweets\n" +\
				"[2] sample_input.txt -- 22 Tweets\n" +\
				"[3] farha_tweets.txt -- 44 Tweets\n" +\
				"[4] test.txt -- 7 Tweets\n" +\
				"[5] Enter my own file\n"
OPTION_MSG = "What do you want to do with the data?\n" +\
				"---------------------------------------\n" +\
				"[1] Print all the tweets in the console\n" +\
				"[2] Make a keyword search\n"
def main():
	print(WELCOME_MSG)
	cur_path = os.getcwd()
	
	dataOpt = input("Select an option: ")
	if dataOpt == '1':
		cur_path += "/datasets/basic.txt"
	elif dataOpt == '2':
		cur_path += "/datasets/sample_input.txt"
	elif dataOpt == '3':
		cur_path += "/datasets/farha_tweets.txt"
	elif dataOpt == '4':
		cur_path += "/datasets/test.txt"
	elif dataOpt == '5':				
		filename = ""
		while (not utility.validFile(filename)):
			if (filename != ""):
				print("File " + filename + " does not exist. Try again.")
			filename = input("Imported Tweets File: ")
		cur_path = filename
	else:
		print("Option not available.")
		return
	
	print(OPTION_MSG)
	actionOpt = input("Select an option: ")
	if actionOpt == '1':
		utility.readtweets(cur_path)
	elif actionOpt == '2':
		utility.getTweets(cur_path)
	else:
		print("Option not available.")
		return

if __name__ == '__main__':
	main()