import customtkinter as ctk
import random
import time

window = ctk.CTk()
window.title("Reaction Test Tool")
window.geometry("635x480")
window.resizable(width=False, height=False)
window.iconbitmap("Images/Icon.ico")

label = ctk.CTkLabel(window, text="Press the button\nas soon as it turns red!", font=("Arial", 24), fg_color="blue")
label.pack(pady=50)

start_button = ctk.CTkButton(window, text="", width=60, height=60, fg_color="orange", corner_radius=0)
start_button.pack()

reaction_times = []

def init_timer():
    delay = random.randint(2, 10)
    window.after(int(delay * 1000), signal_user)

def signal_user():
    button_x = random.randint(100, 550)
    button_y = random.randint(150, 400)
    start_button.place(x=button_x, y=button_y)
    label.configure(text="Reaction Ability")
    start_button.configure(fg_color="red", command=reaction_time)
    start_button.start_time = time.time()

def reaction_time():
    end_time = time.time()
    reaction_duration = end_time - start_button.start_time
    reaction_times.append(reaction_duration)
    if reaction_times:
        average_time = sum(reaction_times) / len(reaction_times)
    label.configure(text=f"You took {reaction_duration:.3f} seconds.\n"
                          f"Average reaction time: {average_time:.3f} seconds.\n"
                          "Prepare quickly for the next button!")
    start_button.configure(fg_color="green", command=None)
    window.after(2000, init_timer)

init_timer()
window.mainloop()
