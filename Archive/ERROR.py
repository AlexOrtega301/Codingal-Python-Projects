print("""Traceback (most recent call last):
  File "<string>", line 8, in forward
  File "C:\Program Files\Python39\lib\turtle.py", line 1638, in forward
    self._go(distance)
  File "C:\Program Files\Python39\lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Program Files\Python39\lib\turtle.py", line 3182, in _goto
    screen._drawline(self.drawingLineItem, ((0, 0), (0, 0)),
  File "C:\Program Files\Python39\lib\turtle.py", line 546, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Program Files\Python39\lib\tkinter\__init__.py", line 2763, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/david/Mis Python/Projectos SIN Identacion De Pecharm/lo_raro.pyw", line 7, in <module>
    forward(30)
  File "<string>", line 12, in forward
turtle.Terminator""")
print("Python FATAL ERROR")
it = input("more info")
err = 1
while True:
    if it == "yes":
        print("ERROR, Contact techincal Support for more INFO")
        err = err + 1
    if err == 100:
        break
python = input("©️Alex")
        
