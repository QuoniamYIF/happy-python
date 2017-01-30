import os

print os.getcwd()

os.chdir("/home/quoniam/version-control/happy-python/happy-secret-word/images")

for filename in os.listdir("/home/quoniam/version-control/happy-python/happy-secret-word/images"):
    oldname = filename
    newname = filename.translate(None, "0123456789")
    os.rename(oldname, newname)
