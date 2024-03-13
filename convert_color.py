import os
import cv2
import os


base = "./download/"
src = os.path.join(base, "imgs")
out = os.path.join(base, "gray_img")

if not os.path.exists(out):
    os.mkdir(out)

for img in os.listdir(src):
    image = cv2.imread(os.path.join(src, img))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # # backtorgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB) * 255
    name, exten = os.path.splitext(img)
    filepath = os.path.join(out, f"{name}_gray{exten}")
    if cv2.imwrite(filepath, gray):
        print(filepath)

print("......Success")

# cv2.imshow('image', image)
# cv2.imshow('gray', gray)
# cv2.waitKey()