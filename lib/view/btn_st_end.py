import sys
import datetime
from tkinter import *
#TODO delete file
class App():

    def task_start(self):
        self.dt_start = datetime.datetime.now()
        self.lbl['text'] = self.dt_start
        self.update_time()

    def task_end(self):
        self.dt_end = datetime.datetime.now()
        dt_str = self.dt_end - self.dt_start
        self.lbl['text'] = str(dt_str) + ' ' + self.dt_end.strftime("%Y-%m-%d %H:%M:%S")
        self.root.after_cancel(self.idddd)


    def update_time(self):
        dt_str = datetime.datetime.now() - self.dt_start
        self.lbl['text'] = dt_str
        self.idddd = self.root.after(1000, self.update_time)

    def __init__(self):
        self.dt_start = datetime.datetime.now();
        self.dt_end = datetime.datetime.now();

        self.root = Tk()
        self.root.title('Менеджер учета времени и задач')
        self.root.geometry('200x200')
        self.root.lift()
        self.root.attributes('-topmost',True)
        #self.root.after_idle(root.attributes,'-topmost',False)
        self.app = Frame(self.root)
        self.app.grid()
        self.lbl = Label(self.app, text = 'Список проектов')
        self.lbl.grid()
        self.btn = Button(self.app, text = 'начать', command=self.task_start)
        self.btn.grid()
        self.btn2 = Button(self.app, text = 'закончить', command=self.task_end)
        self.btn2.grid()
        self.btn_quite = Button(self.app, text = 'Выйти', command=self.root.quit)
        self.btn_quite.grid()
        self.update_time()
        self.root.mainloop()

