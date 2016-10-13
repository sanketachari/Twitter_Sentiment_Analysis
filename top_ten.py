import sys
import json
import types


def top_ten(tweet_file):

    for line in open(tweet_file).readlines():

        jsonData = json.loads(line)

        # Evalute hashtags from the tweet
        hashtags ={}
        if 'entities' in jsonData and type(jsonData['entities']) is not types.NoneType:
            if 'hashtags' in jsonData['entities'] and type(jsonData['entities']['hashtags']) is not types.NoneType:
                for hashtag in jsonData['entities']['hashtags']:
                    tag = hashtag['text'].encode("utf-8")
                    if hashtags.has_key(tag):
                        hashtags[tag] += 1
                    else:
                        hashtags[tag] = 1

    # Top ten hash tags present in the tweets
    topTen = sorted(hashtags.items(), key= lambda hashtags: hashtags[1], reverse= True)[:10]

    for tag in topTen:
        print (tag[0] + ": " + str(tag[1]))


if __name__ == '__main__':
    top_ten(sys.argv[1])

