import features.operators

#get input for what operation to do
def operation():
    operations = ["Add","Subtract","Divide","Multiply"] #list of operations for easy elif statements
    operator = str(input("Operation:Add,Subtract,Divide,Multiply or Other?")).lower() #get input and lowercase it
    if(operator == "other"): #get more input if necessary
        #TODO
        pass
    elif(operator == operations[0]):#if add
        return "add"
    elif(operator == operations[1]):#if subtract
        return "subtract"
    elif(operator == operations[2]):#if divide
        return "divide"
    elif(operator == operations[3]):#if multiply
        return "multiply"

#process the data in accordance to the features
def processinput():
    num1 = input("What is your first number")
    num2 = input("What is your second number")
    #TODO