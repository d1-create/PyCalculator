#import all necessary items
import features.mainfeatures as mainfeatures

def main():
    #find what operation the user wants to do
    operator = mainfeatures.operationinput()

    #process the input with numbers to do the calculation
    answer,num1,num2 = mainfeatures.processinput(operator)
    
    #output the text showing the answer
    mainfeatures.output(operator,answer,num1,num2)

main()