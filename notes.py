import sys
import os
import glob
import datetime
import shutil
import time

while True:
    os.chdir('../../notes')

    for file in glob.glob("*.txt") :
        file_text = open(file, 'r').readline()
        if 'journal' in file_text:
            today = datetime.datetime.today()
            path = os.getcwd()+'/journal/{}/{}/{}'.format(today.year, today.month, today.day)
            if not os.path.isdir(path):
                os.makedirs(path)
            shutil.move(os.getcwd()+'/'+file, path+'/'+file )
    time.sleep(3600)