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
    create the main window interface (self explainatory huh?)

    """
    def cleanlist(self):
        self.proclist.delete(0, Tk.END) # clear

    def __init__(self, window):

        Tk.Frame.__init__(self, window)
        self.root = window

        self.search = Tk.Entry(self.root)
        self.search.grid(column=0, row=0, columnspan=2)

        self.proclist = Tk.Listbox(self.root)
        self.proclist.grid(column=0, row=1, columnspan=2, rowspan=6)

        self.currentproc = Tk.Label(self.root, text="This is a test, but "\
            "a very nice one", anchor=Tk.E)
        self.currentproc.grid(column=3, row=0, columnspan=4, rowspan=8)


        for item in ["one", "two", "three", "four"]:
            self.proclist.insert(Tk.END, item)


        #test
        self.button = Tk.Button(self.root, text="clean", command=self.cleanlist)
        self.button.grid(column=7, row=0)

        return

    def start(self):
        """
        show the window and launch its main loop

        """

        self.root.mainloop()
        return



def main():
    """
    main function

    """

    window = Tk.Tk()
    app = Interface(window)
    app.start()

    pass


if __name__ == '__main__':
    main()
