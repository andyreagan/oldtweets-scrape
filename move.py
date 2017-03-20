import sys
if __name__ == "__main__":
    # fname = sys.stdin.read()
    fname = sys.argv[1]
    basename,ending = fname.split(".")
    start,stop = basename.split("-")
    # print(start)
    # print(stop)
    sys.stdout.write("{0:019d}-{1:019d}.{2}".format(int(start),int(stop),ending))
