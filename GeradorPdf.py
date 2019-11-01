# encoding: utf-8
from datetime import date
from fpdf import fpdf


class GeradorPdf():

    def __init__(self, tipo_relatorio, titulo_relatorio, nome_empresa, periodo_inicial, periodo_final, funcao='',
                 turno=''):
        # Definindo as informações do cabeçalho
        self.pdf = fpdf.FPDF()
        self.pdf.set_font('Arial', '', 13)
        self.informacoes_cabecalho = {
            'tipo_relatorio': tipo_relatorio,
            'titulo_relatorio': titulo_relatorio,
            'nome_empresa': nome_empresa,
            'periodo_inicial': periodo_inicial,
            'periodo_final': periodo_final,
            'data_impressao': date.today().strftime('%d/%m/%Y')
        }
        self.informacoes_cabecalho['periodo_completo'] = self.informacoes_cabecalho['periodo_inicial'] + u" até " + \
                                                         self.informacoes_cabecalho['periodo_final']
        if funcao:
            self.informacoes_cabecalho['funcao'] = funcao
        if turno:
            self.informacoes_cabecalho['turno'] = turno
