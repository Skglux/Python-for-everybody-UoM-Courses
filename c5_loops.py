
largest = None
smallest = None


while True:
    arithmos = input("Please enter an integer number, if you would like to exit, enter 'done'.")
    if arithmos == "done":
        break
    else:
        try:
            iarithmos = int(arithmos)
            if largest is None and smallest is None:
                largest = iarithmos
                smallest = iarithmos
            else:
                if largest < iarithmos:
                    largest = iarithmos
                if smallest > iarithmos:
                    smallest = iarithmos

        except:
            print("Invalid input")

print("Maximum is", largest)
print("Minimum is",smallest)

     