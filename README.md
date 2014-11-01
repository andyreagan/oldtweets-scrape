Scraping early tweets
=====================
Sraping twitter for the first tweets, by requesting tweets by ID through the REST API, sequentially.

Set up with the VACC-cmd-line twitter application for user VACCKing (pw arret3).
Application keys and things are the file "keys."

Method
------

Every hour on the 0,20,40, run-minutely.cron is executed, which calls scrape-oauth2.py.
This reads in the current tweet number from "completed.txt," and attempts to get the next 180 tweets.
Tweets are put into data/, and the log files (twitter's return status) is put into log/.
Then it writes out the number completed to the same file.

Results
-------

There is a bunch of other stuff in here, to look at the data that has been pulled down.

Missing Data
------------

Deleted data/11600-11699.json ...need to recover


