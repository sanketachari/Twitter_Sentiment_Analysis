import sys
import json

# Store existing terms and their sentiment scores in dictionary
def sentiment_scores(fp):
    scores = {}  # initialize an empty dictionary
    for line in fp.readlines():
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

# Compute sentiment score for the tweet and store it in score.txt file
def tweet_score(sent_scores, tweet):
    score = 0.0
    for word in tweet.split():
        if word in sent_scores.keys():
            score += sent_scores[word]

    print(score)
    #tweet_score_file = open("score.txt", 'a')
    #tweet_score_file.write(str(score) + '\n')


# Find total number of tweets
def lines(fp):
    print str(len(fp.readlines()))
        

def main():

    # Calcaulate total number of lines in sentiment and tweet files
    lines(open(sys.argv[1]))
    lines(open(sys.argv[2]))

    # Store sentiment score into dictionary
    sent_scores = sentiment_scores(open(sys.argv[1]))

    # print sent_scores
    tweet_file = open(sys.argv[2])
    for line in tweet_file.readlines():

        jsonData = json.loads(line)
        if 'text' in jsonData:
            tweet = jsonData['text'].encode('utf-8')
            tweet_score(sent_scores, tweet)


if __name__ == '__main__':
    main()
