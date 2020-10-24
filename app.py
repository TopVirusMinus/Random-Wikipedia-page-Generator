import wikipedia, webbrowser
import tkinter as tk

chrome= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

play= "n"
while play == "n":
    rand= wikipedia.random()
    page= wikipedia.page(rand)
    title= page.title
    summaryRandom= wikipedia.summary(f"{rand}")
    print("Do You Want To Read About: ",title,"? (y/n): ")
    choice= input()
    choice.lower()
    if choice == "y":
        print(summaryRandom)
        openLink= input("Open Page in chrome? (y/n): ")
        if openLink == "y":
            webbrowser.get(chrome).open_new("https://en.wikipedia.org/wiki/"+rand)

        restart= input("Another Thing? (y/n) : ")
        if(restart == "n"):
            play= 'y'

root= tk.Tk()
root.mainloop()