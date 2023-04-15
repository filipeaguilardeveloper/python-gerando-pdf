# encoding: utf-8
from pdfGenerator import pdfGenerator as pdfgen

doc = []

doc.append(pdfgen(tipo_relatorio=1, titulo_relatorio=u"Apuração de Comissão",
                            nome_empresa=u"RS Embreagem LTDA.", periodo_inicial=u"01/07/2019",
                            periodo_final=u"31/07/2019"))


doc.append(pdfgen(tipo_relatorio=2, titulo_relatorio=u"Relatório de comissão de mecânico",
                            nome_empresa=u"QRLabel58", periodo_inicial=u"01/07/2019", periodo_final=u"31/07/2019",
                            funcao=u"Ajudante de mecânico"))

doc.append(pdfgen(tipo_relatorio=3, titulo_relatorio=u"Relatório de comissão telemarketing",
                            nome_empresa=u"RS Embreagem LTDA.", periodo_inicial=u"01/07/2019",
                            periodo_final=u"31/07/2019", turno=u"Tarde"))


doc.append(pdfgen(tipo_relatorio=4, titulo_relatorio=u"Relatório de prêmio",
                            nome_empresa=u"RS Embreagem LTDA.", periodo_inicial=u"01/07/2019",
                            periodo_final=u"31/07/2019"))


doc.append(pdfgen(tipo_relatorio=5, titulo_relatorio=u"Relatório de comissão de vendedor",
                            nome_empresa=u"RS Embreagem LTDA.", periodo_inicial=u"01/07/2019",
                            periodo_final=u"31/07/2019"))



for i in range(len(doc)):
    #print(doc[i])
    doc[i].criarCabecalhoPdf()
    doc[i].prepararDadosTabela()
    doc[i].criarDocumentoPdf(f'modelo_exemplo{i}',folder='docs')