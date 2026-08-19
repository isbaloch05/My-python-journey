class Calculator:
    def __init__(self, value):
        '''calculator initializes with a value'''
        self.value = value
    def multiply(self, factor):
        '''then the value is multiplyed by the factor'''
        self.value = self.value * factor
    @staticmethod
    def add(a,b):
        '''gives the sum of two numbers'''
        return a+b
if __name__ =="__main__":
  cal=Calculator(5)
  print(cal.value,)    #the value
  cal.multiply(7)      #the factor
  print(cal.value)     #value*factor
  result=cal.add(4,8)
  print(result)