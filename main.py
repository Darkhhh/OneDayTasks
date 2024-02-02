# Python program to create a basic GUI
# application using the customtkinter module

import customtkinter as ctk
from Utils.GetAssetsModule import resource_path
from Controls.CustomFrames.AllTasksFrameModule import TasksFrame
from Controls.CustomFrames.HeaderFrameModule import HeaderFrame

# Basic parameters and initializations
# Supported modes : Light, Dark, System
ctk.set_appearance_mode("Dark")

# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("green")


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("One Day Tasks")
    app.iconbitmap(resource_path("Assets/app.ico"))
    app.geometry("400x350")
    app.resizable(width=False, height=False)

    header = HeaderFrame(app)
    header.configure(width=400)
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=1)
    header.grid(row=0, column=0)
    header.set_progress(0)

    def show_progress(progress):
        header.set_progress(progress=progress)

    tasks = TasksFrame(app, show_progress)
    tasks.configure(width=400)

    def add_task():
        tasks.add_task()

    def finish_day():
        tasks.delete_all()
        header.set_progress(0)

    header.subscribe_to_add_button(add_task)
    header.subscribe_to_finish_button(finish_day)
    app.mainloop()


