#def divisors(n):
#n = int(input("input number"))
#x=0
#while x < n:
#x+=1
#if n%x ==0:
#print(x)
#divisors(6)

#word=input("input word")
#x=0
#y=-1
#for i in word:
#x+=1
#y-=1
#if x==len(word)/2:
#break
#if word[x]== word[y]:
#print("True")
	

		
import random
play="Y"
prob=int(input("input probabilty of TAILS (ex:25 / 50) : " ))
division = 100/prob
minus = division - 1
while play=="Y":
   tails=random.randint(0,prob)
   if tails==0:
       print("YOU GOT TAILS")
   else:
       print("YOU GOT HEADS") 
   play = input("would you like to play? [Y/N]" )


#coinflips=int(input("how many times do you want to flip coin? "))
#for i in range(coinflips):
#tails=random.randint(0,1)
#if tails==0:
#print("YOU GOT TAILS")
#else:
#print("YOU GOT HEADS")


#for i in range(0,3):
#name=input("input name")
#age=input("input age")
#d1={"name":name,"age": age}
#d2={"name":name,"age": age}
#d3={"name":name,"age": age}
#datalist=[d1,d2,d3]
#print(datalist)





	
	
