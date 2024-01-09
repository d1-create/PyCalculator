#import all necessary items
import features.mainfeatures as mainfeatures

def main():
    operator = mainfeatures.operationinput()
    answer,num1,num2 = mainfeatures.processinput(operator)
    print(f"You tried to {operator} {num1} and {num2} so you got an answer of {answer}")


main()