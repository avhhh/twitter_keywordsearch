# Twitter Keyword Search
A keyword search engine that accepts a text file of tweets as input and outputs the most relevants tweets.

## Environment
- Python 3
- Ubuntu LTS

## How to run
Run the following commands to clone the repo and to run the source code.
```sh
$ git clone https://github.com/avhhh/twitter_keywordsearch.git
$ cd twitter_keywordsearch/
$ python controller.py
```
## Demo
This first demo shows the program work for a small set of sample tweets. As observed, the program ranks the tweets based on how many times each word of the pattern shows up.

![Software Demo](img/demo.gif "Simple demo")

The second demo shows that the user can read the tweets used in the dataset. In addition to this, the dataset used are real tweets extracted from Twitter. The tweets with pattern "girl cry" is printed.

![Software Demo2](img/demo2.gif "Real Tweets demo")