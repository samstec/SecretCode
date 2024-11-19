from collections import deque
from tkinter import *
import random

root = Tk()

#title============================================================================================================================================================================================================

root.title("It Puts the lotion on")
    
#Widget============================================================================================================================================================================================================

#Label #1
label = Label(root, text="User, Please input your secret message!",font=("Papyrus",25),fg="red")
label.grid(row=1, column=2)

#Label #2
label2 = Label(root, text="User, Please enter an integer as a key\nfor your ceasar cypher, or click random\nfor a message that is only decipherable once!",font=("Papyrus",25),fg="red")
label2.grid(row=3, column=2)

#Label for the KEY
labelKEY = Label(root, text="KEY:",font=("Papyrus",15),fg="red")
labelKEY.grid(row=4, column=1,stick=E)

#Entry #1
entry1 = Entry(root,bg="black",fg="red",font=("Papyrus",15))
entry1.grid(row=2, column=1, columnspan=3,stick=W+E)

#Entry #2
entryK = Entry(root,bg="black",fg="red",font=("Papyrus",15))
entryK.grid(row=4, column=2,stick=W+E)

#Entry 3------->displays the encrypted message
entrySM = Entry(root,bg="black",fg="red",font=("Papyrus",15))
entrySM.grid(row=6, column=2,sticky=E+W)

#Entry 4------->displays the decrypted message
entryDSM = Entry(root,bg="black",fg="red",font=("Papyrus",15))
entryDSM.grid(row=8, column=2,sticky=E+W)

#Entry 5------->displays both decrypted and encrypted messages(ENCRYPTED)
entryDSM1 = Entry(root,bg="black",fg="red",font=("Papyrus",15))
entryDSM1.grid(row=10, column=1,sticky=E+W)

#Entry 6------->displays both decrypted and encrypted messages(DECRYPTED)
entrySM1 = Entry(root,bg="black",fg="red",font=("Papyrus",15))
entrySM1.grid(row=10, column=3,sticky=E+W)

#Functions============================================================================================================================================================================================================

#Random buttom function
def Random_():
    shift=random.randint(0,26)
    print(shift)
    entryK.delete(0,END)
    entryK.insert(0,shift)
#Self destruct function(quits widget)   
def Self_Des():
    quit(0)
    
#Encypted message function.
def encypt():
    x = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    EM = entry1.get().lower()
    Shift = int(entryK.get())
    new_word = []
    new_a=list(EM)
    new_list = x[:]
    new_list = deque(new_list)
    new_list.rotate(-Shift)
    new_list = list(new_list)
    for i in new_a:
        idNum = x.index(i)
        new_word.append(new_list[idNum])
    entrySM.delete(0, END)
    entrySM.insert(0, new_word)
    
#Decrypted message function.
def decrypt():
    EM = entry1.get()
    entryDSM.delete(0, END)
    entryDSM.insert(0, EM)
#Display both in text boxs function.
def both():
    XY = entryDSM.get()
    entryDSM1.delete(0, END)
    entryDSM1.insert(0,XY)

    ZY = entrySM.get()
    entrySM1.delete(0, END)
    entrySM1.insert(0,ZY)
    
#Self Destruct button (ENDS PROGRAM)
butt_SD = Button(root,text="Self Destruct ",padx=50, pady=5,fg="red",bg="black",font=("Papyrus",25), command=Self_Des)
butt_SD.grid(row=11, column=1, columnspan=3,sticky=E+W)

#Display both decrypted and encrypted messages button
butt_DB = Button(root,text="Click to Display Both Messages Side by Side ",padx=50, pady=5,fg="red",bg="black",font=("Papyrus",25), command=both)
butt_DB.grid(row=9, column=1, columnspan=3,sticky=E+W)

#Display decrypted message button
butt_DD = Button(root,text="Click to Display Deciphered Secret Message",padx=50, pady=5,fg="red",bg="black",font=("Papyrus",25), command=decrypt)
butt_DD.grid(row=7, column=1, columnspan=3,sticky=E+W)

#Random Button
butt_R = Button(root,text="Random",padx=20, pady=5,fg="red",bg="black",font=("Papyrus",10), command=Random_)
butt_R.grid(row=4, column=3,stick=W)

#Display encrypted message button
butt_D = Button(root,text="Click to Display Secret Message",padx=50, pady=5,fg="red",bg="black",font=("Papyrus",25), command=encypt)
butt_D.grid(row=5, column=1, columnspan=3,sticky=E+W)

root.mainloop() 