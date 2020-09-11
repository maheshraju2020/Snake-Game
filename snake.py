import turtle
import time
import random

delay = 0.1
score = 0
highscore = 0


def boundaries():
    bound = turtle.Turtle()
    bound.penup()
    bound.goto(-270, 250)
    bound.pendown()
    bound.forward(550)
    bound.right(90)
    bound.forward(530)
    bound.right(90)
    bound.forward(560)
    bound.right(90)
    bound.forward(530)
    bound.hideturtle()


class blockcreation:
    block = None
    @staticmethod
    def blockcreation():
        block = turtle.Turtle()
        block.shape("square")
        block.color("grey")
        block.speed(0)
        block.penup()
        block.direction = "stop"
        return block


class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


llnode = llnode1 = None
lastnode = None


class LinkedList:
    @staticmethod
    def Add(dat):
        new_Node = Node()
        new_Node.data = dat
        global llnode, llnode1, lastnode

        if llnode is None:
            llnode = new_Node
            llnode1 = llnode

        else:
            llnode.next = new_Node
            new_Node.prev = llnode
            llnode = llnode.next
            lastnode = llnode


List = LinkedList

# setting up the screen
window = turtle.Screen()
window.title("Snake Game By Raju")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0)  # turns off the screen updates

# snake head
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.penup()
head.direction = "stop"
head.goto(0, 0)
head.speed(0)
List.Add(head)

# snake Food
food = turtle.Turtle();
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

newpen = turtle.Turtle()
newpen.hideturtle()
newpen1 = turtle.Turtle()
newpen1.hideturtle()

pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.speed(0)
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "normal"))


def restart():
    global score
    food.showturtle()
    head.goto(0, 0)
    head.direction = "stop"
    pen.clear()
    newpen.clear()
    newpen1.clear()
    head.showturtle()
    List.Add(head)
    score = 0
    pen.goto(0, 260)
    pen.color("white")
    pen.write("Score: {}  High Score: {}".format(score, highscore), align="center", font=("Arial", 24, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    # daprint(head.direction)
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def deletesnake():
    global llnode1
    food.hideturtle()
    while llnode1 is not None:
        curr = llnode1.data
        curr.hideturtle()
        llnode1 = llnode1.next

    newpen.goto(0, 0)
    newpen.clear()
    newpen1.clear()
    newpen.color("black")
    newpen.write("Game Over\n Score: {}".format(score), align="center", font=("Arial", 30, "normal"))
    newpen.penup()
    newpen1.penup()
    newpen1.goto(0, -100)
    newpen1.color("white")
    newpen1.write("Press y to play again", align="center", font=("Arial", 28, "normal"))
    llnode1 = None
    window.onkeypress(restart, "y")


window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_right, "d")
window.onkeypress(go_left, "a")

# main loop to follow
while True:
    window.update()
    boundaries()

    if (head.distance(food)) < 20:
        x = random.randint(-260, 260)
        y = random.randint(-260, 230)
        food.goto(x, y)
        List.Add(blockcreation.blockcreation())
        score += 1
        if (score > highscore):
            highscore = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highscore), align="center", font=("Arial", 24, "normal"))

    if lastnode is not None:
        lol = lastnode
        lol = lol.prev
        lol1 = lol.prev
        while lol and lol1 is not None:
            d = lol.data
            n = lol.next.data
            x = d.xcor()
            y = d.ycor()
            n.goto(x, y)
            lol = lol.prev

        if llnode1.next is not None:
            x = llnode1.data.xcor()
            y = llnode1.data.ycor()
            llnode1.next.data.goto(x, y)

    if head.xcor() > 260 or head.xcor() < -260 or head.ycor() > 230 or head.ycor() < -260:
        head.direction = "stop"
        llnode = lastnode = None
        deletesnake()
        time.sleep(1)

        # window.onkeypress(restart,"y")

    move()
    temp = llnode1
    if temp is not None:
        while temp.next is not None:
            if (temp.next.data.distance(head)) < 20:
                time.sleep(1)
                head.direction = "stop"
                llnode = lastnode = None
                deletesnake()
                break

            temp = temp.next

    time.sleep(delay)
window.mainloop()