def base():
	
	ageList = []
	for i in range(0,3):  #3x megy végbe a ciklus
		age =int( input("Kor: "))
		ageList.append( age )
	
	average = ageAverage( ageList)	
	print("A korok átlaga:  {:>10.2f} év".format(average))
	

def ageAverage(ageList):
	
	average = (ageList[0]+ageList[1]+ageList[2])/len(ageList)
	
	return average
	
	
base()	
