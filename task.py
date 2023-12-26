# local exampla

def function(n):
    l=8#local
    m=9#local
    print(l,m)
    print(n,"yeah its me")

function("this is me")

#Global example
l=10#global

def function(n):
    #l=8#local
    m=9#local
    print(l,m)
    print(n,"yeah its me")

function("this is me")
print(l)


#indentation
name = 'sam'
if name == 'sam':
    print('hello sam')
else:
    print('Hello dude')
print('How are you')


#if statement
x=5
if x < 50 :
    print("x is less then 50")
print("End of the program")

#Nested if statement 
x =10
if x < 50:
    if x == 10:
        print("x is equal to 10")
    print("x is less then 50")
print("End of the program")

#if else statement
age = 19
if age < 17:
    print ("you cant vote!")
else:
    print("you cant vote!")
print("Done")    

#if-elif-else
x = 5
if x == 5:
    print("x is 5")
elif x < 5:
    print("x is less then 5")
else:
    print("x is greater then 5")
print("Done!")    

#for loop with range(stop)
for i in range (3):
    print(i)
    print("Done!")

#for loop with range(start ,stop)
for i in range (1,3):
    print(i)
print("Done!")        

#for loop with range(start , stop , step)
for i in range (1,10,2):
    print(i)
print("Done!")    
