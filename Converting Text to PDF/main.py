# تبدیل متون به PDF

from fpdf import FPDF

# تابع برای تبدیل متن به PDF
def text_to_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    pdf.multi_cell(0, 10, text)  # نوشتن متن در صفحه PDF
    
    pdf.output(filename)  # ذخیره فایل PDF

# دریافت متن و نام فایل
text = input("Enter the text you want to convert to PDF: ")
filename = input("Enter the output PDF file name: ")

# تبدیل و ذخیره PDF
text_to_pdf(text, filename)
print(f"Text has been converted to PDF and saved as {filename}.")
