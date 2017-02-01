import urllib2
import time

start = time.time()

max=0

min=100000

for i in range(1,100):
    start2 = time.time() 
    urllib2.urlopen("http://ec2-54-221-10-32.compute-1.amazonaws.com/do5xb-healthcare/").read()
    end2 = time.time()
    if end2-start2 < min : min=end2-start2 
    if end2-start2 > max : max=end2-start2 
        
end = time.time()

print("average max and min are respectively ",  (end - start)/100, max, min)

