# encoding: utf-8
from datetime import date
from fpdf import fpdf
import os


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

    def criarCabecalhoSecundarioPdf(self):
        '''
        :param tipo_relatorio:
        1 p/ 'apuração de comissão';
        2 p/ 'comissão mecânico';
        3 p/ 'comissão telemarketing';
        4 p/ 'Relatório de prêmio';
        5 p/ 'Relatório de comissão de vendedor'
        '''
        if self.informacoes_cabecalho['tipo_relatorio'] == 1:
            cell_largura_metade = self.largura_doc / 2
            cell_altura = 7
            self.pdf.set_font('Arial', 'B', 10)
            self.pdf.cell(cell_largura_metade, cell_altura, u"Contabilizadores de resultados".upper(), "LR", 0, "C")
            self.pdf.set_x(cell_largura_metade + 10)
            self.pdf.set_font('Arial', 'B', 10)
            self.pdf.cell(cell_largura_metade, cell_altura, u"Taxas de comissão".upper(), "R", 1, "C")
            self.pdf.set_font('Arial', '', 10)
            self.pdf.cell(cell_largura_metade, cell_altura, u"Quantidade de dias trabalhados: 27", "LR", 0, "L")
            self.pdf.set_x(cell_largura_metade + 10)
            self.pdf.cell(cell_largura_metade, cell_altura, u"Ajudante de mecânico: %", "R", 1, "L")
            self.pdf.cell(cell_largura_metade, cell_altura, u"Meta no mês:  837 carros", "LR", 0, "L")
            self.pdf.set_x(cell_largura_metade + 10)
            self.pdf.cell(cell_largura_metade, cell_altura, u"Mecânico I: %", "R", 1, "L")
            self.pdf.cell(cell_largura_metade, cell_altura, u"Meta de carros media/dia: 31 carros", "LR", 0, "L")
            self.pdf.set_x(cell_largura_metade + 10)
            self.pdf.cell(cell_largura_metade, cell_altura, u"Mecânico II: %", "LR", 1, "L")
            self.pdf.cell(cell_largura_metade, cell_altura, u"Produção mensal alcançada: 922 carros", "LR", 0, "L")
            self.pdf.set_x(cell_largura_metade + 10)
            self.pdf.cell(cell_largura_metade, cell_altura, u"", "LR", 1, "L")
            self.pdf.cell(cell_largura_metade, cell_altura, u"Produção mensal alcançada: 922 carros", "LRB", 0, "L")
            self.pdf.set_x(cell_largura_metade + 10)
            self.pdf.cell(cell_largura_metade, cell_altura, u"", "LRB", 1, "L")

        elif self.informacoes_cabecalho['tipo_relatorio'] == 3:
            cell_largura_metade = self.largura_doc / 2
            cell_altura = 7
            self.pdf.cell(cell_largura_metade, cell_altura, u"Meta: R$ 16.000,00", "LR", 0, "L")
            self.pdf.set_x(cell_largura_metade + 10)
            self.pdf.cell(cell_largura_metade, cell_altura, u"Cálculo Meta - 1% sobre o total da venda", "R", 1, "L")
            self.pdf.cell(cell_largura_metade, cell_altura, u"Super Meta: R$ 20.000,00", "LR", 0, "L")
            self.pdf.set_x(cell_largura_metade + 10)
            self.pdf.cell(cell_largura_metade, cell_altura, u"Cálculo Meta - 1% sobre o total da venda", "R", 1, "L")
            self.pdf.cell(cell_largura_metade, cell_altura, u"Total geral do turno: R$ 55.865,00", "LR", 0, "L")
            self.pdf.set_x(cell_largura_metade + 10)
            self.pdf.cell(cell_largura_metade, cell_altura, u"Cálculo Meta - 1% sobre o total da venda", "R", 1, "L")
            self.pdf.cell(cell_largura_metade, cell_altura, u"", "LRB", 0, "L")
            self.pdf.set_x(cell_largura_metade + 10)
            self.pdf.cell(cell_largura_metade, cell_altura, u"Cálculo Meta - 1% sobre o total da venda", "RB", 1, "L")
    
    def prepararDadosTabela(self):
        '''
        tipo_relatorio:
        1 p/ 'apuração de comissão';
        2 p/ 'comissão mecânico';
        3 p/ 'comissão telemarketing';
        4 p/ 'Relatório de prêmio';
        5 p/ 'Relatório de comissão de vendedor'
        '''
        # Criando a tabela com as informações:
        if self.informacoes_cabecalho['tipo_relatorio'] == 1:
            atributos = ["Produção", "Ajudante", "Mecânico I", "Mecânico II"]
            tuplas = [
                ["0 - 2000", "0,25%", "0,5%", "1%"],
                ["0 - 2000", "0,25%", "0,5%", "1%"]
            ]
            # Criando tabela com as informações
            self.criarTabela(atributos=atributos, tuplas=tuplas, header_font_size=10, body_font_size=10, extra=0)

        elif self.informacoes_cabecalho['tipo_relatorio'] == 2:
            atributos = ["Nome", "Qtde. Carros", "Valor em troca", "Taxa de Comissão", "Valor de Comissão",
                        "Assinatura"]
            tuplas = [
                ['DILSON 1', '78', 'R$ 14.045,50', '1%', 'R$ 127,60', '__________________'],
                ['DILSON 2', '78', 'R$ 4.760,00', '1%', 'R$ 127,60', '__________________'],
                ['DILSON 3', '78', 'R$ 760,00', '1%', 'R$ 127,60', '__________________'],
                ['DILSON 4', '78', 'R$ 12.760,00', '1%', 'R$ 127,60', '__________________'],
                ['DILSON 3', '78', 'R$ 760,00', '1%', 'R$ 127,60', '__________________'],
                ['DILSON 4', '78', 'R$ 12.760,00', '1%', 'R$ 127,60', '__________________']
            ]
            tupla_totais = ["T. carros", "T. v.troca", "", "T. v.comissão"]

            # Criando tabela com as informações
            self.criarTabela(atributos=atributos, tuplas=tuplas, tupla_totais=tupla_totais, header_font_size=10,
                            body_font_size=10, extra=0)

        elif self.informacoes_cabecalho['tipo_relatorio'] == 3:
            atributos = ["Operador", "Produção", "Atingiu a Meta?", "Atingiu Super Meta?", "Taxa Meta",
                        "Taxa SuperMeta",
                        "Valor Meta",
                        "Valor SuperMeta", "Total"]
            tuplas = [
                ['DARLEY LOPES', 'R$ 21.731,00', 'SIM', 'SIM', '1%', '1,5%', 'R$ 00,00', 'R$ 325,96', 'R$ 0,00'],
                ['DEIVID SANTOS', 'R$ 20.379,00', 'SIM', 'SIM', '1%', '1,5%', 'R$ 00,00', 'R$ 305,69', 'R$ 0,00'],
                ['MATHEUS FELIPE', 'R$ 13.585,00', 'NÃO', 'NÃO', '1%', '1,5%', 'R$ 00,00', 'R$ 0,00', 'R$ 0,00'],
                ['RAFAEL SOARES', 'R$ 170,00', 'SIM', 'NÃO', '1%', '1,5%', 'R$ 00,00', 'R$ 157,91', 'R$ 0,00']
            ]
            tupla_totais = ["T. produção", "", "", "", "", "T. Meta", "T. supermeta", "T. total"]

            # Criando tabela com as informações
            self.criarTabela(atributos=atributos, tuplas=tuplas, tupla_totais=tupla_totais, header_font_size=7,
                            body_font_size=7, extra=0)

        elif self.informacoes_cabecalho['tipo_relatorio'] == 4:
            atributos = ["Nome", "Valor em troca", "Valor da comissão", "Assinatura"]
            tuplas = [
                ['PATRICK GONÇALVES MEC', 'R$ 16.920,00', 'R$ 250,00', '_________________'],
                ['GUILHERME JUNIOR MENDES MEC', 'R$ 16.677,00', 'R$ 50,00', '_________________']
            ]
            tupla_totais = ["", "R$300,00", "", " "]

            # Criando tabela com as informações
            self.criarTabela(atributos=atributos, tuplas=tuplas, tupla_totais=tupla_totais, header_font_size=10,
                            body_font_size=10, extra=0)

        elif self.informacoes_cabecalho['tipo_relatorio'] == 5:
            atributos = ["Nome", "Qtde. Carros", "Produção", "Média", "Produção + Média", "Taxa", "Valor da comissão",
                        "Assinatura"]
            tuplas = [
                ['Alexandre Siqueira Cardoso', '416', 'R$ 83.809,10', 'R$ 0,00', 'R$ 83.809,10', '0,5%', 'R$ 419,05',
                '________________'],
                ['Lucas Almeida', '380', 'R$ 642,00', 'R$ R$ 48.657,82', 'R$ 49.299,82', '0,5%', 'R$ 420,00',
                '________________']
            ]
            tupla_totais = ["", "R$ 84.451,10", "", "", "", "839,05", ""]

            # Criando tabela com as informações
            self.criarTabela(atributos=atributos, tuplas=tuplas, tupla_totais=tupla_totais, header_font_size=7,
                            body_font_size=7, extra=0)

    def criarTabela(self, atributos, tuplas, tupla_totais='', header_font_size=10, body_font_size=10, extra=0.5,
                    espacamento=2):
        '''
        :param pdf: instância de FDPF
        :param atributos: array contendo as colunas da tabela
        :param tuplas: array contendo as tuplas da tabela
        :param tupla_totais: array contendo a tupla de totais (quando houver)
        :param header_font_size: tamanho da fonte do cabeçalho da tablea
        :param body_font_size: tamanho da fonte do corpo da tabela
        :param extra: medida extra adicionada à largura das colunas
        tipo_relatorio:
        1 p/ 'apuração de comissão';
        2 p/ 'comissão mecânico';
        3 p/ 'comissão telemarketing';
        4 p/ 'Relatório de prêmio';
        5 p/ 'Relatório de comissão de vendedor'
        '''

        qtde_atributos = len(atributos)
        col_largura = self.largura_doc / qtde_atributos + extra
        col_altura = 5

        # Criando o contorno do cabeçalho da tabela:
        self.pdf.line(10, self.pdf.get_y(), 10, self.pdf.get_y() + col_altura * espacamento)
        self.pdf.line(10, (self.pdf.get_y() + col_altura * espacamento), self.pdf.w - 10,
                    (self.pdf.get_y() + (col_altura * espacamento)))
        self.pdf.line(self.pdf.w - 10, self.pdf.get_y(), self.pdf.w - 10, self.pdf.get_y() + col_altura * espacamento)

        # Adicionando os atributos da tabela do PDF
        self.pdf.set_font('Arial', 'B', header_font_size)
        for atributo in atributos:
            atributo = str(atributo)
            self.pdf.cell(col_largura, col_altura * espacamento, txt=atributo.upper(), border='',
                        align="R")
        self.pdf.ln(col_altura * espacamento)

        # Adcionando as tuplas da tabela PDF:
        self.pdf.set_font('Arial', '', body_font_size)
        for tupla in tuplas:
            # Criando o contorno para cada tupla da tabela do PDF:
            self.pdf.line(10, self.pdf.get_y(), 10, self.pdf.get_y() + col_altura * espacamento)
            self.pdf.line(10, (self.pdf.get_y() + col_altura * espacamento), self.pdf.w - 10,
                        (self.pdf.get_y() + col_altura * espacamento))
            self.pdf.line(self.pdf.w - 10, self.pdf.get_y(), self.pdf.w - 10,
                        self.pdf.get_y() + col_altura * espacamento)

            for item in tupla:
                item = str(item)
                self.pdf.cell(col_largura, col_altura * espacamento, txt=item[0:20].upper(), border='',
                            align="R")
            self.pdf.ln(col_altura * espacamento)

        if tupla_totais:
            # Adicionando a tupla de totais da tabela PDF:
            # Criando o contorno para cada tupla da tabela do PDF:
            self.pdf.line(10, self.pdf.get_y(), 10, self.pdf.get_y() + col_altura * espacamento)
            self.pdf.line(10, (self.pdf.get_y() + col_altura * espacamento), self.pdf.w - 10,
                        (self.pdf.get_y() + col_altura * espacamento))
            self.pdf.line(self.pdf.w - 10, self.pdf.get_y(), self.pdf.w - 10,
                        self.pdf.get_y() + col_altura * espacamento)
            self.pdf.set_font('Arial', 'B', header_font_size)
            self.pdf.cell(col_largura, col_altura * espacamento, txt=u"Totais: ".upper(), border='',
                        align="R")
            self.pdf.set_font('Arial', '', body_font_size)
            for item in tupla_totais:
                item = str(item)
                self.pdf.cell(col_largura, col_altura * espacamento, txt=item.upper(), border='',
                            align="R")
    
    def criarDocumentoPdf(self, pdf_name, folder=""):
        '''
        :param pdf_name: nome do arquivo .pdf
        :param folder: pasta de destino do arquivo
        '''

        dir = os.getcwd()
        path = dir + "/" + folder
        os.makedirs(path, exist_ok=True)
        print(f"\033[0;32mDocumento criado em : {path}\033[0m")

        pdf_file = path + "/" + pdf_name + '.pdf'

        self.pdf.output(pdf_file, 'F')