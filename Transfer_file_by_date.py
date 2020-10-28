#
#Python Version             3.8.5
#
#Author                     Casey Fairbanks
#
#
#Purpose                    To create a program that checks for newly created or
#                           edited files and move them to another file and the
#                           end of the day.

import shutil
import os
from datetime import datetime, timedelta

#variable for today's date

local = datetime.now() - timedelta(hours = 24)

#set where the source of the files are
source = "C:\\Users\\ccfai\\OneDrive\\Desktop\\Folder_A/"

#set the destination path to folder_B
destination = "C:\\Users\\ccfai\\OneDrive\\Desktop\\Folder_B/"
files = os.listdir(source)


#check files that have been created or modified

for i in files:
    absolutepath = os.path.join(source,i)
    modTimes = os.path.getmtime(absolutepath)
    Mtime = datetime.fromtimestamp(modTimes)
        
    if Mtime > local:
    #we are saying move the files represented by 'i' to their new destination
        shutil.move(source+i, destination)



