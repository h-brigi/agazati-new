corp01 =1.8
corp02 = 2.8
corp03 = 1.98

corpAverage = ( corp01 + corp02 + corp03) /3

if (corpAverage <2):
	print ("Az átlag {:^10.3f} tonna. Szükség van újabb táblára.".format(corpAverage))
	
else:
	print("Az átlag {:^10.3f} tonna. Nincs szükség újabb táblára.".format(corpAverage))

