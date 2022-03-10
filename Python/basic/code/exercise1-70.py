numbers=list()
for num in range(10):
    numbers.append(num)
    
numbers.append(3.14)
print(numbers)

for num in numbers:
    if num%2==0:
        print("Even Number")
    elif num%2==1:
        print("Odd Number")
    else:
        print("Not an Integer")