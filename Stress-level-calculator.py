import time

def get_validated_input(prompt, min_val, max_val):
    """
    Prompts the user for input and ensures it is an integer within the specified range.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Input must be between {min_val} and {max_val}. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def calculate_stress_level(sleep_quality, workload, mood):
    """
    Calculates the stress level (0-100) based on three input scores.

    Scores are weighted: higher input score generally means *lower* stress.
    Total 'Relaxation Score' max is 30 (10 + 10 + 10).
    Stress Score = 30 - Relaxation Score.
    Stress Percentage = (Stress Score / 30) * 100.
    """
    # Sum of positive indicators (higher is better)
    relaxation_score = sleep_quality + workload + mood

    # Stress score is the inverse (max 30 - min 0)
    max_score = 30
    stress_points = max_score - relaxation_score

    # Normalize to a 0-100 percentage
    stress_percentage = round((stress_points / max_score) * 100)
    return stress_percentage

def display_meter(percentage):
    """
    Displays a textual visualization of the stress meter and an interpretation.
    """
    if not 0 <= percentage <= 100:
        percentage = max(0, min(100, percentage))

    # Determine the length of the 'filled' part of the meter
    meter_length = 50
    filled_chars = int(percentage * meter_length / 100)
    empty_chars = meter_length - filled_chars

    # Color the output (only works in terminals supporting ANSI codes)
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'

    # Determine color and interpretation based on level
    if percentage >= 75:
        color = RED
        interpretation = "CRITICAL: High stress detected. It's time to prioritize rest and relaxation."
    elif percentage >= 50:
        color = YELLOW
        interpretation = "HIGH: Elevated stress level. Take a moment to breathe and manage your workload."
    elif percentage >= 25:
        color = GREEN
        interpretation = "MODERATE: Stress is manageable. Keep an eye on your self-care."
    else:
        color = GREEN
        interpretation = "LOW: You seem relaxed and well-managed. Great job!"

    # Build the meter visualization
    meter = color + "█" * filled_chars + ENDC + "-" * empty_chars
    print("\n" + "=" * 55)
    print(f"| {color}STRESS METER{ENDC}: [{meter}] {percentage: >3}% |")
    print("=" * 55 + "\n")
    print(f"Interpretation: {interpretation}")
    print("-" * 55)

def run_stress_meter():
    """
    Main function to run the stress meter application.
    """
    print("--- Richard's Mental Wellness Stress Meter ---")
    print("Please rate the following aspects of your life on a scale of 0 (Worst) to 10 (Best).\n")

    # Question 1: Sleep Quality (Direct correlation to stress management)
    sleep_quality = get_validated_input(
        "1. How would you rate your sleep quality last night (0=Restless, 10=Deeply Rested)? ",
        0, 10
    )

    # Question 2: Workload Management (Indicator of external pressure)
    workload = get_validated_input(
        "2. How manageable is your current workload/to-do list (0=Overwhelmed, 10=Fully Controlled)? ",
        0, 10
    )

    # Question 3: Current Mood/Emotional State (Indicator of internal reaction to stress)
    mood = get_validated_input(
        "3. How would you describe your current mood (0=Highly Irritable, 10=Calm and Happy)? ",
        0, 10
    )

    print("\nCalculating your stress level...")
    time.sleep(1) # Simulate processing time for dramatic effect

    stress_level = calculate_stress_level(sleep_quality, workload, mood)
    display_meter(stress_level)

if __name__ == "__main__":
    run_stress_meter()
