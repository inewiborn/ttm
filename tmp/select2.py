#!/usr/bin/env python3

#TODO delete file

import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
frame = tk.Frame(root)
frame.grid()
combobox = ttk.Combobox(frame,values = [u"ОДИН",u"ДВА",u"ТРИ"],height=3)
#frame - задает родительский виджет, на его территории будет располагаться Combobox
#values - задает набор значений, которые будут содержаться в Combobox изначально
#height - задает высоту выпадающего списка. Если число элементов списка меньше 11, то можно не задавать.
#Если не задано при количестве элементов больше 10, то с правой стороны появится полоса прокрутки.
#Если в нашем примере задать значение height меньше трех, то с правой стороны появится полоса прокрутки,
#но она будет недоступна, а все элементы будут отображаться одновременно.
combobox.set(u"ОДИН")#с помощью этой строчки мы установим Combobox в значение ОДИН изначально
combobox.grid(column=0,row=0)#Позиционируем Combobox на форме
root.mainloop()

