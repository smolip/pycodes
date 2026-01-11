m = [{1:{1:(1,2,3)},2:[9,8,0]}]

print(type(m))
print(type(m[0]))
print(type(m[0][1]))
print(type(m[0][1][1]))
print(type(m[0][1][1][1]))

print(len(m[0][1][1]))

print()

import math

y=lambda x: x*4
print(int(y(math.pi)))
print(int(math.pi))
print(math.pi)

print()

from collections import namedtuple
singer = namedtuple("Singer",["voice","music","country"])
Bocelli=singer("baryton","opera","Italy")
Madonna=singer("sopran","pop","USA")
Cash=singer("baryton","country","USA")
songs={Cash.music:Cash, Bocelli.music:Bocelli, Madonna.music:Madonna}

print(songs.keys())

print()

list_of_elements ={'0': 0, '1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18,'J': 19,   'K': 20,'L': 21,'M': 22,'N': 23,'O': 24,'P': 25,'Q': 26,'R': 27,'S': 28,'T': 29,'U': 30,'V': 31,'W': 32,'X': 33,'Y': 34,'Z': 35}

l={k.lower():v
    for k,v in list_of_elements.items() if k.isdigit() and int(k) > 5}

print(l)

print()

a="The sixth sick sheikh's sixth sheep's sick"
b=set(a.split("'s "))

print(b)

print()

x = [(1,12),('A',8),(7,5)]
temp = []

for i in range(len(x)):
    temp.append(x[i][1])

print(max(temp))
print(min(temp))

print()

a = 13
all(a % i for i in range(2, a))	


def divide(x, y):
	try:
		result = x / y
	except TypeError:
		print("You cannot divide by yero!")
	else:
		print("Result is", result)
	finally:
		print("Never give up")

divide(5,2)

print()


while True:
    x=input("Enter digit, q for quit: ")
    if x.upper() == "Q":
        break
    elif x.isdigit():
        print(x)



                                           





