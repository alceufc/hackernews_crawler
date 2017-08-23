Hacker News Crawler
===================

A python crawler that uses the Hacker News API to collect user data from [Hacker News](https://news.ycombinator.com/).

How to use
----------

To collect JSON data from a user use (in this case `pg`):

`python get_user_comments.py pg`

This will save the data to the directory `data/json`. The directory will be automatically created if necessary.

You can also get a list of users names by searching for users that have commented on the top stories:

`python get_user_list.py 100`

In this case the argument 100 tells the script to stop searching for users once we have at least 100 users.
The list of users will be saved on the file `data/user_list.txt`.

Now that we have the list of users, we can use the following command to download JSON data from all users in the user list:

python get_user_comments_from_user_list.py

Users that are already in the `data/json` directory will be skipped (use this to resume the download).

