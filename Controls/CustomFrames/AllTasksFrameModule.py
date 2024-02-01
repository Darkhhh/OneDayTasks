import customtkinter as ctk
from Controls.CustomFrames.TaskFrameModule import TaskFrame


class TasksFrame(ctk.CTkScrollableFrame):
    def __init__(self, master: ctk.CTk, progress_changed):
        super().__init__(master)
        self.progress_changed = progress_changed
        self.grid(row=1, column=0, padx=10, sticky="ns", pady=5)
        self.grid_columnconfigure(0, weight=1)
        self.all_tasks = []
        task = TaskFrame(self)
        task.grid(column=0, row=0, sticky="ew")
        self.all_tasks.append(task)

    def add_task(self):
        t = TaskFrame(self)
        t.grid(column=0, sticky="ew")
        self.all_tasks.append(t)
        self.recalculate_percentages()
        self.progress_changed(self.count_progress())

    def delete_task(self, deleted_task):
        self.all_tasks.remove(deleted_task)
        deleted_task.destroy()
        self.recalculate_percentages()
        self.progress_changed(self.count_progress())

    def task_checked(self):
        self.progress_changed(self.count_progress())

    def sort_tasks(self):
        self.all_tasks = sorted(self.all_tasks, reverse=True)
        for index in range(0, len(self.all_tasks)):
            self.all_tasks[index].grid(row=index)

    def delete_all(self):
        for t in self.all_tasks:
            t.destroy()
        self.all_tasks.clear()

    def recalculate_percentages(self):
        custom_tasks = 0
        custom_percentage = 0
        for t in self.all_tasks:
            if not t.is_custom():
                continue
            custom_percentage += t.get_percent()
            custom_tasks += 1

        if custom_percentage >= 100:
            dif = (custom_percentage - 100)
            for t in self.all_tasks:
                if not t.is_custom():
                    continue
                t.set_percent(t.get_percent() - (t.get_percent() / dif))
            avg_percent = 0
        else:
            std_tasks_number = len(self.all_tasks) - custom_tasks
            if std_tasks_number <= 0:
                return
            avg_percent = (100 - custom_percentage) / std_tasks_number

        if custom_percentage >= 100:
            avg_percent = 0
        for t in self.all_tasks:
            if not t.is_custom():
                t.set_percent(avg_percent)

    def count_progress(self):
        progress = 0
        for t in self.all_tasks:
            if t.is_checked():
                progress += t.get_percent()
        return progress
