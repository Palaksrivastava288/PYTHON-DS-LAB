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