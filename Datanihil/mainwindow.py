#!/usr/bin/python
# coding: latin-1

"""
main window for the Datanihil app test
This app aims to provide an easy way to write down procedures for
the support of my company (for a personal use)

"""

import Tkinter as Tk

class Interface(Tk.Frame):
    """
    definition of the main window interface (self explainatory huh?)

    """

    def __init__(self, window):
        Tk.Frame.__init__(self, window, width=600, height=400)
        self.root = window
        self.pack(fill=Tk.BOTH)


        self.root.mainloop()


def main():
    """
    main function

    """

    window = Tk.Tk()
    app = Interface(window)
    pass


if __name__ == '__main__':
    main()
