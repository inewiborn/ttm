import sys
import datetime
from tkinter import *
import tkinter.ttk as ttk

class App():
    def task_start(self):
        self.dt_start = datetime.datetime.now()
        self.lbl['text'] = self.dt_start
        self.update_time()

    def task_end(self):
        self.dt_end = datetime.datetime.now()
        dt_str = self.dt_end - self.dt_start
        self.lbl['text'] = str(dt_str) + ' ' + self.dt_end.strftime("%Y-%m-%d %H:%M:%S")
        self.root.after_cancel(self.id_label_timer)

    def update_time(self):
        dt_str = datetime.datetime.now() - self.dt_start
        dt_str = self.chop_microseconds(dt_str)
        self.lbl['text'] = dt_str
        self.id_label_timer = self.root.after(1000, self.update_time)

    def chop_microseconds(self, delta):
        return delta - datetime.timedelta(microseconds=delta.microseconds)

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

        self.combobox = ttk.Combobox(self.app, values = [u"ОДИН",u"ДВА",u"ТРИ"],height=3)
        self.combobox.set(u"ОДИН")
        self.combobox.grid()

        self.update_time()
        self.root.mainloop()

"""
class MainWindow(Frame):
    def __init__(self, master):
        supper(MainWindow, self).__init(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(app, text = 'Список проектов')
        self.lbl.grid()

        self.btn = Button(app, text = 'Выйти', command=root.quit)
        self.btn.grid()
"""
