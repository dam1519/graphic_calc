import pygame

# ;D

graph_flag = 1

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
                inputi = "x^2+y^2"
                graph_input = inputi.replace("^", "**")
                result = eval(graph_input)
                print("x", x)
                print("y", y)
                print(result)
                if result == 50**2:
                    pygame.draw.rect(graph, (255, 0, 0), (x + 400, y + 300, 1, 1))
        graph_flag = 0


    pygame.display.flip()

    clock.tick(60)

pygame.quit()