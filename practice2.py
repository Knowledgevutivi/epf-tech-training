first =-0
sec= 1
count = 0
sum = 0

while count < 4000000:
    sum = first + sec
    first = sec
    sec = sum
    
    if sum % 2 ==0:
        count = sum + count
        
print(count)