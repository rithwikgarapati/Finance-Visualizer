import cv2
import pytesseract
import ipdb


def convert_image_to_string(url, tesseract_exec_path='/usr/local/bin/tesseract'):
    pytesseract.pytesseract.tesseract_cmd = tesseract_exec_path

    img = cv2.imread(url)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 16))

    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    im2 = img.copy()

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cropped = im2[y:y + h, x:x + w]

        text = pytesseract.image_to_string(cropped)

        file_path = 'text/' + url.split("/")[-1]
        file_path = file_path.split(".")[0] + ".txt"
        file = open(file_path, "a")
        file.write(text)
        file.write("\n")
        file.close()

    file_name = url.split("/")[-1]
    print(f"Successfully generated text for Image: {file_name}")
