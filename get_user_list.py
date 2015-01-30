import urllib2
import os
import json
import sys

import settings

def getTopStoriesIdList():
    requestUrl = "https://hacker-news.firebaseio.com/v0/topstories.json"
    req = urllib2.Request(requestUrl, None)
    try:
        httpResponse = urllib2.urlopen(req, timeout=10)
        jsonData = json.load(httpResponse)
    except:
        print 'Failed to get top stories.'
        return

    return jsonData


def getCommentIdList(storyId):
    requestUrl = "https://hacker-news.firebaseio.com/v0/item/%d.json" % (storyId)
    req = urllib2.Request(requestUrl, None)
    try:
        httpResponse = urllib2.urlopen(req, timeout=10)
        jsonData = json.load(httpResponse)
    except:
        print 'Failed to get story data.'
        return None

    if 'title' in jsonData:
        print jsonData['title']

    if 'kids' in jsonData:
        return jsonData['kids']
    else:
        return None


def getUserName(commentId):
    requestUrl = "https://hacker-news.firebaseio.com/v0/item/%d.json" % (commentId)
    req = urllib2.Request(requestUrl, None)
    try:
        httpResponse = urllib2.urlopen(req, timeout=10)
        jsonData = json.load(httpResponse)
    except:
        print 'Failed to get user name.'
        return None

    if 'by' not in jsonData:
        print jsonData
        return None
    else:
        return jsonData['by']


def getUserList(userName):
    settingsDict = settings.loadSettings()
    datasetPath = settingsDict['dataset_path']

    topStoriesIdList = getTopStoriesIdList()
    currentStory = 0

    collectedUsers = set()
    while len(collectedUsers) < numberOfUsers and currentStory < len(topStoriesIdList):
        print 'I have %d users.' % len(collectedUsers)

        currentStory += 1
        storyId = topStoriesIdList[currentStory]
        commentIdList = getCommentIdList(storyId)
        if commentIdList is None:
            continue
        else:
            for commentId in commentIdList:
                userName = getUserName(commentId)
                if userName is not None:
                    collectedUsers.add(getUserName(commentId))

    # Print collected users.
    outputFilePath = os.path.join(datasetPath, 'user_list.txt')
    outputFile = open(outputFilePath, 'w')
    for userName in collectedUsers:
        outputFile.write(userName + '\n')
    outputFile.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nUsage: python %s [number of users]\n" % sys.argv[0])
        exit()

    numberOfUsers = int(sys.argv[1])
    getUserList(numberOfUsers)