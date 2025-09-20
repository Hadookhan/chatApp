import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)


    def display_contents(self, event):
        pass

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

def createApp():
    myApp = App()

    myApp.master.title("Chat App")
    myApp.master.maxsize(1000, 500)

    myApp.mainloop()