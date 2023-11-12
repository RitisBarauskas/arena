<<<<<<< HEAD
from tkinter import Tk, Canvas
import time

tk = Tk()
tk.title('Battle')
tk.resizible(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
canvas.pack()
tk.update()


class Ball:
    def __init__(self, canvas, color, x, y, up, down, left, right):
        # задаём параметры нового объекта при создании
        # игровое поле
        self.canvas = canvas
        # координаты
        self.x = 0
        self.y = 0
        # цвет нужен был для того, чтобы мы им закрасили весь шарик
        # здесь появляется новое свойство id, в котором хранится внутреннее название шарика
        # а ещё командой create_oval мы создаём круг радиусом 15 пикселей и закрашиваем нужным цветом
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        # помещаем шарик в точку с переданными координатами
        self.canvas.move(self.id, x, y)
        # если нажата стрелка вправо — двигаемся вправо
        self.canvas.bind_all(right, self.turn_right)
        # влево
        self.canvas.bind_all(left, self.turn_left)
        # наверх
        self.canvas.bind_all(up, self.turn_up)
        # вниз
        self.canvas.bind_all(down, self.turn_down)
        # шарик запоминает свою высоту и ширину
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    # движемся вправо
    # смещаемся на 2 пикселя в указанную сторону
    def turn_right(self, event):
        # получаем текущие координаты шарика
        pos = self.canvas.coords(self.id)
        # если не вышли за границы холста
        if not pos[2] >= self.canvas_width:
            # будем смещаться правее на 2 пикселя по оси х
            self.x = 2
            self.y = 0

    # влево
    def turn_left(self, event):
        pos = self.canvas.coords(self.id)
        if not pos[0] <= 0:
            self.x = -2
            self.y = 0

    # вверх
    def turn_up(self, event):
        pos = self.canvas.coords(self.id)
        if not pos[1] <= 0:
            self.x = 0
            self.y = -2

    # вниз
    def turn_down(self, event):
        pos = self.canvas.coords(self.id)
        if not pos[3] >= self.canvas_height:
            self.x = 0
            self.y = 2

    # метод, который отвечает за отрисовку шарика на новом месте
    def draw(self):
        # передвигаем шарик на заданный вектор x и y
        self.canvas.move(self.id, self.x, self.y)
        # запоминаем новые координаты шарика
        pos = self.canvas.coords(self.id)

        # если коснулись левой стенки
        if pos[0] <= 0:
            # останавливаемся
            self.x = 0
        # верхней
        if pos[1] <= 0:
            self.y = 0
        # правой
        if pos[2] >= self.canvas_width:
            self.x = 0
        # нижней
        if pos[3] >= self.canvas_height:
            self.y = 0


ball_one = Ball(
    canvas, 'red', 150, 150,  '<KeyPress-Up>',
    '<KeyPress-Down>', '<KeyPress-Left>', '<KeyPress-Right>'
)
# создаём второй шарик
ball_two = Ball(
    canvas, 'green', 100, 100,
    '<w>', '<s>', '<a>', '<d>'
)

while not False:
    # рисуем шарик
    ball_one.draw()
    ball_two.draw()
    tk.update_idletasks()
    tk.update()
=======
from tkinter import Tk, Canvas
import time

tk = Tk()
tk.title('Battle')
tk.resizible(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
canvas.pack()
tk.update()


class Ball:
    def __init__(self, canvas, color, x, y, up, down, left, right):
        # задаём параметры нового объекта при создании
        # игровое поле
        self.canvas = canvas
        # координаты
        self.x = 0
        self.y = 0
        # цвет нужен был для того, чтобы мы им закрасили весь шарик
        # здесь появляется новое свойство id, в котором хранится внутреннее название шарика
        # а ещё командой create_oval мы создаём круг радиусом 15 пикселей и закрашиваем нужным цветом
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        # помещаем шарик в точку с переданными координатами
        self.canvas.move(self.id, x, y)
        # если нажата стрелка вправо — двигаемся вправо
        self.canvas.bind_all(right, self.turn_right)
        # влево
        self.canvas.bind_all(left, self.turn_left)
        # наверх
        self.canvas.bind_all(up, self.turn_up)
        # вниз
        self.canvas.bind_all(down, self.turn_down)
        # шарик запоминает свою высоту и ширину
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    # движемся вправо
    # смещаемся на 2 пикселя в указанную сторону
    def turn_right(self, event):
        # получаем текущие координаты шарика
        pos = self.canvas.coords(self.id)
        # если не вышли за границы холста
        if not pos[2] >= self.canvas_width:
            # будем смещаться правее на 2 пикселя по оси х
            self.x = 2
            self.y = 0

    # влево
    def turn_left(self, event):
        pos = self.canvas.coords(self.id)
        if not pos[0] <= 0:
            self.x = -2
            self.y = 0

    # вверх
    def turn_up(self, event):
        pos = self.canvas.coords(self.id)
        if not pos[1] <= 0:
            self.x = 0
            self.y = -2

    # вниз
    def turn_down(self, event):
        pos = self.canvas.coords(self.id)
        if not pos[3] >= self.canvas_height:
            self.x = 0
            self.y = 2

    # метод, который отвечает за отрисовку шарика на новом месте
    def draw(self):
        # передвигаем шарик на заданный вектор x и y
        self.canvas.move(self.id, self.x, self.y)
        # запоминаем новые координаты шарика
        pos = self.canvas.coords(self.id)

        # если коснулись левой стенки
        if pos[0] <= 0:
            # останавливаемся
            self.x = 0
        # верхней
        if pos[1] <= 0:
            self.y = 0
        # правой
        if pos[2] >= self.canvas_width:
            self.x = 0
        # нижней
        if pos[3] >= self.canvas_height:
            self.y = 0


ball_one = Ball(
    canvas, 'red', 150, 150,  '<KeyPress-Up>',
    '<KeyPress-Down>', '<KeyPress-Left>', '<KeyPress-Right>'
)
# создаём второй шарик
ball_two = Ball(
    canvas, 'green', 100, 100,
    '<w>', '<s>', '<a>', '<d>'
)

while not False:
    # рисуем шарик
    ball_one.draw()
    ball_two.draw()
    tk.update_idletasks()
    tk.update()
>>>>>>> 714f80adfb505a0885ac929d8263472864537e43
    time.sleep(0.01)