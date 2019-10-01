import pygame

pygame.init()

size = width, height = 300, 300

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Флаг России")
screen.fill((255, 255, 255))


def draw_flagshtok():
    rect_color = pygame.Color("black")
    rect_width = 0
    rect_point = [(20, 10), (20, 280)]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)
    pygame.draw.rect(screen, rect_color, [(10, 270),(30,280)], rect_width)


draw_flagshtok()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()