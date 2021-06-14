import turtle


def draw_square(t, size):
    '''Draw a square

    Parameters:
        t (Turtle object): Turtle (pen) that will draw the square
        size (int): The length of each side of the square
    '''
    t.begin_fill()
    t.right(90)
    t.forward(size/2)
    t.left(90)

    for i in range(3):
        t.forward(size)
        t.left(90)
        
    t.forward(size/2)
    t.left(90)
    t.end_fill()

def draw_circle(t, size):
    '''Draw a circle

    Parameters:
        t (Turtle object): Turtle (pen) that will draw the circle
        size (int): The diameter of the circle
    '''
    t.begin_fill()
    t.right(90)
    t.circle(size/2)
    t.left(90)
    t.end_fill()

def draw_rhombus(t, size):
    '''Draw a rhombus

    Parameters:
        t (Turtle object): Turtle (pen) that will draw the circle
        size (int): The diagonal of the circle
    '''
    t.begin_fill()
    t.right(90)
    t.circle(size/2, steps=4)
    t.left(90)
    t.end_fill()


def draw_branch_up(t, branch_up):
    '''Draw a vertical branch

    Parameters:
        t (Turtle object): Turtle (pen) that will draw the branch
        branch_up (int): The length of the branch
    '''
    t.forward(branch_up)

def draw_branches(turtle1, turtle2, branch):
    '''Draw horizontal branches

    Parameters:
        turtle1 (Turtle object): Turtle (pen) that will draw the branch going left
        turtle2 (Turtle object): Turtle (pen) that will draw the branch going right
        branch (int): The length of each horizontal branch
    '''
    turtle1.left(90)
    turtle1.forward(branch)
    turtle1.right(90)
    turtle2.forward(branch)
    turtle2.left(90)

def jump_up(t, size):
    '''Make a turtle "jump" upwards a distance equal to the size variable divided by two

    Parameters:
        t (Turtle object): Turtle (pen) that will do the "jump"
        size (int): The height of each shape (corresponding to the jumping distance multiplied by two)
    '''
    t.penup()
    t.sety(t.ycor() + size/2)
    t.pendown()

def write_name(t, name):
    '''Write the name of a family member 

    Parameters:
        t (Turtle object): Turtle (pen) that will write the name
        name (str): The name of the family member
    '''
    t.write(name, align='center')

def set_fillcolor(t, name, number):
    '''Ask the user if a person (name) is alive and set the fillcolor for t accordingly

    Parameters:
        t (Turtle object): Turtle (pen) for which to set the fillcolor
        name (str): The name of the family member
        number (str): Number for when the family member is added to the tree (1-15)
    '''
    while True:
        try:
            alive = turtle.textinput(f'Person number {number}', f'Is {name} alive? Enter yes or no').lower()
            if alive == 'yes':
                t.fillcolor(alive_color)
                break
            elif alive == 'no':
                t.fillcolor(dead_color)
                break
        except:
            pass


# Declare variables determining the size of different components of the tree
size = 80
branch_up = 20
branch = 196

# Ask the user about color settings
wn = turtle.Screen()
while True:
    try:
        wn_color = turtle.textinput("Let's start!", '''What background color do you want? Enter a color name (e.g. green) or hex code (e.g. #86ff94). 
Please note that the darker color you choose, the harder will it be to see the tree.''')
        wn.bgcolor(wn_color)
        if 'yes' == turtle.textinput('Confirmation of color choice', 'Is this the background color you want? If so, write yes'):
            break
    except:
        pass

while True:
    try:
        alive_color = turtle.textinput('Color settings', '''What color should represent those who are alive? Enter a color name (e.g. green) or hex code (e.g. #86ff94). 
Please note that the darker color you choose, the harder will it be to see the name.''')
        wn.bgcolor(alive_color)
        if 'yes' == turtle.textinput('Confirmation of color choice', 'Is this the color you want for those who are alive? If so, write yes'):
            wn.bgcolor(wn_color)
            break
    except:
        pass

while True:
    try:
        dead_color = turtle.textinput('Color settings', '''What color should represent those who are dead? Enter a color name (e.g. green) or hex code (e.g. #86ff94). 
Please note that the darker color you choose, the harder will it be to see the name.''')
        wn.bgcolor(dead_color)
        if 'yes' == turtle.textinput('Confirmation of color choice', 'Is this the color you want for those who are dead? If so, write yes'):
            wn.bgcolor(wn_color)
            break
    except:
        pass

# Create the first Turtle object
t1 = turtle.Turtle()
t1.shape('turtle')


# Write legend
t1.penup()
t1.setposition(-370, -180)
t1.pendown()
t1.write('FILLCOLOR | STATUS', font=('Georgia', 10, 'bold'))

