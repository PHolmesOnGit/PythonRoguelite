from tkinter import messagebox
from tkinter import *
from random import *


window = Tk()
window.title("GAME TITLE YEAH BBY")
window.config(padx=15, pady=15)

player_name = Label(text="Player")
player_name.grid(row=0, column=0)

player_health = Label(text="Health")
player_health.grid(row=1, column=0)

enemy_name = Label(text="Enemy")
enemy_name.grid(row=0, column=1)

enemy_health = Label(text="Health")
enemy_health.grid(row=1, column=1)



add_button = Button(text="Move 1", width=20)
add_button.grid(row=2, column=0)

add_button = Button(text="Move 2", width=20)
add_button.grid(row=2, column=1)

add_button = Button(text="Move 3", width=20)
add_button.grid(row=3, column=0)

add_button = Button(text="Move 4", width=20)
add_button.grid(row=3, column=1)


window.mainloop()
