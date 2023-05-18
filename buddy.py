from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import webbrowser
from functools import partial
import re

f = open('conversation.txt', 'r')

train_data = []

for line in f:
    m = re.search("(Q:|A:)?(.+)", line)
    if m:
        train_data.append(m.groups()[1])

bot = ChatBot("My Bot")
bot.storage.drop()

trainer = ListTrainer(bot)

trainer.train(train_data)

main = Tk()
main.geometry("500x650")
main.title("CoU Buddy")
img = PhotoImage(file="cou.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "You   : " + query + "\n")
    print(type(answer_from_bot))
    msgs.insert(END, "Buddy : " + str(answer_from_bot) + "\n\n")
    textF.delete(0, END)
    msgs.see('end')

frame = Frame(main)
l = Label(text="CONVERSATION ", font=("Verdana", 15))
l.pack()
sc = Scrollbar(frame)

msgs = Text(frame, width=80, height=16, yscrollcommand=sc.set, wrap='word', fg='blue')
msgs.insert(END,"Ask CoU buddy anything like 'Comilla University' name of any subject or have a conversation "+ "\n")
sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)
def delete():
   msgs.delete("1.0","end")

frame.pack()
btn1 = Button(main, text="clear", font=("Verdana", 15), command=delete)
btn1.pack()
textF = Entry(main, font=("Verdana", 15))
textF.pack(fill=X, pady=10)

btn = Button(main, text="SEND", font=("Verdana", 15), command=ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>', enter_function)

main.mainloop()