for a, b, c in ((-200, alive_color, 'Alive'), (-220, dead_color, 'Dead')):
    t1.penup()
    t1.setposition(-330, a)
    t1.pendown()
    t1.fillcolor(b)
    t1.begin_fill()
    t1.circle(8)
    t1.end_fill()
    t1.penup()
    t1.setx(-260)
    t1.pendown()
    t1.write(c, font=('Georgia', 9))

t1.penup()
t1.setposition(-350, -250)
t1.pendown()
t1.write('SHAPE       |     SEX', font=('Georgia', 10, 'bold'))

for d, e in ((-270, 'Female'), (-290, 'Male'), (-310, 'Intersex')):
    t1.penup()
    t1.setposition(-245, d)
    t1.pendown()
    t1.write(e, align='center', font=('Georgia', 9))

t1.penup()
t1.setposition(-330, -270)
t1.pendown()
t1.circle(8)

t1.penup()
t1.setposition(-324, -289)
t1.pendown()
t1.left(45)
t1.circle(9, steps=4)
t1.right(45)

t1.penup()
t1.setposition(-330, -310)
t1.pendown()
t1.circle(8, steps=4)


# Position t1
t1.penup()
t1.setposition(0, -250)
t1.pendown()
t1.setheading(90)

# Create person number one
p1_name = turtle.textinput('Person number 1', 'Enter the name of the person whose family tree we are creating:').capitalize()
set_fillcolor(t1, p1_name, 1)

while True:
    try:
        p1_sex = turtle.textinput('Person number 1', f"What is {p1_name}'s sex (female, male or intersex)?").lower()
        if p1_sex == 'female':
            draw_circle(t1, size)
            break
        elif p1_sex == 'male':
            draw_square(t1, size)
            break
        elif p1_sex == 'intersex':
            draw_rhombus(t1, size)
            break
    except:
        pass

jump_up(t1, size)
write_name(t1, p1_name)
jump_up(t1, size)
draw_branch_up(t1, branch_up)

# Create the second Turtle object
t2 = turtle.Turtle()
t2.shape('turtle')

# Position t2
t2.penup()
t2.setposition(t1.position())
t2.pendown()

# Create two branches originating from the same point
draw_branches(t1, t2, branch)

# Start working on the left branch
draw_branch_up(t1, branch_up)

# Create person number two (p1's mother)
p2_name = turtle.textinput('Person number 2', f"Enter the name of {p1_name}'s mother:").capitalize()
set_fillcolor(t1, p2_name, 2)
draw_circle(t1, size)

jump_up(t1, size)
write_name(t1, p2_name)
jump_up(t1, size)
draw_branch_up(t1, branch_up)

# Create the third Turtle object
t3 = turtle.Turtle()
t3.shape('turtle')

# Position t2
t3.penup()
t3.setposition(t1.position())
t3.pendown()

# Create two branches originating from the same point
draw_branches(t1, t3, branch/2)

# Start working on the left branch
draw_branch_up(t1, branch_up)

# Create person number three (p2's mother)
p3_name = turtle.textinput('Person number 3', f"Enter the name of {p2_name}'s mother:").capitalize()
set_fillcolor(t1, p3_name, 3)
draw_circle(t1, size)

jump_up(t1, size)
write_name(t1, p3_name)
jump_up(t1, size)
draw_branch_up(t1, branch_up)

# Create the fourth Turtle object
t4 = turtle.Turtle()
t4.shape('turtle')

# Position t2
t4.penup()
t4.setposition(t1.position())
t4.pendown()

# Create two branches originating from the same point
draw_branches(t1, t4, branch/4)

# Start working on the left branch
draw_branch_up(t1, branch_up)

# Create person number four (p3's mother)
p4_name = turtle.textinput('Person number 4', f"Enter the name of {p3_name}'s mother:").capitalize()
set_fillcolor(t1, p4_name, 4)
draw_circle(t1, size)

jump_up(t1, size)
write_name(t1, p4_name)

# Write title
t1.penup()
t1.setposition(0, t1.ycor()+80)
t1.pendown()
t1.write(f"{p1_name}'s Family Tree", align='center', font=('Georgia', 30, 'bold'))
t1.penup()
t1.sety(t1.ycor()-20)
t1.pendown()
t1.write('GitHub: @the-exceptional-exception', align='center', font=('Georgia', 15))
t1.penup()
t1.home()

# Create person number five (p3's father)
draw_branch_up(t4, branch_up)
p5_name = turtle.textinput('Person number 5', f"Enter the name of {p3_name}'s father:").capitalize()
set_fillcolor(t4, p5_name, 5)
draw_square(t4, size)

