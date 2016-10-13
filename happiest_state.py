import sys
import json
import re
import types


# Store existing terms and their sentiment scores in dictionary
def sentiment_scores(fp):
    scores = {}  # initialize an empty dictionary
    for line in fp.readlines():
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores


# Compute sentiment score for the tweet
def tweet_score(sent_scores, tweet):
    score = 0.0
    for word in tweet:
        if word in sent_scores.keys():
            score += sent_scores[word]
    return score


# Evaluate happiest state in United States based on the sentiment scores of the tweets
def happiest_state(tweet_file, sent_scores):

    state_score = {}
    for line in open(tweet_file).readlines():

        jsonData = json.loads(line)

        if 'text' in jsonData:

            # Evaluate text of tweet
            tweet = jsonData["text"].encode("utf-8")
            tweet = re.split("[^a-zA-Z]*", tweet)

            # Find tweet sentiment score
            score = tweet_score(sent_scores, tweet)

            # Evaluate statewise sentiment scores of tweets
            if 'place' in jsonData and type(jsonData['place']) is not types.NoneType:
                if 'full_name' in jsonData['place'] and type(jsonData['place']['full_name']) is not types.NoneType:
                    if 'country_code' in jsonData['place'] and type(jsonData['place']['country']) is not types.NoneType:
                        if jsonData['place']['country'] == 'United States':

                            state = jsonData['place']['full_name'].split(", ")[1]

                            if len(state) == 2:
                                if state_score.has_key(state):
                                    state_score[state] += score;
                                else:
                                    state_score[state] = score

    # Find happiest state based on maximum sentiment score
    happiestState = "None"

    if len(state_score) > 0:
        happiestState = state_score.keys()[0]

        for state in state_score:
            if state_score[state] > state_score[happiestState]:
                happiestState = state

    print("Happiest State: " + happiestState + "     Sentiment Score: " + str(state_score[happiestState]))


if __name__ == '__main__':
    sent_scores = sentiment_scores(open(sys.argv[1]))
    happiest_state(tweet_file=sys.argv[2], sent_scores=sent_scores)
