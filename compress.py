import os
import subprocess

rootmediadir = os.getcwd()
print(rootmediadir)
crf = 30        # lower the better quality but takes much more time (keep the range between 22-30)

for subdirs, dirs, files in os.walk(rootmediadir):
    for file in files: # file = .mp4
        # print(files)
        extension = os.path.splitext(file)[-1].lower()
        if extension == ".mp4":
            if not os.path.exists(subdirs + "/compressed"):
                print(subdirs)
                os.makedirs(subdirs + "/compressed")

            media_in = subdirs + "/" + file
            media_out = subdirs + "/compressed/" + file