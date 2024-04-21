# built-in math module
print(abs(-25))
print(pow(2,4))
print(min(10,20,30,40,50))
print(max(10,20,30,40,50))
print(divmod(17,3))
print(bin(64),oct(64),hex(64))
print(round(2.567),round(2.5678,2))

#mathematical functions from maths module
import math
x=1.5375
print(math.pi,math.e)
print(math.sqrt(x))
print(math.factorial(6))
print(math.fabs(x))
print(math.log(x))
print(math.log10(x))
print(math.exp(x))
print(math.trunc(x))
print(math.floor(x))
print(math.ceil(x))
print(math.trunc(-x))
print(math.floor(-x))
print(math.ceil(-x))
print(math.modf(x))

s = "Bamboozled"
#extract B a
print(s[0]),s[1]
print(s[-10],s[-9])
#extract mboozled
print(s[2:10])
print(s[2:])
print(s[-8])
# extract Bamboo
print(s[0:6])
print(s[-6:])
print(s[-10:4])
print(s[:-4])
# reverse bamboozled
print([-1])

print(s[0:10:1])
print(s[0:10:2])
print(s[0:10:3])
print(s[0:10:3])
print(s[0:10:4])

s=s+'HYPE'
print(s)
s=s[:6]+'Monger'+ s[-1]
print(s)

#the driver should be insured or not
ms =input('enter martial status:')
s = input ('enter sex:')
age =int(input('enter age:'))
if (ms == 'm') or (ms == 'u' and s == 'm' and age>30)\
    or(ms == 'u' and s == 'f' and age>25):
    print('insured')
else:
    print('not insured')

#WAP that prints all unique combination of 1,2 and 3
i=1
while i<=3:
    j=1
    while j<=3:
        k=1
        while k<=3:
            if i == j or j == k or k == i:
                k += 1
                continue
            else:
                print(i, j, k)
            k += 1
        j += 1
    i += 1

# WAP to print square root and cube roots  from 1 to 10
import math
width =10
precision = 4
for n in range(1,10):
    s=math.sqrt(n)
    c=math.pow(n,1/3)
    print(f'{n^5}{s:{width}.{precision}}{c:{width}.{precision}}')

# Perform the following operations on a list names
# create a list of 5 names
names=['Anil','Amol','Aditya','Avi','Alka']
print(names)
#insert a name 'Anuj before aditya'
names.insert(2,'Anuj')
print(names)
#append a name 'Zulu'
names.append('Zulu')
print(names)
# replace 'Anil with' 'Anilkumar'
i= names.index('Anil')
names[i] ='Anilkumar'
print(names)
#sort all the names in the list
names.sort()
print(names)
#print revered sorted list
names.reverse()
print(names)


import random
# Generate a set containing 10 random numbers in the range of 15 to 45
random_numbers_set = set()
while len(random_numbers_set) < 10:
    random_number = random.randint(15, 45)
    random_numbers_set.add(random_number)

print("Original set of random numbers:", random_numbers_set)

# Count how many numbers are less than 30
count_less_than_30 = sum(1 for num in random_numbers_set if num < 30)
print("Count of numbers less than 30:", count_less_than_30)

# Delete all the numbers less than 30 from the set
random_numbers_set = {num for num in random_numbers_set if num >= 30}

print("Set after deleting numbers less than 30:", random_numbers_set)



