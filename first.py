num1=float(input("enter the first number: "));
num2=float(input("enter the second number: "));
operations=input("enter the operation(+ - * /): ");

def add(num1,num2):
  return num1+num2;
def Subtract(num1,num2):
  return num1-num2;
def Multiply(num1,num2):
  return num1*num2;
def divide(num1,num2):
  return num1/num2;
def modlus(num1,num2):
  return num1%num2;

if operations=="+":
  print(add(num1,num2));
elif operations=="-":
  print(Subtract(num1,num2));
elif operations=="*":
  print(Multiply(num1,num2));
elif operations=="/":
  print(divide(num1,num2));
elif operations=="%":
  print(num1%num2);
  
