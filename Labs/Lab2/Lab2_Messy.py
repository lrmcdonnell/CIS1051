## changed the single quo to double
print("It’s time to go on a scavenger hunt!")
print("You'd be amazed how many things can go wrong!")
time = input("Please enter how many minutes you want to travel for: ")

time = int(time)

initialPos = 7.0
velocity = 5.0
acceleration = 1.0

position = initialPos + velocity * time + (1/2) * acceleration * time ** 2

print("you are now at the following position:", position)
