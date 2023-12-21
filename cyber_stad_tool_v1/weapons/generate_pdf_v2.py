from reportlab.pdfgen import canvas


def create_pdf():
    c = canvas.Canvas("simple_pdf.pdf")
    c.drawString(100, 750, "Hello, I am a PDF document created with Python!")
    c.save()

if __name__ == "__main__":
    create_pdf()