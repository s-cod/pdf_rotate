from PyPDF2 import PdfReader, PdfWriter
import os


def pdf_rotate(name: str):
    pdf = PdfReader(f"./in/{name}")
    pdfw = PdfWriter()
    for i in pdf.pages:
        i.rotate(90)
        pdfw.add_page(i)
    with open(f"./out/{name}", "wb") as f:
        pdfw.write(f)

def main():
    files = os.listdir("./in")
    for i in files:
        # print(i)
        pdf_rotate(i)


if __name__ == "__main__":
    main()
