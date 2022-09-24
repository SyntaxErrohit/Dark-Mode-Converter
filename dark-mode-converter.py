import tkinter.filedialog, pdf2image, numpy, PIL, img2pdf, os

path = tkinter.filedialog.askopenfilename()
images = pdf2image.convert_from_path(path, poppler_path="bin")
photos = []

for i in range(len(images)):
    photos.append(f"photo{i}.png")
    PIL.Image.fromarray(255 - numpy.array(images[i])).save(photos[-1])

with open(path.replace(".pdf", " inverted.pdf"), "wb") as pdf:
    pdf.write(img2pdf.convert(photos, layout_fun=img2pdf.get_layout_fun((597.6, 842.4))))

for i in photos:
    os.remove(i)

print("Inverting colors is done.")