import os

from employee import Employee
from datetime import datetime


class Worker: 
	
	def __init__(self):
		
		self.workerList = []
		self.read()
		self.countWorker()
		self.sumSzeged()
		self.averageSzolnokMoney()
		self.getYoungest()
		
			
	def read( self):
		
		if( os.path.exists("employee.txt")): #ell. hogy a könyvtárban van e ilyen fajl
			
			file = open("employee.txt", "r", encoding = "utf-8")
			file.readline()			
			
			row = file.readline()
			
			while(row):
				worker =Employee()
				
				spWorker= row.split(":")
				
				worker.name = spWorker[0]
				worker.city = spWorker[1]
				worker.address = spWorker[2]
				worker.salary = spWorker[3]
				worker.bonus = spWorker[4]
				worker.borndate = spWorker[5]
				worker.hiredate = spWorker[6]
				
				self.workerList.append( worker)
				row = file.readline()
				
			file.close()
			print ("A fájl beolvasás sikeres.")
			
		else:
			print ("A fájl nem létezik.")
			

	def countWorker(self):
		
		counter =0
		
		for i in self.workerList:
			counter += 1
			
		print("A dolgozók száma {}".format(counter))

	def sumSzeged(self):
		
		sumSalary=0
		for worker in self.workerList:
			
			if(worker.city == "Szeged"):
				sumSalary += int(worker.salary)
		print ("Szegediek fizetés összege:{}".format(sumSalary))

	def averageSzolnokMoney(self):
		
		sumMoney = 0
		counter = 0
		for worker in self.workerList:
			
			if (worker.city == "Szolnok"):
				
				sumMoney += (int(worker.salary)+ int(worker.bonus))
				counter += 1
		
		average = sumMoney /counter
		print ("A szolnokiak átlagos bevétele: {:.2f}".format(average))


	def getYoungest(self):
		
		youngest = self.workerList[0].borndate #bekerült az első ember születési ideje, ehez viszonyítunk
				
		for worker in self.workerList:
			
			date = worker.borndate   #date változó miatt dátumtipust fog gyártani
			if (date < youngest):
				youngest = date
				
		name =""
		for worker in self.workerList:
			
			if (worker.borndate == youngest):
				name = worker.name
						
				print("A legfiatalabb {} született: {}".format(name, youngest))


Worker()
