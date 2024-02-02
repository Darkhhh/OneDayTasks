import customtkinter as ctk
from PIL import Image
from Utils.GetAssetsModule import resource_path
add_icon_path = "Assets/new_task_icon.png"
finish_icon_path = "Assets/finish_day_icon.png"


class HeaderFrame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk):
        super().__init__(master)
        self.grid_anchor("center")
        self.configure(fg_color="transparent")
        self.grid_configure(pady=(20, 10))
        self.grid_columnconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=1, weight=3)
        self.grid_columnconfigure(index=2, weight=1)
        self.grid_columnconfigure(index=3, weight=2)

        add_img_src = Image.open(resource_path(add_icon_path))
        img = ctk.CTkImage(light_image=add_img_src, dark_image=add_img_src, size=(15, 15))
        self.add_button = ctk.CTkButton(self, text='', width=30, height=30, image=img)
        self.add_button.grid(row=0, column=0, padx=10, sticky="ew")
        self.progress_bar = ctk.CTkProgressBar(self, width=180, progress_color="green", height=5)
        self.progress_bar.grid(row=0, column=1, padx=10, sticky="ew")
        self.progress_label = ctk.CTkLabel(self, text="50%", width=40)
        self.progress_label.grid(row=0, column=2, padx=10, sticky="ns")
        fin_img_src = Image.open(resource_path(finish_icon_path))
        fin_img = ctk.CTkImage(light_image=fin_img_src, dark_image=fin_img_src, size=(15, 15))
        self.finish_button = ctk.CTkButton(self, height=30, width=30, text="", image=fin_img, fg_color="transparent")
        self.finish_button.grid(row=0, column=3, padx=10, sticky="ew")

    def set_progress(self, progress):
        if progress < 0:
            progress = 0
        if progress > 100:
            progress = 100

        self.progress_bar.set(progress / 100)
        s = ('%.f' % progress) + "%"
        l_color = "white"
        p_color = "red"
        if progress > 60:
            p_color = "green"
            l_color = "green"

        self.progress_bar.configure(progress_color=p_color)
        self.progress_label.configure(text=s, text_color=l_color)

    def get_progress(self):
        p = self.progress_bar.get()
        return p * 100

    def subscribe_to_add_button(self, button_command):
        self.add_button.configure(command=button_command)

    def subscribe_to_finish_button(self, button_command):
        self.finish_button.configure(command=button_command)
