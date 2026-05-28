import pygame
import math

class GraphEngine:
    def __init__(self, graph, eq):
        self.graph_flag = 1
        self.inputi = graph
        self.graph_input = self.inputi.replace("^", "**")
        self.raw_eq = eq
        self.eq = self.raw_eq.replace("^", "**")
        self.contx = {"sin": math.sin,
                     "cos": math.cos,
                     "tan": math.tan,
                     "max": max,
                     "min": min,
                     "abs": abs,
                     "pi": math.pi,
                     "e": math.e}

    def Optimisation(self):
        self.compil_graph = compile(self.graph_input, '<string>', 'eval')
        self.compil_eq = compile(self.eq, '<string>', 'eval')
        self.pixel = pygame.PixelArray(self.graph)

    def PygInit(self, name, setmode, fillcolr):
        pygame.init()
        self.graph = pygame.display.set_mode(setmode)
        pygame.display.set_caption(name)
        self.clock = pygame.time.Clock()
        self.graph.fill(fillcolr)

    def Calculation(self, x, y):
        self.x = x
        self.y = y
        self.contx["x"] = self.x
        self.contx["y"] = self.y
        self.result = eval(self.compil_graph, {}, self.contx)
        self.result_eq = eval(self.compil_eq, {}, self.contx)

        self.contx["x"] = self.x + 1
        self.raw_nextx = eval(self.compil_graph, {}, self.contx)

        self.contx["x"] = self.x
        self.contx["y"] = self.y + 1
        self.raw_nexty = eval(self.compil_graph, {}, self.contx)
        self.nextx = self.raw_nextx - self.result
        self.nexty = self.raw_nexty - self.result
        self.thickness = (self.nextx ** 2 + self.nexty ** 2) ** 0.5

    def Render(self):
        if self.thickness > 0 and abs(self.result - self.result_eq) / self.thickness < 0.99:
            self.pixel[self.x + 400, -self.y + 300] = (255, 0, 0)
# ;D

calc = GraphEngine("max(abs(x),abs(y))", "50")

calc.PygInit("графический калькулятор 3.0", (800, 600), (0, 0, 0))

calc.Optimisation()






running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if calc.graph_flag == 1:
        for x in range(-400, 400):
            for y in range(-300, 300):
                try:
                    calc.Calculation( x, y)
                    calc.Render()
                except:
                    continue

            pygame.display.update()

        calc.graph_flag = 0


    pygame.display.flip()

    calc.clock.tick(60)

pygame.quit()
