import numpy as np

from datetime import datetime
from gym_log.utils.helpers import format_date 
from gym_log.ui.main_window import MainWindow


def main():
    print(format_date(datetime.now()), "This is a gym log in the making")

    mw = MainWindow()
    mw.mainloop()

if __name__ == "__main__":
    main()