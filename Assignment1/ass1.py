import time
import hashlib
 
string1 = input("Enter the string: ")
string2 = string1
Flag = 1
i = 1
StartTime = time.time()
while Flag==1:
  bytes = string2.encode(encoding='UTF-8',errors='strict')       # this is to read the file as bytes
  Hash = hashlib.sha256(bytes).hexdigest();
  Flag2=1
  for j in range(0,5):
    if Hash[j]!='0':
      Flag2=0
      break
  if Flag2==1:
    print("The hash value is",Hash)  
    print("The nonce value is",i-1)
    Flag=0
  string2 = string1 + str(i)
  i+=1  
print("Time taken: %s seconds" % (time.time() - StartTime))