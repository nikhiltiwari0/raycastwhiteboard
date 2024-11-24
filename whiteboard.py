import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

class Whiteboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Whiteboard")
        self.master.resizable(False, False)

        self.style = Style(theme="pulse")

        self.canvas = tk.Canvas(self.master, width=1200, height=800, bg="white")
        self.canvas.pack()

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(side="top", pady=10)

        button_config = {
            "black": ("dark.Tbutton", lambda: self.change_color("black")),
            "red": ("danger.Tbutton", lambda: self.change_color("red")),
            "green": ("success.Tbutton", lambda: self.change_color("green")),
            "blue": ("info.Tbutton", lambda: self.change_color("blue")),
            "yellow": ("warning.Tbutton", lambda: self.change_color("yellow")),
            "eraser": ("secondary.Tbutton", lambda: self.change_color("white")),
            "clear": ("outline.Tbutton", self.clear_canvas)
        }

        for color, (style, command) in button_config.items():
            button = ttk.Button(self.button_frame, text=color.capitalize(), style=style, command=command)
            button.pack(side="left", padx=5)

        self.color = "black"
        self.old_x = None
        self.old_y = None
        self.line_width = 5

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        self.canvas.bind("<MouseWheel>", self.change_line_width)
    def paint(self, event):
        x, y = event.x, event.y
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, x, y, fill=self.color, width=self.line_width, capstyle=tk.ROUND, smooth=True)

        self.old_x = x
        self.old_y = y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def change_color(self, new_color):
        self.color = new_color

    def change_line_width(self, event):
        if event.delta > 0:
            self.line_width += 1
            if self.line_width > 20:
                self.line_width = 20

        else:
            self.line_width -= 1
            if self.line_width < 1:
                self.line_width = 1

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    whiteboard = Whiteboard(root)
    root.mainloop()

        # self.create_message_widgets()
        # # Create a frame to organize the layout
        # self.main_frame = tk.Frame(self.master)
        # self.main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # # Create and place the message label and text box
        # self.label_message = tk.Label(self.main_frame, text="Enter your message:")
        # self.label_message.pack(anchor="w")

        # # Text widget for multi-line message input
        # self.text_message = tk.Text(self.main_frame, height=10, width=50)
        # self.text_message.pack(side=tk.TOP, fill=tk.BOTH, expand=True)  # Pack the text box at the top of the frame

        # # Automatically focus on the text box so you can start typing
        # self.text_message.focus_set()

        # # Allow the window to adjust to the content dynamically
        # self.master.geometry("500x400")