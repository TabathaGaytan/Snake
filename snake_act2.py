from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
movimientos_food = [ vector(-10,0), vector(10,0), vector(0,-10), vector(0,10)] 
aim = vector(0, -10)
color_snake ='pink' #colores de inicio
color_food = 'yellow'


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190 #limites del snake 

def move():
    global color_snake, color_food
    "Move snake forward one segment."
    head = snake[-1].copy() #movimiento del snake
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red') #cuando topa con las esquinas y se termina el juego
        update()
        return

    snake.append(head) #agregar largo al snake
    
    newcolor_snake = ('pink', 'blue','yellow', 'green', 'black') #variable de colores
    newcolor_food = ('yellow', 'black','pink', 'green','blue' )

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        color_snake = newcolor_snake[randrange(0,5)] #escoge alateoriamente los colores
        color_food = newcolor_food[randrange(0,5)]
    else:
        snake.pop(0)
        #mover comida aleatoriamente
        food.move(movimientos_food[randrange(0,4)])

    clear()

#dibuja cuerpo
    for body in snake:
        square(body.x, body.y, 9, color_snake)

#dibuja comida
    square(food.x, food.y, 9, color_food)
    update()
    ontimer(move, 1000) #velocidad

setup(420, 420, 370, 0) #margenes
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right') #movimientos del teclado
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
