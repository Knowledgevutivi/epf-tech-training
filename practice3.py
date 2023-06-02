num = 600851475143
i = 2

while (num != 1): 
    remind = num%i
   
    if remind == 0:
         num = num /i
         print(i)
    else:
      i = i + 1
     
