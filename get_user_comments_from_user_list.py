import urllib2
import os
import json
import sys

import settings
import get_user_comments

def getUserCommentsFromUserList():
    settingsDict = settings.loadSettings()
    datasetPath = settingsDict['dataset_path']
    jsonPath = os.path.join(datasetPath, settingsDict['json_dir'])

    # Get list of users that we have to download.
    userListFilePath = os.path.join(datasetPath, 'user_list.txt')
    userListFile = open(userListFilePath, 'r')
    allUsers = set([line.strip() for line in userListFile])
    userListFile.close()

    # Check for user data that we already downloaded.
    downloadedUsers = set([fname.split('.')[0] for fname in  os.listdir(jsonPath)])
    usersToDownload = allUsers.difference(downloadedUsers)

    print('Downloaed %d users. %d users to download.' % (len(downloadedUsers), len(usersToDownload)))
    return

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