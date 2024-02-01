import customtkinter as ctk
from PIL import Image

delete_icon_path = "Assets/delete_task_icon.png"
percent_icon_path = "Assets/percent_icon.png"


class TaskFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Grid Configuration
        self.grid(pady=10)
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=1, weight=3)
        self.grid_columnconfigure(index=2, weight=1)
        self.grid_columnconfigure(index=3, weight=1)

        # Instance Data
        self.global_frame = master
        self.percent = float(0)
        self.checked = False
        self.custom_percent = False

        # Checkbox
        self.checkbox = ctk.CTkCheckBox(self, text='', width=25, checkbox_height=25, checkbox_width=25)
        self.checkbox.grid(column=0, row=0, sticky="ew")
        self.checkbox.configure(command=self.checkbox_event)

        # Task Itself
        self.task = ctk.CTkEntry(self, placeholder_text="Enter your task here", width=200)
        self.task.grid(column=1, row=0, sticky="ew", padx=15)

        # Percent Button
        percent_img_src = Image.open(percent_icon_path)
        percent_img = ctk.CTkImage(light_image=percent_img_src, dark_image=percent_img_src, size=(20, 20))
        self.percentage_button = ctk.CTkButton(self, text='', image=percent_img, width=25, height=25)
        self.percentage_button.configure(fg_color="RoyalBlue3", hover_color="RoyalBlue4", command=self.percent_event)
        self.percentage_button.grid(column=2, row=0, sticky="ew", padx=5)

        # Delete Button
        delete_img_src = Image.open(delete_icon_path)
        delete_img = ctk.CTkImage(light_image=delete_img_src, dark_image=delete_img_src, size=(20, 20))
        self.delete_button = ctk.CTkButton(self, width=25, height=25, text="", image=delete_img)
        self.delete_button.configure(hover_color="red4", fg_color="red3", command=self.delete_event)
        self.delete_button.grid(column=3, row=0, sticky="ew", padx=5)

    def set_percent(self, value: float):
        self.percent = value

    def get_percent(self):
        return self.percent

    def is_checked(self):
        return self.checked

    def is_custom(self):
        return self.custom_percent

    def checkbox_event(self):
        self.checked = not self.checked
        self.task.cget("font").configure(overstrike=self.checked)
        self.global_frame.task_checked()

    def delete_event(self):
        self.global_frame.delete_task(self)

    def percent_event(self):
        txt = "Set new (current " + '%.2f' % self.percent + "):"
        dialog = ctk.CTkInputDialog(text=txt, title="Set Custom Percent")
        result = dialog.get_input()
        if not result:
            return

        percent = float(result.replace(',', '.'))
        self.percent = percent
        self.custom_percent = True
        self.percentage_button.configure(self, fg_color="MediumPurple1", hover_color="MediumPurple2")
        self.global_frame.recalculate_percentages()
        self.global_frame.sort_tasks()

    def __lt__(self, other):
        return self.percent < other.percent
