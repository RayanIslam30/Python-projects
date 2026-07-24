#Code that puts text onto a blank shirt, signifying that a user inputted string 'took CS50'. The shirt is a sort of 'certificate'

from fpdf import FPDF #Module to write text onto image

def main():
    shirt(input("Enter full name: "))

def shirt(name):
    pdf = FPDF(orientation="P", format="A4") #Get a blank A4 portrait page
    pdf.add_page()

#Print our header
    pdf.set_font("Helvetica", size=50) #Set the font to Helvetica 
    pdf.ln(15) #Move down 15 mm
    pdf.cell(w=0,text="CS50 Shirtificate", align="C") #Print this string at the top center of the page

#Put our blank shirt image
    pdf.ln(20) #Move down 20 mm
    pdf.image("images/shirt_template.png", x=11,y=70, w=190)

#Print text on shirt
    pdf.ln(85) #Move down 85 mm
    pdf.set_font("Helvetica", size=20) #Set font to Helvetica bold, smaller
    pdf.set_text_color(255,255,255) #Set text color to white
    pdf.cell(w=200, text=f"{name} took CS50", align="C")
    pdf.output("images/shirtificate.pdf")

if __name__ == "__main__": #Only run main if called directly
    main()