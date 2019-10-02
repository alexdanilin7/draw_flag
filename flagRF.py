import pygame

pygame.init()

size = width, height = 600, 400

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Флаг России")
screen.fill((117, 187, 253))


def draw_flagshtok():
    rect_color = pygame.Color("black")
    rect_width = 0
    rect_point = [(20, 10), (2, 280)]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)
    pygame.draw.rect(screen, rect_color, [(10, 270),(50, 20)], rect_width)

def draw_BlueRect():
    rect_color = pygame.Color("blue")
    rect_width = 0
    rect_point = [(22, 40), (100, 30)]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)
def draw_WhiteRect():
    rect_color = pygame.Color("white")
    rect_width = 0
    rect_point = [(22, 10), (100, 30)]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)

def otherRect():
    rect_color = pygame.Color("green")
    rect_width = 0
    rect_point = [(22, 10), (100, 30)]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)

draw_flagshtok()
draw_BlueRect()
draw_WhiteRect()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()