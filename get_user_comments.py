import urllib2
import os
import json
import sys

import settings

def getTimestampFromSubmission(submissionId):
    requestUrl = "https://hacker-news.firebaseio.com/v0/item/%d.json" % (submissionId)
    req = urllib2.Request(requestUrl, None)
    try:
        httpResponse = urllib2.urlopen(req, timeout=10)
        jsonData = json.load(httpResponse)
    except:
        print 'Failed to get submission data.'
        return None

    if 'time' in jsonData:
        return jsonData['time']
    else:
        print jsonData
        return None


def getUserComments(userName):
    settingsDict = settings.loadSettings()
    datasetPath = settingsDict['dataset_path']
    jsonPath = os.path.join(datasetPath, settingsDict['json_dir'])

    # Create directory for dataset if it does not exists.
    if not os.path.exists(jsonPath):
        os.makedirs(jsonPath)

    requestUrl = "https://hacker-news.firebaseio.com/v0/user/%s.json" % (userName)
    req = urllib2.Request(requestUrl, None)
    try:
        httpResponse = urllib2.urlopen(req, timeout=10)
        userData = json.load(httpResponse)
    except:
        print 'Failed to download user comments.'
        return
    
    if 'submitted' in userData:
        submittedIdList = userData['submitted']
        timestampList = []
        
        for submissionId in submittedIdList:
            timestamp = getTimestampFromSubmission(submissionId)
            if timestamp is not None:
                timestampList.append(timestamp)
        userData['timestamps'] = timestampList

    outputFilePath = os.path.join(jsonPath, '%s.comments.json' % (userName))
    outputFile = open(outputFilePath, 'w')
    outputFile.write(json.dumps(userData))
    outputFile.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nUsage: python %s [user name]\n" % sys.argv[0])
        exit()

    userName = sys.argv[1]
    getUserComments(userName)