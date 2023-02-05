import tkinter as tk

# List to store scores
scores = [("User1", 50), ("User2", 60), ("User3", 70)]

# Function to get the leaderboard
def get_leaderboard():
    # Sort scores in descending order
    scores.sort(key=lambda x: x[1], reverse=True)

    # Clear the leaderboard frame
    for widget in leaderboard_frame.winfo_children():
        widget.destroy()

    # Display the leaderboard
    tk.Label(leaderboard_frame, text="Username", font=("Helvetica", 16)).pack()
    tk.Label(leaderboard_frame, text="Score", font=("Helvetica", 16)).pack()
    for user, score in scores:
        tk.Label(leaderboard_frame, text=user, font=("Helvetica", 14)).pack()
        tk.Label(leaderboard_frame, text=str(score), font=("Helvetica", 14)).pack()

# Function to show the leaderboard
def show_leaderboard():
    get_leaderboard()
    leaderboard_frame.pack(fill="both", expand=True)

# Function to hide the leaderboard
def hide_leaderboard():
    leaderboard_frame.pack_forget()

# Create the window
root = tk.Tk()
root.title("Leaderboard")

# Create the main frame
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Create the show leaderboard button
show_leaderboard_button = tk.Button(main_frame, text="Show Leaderboard", command=show_leaderboard)
show_leaderboard_button.pack()

# Create the leaderboard frame
leaderboard_frame = tk.Frame(root)

# Start the event loop
root.mainloop()
