import cv2
import os


a = 1

for i in os.listdir():
    dosya, uzantı = os.path.splitext('{}'.format(i))
    if uzantı == ".jpg":
        res = "One_{}".format(a)+uzantı
        img = cv2.imread(res)
        crop = img[0:224, 87:311]

        cv2.imwrite("One_{}".format(a)+uzantı,crop)


    else :
        continue
    a+=1


cv2.destroyAllWindows()
