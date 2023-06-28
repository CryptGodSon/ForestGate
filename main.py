import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import pygame
import webbrowser



def intro():
    text.insert(tk.END, "You are in a mysterious abandoned cottage in the forest.\n")
    text.insert(tk.END, "You just woke up and can't remember how you got here.\n")
    text.insert(tk.END, "Your goal is to find your way home.\n")
    text.insert(tk.END, "You notice a strange symbol engraved on the wall.\n")
    play_sound("intro_sound.wav")
    play_music("background_music.wav")  # Odtwarzaj muzykę w tle


def check_window():
    text.insert(tk.END, "The windows are boarded up. You can't see through them.\n")
    play_sound("window_sound.wav")


def open_door():
    text.insert(tk.END, "The door is locked. You need to find the key.\n")
    play_sound("door_sound.wav")


def search_room():
    text.insert(tk.END, "While searching the room, you find a key under the pillow.\n")
    text.insert(tk.END, "You unlock the door and exit the cottage.\n")
    text.insert(tk.END, "Congratulations! You have regained your freedom.\n")
    tk.messagebox.showinfo("Congratulations", "You have regained your freedom.")
    update_score(50)  # Przyznaj 50 punktów za znalezienie klucza i ucieczkę
    play_sound("success_sound.wav")


def explore_forest():
    text.insert(tk.END, "You decide to explore the surrounding forest.\n")
    text.insert(tk.END, "As you venture deeper, you come across an old well.\n")
    text.insert(tk.END, "You can hear faint whispers coming from within.\n")
    text.insert(tk.END, "What would you like to do? (1) Investigate the well. (2) Return to the cottage.\n")
    play_sound("forest_sound.wav")


def investigate_well():
    text.insert(tk.END, "You approach the well cautiously.\n")
    text.insert(tk.END, "Peering inside, you see a glimmering object at the bottom.\n")
    text.insert(tk.END, "It seems to be a small amulet.\n")
    text.insert(tk.END, "You reach out to grab it, but suddenly, the well starts to shake.\n")
    text.insert(tk.END, "The ground beneath you crumbles, and you fall into darkness...\n")
    text.insert(tk.END, "To be continued...\n")
    update_score(-20)  # Odejmij 20 punktów za niebezpieczne badanie studni
    play_sound("well_sound.wav")


def make_decision(decision):
    if decision == 1:
        check_window()
    elif decision == 2:
        open_door()
    elif decision == 3:
        search_room()
    elif decision == 4:
        explore_forest()
    elif decision == 5:
        investigate_well()
    else:
        text.insert(tk.END, "Invalid choice. Please try again.\n")


def handle_button_click():
    decision = int(entry.get())
    entry.delete(0, tk.END)
    make_decision(decision)


def toggle_fullscreen(event=None):
    window.attributes("-fullscreen", not window.attributes("-fullscreen"))


def handle_key_press(event):
    if event.char.isdigit():
        decision = int(event.char)
        make_decision(decision)


def update_score(points):
    global score
    score += points
    score_label.config(text="Score: " + str(score))


def play_sound(sound_file):
    pygame.mixer.Sound(sound_file).play()


def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)  # -1 oznacza zapętlenie muzyki


def open_github(event):
    webbrowser.open("https://github.com/CryptGodSon")

def show_credits():
    credits_window = tk.Toplevel()
    credits_window.title("Credits")
    credits_window.geometry("250x100")
    center_window(credits_window)


    label = tk.Label(credits_window, text="Created by ")
    label.pack()

    name_label = tk.Label(credits_window, text="CryptGodSon", fg="blue", cursor="hand2")
    name_label.pack()

    name_label.bind("<Button-1>", open_github)

    credits_window.mainloop()

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))



def show_multiplayer():
    # Czyść tekst w polu tekstowym
    text.delete("1.0", tk.END)

    # Wyświetl informacje o trybie wieloosobowym
    text.insert(tk.END, "Multiplayer Mode\n")
    text.insert(tk.END, "Choose one of the following options:\n")
    text.insert(tk.END, "(H) Host a multiplayer game\n")
    text.insert(tk.END, "(J) Join a multiplayer game\n")
    text.insert(tk.END, "(B) Back to main menu\n")

    # Ukryj przycisk
    button.pack_forget()

    # Przyciski dla trybu wieloosobowego
    # Przycisk H
    multiplayer_button1 = tk.Button(window, text="H - Host a game", command=host_multiplayer_game)
    # Przycisk J
    multiplayer_button2 = tk.Button(window, text="J - Join a game", command=join_multiplayer_game)
    # Przycisk B
    multiplayer_button3 = tk.Button(window, text="B - Back to main menu", command=back_to_main_menu)

    # Wyświetl przyciski dla trybu wieloosobowego
    multiplayer_button1.pack()
    multiplayer_button2.pack()
    multiplayer_button3.pack()


# Przykładowe funkcje obsługujące przyciski
def host_multiplayer_game():
    print("Host a multiplayer game")
    tk.messagebox.showinfo("Error", "Check Internet Connection and try again")



def join_multiplayer_game():
    print("Join a multiplayer game")
    tk.messagebox.showinfo("Error","Check Internet Connection and try again")

def back_to_main_menu():
    text.delete("1.0", tk.END)
    label.config( 
        text="Choose one of the options: (1) Check the windows. (2) Open the door. (3) Search the room. (4) Explore the forest.")
    entry.delete(0, tk.END)
    button.pack()
    multiplayer_button1.pack_forget()
    multiplayer_button2.pack_forget()
    multiplayer_button3.pack_forget()


pygame.init()
pygame.mixer.init()

window = tk.Tk()
window.title("Text Adventure Game")
window.geometry("1280x720")

# Ustawienie ikony
window.iconbitmap(r"C:\Users\monte\PycharmProjects\pythonProject6\favicon.ico")

# Dodanie obrazu lasu jako tła
background_image = ImageTk.PhotoImage(Image.open(r'C:\Users\monte\PycharmProjects\pythonProject6\222.jpg'))
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

text = tk.Text(window, bg="black", fg="white")
text.pack()

intro()

label = tk.Label(window,
                 text="Choose one of the options: (1) Check the windows. (2) Open the door. (3) Search the room. (4) Explore the forest.",
                 bg="black", fg="white")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Submit", command=handle_button_click)
button.pack()

score = 0
score_label = tk.Label(window, text="Score: " + str(score), bg="black", fg="white")
score_label.pack()

menu = tk.Menu(window)
window.config(menu=menu)

settings_menu = tk.Menu(menu, tearoff=0)
settings_menu.add_command(label="Multiplayer", command=show_multiplayer)
menu.add_cascade(label="Settings", menu=settings_menu)

credits_menu = tk.Menu(menu, tearoff=0)
credits_menu.add_command(label="Creators", command=show_credits)
menu.add_cascade(label="Credits", menu=credits_menu)

menu.add_command(label="Quit", command=window.quit)

window.bind("<F11>", toggle_fullscreen)
window.bind("<Key>", handle_key_press)

window.mainloop()
