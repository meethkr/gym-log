import tkinter as tk

class ViewLoggedWorkouts(tk.Frame):
    def __init__(self, container_frame, on_back_button):
        super().__init__(master=container_frame)
        self.view_log_label = tk.Label(self, text="Logged Workouts")
        self.view_log_label.pack()

        self.back_button = tk.Button(self, text="< Back", command=on_back_button)
        self.back_button.pack()
