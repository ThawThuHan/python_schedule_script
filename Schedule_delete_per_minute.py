#!/usr/bin/env python3

from datetime import datetime
import os
import sys
import optparse

parser = optparse.OptionParser()
parser.add_option('-n', dest='num', type='int', help="specify -n recurring time!")
parser.add_option('-p', dest='path', help="specify file path!")

(option, args) = parser.parse_args()

if option.num == None and option.path == None:
    print(parser.print_help())
    exit(0)
else:
    currentDateTime = datetime.now()
    currentDate = int(currentDateTime.strftime("%M"))
    path = option.path
    while True:
        updateTime = int(datetime.now().strftime("%M"))
        if currentDate == updateTime:
            if os.path.exists(path):
                try:
                    os.system(f"rm -rf {path}")
                    print(datetime.now() ," >>> delete!", file=sys.stdout)
                except:
                    print("error")
            else:
                print(datetime.now(), " >>> File not exist!", file=sys.stdout)
                pass
            currentDate = updateTime + option.num
        else:
            pass