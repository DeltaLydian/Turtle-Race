from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)

excitement = random.randint(0,3)
if excitement == 3:
    status = "Today is a high intensity game!"
else:
    status = ""

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
accepted = False
while accepted == False:
    user_bet = screen.textinput(title = "TURTLE RACE!",prompt = f"Which turtle will win the race?\nRed, Orange, Yellow, Green, Blue or Purple\n{status}\nTo place your bet,\nEnter a color: " )
    user_bet = user_bet.lower()
    if colors.count(user_bet) == 1:
        accepted = True


#names = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot"]
#for turtle_index in range(0,6):
#     name = names[turtle_index]
#     name = Turtle(shape ="turtle")
#     name.color(colors[turtle_index])
#     name.penup()
#     y_pos = -70 + (30 * turtle_index)
#     name.goto(x=-230, y = y_pos)
#charlie.color("black")


# Create the Racers
all_turtles = []
for turtle_index in range(0,6):
     new_turtle = Turtle(shape ="turtle")
     new_turtle.color(colors[turtle_index])
     new_turtle.penup()

     if new_turtle.pencolor() == user_bet:
        shape = random.randint(4,15)
        size = random.randint(15,75)
        new_turtle.circle(radius=size, steps=shape)

     y_pos = -70 + (30 * turtle_index)
     new_turtle.goto(x=-230, y = y_pos)
     all_turtles.append(new_turtle)



#Create referee:
referee = Turtle(shape = "turtle")
referee.color("black")
referee.penup()
referee.goto(230, 150) #window is from +200 to -200
referee.setheading(270)
referee.pensize(2)
#draw finish line
for _ in range(0,12):
    referee.forward(12.5)
    referee.penup()
    referee.forward(12.5)
    referee.pendown()
# put ref into position for race
referee.penup()
referee.goto(225, -175)
referee.setheading(90)




# Run the race
winning_turtle = []
if excitement == 3:
    speed = 35
else:
    speed = 10
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        # each turtle once more after one of the turtles wins
        # more easily create ties for more interesting races, and compensated red's advantage of going first
        if turtle.xcor() > 230:
            winning_turtle.append(turtle.pencolor())
            is_race_on = False  #the turtle loop continues, to let the rest of the turtles complete their turn

        # responsible for moving the turtles:
        rand_distance = random.randint(0, speed)
        turtle.forward(rand_distance)


# game is over, take score
print("\n")
if len(winning_turtle) > 1:
    if winning_turtle.count(user_bet) == 1:
        print("Although fiercely debated, the race was unfortunately deemed too close to call!  \n No refunds on bets!  Be more careful with your money...")
    else:
        print("Despite there being a tie among the winners, your turtle was still a loser.")
elif len(winning_turtle) == 1:
     if winning_turtle[0] == user_bet:
         print(f"You've won! The {winning_turtle[0]} Racing Turtle is the winner!")
     else:
         print(f"You've lost! The {winning_turtle[0]} Racing Turtle is the winner!")

print(f"\n\nYour bet: {user_bet}")
print(f"Race Leader:  {winning_turtle}")
screen.exitonclick()
