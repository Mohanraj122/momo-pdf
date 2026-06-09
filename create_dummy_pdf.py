from reportlab.pdfgen import canvas

def create_pdf(filename):
    c = canvas.Canvas(filename)
    c.drawString(100, 750, "Hello World")
    c.save()

create_pdf("test.pdf")
create_pdf("test2.pdf")
