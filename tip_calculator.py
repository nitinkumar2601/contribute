def tip_calculator():
    print("Enter your total bill value.")
    Bill = int(input())
    print("Enter the percentage of tip you are wishing to give")
    tip_percentage = int(input())
    print("Tip amount will be : ")
    print(Bill*tip_percentage*0.01)
