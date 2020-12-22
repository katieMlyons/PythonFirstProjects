from glob import glob
import cv2

for jpg in glob('sample_images/*'):
    img = cv2.imread(jpg, 0)
    resized_img = cv2.resize(img,(100,100))
    cv2.imwrite(f'{jpg}_resized.jpg', resized_img)
