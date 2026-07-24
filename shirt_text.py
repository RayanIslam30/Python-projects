#Code that puts text onto a blank shirt, signifying that a user inputted string 'took CS50'. The shirt is a sort of 'certificate'

from fpdf import FPDF #Module to write text onto image

pdf = FPDF(orientation="P", format="A4") #Get a blank A4 portrait page
pdf.add_page()

pdf.set_font("Helvetica", size=30) #Set the font to Helvetica 
pdf.ln(5) #Move down 5 mm
pdf.cell(w=0,text="Test string", align="C") #Print this string at the top center of the page



pdf.set_font("Helvetica", "B", size=20) #Set font to Helvetica bold, smaller
pdf.set_text_color(255,255,255) #Set text color to white

pdf.output("images/test.pdf")