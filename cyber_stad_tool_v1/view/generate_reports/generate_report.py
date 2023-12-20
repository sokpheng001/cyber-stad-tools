from fpdf import FPDF
import time
import sys


class PentestReportGenerator(FPDF):
    def __init__(self):
        super().__init__()
        self.loading_symbols = ["|", "/", "-", "\\"]
        self.loading_index = 0

    def loading_indicator(self):
        # sys.stdout.write(f"\r[*] Generating PDF... {self.loading_symbols[self.loading_index]}")
        sys.stdout.write(f"\r[*] Generating PDF...")
        sys.stdout.flush()
        self.loading_index = (self.loading_index + 1) % len(self.loading_symbols)

    def generate_pdf_report(self):
        # Simulate PDF generation process
        for _ in range(10):
            self.loading_indicator()
            time.sleep(0.1)

        # Your PDF generation code here
        self.add_page()
        self.set_font("Arial", size=12)
        # self.cell(200, 10, txt="Hello, this is your report content.", ln=True, align='C')
        # self.cell(500, txt="Web Application pentest report", ln=True, align="C")

        self.image("logo.png",  x=10, y=8, w=200, h=30)
        # Additional content or customization can be added here

    def output(self, name='output.pdf', dest=''):
        # Disable loading indicator before saving the PDF
        sys.stdout.write("\r" + " " * 30 + "\r")  # Clear the loading indicator
        super().output(name, dest)


if __name__ == "__main__":
    pdf = PentestReportGenerator()
    print("[+] Starting PDF report generation...")
    pdf.generate_pdf_report()
    pdf.output()
    print("\nReport generation complete.")
