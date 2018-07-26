import sys
import os.path

try:
    print("Song name: "+sys.argv[1])
except IndexError:
    print("Error: Need to provide target file path!")
    sys.exit()

target = os.path.join(os.getcwd(),sys.argv[1])
print("Full file path: "+target)
