def abc(x):
    try:
        print(20/x)
    except:
        print("Wrong ",end="")
    finally:
        print("Cheers ",end="")

abc(0)
abc(10)

#try:
    # kód, který může vyhodit chybu
#except:
    # co se provede, když nastane chyba
#finally:
    # kód, který se provede VŽDY

print(" ")
print(" ")



def call(x,y):
    if y < x:
        return
    return y - x

print(call(8,9)) #1
print(call(9,8)) #None

print(" ")

m = [{1:{1:{1,2,3}},2:{9,8,0}}]
""" print(type(m))
print(type(m[0]))
print(type(m[0][1]))
print(type(m[0][1][1]))
print(type(m[0][1][1][1]))
print(len(m))
 """

# List [] - seznam
# Dict {} - slovník
# Set {} - množina  
# Tuple () - n-tice

#6': 6,'7': 7,'8': 8,'9': 9

list_of_elements ={'0': 0, '1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9, 'A': 10, 'B': 11, 'C':
12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18,'J': 19, 'K': 20,'L': 21,'M': 22,'N': 23,'O': 24,'P':
25,'Q': 26,'R': 27,'S': 28,'T': 29,'U': 30,'V': 31,'W': 32,'X': 33,'Y': 34,'Z': 35}

l={k.lower():v
 for k,v in list_of_elements.items() if v > 5 and k.isdigit()}
print(l) # print all

a="The sixth sick sheikh's sixth sheep's sick"
b=set(a.split("'s "))
print(b)

x = ["Yesterday","Today","Tomorrow","Day after tomorrow"]
b = [(i,j) for i, j in enumerate(x,start=5)]

print(b)
print(type(b[1]))

while True:
 x=input("Enter letter, q for quit: ")
 if x.upper() == "Q":
    break
 else:
    print(x)

def call(v1=20,v2=5,v3=2):
 if v3 > 2:
    print(v1*v2-v3)
 else:
    print(v3)
call(7,4,3)

a = 13
print(any(a % i for i in range(2, a)))

from collections import namedtuple
singer = namedtuple("singer",["voice","music","country"])
Bocelli=singer("baryton","opera","Italy")
Gott=singer("tenor","popmusic","Czechia")
Madonna=singer("sopran","popmusic","USA")

print(Gott.country)

items = "Pythagoras honed his skills"
splt = items.split(" ") # (" ") is one space
print ("Winter = ", splt[0][:4] + splt[1][1:3] + " + " + splt[3][:3]) # what is output?

items = {1: "python", 2: "basics", 3: "examination"}
print(items[3][::1]) # What is output
print(items[3][:1]) # What is output
print(items[3][1]) # What is output
print(items[3][1:3]) # What is output