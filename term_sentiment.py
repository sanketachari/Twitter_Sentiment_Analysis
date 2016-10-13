import sys
import json
import re


def lines(fp):
    print ("\nNumber of Tweets:" + str(len(fp.readlines())))


# Find sentiment score of the terms whose sentiment scores are not known
def term_sentiment():

    sent_scores = {}  # initialize an empty dictionary.
    sent_file = open(sys.argv[1])
    for line in sent_file.readlines():
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        sent_scores[term] = int(score)  # Convert the score to an integer.

    exist_word = {}        #
    new_sent_scores = {}   # Guess sentiment for new terms
    tweet_score = {}       # Store sentiment scores for each tweet
    tweet_file = open(sys.argv[2])

    for tweet in tweet_file.readlines():
        score = 0.0
        jsontweet = json.loads(tweet)

        # Extract text of tweet and find out the sentiment score for each term
        if 'text' in jsontweet:

            tweet = jsontweet["text"].encode('utf-8')
            tweet = re.split("[^a-zA-Z]*", tweet)
            for word in tweet.split():

                if word in sent_scores.keys():
                    score += sent_scores[word]

                elif not word in new_sent_scores.keys():
                    new_sent_scores[word] = 0

        for word in tweet.split():

            if word in new_sent_scores.keys():
                new_sent_scores[word] += score/len(tweet.split())     # Calculate score for the new term

            elif word in sent_scores.keys():
                exist_word[word] = sent_scores[word]                 # Assign sentiment score for known terms

        tweet_score[tweet] = score

    print "Tweets and their sentiment score:\n"
    for tweet in tweet_score.keys():
        print(tweet + ": " + str(tweet_score[tweet]))

    print "\nSentiments of existing words:"
    for word, score in exist_word.items():
        print word, score

    print "\nGuessed sentiments:"
    for word, score in new_sent_scores.items():
        print word, score

    # Total number of tweets
    lines(open(sys.argv[2]))

if __name__ == '__main__':
    term_sentiment()
