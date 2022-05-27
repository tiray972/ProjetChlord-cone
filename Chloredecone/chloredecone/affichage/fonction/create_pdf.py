from fpdf import FPDF

width = 210
height = 297

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
    pdf.image('affichage/fonction/resources//pdf_python-footer.png', 0, height-70, width+20)
def header(pdf):
    pdf.image('affichage/fonction/resources/pdf_python-head.png', 0, 0, width + 20)

def make_pdf(titre,ville):
    pdf =FPDF('P','mm','Letter')
    pdf.set_font('Arial','B',16)
    pdf =FPDF('P','mm','Letter')
    pdf.add_page()
    
    header(pdf)
    create_title(ville,pdf)
    
    hauteur=150
    pdf.image('affichage/fonction/resources//boom.jpg',0+5,hauteur,width/2-5)
    pdf.image('affichage/fonction/resources//boom.jpg',5+(width/2),hauteur,width/2-5)
    """ PAGE 1"""
    pdf.add_page()

    create_title(titre, pdf)

    pdf.image('affichage/fonction/resources//boom.jpg', 0 + 5, hauteur, width / 2 - 5)
    pdf.image('affichage/fonction/resources//boom.jpg', 5 + (width / 2), hauteur, width / 2 - 5)


    pdf.add_page()

    footer(pdf)
    output_path="ville/tmp/"+titre+'.pdf'
    pdf.output(output_path,'F')

    return