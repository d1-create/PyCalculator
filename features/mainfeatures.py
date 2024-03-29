import features.operators as calcfunctions

#get input for what operation to do
def operationinput():
    #list of operations for easy elif statements
    operations = ["add","subtract","divide","multiply","square root", "square"] 
    #get input and lowercase it
    operator = input("Operation:Add,Subtract,Divide,Multiply or Other? ").lower() 

    #if it is processable then do operation
    if(operator in operations):
        return operator
    #if it cannot be processed then quit the application
    elif(operator not in operations):
        print("Incorrect input, please restart program")
        quit()

#process the data in accordance to the features
def processinput(operator):
    #list of operations for easy elif statements
    operations = ["add","subtract","divide","multiply","square root", "square"] 
    
    #input for 2 numbers
    num1 = float(input("What is your first number "))
    num2 = float(input("What is your second number (if square root skip) "))

    #all if statements
    if(operator == operations[0]):#if add
        output = calcfunctions.Add(num1,num2)
    elif(operator == operations[1]):#if subtract
        output = calcfunctions.Subtract(num1,num2)
    elif(operator == operations[2]):#if divide
        output = calcfunctions.Divide(num1,num2)
    elif(operator == operations[3]):#if multiply
        output = calcfunctions.Multiply(num1,num2)
    elif(operator == operations[4]):#if sqrt
        print("processing the first number")
        output = calcfunctions.sqrt(num1)
    elif(operator == operations[5]):#if square
        output = calcfunctions.power(num1,num2)
    #ENDOFIFSTATEMENTS
        
    #return the output and two numbers for printing
    return output,num1,num2

#output the whole text
def output(operator,answer,num1,num2):
    print(f"You tried to {operator} {num1} and {num2} so you got {answer} as the answer")