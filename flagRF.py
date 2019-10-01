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


draw_flagshtok()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()