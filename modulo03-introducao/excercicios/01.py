from numpy import True_


myString = "Is this a string?"
myInt = 42
myFloat = 3.1415
myBool = True

myArrayOfTypes = [myString, myInt, myFloat, myBool]

for i in range(len(myArrayOfTypes)):
    print(f"What type is this? : {myArrayOfTypes[i]} => This is a {type(myArrayOfTypes[i])}")