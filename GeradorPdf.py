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
        
    def criarCabecalhoPdf(self):
                '''
                :param tipo_relatorio:
                1 p/ 'apuração de comissão';
                2 p/ 'comissão mecânico';
                3 p/ 'comissão telemarketing';
                4 p/ 'Relatório de prêmio';
                5 p/ 'Relatório de comissão de vendedor'
                '''
                if self.informacoes_cabecalho['tipo_relatorio'] == 1:
                    self.pdf.add_page('Portrait')
                    self.largura_doc = self.pdf.w - 20
                    # titulo principal
                    self.pdf.set_font('Arial', 'B', 13)
                    self.pdf.cell(self.largura_doc, 8, txt=self.informacoes_cabecalho['titulo_relatorio'].upper(), border='LTR',
                                ln=1, align='C')
                    # Periodo pesquisado
                    self.pdf.set_font('Arial', '', 10)
                    self.pdf.cell(self.largura_doc / 3, 8, txt=self.informacoes_cabecalho['periodo_completo'], border='LB',
                                align='L')
                    # Nome empresa
                    self.pdf.set_font('Arial', 'B', 10)
                    self.pdf.cell(self.largura_doc / 3, 8, txt=self.informacoes_cabecalho['nome_empresa'].upper(), border='B',
                                align='C')
                    # Data de impressao
                    self.pdf.set_font('Arial', '', 10)
                    self.pdf.cell(self.largura_doc / 3, 8,
                                txt=u'Data de impressão: ' + self.informacoes_cabecalho['data_impressao'], border='RB', ln=1,
                                align='R')

                    self.criarCabecalhoSecundarioPdf()

                elif self.informacoes_cabecalho['tipo_relatorio'] == 2:
                    self.pdf.add_page('Landscape')
                    self.largura_doc = self.pdf.w - 20
                    # titulo principal
                    self.pdf.set_font('Arial', 'B', 13)
                    self.pdf.cell(self.largura_doc, 8, txt=self.informacoes_cabecalho['titulo_relatorio'].upper(),
                                border='LTR', ln=1, align='C')
                    # função
                    self.pdf.set_font('Arial', '', 10)
                    self.pdf.cell(self.largura_doc, 8, txt=u'Função: ' + self.informacoes_cabecalho['funcao'],
                                border='LR', ln=1, align='C')
                    # Periodo pesquisado
                    self.pdf.set_font('Arial', '', 10)
                    self.pdf.cell(self.largura_doc / 3, 8, txt=self.informacoes_cabecalho['periodo_completo'], border='LB',
                                align='L')
                    # Nome empresa
                    self.pdf.set_font('Arial', 'B', 10)
                    self.pdf.cell(self.largura_doc / 3, 8, txt=self.informacoes_cabecalho['nome_empresa'].upper(),
                                border='B', align='C')
                    # Data de impressao
                    self.pdf.set_font('Arial', '', 10)
                    self.pdf.cell(self.largura_doc / 3, 8,
                                txt=u'Data de impressão: ' + self.informacoes_cabecalho['data_impressao'], border='RB', ln=1,
                                align='R')
                    self.criarCabecalhoSecundarioPdf()

                elif self.informacoes_cabecalho['tipo_relatorio'] == 3:
                    self.pdf.add_page('Landscape')
                    self.largura_doc = self.pdf.w - 20
                    # titulo principal
                    self.pdf.set_font('Arial', 'B', 13)
                    self.pdf.cell(self.largura_doc, 8, txt=self.informacoes_cabecalho['titulo_relatorio'].upper(),
                                border='LTR', ln=1, align='C')
                    # turno
                    self.pdf.set_font('Arial', '', 10)
                    self.pdf.cell(self.largura_doc, 8, txt=u'Turno: ' + self.informacoes_cabecalho['turno'],
                                border='LR', ln=1, align='C')
                    # Periodo pesquisado
                    self.pdf.set_font('Arial', '', 10)
                    self.pdf.cell(self.largura_doc / 3, 8, txt=self.informacoes_cabecalho['periodo_completo'], border='LB',
                                align='L')
                    # Nome empresa
                    self.pdf.set_font('Arial', 'B', 10)
                    self.pdf.cell(self.largura_doc / 3, 8, txt=self.informacoes_cabecalho['nome_empresa'].upper(),
                                border='B', align='C')
                    # Data de impressao
                    self.pdf.set_font('Arial', '', 10)
                    self.pdf.cell(self.largura_doc / 3, 8,
                                txt=u'Data de impressão: ' + self.informacoes_cabecalho['data_impressao'], border='RB', ln=1,
                                align='R')

                    self.criarCabecalhoSecundarioPdf()

                elif self.informacoes_cabecalho['tipo_relatorio'] == 4:
                    self.pdf.add_page('Landscape')
                    self.largura_doc = self.pdf.w - 20
                    # titulo principal
                    self.pdf.set_font('Arial', 'B', 13)
                    self.pdf.cell(self.largura_doc, 8, txt=self.informacoes_cabecalho['titulo_relatorio'].upper(),
                                border='LTR', ln=1, align='C')
                    # Periodo pesquisado
                    self.pdf.set_font('Arial', '', 10)
                    self.pdf.cell(self.largura_doc / 3, 8, txt=self.informacoes_cabecalho['periodo_completo'], border='LB',
                                align='L')
                    # Nome empresa
                    self.pdf.set_font('Arial', 'B', 10)
                    self.pdf.cell(self.largura_doc / 3, 8, txt=self.informacoes_cabecalho['nome_empresa'].upper(),
                                border='B', align='C')
                    # Data de impressao
                    self.pdf.set_font('Arial', '', 10)
                    self.pdf.cell(self.largura_doc / 3, 8,
                                txt=u'Data de impressão: ' + self.informacoes_cabecalho['data_impressao'], border='RB', ln=1,
                                align='R')

                elif self.informacoes_cabecalho['tipo_relatorio'] == 5:
                    self.pdf.add_page('Landscape')
                    self.largura_doc = self.pdf.w - 20
                    # titulo principal
                    self.pdf.set_font('Arial', 'B', 13)
                    self.pdf.cell(self.largura_doc, 8, txt=self.informacoes_cabecalho['titulo_relatorio'].upper(),
                                border='LTR', ln=1, align='C')
                    # Periodo pesquisado
                    self.pdf.set_font('Arial', '', 10)
                    self.pdf.cell(self.largura_doc / 3, 8, txt=self.informacoes_cabecalho['periodo_completo'], border='LB',
                                align='L')
                    # Nome empresa
                    self.pdf.set_font('Arial', 'B', 10)
                    self.pdf.cell(self.largura_doc / 3, 8, txt=self.informacoes_cabecalho['nome_empresa'].upper(),
                                border='B', align='C')
                    # Data de impressao
                    self.pdf.set_font('Arial', '', 10)
                    self.pdf.cell(self.largura_doc / 3, 8,
                                txt=u'Data de impressão: ' + self.informacoes_cabecalho['data_impressao'], border='RB', ln=1,
                                align='R')