jump_up(t4, size)
write_name(t4, p5_name)
t4.penup()
t4.home()

# Create person number six (p2's father)
draw_branch_up(t3, branch_up)
p6_name = turtle.textinput('Person number 6', f"Enter the name of {p2_name}'s father:").capitalize()
set_fillcolor(t3, p6_name, 6)
draw_square(t3, size)

jump_up(t3, size)
write_name(t3, p6_name)
jump_up(t3, size)
draw_branch_up(t3, branch_up)

# Create two branches originating from the same point
t1.setposition(t3.position())
t1.pendown()
draw_branches(t3, t1, branch/4)

# Start working on the left branch
draw_branch_up(t3, branch_up)

# Create person number seven (p6's mother)
p7_name = turtle.textinput('Person number 7', f"Enter the name of {p6_name}'s mother:").capitalize()
set_fillcolor(t3, p7_name, 7)
draw_circle(t3, size)

jump_up(t3, size)
write_name(t3, p7_name)
t3.penup()
t3.home()

# Create person number eight (p6's mother)
draw_branch_up(t1, branch_up)
p8_name = turtle.textinput('Person number 8', f"Enter the name of {p6_name}'s father:").capitalize()
set_fillcolor(t1, p8_name, 8)
draw_square(t1, size)

jump_up(t1, size)
write_name(t1, p8_name)
t1.penup()
t1.home()

# Move on to the right branch
draw_branch_up(t2, branch_up)

# Create person number nine (p1's father)
p9_name = turtle.textinput('Person number 9', f"Enter the name of {p1_name}'s father:").capitalize()
set_fillcolor(t2, p9_name, 9)
draw_square(t2, size)

jump_up(t2, size)
write_name(t2, p9_name)
jump_up(t2, size)
draw_branch_up(t2, branch_up)

# Create two branches originating from the same point
t1.setposition(t2.position())
t1.pendown()
draw_branches(t2, t1, branch/2)

# Start working on the left branch
draw_branch_up(t2, branch_up)

# Create person number ten (p9's mother)
p10_name = turtle.textinput('Person number 10', f"Enter the name of {p9_name}'s mother:").capitalize()
set_fillcolor(t2, p10_name, 10)
draw_circle(t2, size)

jump_up(t2, size)
write_name(t2, p10_name)
jump_up(t2, size)
draw_branch_up(t2, branch_up)

# Create two branches originating from the same point
t3.setposition(t2.position())
t3.pendown()
draw_branches(t2, t3, branch/4)

# Start working on the left branch
draw_branch_up(t2, branch_up)

# Create person number eleven (p10's mother)
p11_name = turtle.textinput('Person number 11', f"Enter the name of {p10_name}'s mother:").capitalize()
set_fillcolor(t2, p11_name, 11)
draw_circle(t2, size)

jump_up(t2, size)
write_name(t2, p11_name)
t2.penup()
t2.home()

# Create person number twelve (p10's father)
draw_branch_up(t3, branch_up)
p12_name = turtle.textinput('Person number 12', f"Enter the name of {p10_name}'s father:").capitalize()
set_fillcolor(t3, p12_name, 12)
draw_square(t3, size)

jump_up(t3, size)
write_name(t3, p12_name)
t3.penup()
t3.home()

# Create person number thirteen (p9's father)
draw_branch_up(t1, branch_up)
p13_name = turtle.textinput('Person number 13', f"Enter the name of {p9_name}'s father:").capitalize()
set_fillcolor(t1, p13_name, 13)
draw_square(t1, size)

jump_up(t1, size)
write_name(t1, p13_name)
jump_up(t1, size)
draw_branch_up(t1, branch_up)

# Create two branches originating from the same point
t2.setposition(t1.position())
t2.pendown()
draw_branches(t1, t2, branch/4)

# Start working on the left branch
draw_branch_up(t1, branch_up)

# Create person number fourteen (p13's mother)
p14_name = turtle.textinput('Person number 14', f"Enter the name of {p13_name}'s mother:").capitalize()
set_fillcolor(t1, p14_name, 14)
draw_circle(t1, size)

jump_up(t1, size)
write_name(t1, p14_name)
t1.penup()
t1.home()

# Create person number fifthteen (p13's father)
draw_branch_up(t2, branch_up)
p15_name = turtle.textinput('Person number 15', f"Enter the name of {p13_name}'s father:").capitalize()
set_fillcolor(t2, p15_name, 15)
draw_square(t2, size)

jump_up(t2, size)
write_name(t2, p15_name)

for t in wn.turtles():
    t.hideturtle()

turtle.done()