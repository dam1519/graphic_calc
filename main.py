import pygame
import math

# ;D

graph_flag = 1
inputi = "x^2+y^2"
graph_input = inputi.replace("^", "**")
raw_eq = "50^2"
eq = raw_eq.replace("^", "**")

pygame.init()
graph = pygame.display.set_mode((800, 600))
pygame.display.set_caption("графический калькулятор 0.21")
clock = pygame.time.Clock()
graph.fill((0, 0, 0))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if graph_flag == 1:
        for x in range(-400, 400):
            pygame.event.pump()
            for y in range(-300, 300):
                try:
                    contx = {"x": x, "y": y, "sin": math.sin, "cos": math.cos, "tan": math.tan, "max": max,
                             "min": min, "abs": abs}
                    result = eval(graph_input, {}, contx)
                    result_eq = eval(eq, {}, contx)
                    raw_nextx = eval(graph_input, {}, {"x": x + 1, "y": y, "sin": math.sin, "cos": math.cos,
                                                       "tan": math.tan, "max": max,"min": min, "abs": abs})
                    raw_nexty = eval(graph_input, {}, {"y": y + 1, "x": x, "sin": math.sin, "cos": math.cos,
                                                       "tan": math.tan})
                    nextx = raw_nextx - result
                    nexty = raw_nexty - result
                    thickness = (nextx ** 2 + nexty ** 2) ** 0.5
                    if thickness > 0 and abs(result - result_eq) / thickness < 0.99:
                        graph.set_at((x + 400, -y + 300), (255, 0, 0))
                except:
                    continue
        graph_flag = 0


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
