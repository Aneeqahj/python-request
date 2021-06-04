import requests
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x300")
window.resizable("false", "false")
window.title("Chuck norris jokes")
window["bg"] = "violet"


def getJoke():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        data = response.json()
        messagebox.showinfo("Joke", data["value"])
    except requests.exceptions.ConnectionError as x:
        messagebox.showerror("Error", "No connection")


btn = Button(window, text="Get Joke", command=getJoke, borderwidth=5, bg="pink")
btn.place(x=110, y=100)

window.mainloop()
