#Angelica ACOSTA ARTETA

#Function that returns the result of adding all the elements of an array 
def summing(array):
	total=0
	for x in range(len(array)):
		total+=array[x]
	return total

#Function that returns a string made of all the elements of an array 
def stringarray(array):
	string=""
	for x in range(len(array)):
		string+=str(array[x])+" "
	return string

#Function that determines the minimum weight needed to represent n
def need(n):
	total=1
	top=1
	i=0
	while total<n:
		top*=3
		total+=top
		i+=1	
	return(top, i)

print("Please write how much you want to weight: ")
inp=input()
inp=int(inp)
current, i=need(inp)

add=[]				#Right side of the balance
sub=[inp]			#Left side of the balance
missing=inp			#How much do we need to weight
substracting=False	#Variable that represents if we have weighted more than needed

#Loop that goes from the maximum weight needed to the smallest one
for j in range(i+1):

	#If we already finished weighting we exit the loop
	if missing==0:
		break

	#If the current weight is bigger than the maximum needed we skip 
	elif need(missing)[0]<current:
		current=int(current/3)
		pass	

	#If we weighted more than needed
	if substracting:
		sub.append(current) #We add the current weight to the left side of the balance

		#If we need to keep weighting on the right
		if summing(sub)>summing(add):
			substracting=False
			missing=summing(sub)-summing(add)

		else:
			missing=summing(add)-summing(sub)

	#If we have not weighted enough
	else:
		add.append(current) #We add the current weight to the right side of the balance

		#If we need to keep weighting on the left
		if summing(add)>summing(sub):
			substracting=True
			missing=summing(add)-summing(sub)		
		else:
			missing=summing(sub)-summing(add)
	
	current=int(current/3) #We obtain the next smaller weight

#We print both sides of the balance
print("right: "+stringarray(add))
print("left: "+stringarray(sub))