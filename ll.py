import urllib2
import time

start = time.time()

for i in range(1,100): urllib2.urlopen("http://www.google.com").read()

end = time.time()
print(end - start)
