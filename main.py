import pygame
import math
import ctypes
import tkinter as tk
from tkinter import ttk
import os
import re

# it very cursed (x_x)

# calculations
class GraphicEngine:
    def __init__(self, left_side, right_side, op):
        self.graph_flag = 1
        self.inputi = left_side
        self.graph_input =  re.sub(r'\|([^|]+)\|', r'abs(\1)', self.inputi.replace("^", "**"))
        self.op = op
        self.raw_eq = right_side
        self.eq = re.sub(r'\|([^|]+)\|', r'abs(\1)', self.raw_eq.replace("^", "**"))
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

# engine
    def Calculation(self):
        points = []
        match self.op:
            case "=":
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
            case "<":
                for x in range(-400, 400):
                    for y in range(-300, 300):
                        try:
                            self.contx["x"] = x
                            self.contx["y"] = y
                            result = eval(self.compil_graph, {}, self.contx)
                            result_eq = eval(self.compil_eq, {}, self.contx)
                            if result < result_eq:
                               points.append((x, y))
                        except:
                            continue
            case ">":
                for x in range(-400, 400):
                    for y in range(-300, 300):
                        try:
                            self.contx["x"] = x
                            self.contx["y"] = y
                            result = eval(self.compil_graph, {}, self.contx)
                            result_eq = eval(self.compil_eq, {}, self.contx)
                            if result > result_eq:
                               points.append((x, y))
                        except:
                            continue
            case "<=":
                for x in range(-400, 400):
                    for y in range(-300, 300):
                        try:
                            self.contx["x"] = x
                            self.contx["y"] = y
                            result = eval(self.compil_graph, {}, self.contx)
                            result_eq = eval(self.compil_eq, {}, self.contx)
                            if result <= result_eq:
                               points.append((x, y))
                        except:
                            continue
            case ">=":
                for x in range(-400, 400):
                    for y in range(-300, 300):
                        try:
                            self.contx["x"] = x
                            self.contx["y"] = y
                            result = eval(self.compil_graph, {}, self.contx)
                            result_eq = eval(self.compil_eq, {}, self.contx)
                            if result >= result_eq:
                               points.append((x, y))
                        except:
                            continue
        return points

# pygame
class Canvas:
    def __init__(self):
        pygame.init()
        self.graph = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("графический калькулятор 0.41")
        self.clock = pygame.time.Clock()
        self.graph.fill((0, 0, 0))

# render points
    def Render(self, points):
        self.graph.fill((0, 0, 0))

        points_copy = list(points)

        pixel = pygame.PixelArray(self.graph)
        for i in points_copy:
            try:
                screen_x = int(i[0] + 400)
                screen_y = int(-i[1] + 300)

                if 0 <= screen_x < 800 and 0 <= screen_y < 600:
                    pixel[screen_x, screen_y] = (255, 0, 0)
            except IndexError:
                continue

        del pixel
        pygame.display.flip()

# tkinter
class Interface:
    def __init__(self, on_build_callback):
        self.on_build_callback = on_build_callback

        self.root = tk.Tk()
        self.root.title("графический калькулятор 0.41")
        self.root.geometry("1100x600")
        self.root.resizable(False, False)

        gdi32 = ctypes.WinDLL('gdi32')
        gdi32.AddFontResourceExW("Monocraft.ttc", 0x10, 0)

        self.sidebar = tk.Frame(self.root, width=300, padx=15, pady=15)
        self.sidebar.pack(side=tk.RIGHT, fill=tk.Y)

        self.entry_left = tk.Entry(self.sidebar, font=("Monocraft", 12), width=25)
        self.entry_left.insert(0, "max(|x|, |y|)")
        self.entry_left.pack(pady=1, padx=1)

        self.operator = ttk.Combobox(self.sidebar, values=["=", "<", ">", "<=", ">="], width=5, state="readonly", font="Monocraft")
        self.operator.pack(pady=1, padx=1)
        self.operator.current(0)

        self.entry_right = tk.Entry(self.sidebar, font=("Monocraft", 12), width=25)
        self.entry_right.insert(0, "7^2")
        self.entry_right.pack(pady=1, padx=1)

        self.btn_build = tk.Button(
            self.sidebar, text="plot the graph", command=self.on_click
            , font=("Monocraft", 11), pady=1
        )
        self.btn_build.pack(fill=tk.X, pady=1)

        self.embed = tk.Frame(self.root, width=800, height=600, bg="Black")
        self.embed.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# function for button
    def on_click(self):
        left = self.entry_left.get()
        op = self.operator.get()
        right = self.entry_right.get()
        self.on_build_callback(left, right, op)

# embed id
    def get_embed_id(self):
        self.root.update()
        return self.embed.winfo_id()

# control
class Running:
    def __init__(self):
        self.Interface = Interface(on_build_callback=self.rebuild)
        os.environ['SDL_WINDOWID'] = str(self.Interface.get_embed_id())
        self.canvas = Canvas()
        self.engine = None
        self.graph_flag = 0
        self.Interface.btn_build.invoke()
        self.running = True
        self.clock = pygame.time.Clock()
        self.Interface.root.after(16, self.loop)

# rebuild graph
    def rebuild(self, graph, eq, op):
        self.engine = GraphicEngine(graph, eq, op)
        self.graph_flag = 1

# main loop
    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Interface.root.destroy()
                return

        if self.graph_flag and self.engine is not None:
            points = self.engine.Calculation()
            self.canvas.Render(points)
            self.graph_flag = 0

        pygame.display.flip()
        self.Interface.root.after(16, self.loop)

# run function
    def run(self):
        self.Interface.root.mainloop()
        pygame.quit()



run = Running()
run.run()