#LAB 7 - HURRICANE IRMA TRACKER

#SETUP CODE
import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

# x = longtitude: [-90,-17.66]
# y = latitude: [0,45]


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()
    

    #MY CODE


    #I. Set up Data
    path = open("data/irma.csv", 'r')   #open data file
    lines = path.readlines()
    lat = []                            #list accumulator for latitude
    lon = []                            #list accumulator for longitude
    wind = []                           #list accumulator for wind speed
    total = 0
    for line in lines[1:]:              #omit first line of file (column titles)
        data = line.split(',')          #split values between commas
        lat.append(data[2])         
        lon.append(data[3])
        wind.append(data[4])
    for item in wind:
        total += int(item)
    print(total)
        

    #II. Animate Turtle
    t.speed(0)
    for i in range(len(wind)):          #iterate through all values
        x = float(lon[i])
        y = float(lat[i])
        wind_speed = int(wind[i])
        
        if wind_speed >= 157:           #category 5
            t.color('red')
            t.pensize(9)
            t.write('5')
        elif 130 <= wind_speed <= 156:  #category 4
            t.color('orange')
            t.pensize(7)
            t.write('4')
        elif 111 <= wind_speed <= 129:  #category 3
            t.color('yellow')
            t.pensize(5)
            t.write('3')
        elif 96 <= wind_speed <= 110:   #category 2
            t.color('green')
            t.pensize(3)
            t.write('2')
        elif 74 <= wind_speed <= 95:    #category 1
            t.color('blue')
            t.pensize(2)
            t.write('1')
        else:                           #not hurricane strength
            t.color('white')
        t.goto(x, y)
    
    t.hideturtle()
    
if __name__ == "__main__":
    irma()
