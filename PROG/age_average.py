#bekerünk 3 adatot,beletesszök egy listába (ageList) és számolunk velük

def base():
	
	ageList=[]
	for i in range(0,3):
		age = int(input("Kor: "))
		ageList.append(age)
	
	average = ageAverage(ageList)
	print("A korok átlaga {:>10.2f} év".format(average))


def ageAverage( ageList ):
	
	#average = (ageList[0]+ageList[1]+ageList[3]) /len(ageList)
	
	sumAge =0
	for i in range(len(ageList)):
		sumAge += ageList[i]
	
	average = sumAge / len(ageList)
	
	return average
	

base()
