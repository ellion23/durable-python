import tkinter as tk


class Draw:
    def __init__(selfself,root):
        root.title("Круги и треугольники")
        root.geometry("800x600+200+50")
        self. canvas = tk.Canvas(root, width = 800, height = 550, bg="lightgreen")
        self. canvas.pack()
        self.entry = tk.Entry(root, font="24")
        self.entry.pack(side=tk.LEFT, paxd=100)
        self.button1=tk.Button(root,text="Draw circle", font ="24", command = self.draw_circle)
        self.button1.pack(side=tk.LEFT)
        self.button2 = tk.Button(root, text="Draw triangle", font="24")
        self.button2.pack(side=tk.LEFT)

    def draw_circle(self):
        data = self.param
        if len(data)>2:
            circ= circle.Circle(data[0], data[1], data[2])
            self.canvas.create_oval(circ.x1, circ.y1, circ.x2, circ.y2,fill=circ.color_fill, outline = circ. color_border)

    @property
    def param(selfself):
        return[int(x)for x in self . entry.get().split()]
