#for loop with varible named count within 0-100 (range) (counting up from 1)
for count in range (100):
    #telling count to print these strings with the remainder of the division
    if count % 3 == 0 and count % 5 == 0:
        print("fizzbuzz")
        ## continue will let the program continue counting instead of 
        # printing the number associated with the string
        continue
    if count % 3 == 0:
        print("fizz")
        continue
    if count % 5 == 0:
        print("buzz")
        continue
    #else to continue counting 
    else:
        print(count)