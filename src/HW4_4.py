from tkinter import *
my_password = list("1111")
entered = list("____")
index = 0
msg = ''
end = 0
def click(event):
    global msg, entered, index, end
    if end == 1:
        root.destroy()
    else:
        button = event.widget["text"]
        if button == "del":
            if index == 0:
                msg = 'No letters\n'
                msg += 'to delete'
            else:
                index -= 1
                entered[index] = '_'
                msg = entered[0] + ' ' + entered[1] + ' ' + entered[2] + ' ' + entered[3]
        elif button == "enter":
            if index < 4:
                msg = 'Numbers are not\n'
                msg += 'entered yet'
            else:
                if entered == my_password:
                    end+=1
                    msg = 'Correct Password!!\n'
                    msg += 'Door is open!!'
                else:
                    msg = 'Wrong Password!!\n'
                    msg += 'Try again!!' 
        else:
            if index == 4:
                msg = 'Already clicked\n'
                msg += 'four numbers'
            else:
                entered[index] = button
                msg = entered[0] + ' ' + entered[1] + ' ' + entered[2] + ' ' + entered[3]
                index += 1
        lbl.configure(text=msg)
root = Tk()
lFrame = Frame(root)
lFrame.pack()
lbl = Label(lFrame, text="_ _ _ _", font = ("Helvetica", 16), height = 4)
lbl.pack(pady = 4)
bFrame = Frame(root)
bFrame.pack()
btn_symbols = ['1','2','3','4','5','6','7','8','9','0','del','enter']
btns = []
for i in range(len(btn_symbols)):
    btn = Button(bFrame, text = btn_symbols[i], width=6, height=3, pady=3, padx = 3)
    btn.grid(row=i/3, column=i%3)
    btns.append(btn)
    btns[i].bind("<Button-1>", click)
root.mainloop()