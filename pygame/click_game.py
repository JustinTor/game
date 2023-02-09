my_character = Actor('blob')
my_character.pos = 100, 50

WIDTH = 500
HEIGHT = 500

def draw():
    screen.clear()
    my_character.draw()

def update():
    my_character.left = my_character.left + 2
