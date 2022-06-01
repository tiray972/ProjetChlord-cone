from fpdf import FPDF
import datetime
width = 210
height = 297
ressource="affichage/fonction/resources//"
day=str(datetime.datetime.today().date()) 
class PDF(FPDF):
    def header(self):
        band(self)
        self.image(ressource+'uag.jpg',10,8,25)
        self.set_font('Arial','B',12)
        self.set_text_color(r=255)
        self.cell(0,10, day,align="R")
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial','B',12)
        self.set_text_color(r=155)
        self.cell(0,10, f'Page {self.page_no()}/'+"{nb}",align="C")
def create_title(day, pdf):
  # Unicode is not yet supported in the py3k version; use windows-1252 standard font
  pdf.set_font('Arial', '', 24)  
  pdf.ln(60)
  pdf.write(5)
  pdf.ln(10)
  pdf.set_font('Arial', '', 16)
  pdf.write(4, f'{day}')
  pdf.ln(5)
def footer(pdf):
    pdf.image(ressource+'pdf_python-footer.png', 0, height-70, width+20)
def fond_page1(pdf):
    pdf.image(ressource+'bananas-found.jpg', 0, 0, width + 20)
def band(pdf):
    pdf.image(ressource+'band.png', 0, 0, width + 20)
def make_pdf(titre,ville):
    pdf =PDF('P','mm','Letter')
    pdf.set_font('Arial','B',16)
    pdf =PDF('P','mm','Letter')
    pdf.add_page()
    
    
    create_title(ville,pdf)
    
    hauteur=150

    """ PAGE 1"""
    pdf.add_page()
    

    create_title(titre, pdf)

    fond_page1(pdf)


    pdf.add_page()

    # footer(pdf)
    output_path="ville/tmp/"+titre+'.pdf'
    pdf.output(output_path,'F')

    return