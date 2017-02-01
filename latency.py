
import time
import urllib.request

start = time.time()

for i in range(1,100): urllib.request.urlopen("http://wwww.google.com").read()

end = time.time()
print(end - start)
