import os
import utility

WELCOME_MSG = "Welcome to the Twitter Keyword Search!\n"+\
				"---------------------------------------\n" +\
				"Choose an option for Twitter dataset:\n" +\
				"[1] basic.txt -- 3 Tweets\n" +\
				"[2] sample_input.txt -- 22 Tweets\n" +\
				"[3] farha_tweets.txt -- 44 Tweets\n" +\
				"[4] Enter my own file\n"
def main():
	print(WELCOME_MSG)
	cur_path = os.getcwd()
	print("Current path:", cur_path)
	
	data_option = input("Select an option: ")
	if data_option == '1':
		cur_path += "/test_files/basic.txt"
		print("Current path:", cur_path)
	elif data_option == '2':
		cur_path += "/test_files/sample_input.txt"
	elif data_option == '3':
		cur_path += "/test_files/farha_tweets.txt"
	elif data_option == '4':				
		filename = ""
		while (not utility.validFile(filename)):
			if (filename != ""):
				print("File " + filename + " does not exist. Try again.")
			filename = input("Imported Tweets File: ")
		cur_path = filename
	else:
		print("Option not available.")
		return

	utility.getTweets(cur_path)

if __name__ == '__main__':
	main()