from fpdf import FPDF
def make_pdf(titre,ville):
    pdf =FPDF('P','mm','Letter')
    pdf.set_font('Arial','B',16)
    pdf.add_page()
    pdf.cell(40,10 ,'Hell Worlddddddddddddd')
    output_path="ville/tmp/"+titre+'.pdf'
    pdf.output(output_path,'F')
    return