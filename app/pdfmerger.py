import tkinter 
from tkinter import filedialog
from tkinter import *
import PyPDF2
import datetime

fileCount = 0
filepaths = []

# Create an instance of tkinter frame or window
win = Tk()
win.title("PDF Merger")
win.geometry('500x300')

def selectFile():
    global fpath, fileCount
    fpath = filedialog.askopenfilenames(title="Select file", 
            filetypes=(("pdf files", ".pdf"),))
    fileCount += 1
    filepaths.append(fpath[0])
    appendtext = str(fileCount) + " files added for merge"
    Label(win, text=appendtext).place(x = 10, y = 50)

def mergePDFs():
    dt = datetime.datetime.now()
    merger = PyPDF2.PdfFileMerger()
    for file in range(len(filepaths)):
        merger.append(filepaths[file])
    merger.write(dt.strftime("%Y%m%d_%H%M%S") + "_resultantDoc.pdf")
    merger.close()
    Label(win, text = "---Merged selcetd PDFs---").place(x = 184, y = 180)

# GUI building blocks
Label(win, text="Select PDF files in order").place(x = 10, y = 10)
pixel = tkinter.PhotoImage(width = 1, height = 1)
selectFileButton = Button(win, text = "Select", activeforeground = 'white', image = pixel, width = 30, 
                height = 13, compound = "c", activebackground = '#46403E', command = selectFile)
selectFileButton.place(x = 150, y = 10)

mergeButton = Button(win, text = "Merge", bg = '#1DF12A', activeforeground = 'white', image = pixel, 
        width = 40, height = 13, compound = "c", activebackground = '#46403E', command = mergePDFs)
mergeButton.place(x = 230, y = 150)

# quit gui
QuitButton = Button(win, text="Quit", activeforeground='white', activebackground='#46403E', 
                    command = win.destroy)
QuitButton.place(x = 235, y = 270)


win.mainloop()