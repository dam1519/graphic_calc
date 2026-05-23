import pygame
import math

# ;D

graph_flag = 1
inputi = "x"
graph_input = inputi.replace("^", "**")
raw_eq = "y"
eq = raw_eq.replace("^", "**")

pygame.init()
graph = pygame.display.set_mode((800, 600))
pygame.display.set_caption("графический калькулятор 0.22")
clock = pygame.time.Clock()
graph.fill((0, 0, 0))

compil_graph = compile(graph_input, '<string>', 'eval')
compil_eq = compile(eq, '<string>', 'eval')

contx = {"sin": math.sin,
         "cos": math.cos,
         "tan": math.tan,
         "max": max,
         "min": min,
         "abs": abs,
         "pi": math.pi,
         "e": math.e}

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if graph_flag == 1:
        for x in range(-400, 400):
            for y in range(-300, 300):
                try:
                    contx["x"] = x
                    contx["y"] = y
                    result = eval(compil_graph, {}, contx)
                    result_eq = eval(compil_eq, {}, contx)

                    contx["x"] = x + 1
                    raw_nextx = eval(compil_graph, {}, contx)

                    contx["x"] = x
                    contx["y"] = y + 1
                    raw_nexty = eval(compil_graph, {}, contx)
                    nextx = raw_nextx - result
                    nexty = raw_nexty - result
                    thickness = (nextx ** 2 + nexty ** 2) ** 0.5
                    if thickness > 0 and abs(result - result_eq) / thickness < 0.99:
                        graph.set_at((x + 400, -y + 300), (255, 0, 0))
                except:
                    continue

            pygame.display.update()

        graph_flag = 0


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
