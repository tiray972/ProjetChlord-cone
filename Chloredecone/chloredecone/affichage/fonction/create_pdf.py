from fpdf import FPDF
import datetime
import os
width = 210
height = 297
ressource="affichage/fonction/resources/"
day=str(datetime.datetime.today().date()) 
class PDF(FPDF):
    def header(self):
        self.image(ressource+'uag.jpg',10,8,25)
        self.set_font('Arial','B',12)
        self.set_text_color(r=0)
        self.cell(0,10, day,align="R")
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial','B',12)
        self.set_text_color(r=155)
        self.cell(0,10, f'Page {self.page_no()}',align="C")
def create_page_garde(text, pdf):
    ville=""
    for lettre in text:
        if lettre != "(":
            ville += lettre
        else:
            break
    pdf.set_font('Arial', '', 24)  
    pdf.ln(60)
    pdf.write(5)
    pdf.ln(10)
    pdf.set_font('Arial', '', 16)
    pdf.cell(width/2,height/2, f'{ville}',align="C")
    pdf.ln(5)
def footer(pdf):
    pdf.image(ressource+'pdf_python-footer.png', 0, height-70, width+20)

def fond_page1(pdf):
    pdf.image(ressource+'bananas-found.jpg', 0, 0, width + 20)
def fond_page2(pdf):
    pdf.image(ressource+'litoraux.jpg', 0, 0, width + 20)
def fond_page3(pdf):
    pdf.image(ressource+'rivière.jpg', 0, 0, width + 20)


def band(pdf):
    pdf.image(ressource+'band.png', 0, 0, width + 20)
def bandB(pdf):
    pdf.image(ressource+'band_bleu.png', 0, 0, width + 20)
def invbandB(pdf):
    pdf.image(ressource+'inv_band_bleu.png', 0, 0, width + 20)
def bandM(pdf):
    pdf.image(ressource+'band_marron.png', 0, 0, width + 20)


#création du pdf    
def make_pdf(titre,ville,data):
    # print((dict(data['tab2']['data'][12]))['uri_taxons_suivis'],"<-------------------")
    
    pdf =PDF('P','mm','Letter')
    pdf.set_font('Arial','B',16) 
    """ PAGE de garde"""
    pdf.add_page()
    create_page_garde(ville,pdf)
    
    hauteur=150
    
    
    

    

    

    #Partie Litoraux
    if (data['meta']['T2']):
        pdf.add_page()
        fond_page2(pdf)
        pdf.add_page()
        bandB(pdf)

    #Partie eau sous téraine
    if (data['meta']['T1']):
        pdf.add_page()
        fond_page3(pdf)
        pdf.add_page()
        bandM(pdf)
        pdf.add_page()
        invbandB(pdf)
    #Partie eau de surface
    if (data['meta']['T3']):
        pdf.add_page()
        fond_page1(pdf)
        pdf.add_page()
        band(pdf)
        
    
    output_path="ville/tmp/"+titre+'.pdf'
    pdf.output(output_path,'F')

    return