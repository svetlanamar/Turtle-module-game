import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["green", "red", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]

def get_number_of_racers():
    racers=0
    while True:
        racers=input("Enter a number between (2-12): ")
        if racers.isdigit(): #we check if the input we got is numeric to avoid a crash
            racers=int(racers)
        else:
            print("Try again, the input isn't numeric!")
            continue #brings us back to the top of the loop
        if 2<= racers <=12:
            return racers #returns the int and breaks the loop
        else:
            print("Number not in range!") #outputs this and goes back to the start because the input is not a num

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 17) #randomly moves to a distance from 1 to 20 pixels
            racer.forward(distance)
            x, y = racer.pos()
            if y>= HEIGHT//2 - 10:
                return colors[turtles.index(racer)] #returns the winning turtle index

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtles race")

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors=COLORS[:racers] #slice up to the num of racers
winner = race(colors)
time.sleep(1)
print("The turtle that has won this time is:", winner)
