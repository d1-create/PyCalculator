import features.operators as calcfunctions

#get input for what operation to do
def operationinput():
    operations = ["add","subtract","divide","multiply","other"] #list of operations for easy elif statements
    operator = input("Operation:Add,Subtract,Divide,Multiply or Other? ").lower() #get input and lowercase it
    
    if(operator in operations):#if it is processable then do operation
        return operator
    elif(operator not in operations):
        print("Incorrect input, please restart program")
        quit()

#process the data in accordance to the features
def processinput(operator):
    operations = ["add","subtract","divide","multiply","other"] #list of operations for easy elif statements
    
    #input for 2 numbers
    num1 = float(input("What is your first number "))
    num2 = float(input("What is your second number "))

    #all if statements
    if(operator == operations[0]):#if add
        output = calcfunctions.Add(num1,num2)
    elif(operator == operations[1]):#if subtract
        output = calcfunctions.Subtract(num1,num2)
    elif(operator == operations[2]):#if divide
        output = calcfunctions.Divide(num1,num2)
    elif(operator == operations[3]):#if multiply
        output = calcfunctions.Multiply(num1,num2)
    return output,num1,num2