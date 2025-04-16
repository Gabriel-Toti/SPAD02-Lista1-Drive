from tkinter import Toplevel, Frame, Label, Entry, Button, END
from tkinter import messagebox
from tkinter.ttk import Treeview

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
  
  def table(self, title, columns, rows, message):
    self.__message_view = Toplevel(master=self)
    self.__message_view.title(title)
    messageLabel = Label(self.__message_view, text=message, anchor="w")
    messageLabel.pack(expand=True)
    table = Treeview(self.__message_view, columns=columns, show="headings")
    for col in columns:
      table.heading(col, text=col)
      table.column(col, anchor="center")
    for item in rows:
      table.insert("", END, values=item)
    table.pack(side="top", anchor="w", fill="both", expand=True)
    close_button = Button(self.__message_view, text="Fechar")
    close_button.pack(expand=True)
    close_button.bind('<Button>', lambda event: self.__message_view.destroy())
