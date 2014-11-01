# going to parse an hour of the twitter stream, from two hours ago

def parser(infile,outfile):
  from json import loads
  import codecs

  f = codecs.open(infile,'r','utf8')
  g = codecs.open(outfile,'w','utf8')

  # go line by line in the minute-ly json
  for line in f:
    try:   # try to load it
      tweet = loads(line)
      # check that it's a real tweet
      if 'delete' not in tweet:
        # try to find english
        try: 
          if tweet['user']['lang'] == 'en':
            # now we know that it's english
            # try to write it
            try: 
              g.write(tweet['text'] + '.\n')
            except: 
              pass
        except:
          pass 
    except:
      pass

  # good housekeeping
  f.close()
  g.close()

if __name__ == '__main__':
  # print out these things for reference
  from sys import argv
  
  # given the json and the txt filename
  if len(argv) == 3:
    infile = argv[1]
    outfile = argv[2]
  # given just the json filename
  # NEED FULL PATHS
  else:
    infile = argv[1]
    # figure out the text file name
    # replace the trailing .json with .csv
    outfile = '{}.csv'.format(infile[:-5])
  print 'converting ' + infile + ' to ' + outfile
  parser(infile,outfile)

  print 'Run success!'
  print '-----------'
  print '-----------'
