import time
import urllib.request

start = time.time()

max=0

min=100000

for i in range(1,100):
    start2 = time.time() 
    urllib.request.urlopen("http://wwww.google.com").read()
    end2 = time.time()
    if end2-start2 < min : min=end2-start2 
    if end2-start2 > max : max=end2-start2 
        
end = time.time()
print("average is ",  (end - start)/100)
print("max is ",  max)
print("min is ",  min)

    
    
    
    