rows=int(input("Enter the no.of rows:"))
"""
THIS IS AN CONCEPT TO PRINT DIAMOND 
for i in range(0, rows):
     for j in range(0, rows-i-1):
         print(" ",end="")
         for j in  range(0, i+1):
            print("* ",end="")
            print()

for i in range(0,rows-1):
    for j in range(0,i+1):
        print(" ",end="")
        for j in range(0,rows-i-1):
            print("* ",end="")
            print() 
"""
for i in range(rows):
    print(" "*(rows-i-1) + "* "*(i+1))#First print space 5-0-1=4 give four space,
    #print star i+1=0+1=1 in first row that will print one star
for j in range(rows-1):
    print(" "*(j+1) +"* "*(rows-1-j))
    # For lower triangle first print space j+1=0+1=1 print one space ,and print stars rows-j-1=5-0-1=4 print four stars

           




