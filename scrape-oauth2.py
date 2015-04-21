#!/usr/bin/python
#
# scrape.py
#
# hammer the twitter API!

from twython import Twython, TwythonError
import json
import codecs

if __name__ == '__main__':
  numToGrab = 180
  
  # read current number
  f = open('completed.txt','r')
  numCompleted = int(f.readline().rstrip())
  f.close()
  
  print 'getting tweets ' + str(numCompleted) + ' to ' + str(numCompleted+numToGrab-1)
  
  f = open('keys','r')
  APP_KEY = f.readline().rstrip()
  f.close()
  f = open('oauth2-key','r')
  ACCESS_TOKEN = f.readline().rstrip()
  f.close()
  

  
  twitter = Twython(APP_KEY,access_token=ACCESS_TOKEN)
  
  tweetIDs = [x for x in range(numCompleted,numCompleted+numToGrab)]
  
  outfile = '/users/a/r/areagan/fun/twitter/scraping/data/{0}-{1}.json'.format(numCompleted,numCompleted+numToGrab-1)
  outlog = '/users/a/r/areagan/fun/twitter/scraping/log/{0}-{1}.log'.format(numCompleted,numCompleted+numToGrab-1)
  

  f = codecs.open(outfile,'w','utf8')
  g = open(outlog,'w')
  
  # f.write('test\n')
  # f.close()
  for tweetID in tweetIDs:
    g.write('getting tweet ID ' + str(tweetID) + '\n')
    try:
      tweet = twitter.show_status(id=tweetID)
      json.dump(tweet,f,ensure_ascii=False)
      # ujson.dump(tweet,f,ensure_ascii=False)
      f.write('\n')
      g.write('success\n')
    except TwythonError as e:
      g.write(str(e))
      g.write('\n')
  f.close()
  g.close()
  
  # write new number
  f = open('completed.txt','w')
  f.write(str(numCompleted+numToGrab)+'\n')
  f.close()









