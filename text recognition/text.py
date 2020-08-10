import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('sample.jpg')
print(img.shape)

height = 400
width = 600
dim = (width, height)
img = cv2.resize(img, dim)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 77, 31)
print(pytesseract.image_to_string(adaptive_threshold))
cv2.imshow('output', gray)
cv2.imshow('output2', adaptive_threshold)
cv2.waitKey(0)