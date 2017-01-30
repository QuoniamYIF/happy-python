import time
import webbrowser

numbers_of_iterations = 5

print "This program starts on " + time.ctime()
count = 0
while(count < numbers_of_iterations):
    time.sleep(20)
    webbrowser.open("http://music.163.com/#/song?id=431695718")
    count += 1