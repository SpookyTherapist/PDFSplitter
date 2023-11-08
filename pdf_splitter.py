import PyPDF2
import os

# Read the list of new names from a text file
with open("list_of_names.txt", "r") as file:
    new_names = file.read().splitlines()

# Open the large PDF file
with open("large_file.pdf", "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Iterate through each page and create separate PDFs
    for i, new_name in enumerate(new_names):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[i])

        # Save the separate PDF with the new name
        output_pdf_path = f"{new_name}.pdf"
        with open(output_pdf_path, "wb") as output_pdf:
            pdf_writer.write(output_pdf)

# Clean up: Delete the original large PDF
os.remove("large_file.pdf")
