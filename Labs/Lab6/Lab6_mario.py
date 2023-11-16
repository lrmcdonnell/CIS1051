
#LAB 6 - MARIO, CASH, CREDIT



#MARIO - more comfortable
h = 0
while (h <= 0 or h > 8):    #reprompts for input if not in correct range
    h = int(input("Enter an integer from 1 to 8 (included): "))

def mario(height):
    for row in range(1, height+1):
        print(" " * (height-row) + '#' * row + '  ' + '#' * row + " " * (height-row))
    
mario(h)

