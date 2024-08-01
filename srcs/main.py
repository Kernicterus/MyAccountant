from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from myaccountant import MyAccountant

def quit_program():
    root.quit()
    root.destroy()

def select_pdf():
    global filepathpdf
    filepathpdf = askopenfilename(title="Select a pdf to scrap",filetypes=[('pdf files','.pdf')])
    if filepathpdf:
        pdf_label.config(text=filepathpdf)

def select_xlsx():
    global filepathxlsx
    filepathxlsx = askopenfilename(title="Select a xlsx to store data",filetypes=[('excel files','.xlsx')])
    if filepathxlsx:
        xlsx_label.config(text=filepathxlsx)

def run_program():
    try:
        str = MyAccountant(filepathpdf,filepathxlsx)
    except :
        str = "ERROR : two files must be selected"
    showinfo("INFO", str)

def graphical_window():
    global root, pdf_label, xlsx_label

    root = Tk()
    root.title("MyAccountant")

    pdf_label = Label(root, text="No PDF selected")
    pdf_label.pack(pady=10)
    xlsx_label = Label(root, text="No XLSX selected")
    xlsx_label.pack(pady=10)
    
    Button(root, text="Select PDF", command=select_pdf).pack(pady=5)
    Button(root, text="Select XLSX", command=select_xlsx).pack(pady=5)
    Button(root, text ='Run scraping', command=run_program).pack(side=LEFT, padx=5, pady=5)
    Button(root, text ='quit', command=quit_program).pack(side=RIGHT, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    graphical_window()		