#def divisors(n):
#n = int(input("input number"))
#x=0
#while x < n:
#x+=1
#if n%x ==0:
#print(x)
#divisors(6)

word=input("input word")
x=0
y=-1
for i in word:
	x+=1
	y-=1
	if x==len(word)/2:
		break
	if word[x]== word[y]:
		print("True")
	

		
			


	
	
