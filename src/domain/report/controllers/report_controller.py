from ..models.report_model import ReportModel
from ..data.report_dao import ReportDataAccess
from ..views.report_view import ReportView
from datetime import datetime

class ReportController():

    def __init__(self, controller):
    self.controller = controller
    self.list = []

  def consultReport(self):
    self.reportConsultView = ReportView.consultReportView(self)

#-------------------

  def searchHandler(self, event):

    start_date = self.reportConsultView.start_date.get()
    end_date = self.reportConsultView.end_date.get()

    if(start_date == '' or end_date == ''):
      self.reportConsultView.showView('Erro', 'Há campos em branco!')
      return

    try:
      start = datetime.strptime(start_date, '%Y-%m-%d')
      end = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
      self.reportConsultView.showView('Erro', 'Data inválida! Use o formato AAAA-MM-DD.')
      self.reportConsultView.start_date.delete(
        0, len(self.reportConsultView.start_date.get()))
      self.reportConsultView.end_date.delete(
        0, len(self.reportConsultView.end_date.get()))
      return

    if start > end:
      self.reportConsultView.showView('Erro', 'Data inicial maior que a data final!')
      self.reportConsultView.start_date.delete(
        0, len(self.reportConsultView.start_date.get()))
      self.reportConsultView.end_date.delete(
        0, len(self.reportConsultView.end_date.get()))
      return
      
    self.list = self.takeList(start, end)
    
    str = ''
    if self.list is not None:
      for i in self.list:
        #AJUSTAR CONFORME DEVOLUTIVA DO BD
        #str += f'{i.employee_id} - Total de Pedidos: {i.orders} = {i.amount} \n'

        self.reportConsultView.showView('Relatório de Ranking', str)
        self.reportConsultView.start_date.delete(
          0, len(self.reportConsultView.start_date.get()))
        self.reportConsultView.end_date.delete(
          0, len(self.reportConsultView.end_date.get()))
        return
        
    self.reportConsultView.showView('Erro', 'Não há registros de vendas nesse período!')
    self.reportConsultView.start_date.delete(
      0, len(self.reportConsultView.start_date.get()))
    self.reportConsultView.end_date.delete(
      0, len(self.reportConsultView.end_date.get()))


#-------------------

  def clearHandler(self, event):
    self.reportConsultView.start_date.delete(
        0, len(self.reportConsultView.start_date.get()))
    self.reportConsultView.end_date.delete(
        0, len(self.reportConsultView.end_date.get()))

#-------------------

  def takeList(self, start, end):
    #AQUI FICARIA A LÓGICA DE REQUISIÇÃO E DEVOLUTIVA DO BD (LIST)
    return list