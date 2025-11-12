import tkinter as tk
from tkinter import ttk

# --- Utility Functions ---

def update_stress_meter(value):
    """
    Updates the visual and textual representation of the stress meter
    based on the input value (0-10) from the slider.
    """
    # Ensure the value is an integer
    level = int(float(value))

    # Determine stress level, corresponding color, and tailored advice
    if level <= 3:
        status_text = "Low Stress: Relaxed and focused."
        color = "#a8e063"  # Light Green
        advice = "Keep up the good work! Maybe enjoy a moment in nature."
    elif level <= 7:
        status_text = "Moderate Stress: Manageable pressure."
        color = "#ffc371"  # Yellow/Orange
        advice = "Take a short break. Try deep breathing or mindfulness exercises."
    else:
        status_text = "High Stress: Urgent need for rest/de-stressing."
        color = "#ff4e50"  # Red
        advice = "Stop and take 15 minutes for self-care. Focus on what truly matters: family, health, and rest."

    # Update the display elements
    current_rating_label.config(text=f"Current Rating: {level}/10")
    status_label.config(text=status_text, background=color)
    advice_label.config(text=advice, background=color)
    status_frame.config(bg=color)
    root.config(bg=color) # Change background color of the main window

# --- Main Application Setup ---
root = tk.Tk()
root.title("Daily Stress Meter")
root.geometry("400x350")
root.resizable(False, False)

# Attempt to use the 'Inter' font for better aesthetics
try:
    from tkinter import font
    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(family="Inter", size=10)
    root.option_add("*Font", default_font)
except Exception:
    # Fallback to default Tkinter font if 'Inter' is not available
    pass

# Styling (using ttk for better widget appearance)
style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', background='white', foreground='#333', padding=5)
style.configure('TScale', background='white', troughcolor='#ddd')

# Title Label
title_label = ttk.Label(root, text="How stressed are you right now?", font=("Inter", 14, "bold"), anchor="center")
title_label.pack(pady=15, padx=10, fill='x')

# Stress Rating Scale (Slider)
stress_slider = ttk.Scale(
    root,
    from_=0,
    to=10,
    orient='horizontal',
    command=update_stress_meter,
    length=300
)
stress_slider.set(5)  # Set initial value to 5 (Moderate)
stress_slider.pack(pady=10)

# Labels for min/max indicators below the slider
min_max_frame = tk.Frame(root, bg=root['bg'])
min_max_frame.pack(fill='x', padx=50)

min_label = ttk.Label(min_max_frame, text="0 (No Stress)", background=root['bg'])
min_label.pack(side='left')
max_label = ttk.Label(min_max_frame, text="10 (Max Stress)", background=root['bg'])
max_label.pack(side='right')

# Current Rating Display
current_rating_label = ttk.Label(root, text="Current Rating: 5/10", font=("Inter", 12), anchor="center")
current_rating_label.pack(pady=10, fill='x')

# Status Frame (Dynamic Color Display area)
status_frame = tk.Frame(
    root,
    relief=tk.RAISED,
    borderwidth=2,
    padx=10,
    pady=10,
    bg="#ffc371", # Initial color (Moderate)
    relief=tk.RIDGE,
    bd=5,
    highlightbackground="#333",
    highlightthickness=1,
    cursor="hand2"
)
status_frame.pack(pady=20, padx=20, fill='x', expand=True)

# Stress Status Label (updates with color change)
status_label = ttk.Label(
    status_frame,
    text="Moderate Stress: Manageable pressure.",
    font=("Inter", 12, "bold"),
    background="#ffc371",
    foreground='black'
)
status_label.pack(pady=5, fill='x')

# Advice Label (provides actionable tips)
advice_label = ttk.Label(
    status_frame,
    text="Take a short break. Try deep breathing or mindfulness exercises.",
    font=("Inter", 10),
    background="#ffc371",
    wraplength=300
)
advice_label.pack(pady=5, fill='x')

# Initialize the meter display to reflect the starting slider value (5)
update_stress_meter(5)

# Start the Tkinter event loop
root.mainloop()

