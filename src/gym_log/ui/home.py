import tkinter as tk
from gym_log.ui.start_workout import StartWorkout

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self. geometry('600x300')
        self.container_frame = tk.Frame(self)
        self.container_frame.pack(fill="both", expand=True)
        self.draw_home()

    def draw_home(self):
        home_frame_label = tk.Label(
            master=self.container_frame, 
            text="Gym Log"
        )
        home_frame_label.pack()

        self.start_workout_button = tk.Button(
            master=self.container_frame,
            text="Start logging a workout", 
            command=self.show_start_workout, 
        )
        self.start_workout_button.pack()

        self.view_log_button = tk.Button(
            master=self.container_frame,
            text="View logged workouts", 
        )
        self.view_log_button.pack()

        self.view_exercise_button = tk.Button(
            master=self.container_frame, 
            text="View statistics by exercise"
        )
        self.view_exercise_button.pack()

    def show_home(self):
        for widget in self.container_frame.winfo_children():
            widget.destroy()
        self.draw_home()
        
    def show_start_workout(self):
        for widget in self.container_frame.winfo_children():
            widget.destroy()
        StartWorkout(self.container_frame, self.show_home).pack()
            


mw = MainWindow()
mw.mainloop()
