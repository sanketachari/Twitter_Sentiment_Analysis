import sys
import json
import matplotlib.pyplot as plt
import numpy as np
import re


# Evaluate frequency of terms
def frequency():

    tweet_terms = {}
    total_terms = 0
    tweet_file = open(sys.argv[1])

    for line in tweet_file.readlines():
        jsonData = json.loads(line)

        # Extract text of tweet and find out the total number of terms
        if 'text' in jsonData:

            tweet = jsonData["text"].encode("utf-8")
            tweet = re.split("[^a-zA-Z]*", tweet)
            for word in tweet:
                if word not in tweet_terms.keys():
                    tweet_terms[word] = 0

                total_terms += 1
                tweet_terms[word] += 1

    # Store total number of occurrences of the term in dictionary
    for word in tweet_terms.keys():
        print(word + ": " + str(tweet_terms[word]))

    # Plot Frequency of all the terms present in tweets
    width = 0.35
    X = np.arange(len(tweet_terms))
    plt.bar(X, tweet_terms.values(), color = 'steelblue', width = width)
    plt.xticks(X + width/2, tweet_terms.keys(), rotation = "vertical", horizontalalignment ='center')
    plt.title("Frequency of all the terms in tweets")
    plt.show()

    # Total number of occurrences of all terms
    print ("\n Total words: " + str(total_terms) + '\n')

    # Calculate frequency of each term
    for word in tweet_terms.keys():
        tweet_terms[word] = float(tweet_terms[word])/total_terms
        print word + ": " + str(tweet_terms[word])

if __name__ == '__main__':
    frequency()
