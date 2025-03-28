import tkinter as tk

class ShowExerciseStatistics(tk.Frame):
    def __init__(self, container_frame, on_back_button):
        super().__init__(master=container_frame)
        self.exercise_statistics_label = tk.Label(self, text="Exercise statistics")
        self.exercise_statistics_label.pack()

        self.back_button = tk.Button(self, text="< Back", command=on_back_button)
        self.back_button.pack()
