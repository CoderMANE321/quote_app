import tkinter as tk
from quote_fetch import send_request

# creates instance of app
# has once function setting label triggered by button event
class quote_app:
    
    def __init__(self):
        self.msgs = ["Ready to get inspired?"]
        self.counter = 0

    def run_app(self):

        msgs = self.msgs

        def button_clicked():
            send_request(msgs)
            label.config(text=msgs[self.counter])
            if self.counter < len(msgs) - 1:
                self.counter += 1
            else:
                self.counter = 0

        root = tk.Tk()
        root.title("Quote App")
        root.geometry('600x300')

        label = tk.Label(root, text=msgs[0])
        label.pack()

        button = tk.Button(root, 
                        text="Want a new quote?", 
                        command=button_clicked,
                        activebackground="blue", 
                        activeforeground="white",
                        anchor="center",
                        bd=3,
                        bg="lightgray",
                        cursor="hand2",
                        disabledforeground="gray",
                        fg="black",
                        font=("Arial", 12),
                        height=2,
                        highlightbackground="black",
                        highlightcolor="green",
                        highlightthickness=2,
                        justify="center",
                        overrelief="raised",
                        padx=10,
                        pady=5,
                        width=15,
                        wraplength=100)

        button.pack(padx=20, pady=20)

        root.mainloop()


