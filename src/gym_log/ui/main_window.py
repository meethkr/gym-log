import tkinter as tk
from gym_log.ui.start_workout import StartWorkout
from gym_log.ui.view_logged_workouts import ViewLoggedWorkouts
from gym_log.ui.show_exercise_statistics import ShowExerciseStatistics
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
            command = self.show_logged_workouts
        )
        self.view_log_button.pack()

        self.view_exercise_button = tk.Button(
            master=self.container_frame, 
            text="View statistics by exercise",
            command = self.show_exercise_statistics
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
        
    def show_logged_workouts(self):
        for widget in self.container_frame.winfo_children():
            widget.destroy()
        ViewLoggedWorkouts(self.container_frame, self.show_home).pack()

    def show_exercise_statistics(self):
        for widget in self.container_frame.winfo_children():
            widget.destroy()
        ShowExerciseStatistics(self.container_frame, self.show_home).pack()
        