# build a network from the json
#
# USAGE
# python build-network.py [threshold]
#
# threshold in [mention,reply,recip]

from json import loads
import codecs
import time


def parser(infile,userDict,method):
  ## open the file
  f = codecs.open(infile,'r','utf8')

  ## go line by line in the json
  for line in f:
    tweet = loads(line)
    ## print tweet['entities']['user_mentions']
    ## print tweet['text']
    if method == 'mention':
      if tweet['entities']['user_mentions']:
        if tweet['user']['id'] not in userDict:
          print 'adding user {}'.format(tweet['user']['id'])
          userDict[tweet['user']['id']] = []
        for mention in tweet['entities']['user_mentions']:
          userDict[tweet['user']['id']].append(mention)
    if method == 'reply':
      if tweet['in_reply_to_user_id']:
        if tweet['user']['id'] not in userDict:
          print 'adding user {}'.format(tweet['user']['id'])
          userDict[tweet['user']['id']] = []
        for replyToID in tweet['in_reply_to_user_id']:
          userDict[tweet['user']['id']].append(replyToID)
    if method == 'retweet':
      if 'retweeted_status' in tweet:
        if tweet['user']['id'] not in userDict:
          print 'adding user {}'.format(tweet['user']['id'])
          userDict[tweet['user']['id']] = []
        userDict[tweet['user']['id']] = tweet['retweeted_status']['user']['id']
    if method == 'retweetSyn':
      if tweet['text'][0:2] == 'RT' or tweet['text'][0:2] == 'rt' or tweet['text'][0:2] == 'Rt':
        if tweet['user']['id'] not in userDict:
          print 'adding user {}'.format(tweet['user']['id'])
          userDict[tweet['user']['id']] = 0
        userDict[tweet['user']['id']] += 1
  f.close()

def parserTimeText(infile,timeMat,volMat):
  ## open the file
  f = codecs.open(infile,'r','utf8')
  ## go line by line in the json
  for line in f:
    tweet = loads(line)
    ## print tweet['created_at']
    tmptime = time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
    ## print tmptime[7]
    ## daily
    if tmptime[0] != 2006:
      print 'out of 2006!'
    timeMat[tmptime[7]-1] +=' '+tweet['text']
    volMat[tmptime[7]-1] +=1
  f.close()

def plotHapps(happs,vol,picname):
  import matplotlib.pyplot as plt
  # create a figure, fig is now a matplotlib.figure.Figure instance
  fig = plt.figure()
  # plot the scatter
  ax1 = fig.add_axes([0.2,0.2,0.7,0.7]) #  [left, bottom, width, height]
  ax1.plot(range(len(happs)),happs,'bo-',linewidth=2)
  ax1.set_xlabel('Days')
  ax1.set_ylabel('Happs')
  #  ax1.set_xlim([min(dates)-buffer,max(dates)+buffer])
  #  ax1.set_ylim([0,24])
  ax1.set_title('Happiness by day')
  #  plt.xticks((1266,1631,1996,2362),('2010','2011','2012','2013'))
  plt.savefig(picname)

if __name__ == '__main__':
  # print out these things for reference
  from sys import argv
  method = argv[1]

  f = open('data/file-list','r')
  files = ['data/'+line.rstrip() for line in f]
  f.close()
  
  print len(files)
  if method in ['reply','mention','retweet','retweetSyn']:
    userDict = dict()
    for infile in files[0:20]:
      print infile
      parser(infile,userDict,method)
    f = open('edgeList{}.csv'.format(argv[1]),'w')
    for userID in userDict:
      if userDict[userID]:
        ## for mention in userDict[userID]:
        ##   f.write('{0},{1}\n'.format(userID,mention))
        f.write('{0},{1}\n'.format(userID,userDict[userID]))
    f.close()
    ##print userDict

  if method == 'happs':
    ## start with just 2006
    textByDay = ['' for day in range(365)]
    volByDay = [0 for day in range(365)]
    for infile in files[0:20]:
      print infile
      parserTimeText(infile,textByDay,volByDay)
    from judge import readLabMT
    LabMT = readLabMT('000') # now LabMT is the dataset as a dict
    from plot_TOD import happiness
    happsByDay = [happiness(textByDay[i],LabMT) for i in range(len(textByDay))]
    print textByDay
    print volByDay
    print happsByDay

    plotHapps(happsByDay,volByDay,'testhapps.png')
    
  print 'Run success!'
  print '-----------'
  print '-----------'


