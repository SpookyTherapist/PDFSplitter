# PDFSplitter

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Description

The PDF Splitter program is a Python-based tool that allows you to split a large PDF file into smaller PDFs based on a list of page numbers provided in a text file.

## Features

- Split a large PDF file into smaller PDFs.
- Maintain the order of pages as specified in the list of page numbers.
- Easy-to-use and suitable for both developers and non-developers.

## Getting Started

### Prerequisites

To use this program, you will need:

- Python (3.6 or higher)
- PyPDF2 library
- PyInstaller (optional, for creating an executable)

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/SpookyTherapist/pdf-splitter.git
   ```

2. Install the required Python packages:

   ```
   pip install PyPDF2
   ```

   If you plan to create an executable, you can also install PyInstaller:

   ```
   pip install pyinstaller
   ```

## Usage

1. Prepare your large PDF file (e.g., "large_file.pdf") and the list of page numbers in a text file (e.g., "list of names.txt").

2. Modify the Python script (e.g., "pdf_splitter.py") to specify the file paths and any other custom settings.

3. Run the script:

   ```
   python pdf_splitter.py
   ```

   - You will be prompted to provide the paths to the large PDF file and the list of page numbers.
   - The program will split the PDF file as specified and create the smaller PDFs.

4. If desired, you can create an executable for the program using PyInstaller:

   ```
   pyinstaller --onefile pdf_splitter.py
   ```

   - This will generate a standalone executable that can be run on your system.

## Configuration

- Customize the script as needed to match your specific requirements.
- Ensure that the paths to the large PDF file and the list of page numbers are correctly specified in the script.

## Troubleshooting

If you encounter any issues while running the program, refer to the troubleshooting section in the script or seek assistance from the program's author.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request to submit your contributions.

## License

This program is open-source and available under the [MIT License](LICENSE).

---

Customize this README file with the specific details of your program, including the file names, descriptions, and any additional instructions that users or contributors may need.
