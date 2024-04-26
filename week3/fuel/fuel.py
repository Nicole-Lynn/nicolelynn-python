#Prompt user for a fraction, formatted X/Y, where each of X and Y is an integer. Use split()

while True:
    try:
        fraction = input("Fraction: ")
        X, Y = fraction.split("/")
        X = int(X)
        Y = int(Y)

        #Raise an exception for when X > Y
        if X > Y :
            raise Exception

        #Percentage rounded to the nearest integer
        percentage = round((X/Y) * 100)
        #If 1% or less remains, output E
        if percentage <= 1:
            print("E")
        #If 99% or more remains, output F
        elif percentage >= 99:
            print("F")
        else:
            print(percentage, "%", sep="")

    #If X or Y is not an integer, ValueError,
    #If X is greater than Y, Exception,
    #If Y is 0, ZeroDivisionError,
            # prompt the user again.
    except (ValueError, Exception, ZeroDivisionError):
        pass
    
    else:
        break








