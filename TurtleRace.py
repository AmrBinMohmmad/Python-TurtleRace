import random
import turtle

def setup_screen():
    screen = turtle.Screen()
    screen.title("Turtle Race")
    screen.setup(width=800, height=600)
    screen.bgcolor("White")
    return screen
    

turtle_colors = ["red", "blue", "green", "yellow", "orange", "purple"]    
turtles_racer = []


def create_turtles():
    starting_position = -250
    for color in turtle_colors:
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.penup()
        racer.goto(-350, starting_position)
        racer.pendown()
        turtles_racer.append(racer)
        starting_position += 50

def betting(screen):
    while True:
        bet = screen.textinput("Place your bet", "Choose a turtle color (red, blue, green, yellow, orange, purple): ").lower()
        if bet in turtle_colors:
            print(f"You have placed a bet on the {bet} turtle.")
            return bet
        else:
            print("Invalid color. Please choose from the available colors.")

def race_turtles():
    winner = None
    while not winner:
        for racer in turtles_racer:
            distance = random.randint(1, 10)
            racer.forward(distance)
            if racer.xcor()>=350:
               winner = racer.pencolor()
               print(f"The {winner} turtle wins!")
               return winner

def main():
    scr = setup_screen()
    create_turtles()
    bet = betting(scr)
    winner = race_turtles()
    if bet == winner:
        print("Congratulations! You won the bet.")
    else:
        print(f"Sorry, you lost. The winner was {winner}.")
    scr.exitonclick()
if __name__ == "__main__":
    main()