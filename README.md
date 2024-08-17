# MyAccountant

## Description

This project was designed to enhance my Python programming skills by implementing a practical application that performs PDF invoice scraping and data structuring. The program leverages the pdfplumber library to extract data from PDF invoices and then organizes this data into an Excel spreadsheet using openpyxl. Additionally, the project utilizes the tkinter library to provide a graphical user interface for final formatting and interaction. 

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)
- [License](#license)


## Installation

1. **Clone the git :**
   ```bash
   git clone https://github.com/Kernicterus/MyAccountant.git
   ```

2. **Be sure python3 + tkinter are installed:**
   ```bash
   sudo apt-get install python3-tk
   ```

3. **Install dependances:**
   ```bash
    make install
   ```

## Usage

4. **Run the program :**
   ```bash
    make
   ```
   Let's try to select example1 or example2.pdf and output.xlsx. Then open the xlsx file et we can see how the data have been extracted.
   You can also try to scrap example1 and then example2.pdf on the same xlsx file. 

## Aknowledgments
 This project use the following librairies and modules :  
    - openpyxl==3.1.5  
    - pdfplumber==0.11.2

## License
This project is licensed under the MIT License. See the [LICENSE file](LICENSE.md) for more details.