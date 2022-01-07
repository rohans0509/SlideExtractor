import img2pdf
import os
def convertToPDF(image_folder="Images",pdf_name="out.pdf"):
    print("Converting...")
    images = [int(i.split('.')[0]) for i in os.listdir(image_folder) if i.endswith(".jpg")]
    images=sorted(images)
    image_locations=[f"{image_folder}/{image}.jpg" for image in images]
    with open(f"Slides/{pdf_name}", "wb") as f:
        f.write(img2pdf.convert(image_locations))
    print(f"Saved pdf as {pdf_name} in Slides")