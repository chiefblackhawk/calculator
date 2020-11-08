#Calculator v1.1 that allows for two integers to execute a few arithmetic methods such as addition, subratction, and so forth...

class Calculator():
	def __init__(self, num1, num2):
		super(Calculator, self).__init__()
		self.num1 = num1
		self.num2 = num2

	def addition(self):
		print(f"The sum of {self.num1} and {self.num2} is {self.num1+self.num2}")

	def subtraction(self):
		print(f"The difference of {self.num1} and {self.num2} is {self.num1-self.num2}")

	def multiplication(self):
		print(f"The profuct of {self.num1} and {self.num2} is {self.num1*self.num2}")

	def division(self):
		print(f"The quotient of {self.num1} and {self.num2} is {self.num1/self.num2}")


def main():
	print("Welcome to the Calculator")
	num_list = []
	
	On = True
	while On:
		try:
			number1 = int(input("Please enter your first number: "))
			number2 = int(input("Please enter your second number: "))
		except ValueError:
			print("You must use an integer value in the calculator.")
			continue
		else:
			my_instance = Calculator(number1, number2)

			function = input("Enter 'a' for addition, 's' for subtraction, 'm' for multiplication, 'd' for division, or 'q' to quit.")
			if function in ['addition', 'ADDITION', 'a', 'A', 'add', 'Add', 'ADD']:
				my_instance.addition()
			elif function in ['subtraction','SUBTRACTION','s','S','subtract','Subtract','SUBTRACT']:
				my_instance.subtraction()
			elif function in ['multiplication','MULTIPLICATION','m','M','multiply','Multiply','MULTIPLY']:
				my_instance.multiplication()
			elif function in ['division','DIVISION','d','D','divide','Divide','DIVIDE']:
				my_instance.division()
			elif function in ['quit','QUIT','q','Q']:
				print("Quiting calculator program...")
				break
			else:
				print("Invalid entry...")

if __name__ == '__main__':
	main()
