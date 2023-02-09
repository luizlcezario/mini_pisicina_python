from antigravity import geohash
import sys

def hash(argv):
    try:
        latitude = float(argv[1])
        longitude = float(argv[2])
        datedow = argv[3].encode('utf-8')
        geohash(latitude, longitude, datedow)
    except Exception as e:
        print(e)

if __name__=='__main__':
    if len(sys.argv) != 4:
        sys.exit()
    hash(sys.argv)