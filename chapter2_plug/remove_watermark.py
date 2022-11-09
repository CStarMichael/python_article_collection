import time

from PIL import Image
from itertools import product
import fitz
import os


def remove_img():
    image_file = input("请输入图片地址：")

    img = Image.open(image_file)
    width, height = img.size

    for pos in product(range(width), range(height)):
        rgb = img.getpixel(pos)[:3]
        print(rgb)

    rgb = img.getpixel(pos)[:3]
    if (sum(rgb) >= 620):
        img.putpixel(pos, (255, 255, 255))

    img.save('d:/qsy.png')


def remove_pdf():
    page_num = 0
    # pdf_file = input("请输入 pdf 地址：")
    pdf_file = 'E:\Work\\bb.pdf'
    pdf = fitz.open(pdf_file);
    zoom = 4
    mat = fitz.Matrix(zoom, zoom)
    for page in pdf:
        page_start = time.perf_counter()
        pixmap = page.get_pixmap(matrix=mat)
        for pos in product(range(pixmap.width), range(pixmap.height)):
            rgb = pixmap.pixel(pos[0], pos[1])
            if (sum(rgb) >= 620):
                pixmap.set_pixel(pos[0], pos[1], (255, 255, 255))
        pixmap.pil_save(f"E:/Work/pdf_imgs/{page_num}.png", dpi=(30000, 30000))
        page_end = time.perf_counter()
        print(f"第{page_num + 1}页水印去除完成，耗时 {page_end - page_start:0.4f} 秒。")
        page_num = page_num + 1


def pic2pdf():
    # pic_dir = input("请输入图片文件夹路径：")
    pic_dir = 'E:\Work\pdf_imgs'

    pdf = fitz.open()
    img_files = sorted(os.listdir(pic_dir), key=lambda x: int(str(x).split('.')[0]))
    for img in img_files:
        print(img)
        imgdoc = fitz.open(pic_dir + '/' + img)
        pdfbytes = imgdoc.convert_to_pdf()
        imgpdf = fitz.open("pdf", pdfbytes)
        pdf.insert_pdf(imgpdf)
    pdf.save("E:/demo.pdf")
    pdf.close()


def main():
    pdf_start = time.perf_counter()
    remove_pdf()
    pdf_end = time.perf_counter()
    print(f"水印去除完成，耗时 {pdf_end - pdf_start:0.4f} 秒。")

    to_pdf_start = time.perf_counter()
    pic2pdf()
    to_pdf_end = time.perf_counter()
    print(f"PDF合成完成，耗时 {to_pdf_end - to_pdf_start:0.4f} 秒。")


if __name__ == '__main__':
    main()
