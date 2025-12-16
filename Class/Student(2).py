class student:
	grade = 8
	name = "Alex"
	
	def introduction(self):
		print("Hi I am a student")

	def details(self):
		print("My name is", self.name)
		print("I study in Grade", self.grade)

ob = student()
ob.introduction()
ob.details()

