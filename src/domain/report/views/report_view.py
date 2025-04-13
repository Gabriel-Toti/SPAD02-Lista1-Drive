from tkinter import Toplevel, Frame, Label, Entry, Button
from tkinter import messagebox

class consultReportView(Toplevel):

  def __init__(self, ReportController):
    self.ReportController = ReportController

    Toplevel.__init__(self)
    self.geometry('400x200')
    self.title("Consultar Ranking")

    self.frameStartDate = Frame(self)
    self.frameStartDate.pack()
    self.frameEndDate = Frame(self)
    self.frameEndDate.pack()
    self.frameButton = Frame(self)
    self.frameButton.pack()

    self.labelStartDate = Label(self.frameStartDate, text="Data Inicial (YYYY-MM-DD): ")
    self.labelStartDate.pack(side='left')
    self.labelEndDate = Label(self.frameEndDate, text="Data Final (YYYY-MM-DD): ")
    self.labelEndDate.pack(side='left')

    self.start_date = Entry(self.frameStartDate, width=20)
    self.start_date.pack(side='left')
    self.end_date = Entry(self.frameEndDate, width=20)
    self.end_date.pack(side='left')

    self.buttonSubmit = Button(self.frameButton, text='Consultar')
    self.buttonSubmit.pack(side='left')
    self.buttonSubmit.bind('<Button>', ReportController.searchHandler)

  def showView(self, title, msg):
    messagebox.showinfo(title, msg)
