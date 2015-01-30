import urllib2
import os
import json
import sys

import settings
import get_user_comments

def getUserCommentsFromUserList():
    settingsDict = settings.loadSettings()
    datasetPath = settingsDict['dataset_path']

    userListFilePath = os.path.join(datasetPath, 'user_list.txt')
    userListFile = open(userListFilePath, 'r')

    for line in userListFile:
        userName = line.strip()
        print 'Downloading data for user %s.' % (userName)
        get_user_comments.getUserComments(userName)
    userListFile.close()


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("\nUsage: python %s\n" % sys.argv[0])
        exit()

    getUserCommentsFromUserList()