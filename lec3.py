# Practicing the concepts:
# loops concepts:
# find the maximum:
a= 5
if a >3:
    print("Hiii")
else:
    print('10')
if a+2 == 7:
    print('True')
else:
    print('False')

# ways for printing the patterns:
a = input('Enter Any Number: ')
print(f"{a}+{a,a}+{a,a,a}= ", int(a) +int(a+a)+int(a+a+a))
# inpput always takes place in string

# Learning for loop:
for i in range(1,10,1):
    print(i, end=" , ")
print()   
for i in range (10) : 
    print(i, end=" , ")
   
print()   
for i in range(1,10,2):
    print(i, end=" , ")
print()

for i in range(10, 1 , -1):
    print(i, end=" , ")
print()

for i in range(9, 0, -2):
    print(i , end=" , ")
print()

for i in range(10):
    i+= 7
    print(i , end=" , ")
print()

print(len('12346'))

# reversing the number:
num = int(input('Enter any Number: '))
rev =0
digit = len(str(num))
for i in range (digit):
    rem = num % 10
    rev = rev * 10 + rem
    num = num//10
print(rev)


# findin th palindrome number:
num1 = int(input('Enter te Number: '))
temp = num1
digit = len(str(num1))
rev = 0
while num1 > 0:
    rem = num1 % 10
    rev = (rev * 10 )+ rem
    num1 = num1//10
if(rev == temp):
    print(rev)
    print('Number Given is Palindrome')
else:
    print(rev)
    print('Number is not palindrome')
    
    # checking for the armstrong number or not!
num = int(input('Enter The Number: '))
digit = len(str(num))
sum = 0
temp = num
while num>0:
    rem = num%10
    sum += rem**digit 
    num = num//10
if(sum == temp):
    print(sum)
    print("Yes, it's Armstrong Nuber")
else:
    print(sum)
    print('Not an Armstrong Number')
    
# Finding out strong number:
num = int(input('Enter Any Number: '))
temp = num
sum =0

while num > 0:
    rem = num % 10
    print(rem)
    fact = 1
    for i in range(1,rem+1,1):
            fact *= i
    sum += fact
    num = num//10
if(temp == sum):
    print('It is a Strong Number')
else:
    print(fact , sum , temp)
    print('It is not Strong Number')        

# hile loop practice:
n= 7
while n>0:
    print(n)
    n-=1
# break and continue statement:
for i in range(1, 10):
    if(1==5):
        break
    print(i)

# continue Statement:
for i in range(1,10):
    if i==5:
        pass
    print(i)
    
a=5
while a >0:
    if a == 2:
        break
    print(a , end=" , ") 
    a-=1
print()

# taking as many input as from the user and calculate the sum, avg and max min:
a = int(input('Enter the number for Calculating max , min avg:'))
max = a
min = a
sum = a
c =1
while True:
     inp = (input())
     if inp =='done':
         break
     n = int(inp)
     sum += n
     if(max < n):
         max = n
     if(min > n):
         min = n
     c = c +1
     avg = sum/c
print(f"max, min and avg is {max} , {min} , {avg}")