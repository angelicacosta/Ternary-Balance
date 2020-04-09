# Author
# Angelica ACOSTA ARTETA

#Function that returns the result of adding all the elements of an array 
def summing(array):
	total=0
	for x in range(len(array)):
		total+=array[x]
	return total

#Function that returns a string made of all the elements of an array 
def stringarray(array):
	try:
		string=str(array[0])
		for x in range(1,len(array)):
			string+=", "+str(array[x])
	except:
		string=""
	
	return string

#Function that determines the minimum weight needed to represent n
def need(n):
	if n>0:
		total=1
		top=1
		i=0
		while total<n:
			top*=3
			total+=top
			i+=1	
		return(top, i)
	else:
		return(None,None)

def weighting(user_input):
	
	left_side 			= [user_input]
	right_side			= []
	missing_to_weight 	= user_input
	substracting		= False
	current_weight, current_power = need(user_input)
	
	# Loop that goes from the maximum weight needed (current) to the smallest one
	while(current_power>=0):

		# If we already finished weighting we exit the loop
		if missing_to_weight==0:
			break

		# If the current weight is bigger than the maximum needed to weigth current then we skip 
		elif need(missing_to_weight)[0]<current_weight:
			current_weight, current_power=need(missing_to_weight) # The current weight will now be the maximum needed that
									# corresponds to 3 to the power of i
			continue	

		# If we weighted more than needed
		if substracting:
			left_side.append(current_weight) # We add the current weight to the left side of the balance

			# If we need to keep weighting on the right
			if summing(left_side)>summing(right_side):
				substracting=False
				missing_to_weight=summing(left_side)-summing(right_side)

			else:
				missing_to_weight=summing(right_side)-summing(left_side)

		# If we have not weighted enough
		else:
			right_side.append(current_weight) # We add the current weight to the right side of the balance

			# If we need to keep weighting on the left
			if summing(right_side)>summing(left_side):
				substracting=True
				missing_to_weight=summing(right_side)-summing(left_side)		
			else:
				missing_to_weight=summing(left_side)-summing(right_side)
		
		current_weight=int(current_weight/3) # We obtain the next smaller weight
		current_power-=1					 # That corresponds to the next smaller power 
	
	return (left_side, right_side)


if __name__ == '__main__':
	while True:
	# We ask the user to specify how much would he like to weight
		inp=input("Please write how much you want to weight: ")

		# We try to convert the input into an integer
		try:
			inp=int(inp)

			# If the input is negative or 0 we'll display an error message
			# and continue the loop to ask for a number again
			if inp<1:
				print("Error: the input must be a positive integer. Please try again.\n")

			# However if the input is a positive integer we can weight
			# and exit the loop
			else:
				break
	
		# If the input is not an integer then we'll display an error message
		# and continue the loop to ask for a number again
		except ValueError:
			print("Error: the input must be a positive integer. Please try again.\n")

	sub, add = weighting(inp)

	print("left: "+stringarray(sub))
	print("right: "+stringarray(add))