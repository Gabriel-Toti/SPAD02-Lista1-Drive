from tkinter import Toplevel
from tkinter import messagebox

class consultReportView(tk.Toplevel):

  def __init__(self, ReportController):
    self.ReportController = ReportController

    tk.Toplevel.__init__(self)
    self.geometry('400x200')
    self.title("Consultar Ranking")

    self.frameStartDate = tk.Frame(self)
    self.frameStartDate.pack()
    self.frameEndDate = tk.Frame(self)
    self.frameEndDate.pack()
    self.frameButton = tk.Frame(self)
    self.frameButton.pack()

    self.labelStartDate = tk.Label(self.frameStartDate, text="Data Inicial (YYYY-MM-DD): ")
    self.labelStartDate.pack(side='left')
    self.labelEndDate = tk.Label(self.frameEndDate, text="Data Final (YYYY-MM-DD): ")
    self.labelEndDate.pack(side='left')

    self.start_date = tk.Entry(self.frameStartDate, width=20)
    self.start_date.pack(side='left')
    self.end_date = tk.Entry(self.frameEndDate, width=20)
    self.end_date.pack(side='left')

    self.buttonSubmit = tk.Button(self.frameButton, text='Consultar')
    self.buttonSubmit.pack(side='left')
    self.buttonSubmit.bind('<Button>', ReportController.searchHandler)

  def showView(self, title, msg):
    messagebox.showinfo(title, msg)
