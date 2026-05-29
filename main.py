import pygame
import math

class GraphicEngine:
    def __init__(self, left_side, right_side):
        self.graph_flag = 1
        self.inputi = left_side
        self.graph_input = self.inputi.replace("^", "**")
        self.raw_eq = right_side
        self.eq = self.raw_eq.replace("^", "**")
        self.contx = {"sin": math.sin,
                 "cos": math.cos,
                 "tan": math.tan,
                 "max": max,
                 "min": min,
                 "abs": abs,
                 "pi": math.pi,
                 "e": math.e}
        self.compil_graph = compile(self.graph_input, '<string>', 'eval')
        self.compil_eq = compile(self.eq, '<string>', 'eval')

    def Calculation(self):
        points = []
        for x in range(-400, 400):
            for y in range(-300, 300):
                try:
                    self.contx["x"] = x
                    self.contx["y"] = y
                    result = eval(self.compil_graph, {}, self.contx)
                    result_eq = eval(self.compil_eq, {}, self.contx)

                    self.contx["x"] = x + 1
                    raw_nextx = eval(self.compil_graph, {}, self.contx)

                    self.contx["x"] = x
                    self.contx["y"] = y + 1
                    raw_nexty = eval(self.compil_graph, {}, self.contx)
                    nextx = raw_nextx - result
                    nexty = raw_nexty - result
                    thickness = (nextx ** 2 + nexty ** 2) ** 0.5
                    if thickness > 0 and abs(result - result_eq) / thickness < 0.99:
                       points.append((x, y))
                except:
                    continue
        return points

class Canvas:
    def __init__(self):
        pygame.init()
        self.graph = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("графический калькулятор 0.31")
        self.clock = pygame.time.Clock()
        self.graph.fill((0, 0, 0))
        self.pixel = pygame.PixelArray(self.graph)

    def Render(self, points):
        l = 0
        for i in points:
            if 0 <= i[0] + 400 < 800 and 0 <= -i[1] + 300 < 600:
                self.pixel[i[0] + 400, -i[1] + 300] = (255, 0, 0)

            l += 1
            if l % 1000 == 0:
                pygame.display.update()
        pygame.display.update()
        del self.pixel

class Running:
    def __init__(self, graph, eq):
        self.canvas = Canvas()
        self.graph = GraphicEngine(graph, eq)
        self.graph_flag = 1
        self.running = True
        self.clock = pygame.time.Clock()

    def Run(self):
        self.running = True
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.graph_flag == 1:
                points = self.graph.Calculation()
                self.canvas.Render(points)
            self.graph_flag = 0

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()



run = Running("max(abs(x), abs(y))", "7^2")
run.Run()