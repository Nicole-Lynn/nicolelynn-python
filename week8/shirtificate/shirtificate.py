from fpdf import FPDF


# The orientation should be Portrait. Format should be A4, 210mm wide by 297mm tall.
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

# The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
pdf.set_font("Helvetica", size=48)
pdf.cell(0, 57, text="CS50 Shirtificate", center=True, align="C")

# The shirt’s image should be centered horizontally.
pdf.image("shirtificate.png", x=10, y=70, w=190, keep_aspect_ratio=True)

# The user’s name should be on top of the shirt, in white text.
pdf.set_font("Helvetica", size=24)
pdf.set_text_color(255, 255, 255)  # RGB notation for the colour white
pdf.ln(122)
pdf.cell(text=f"{input('Name: ')} took CS50", new_x="CENTER", align="C", center=True)

pdf.output("shirtificate.pdf")
