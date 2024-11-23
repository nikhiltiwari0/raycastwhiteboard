import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Message Typer")
root.configure(background='lightgrey')

# Create a frame to organize the layout
main_frame = tk.Frame(root)
main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create and place the message label and text box
label_message = tk.Label(main_frame, text="Enter your message:")
label_message.pack(anchor="w")

# Text widget for multi-line message input
text_message = tk.Text(main_frame, height=10, width=50)
text_message.pack(side=tk.TOP, fill=tk.BOTH, expand=True)  # Pack the text box at the top of the frame

# Automatically focus on the text box so you can start typing
text_message.focus_set()

# Allow the window to adjust to the content dynamically
root.geometry("500x400")
root.mainloop()