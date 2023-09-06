
seconds = input("""Enter a number of seconds, and I will tell you
how many hours, minutes, and seconds it is: """)

seconds = int(seconds)

hours = seconds//3600

remainder = seconds%3600

minutes = remainder//60

remainder2 = remainder%60


print(seconds, "seconds is", hours, "hours,", minutes, "minutes, and", remainder2, "seconds")

