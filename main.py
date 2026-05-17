import pygame

# ;D

graph_flag = 1
inputi = "x^2+y^2"
graph_input = inputi.replace("^", "**")
raw_eq = "50^2"
eq = raw_eq.replace("^", "**")

pygame.init()
graph = pygame.display.set_mode((800, 600))
pygame.display.set_caption("графический калькулятор 0.1")
clock = pygame.time.Clock()
graph.fill((0, 0, 0))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if graph_flag == 1:
        for x in range(-400,400):
            for y in range(-300,300):
                try:
                    result = eval(graph_input)
                    result_eq = eval(eq)
                    if result == result_eq:
                        pygame.draw.rect(graph, (255, 0, 0), (x + 400, -y + 300, 1, 1))
                except:
                    continue
        graph_flag = 0


    pygame.display.flip()

    clock.tick(60)

pygame.quit()