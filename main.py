from tkinter import *
from tkinter.colorchooser import askcolor

class PaintApp:
    def __init__(self, master):
        self.master = master
        self.color = 'black'
        self.lineWidth = 1
        self.start_x = None
        self.start_y = None
        self.canvas_width = 600
        self.canvas_height = 400

        self.canvas = Canvas(master, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()

        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        color_button = Button(master, text="Choose Color", command=self.choose_color)
        color_button.pack()

        self.lineWidthSlider = Scale(master, from_=1, to=20, orient=HORIZONTAL, command=self.setLineWidth)
        self.lineWidthSlider.pack()

    def paint(self, event):
        if self.start_x and self.start_y:
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, width=self.lineWidth, fill=self.color)
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, width=self.lineWidth, fill=self.color)
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, width=self.lineWidth, fill=self.color)
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, width=self.lineWidth, fill=self.color)
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, width=self.lineWidth, fill=self.color)
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, width=self.lineWidth, fill=self.color)
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, width=self.lineWidth, fill=self.color)
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, width=self.lineWidth, fill=self.color)
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, width=self.lineWidth, fill=self.color)
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, width=self.lineWidth, fill=self.color)
        self.start_x = event.x
        self.start_y = event.y

    def reset(self, event):
        self.start_x = None
        self.start_y = None

    def choose_color(self):
        self.color = askcolor(color=self.color)[1]

    def setLineWidth(self, val):
        self.lineWidth = int(val)

if __name__ == '__main__':
    root = Tk()
    root.title("TkPaint") #Only line edited by me (I changed the title)
    paint_app = PaintApp(root)
    root.mainloop()
