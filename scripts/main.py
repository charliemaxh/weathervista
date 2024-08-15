import tkinter as tk
from tkinter import ttk
from create_dashboard import create_dashboard
from fetch_data import WeatherAPI

# Create the main Tkinter window
root = tk.Tk()
root.title("Weather Dashboard")

# Create the dashboard
create_dashboard(root, WeatherAPI)

# Start the Tkinter event loop
root.mainloop()
