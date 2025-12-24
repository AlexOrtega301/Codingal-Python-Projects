class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def calculate_addition(self):
        result = self.num1 + self.num2 + self.num3
        print(f"Sum: {result}")


expr1 = Expression(10, 20, 30)
expr1.calculate_addition()

expr2 = Expression(5, 15, 25)
expr2.calculate_addition()

expr3 = Expression(100, 200, 300)
expr3.calculate_addition()

#no expressions were harmed in the making of this code
#epic. codingallll
