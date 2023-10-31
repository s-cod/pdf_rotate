from PyPDF2 import PdfReader, PdfWriter
import os


def pdf_rotate(name: str):
    pdf = PdfReader(f"./in/{name}")
    pdf_w = PdfWriter()
    for p in pdf.pages:
        p.rotate(90)
        pdf_w.add_page(p)
    with open(f"./out/{name}", "wb") as f:
        pdf_w.write(f)

def main():
    files = os.listdir("./in")
    for i in files:
        # print(i)
        pdf_rotate(i)


if __name__ == "__main__":
    main()
