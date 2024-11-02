#Create a string first
S="Hello World"
St="Hello Friend"
Str="Hello You"

#input string and reverse input (output)
def Strings(S1,S2,S3):
    Answer=S1[::-1]+S2[::-1]+S3[::-1]
    return Answer 
print(Strings(S,St,Str))

# String 1
S=input("enter string one")

# String 2
St=input("enter string two")

# String 3
Str=input("enter string three")

# send the string back to the user. It is reversed in block 2 above
print(Strings(S,St,Str))