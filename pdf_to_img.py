import tkinter
import fitz
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import time

window = tkinter.Tk()
window.geometry('400x200')
window.resizable(False, False)
window.title('Pdf Image Extractor')


def extract():
	if pdf_entry.get() and img_entry.get():
		doc = fitz.open(pdf_entry.get())
		xref_list = []
		for page in doc:
			xref_list.append(page.get_images())

		xref = []
		for i in xref_list:
			for z in i:
				xref.append(z[0])

		progress_bar.configure(maximum= len(xref))
		count = 1
		for y in xref:
			time.sleep(0.05)
			img = doc.extract_image(y)
			pix = fitz.Pixmap(img['image'])
			pix.pil_save(f'{img_entry.get()}/image{count}.jpg')
			progress_bar['value'] +=1
			count +=1
			window.update_idletasks()
		else:
			progress_bar['value'] = 0
			messagebox.showinfo(title='Info', message='Extracted Images Successfully.')
	else:
		messagebox.showwarning(title='Error', message='Pdf or Save Path not selected.')


def select_pdf():
	path= filedialog.askopenfilename(filetypes= (("Pdf Files", "*.pdf"),))
	pdf_entry.delete(0, 'end')
	pdf_entry.insert(0, path)


def select_save():
	path = filedialog.askdirectory()
	img_entry.delete(0, 'end')
	img_entry.insert(0, path)


frame = tkinter.Frame()
pdf_label = tkinter.Label(frame, text='From Pdf', font=('Arial', 15))
pdf_label.grid(row=0, column=0, pady=10)
pdf_entry = tkinter.Entry(frame, font=('Arial', 15))
pdf_entry.grid(row=0, column=1)
img_label = tkinter.Label(frame, text='Save To', font=('Arial', 15))
img_label.grid(row=1, column=0)
img_entry = tkinter.Entry(frame, font=('Arial', 15))
img_entry.grid(row=1, column=1)
button = tkinter.Button(frame, text='Extract', font=('Arial', 12), command=extract)
button.grid(row=2, column=0, columnspan=3, pady=10)
button_add_pdf = tkinter.Button(frame, text='+', command=select_pdf)
button_add_pdf.grid(row=0, column=2)
button_add_save = tkinter.Button(frame, text='+', command=select_save)
button_add_save.grid(row=1, column=2)
progress_bar = ttk.Progressbar(frame, orient='horizontal', length=200)
progress_bar.grid(row=3, column=0, columnspan=3, pady=10)
disclaimer = tkinter.Label(window, text="Disclaimer: All files will be saved under the\ndefault name 'image' followed by serial number.\nCopyright: © Surendar Singh")
disclaimer.pack(side='bottom')
frame.pack()

window.mainloop()
