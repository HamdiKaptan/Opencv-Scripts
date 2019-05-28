import cv2
from fastai.vision import *
import os

learn = load_learner(Path(''), Path('model.pkl'))
dogrulukone = 0

model_name = modelname
f= open("path:/{}.txt".format(model_name),"w+")
for i in (os.listdir("path")):
    dosya, uzantı = os.path.splitext('{}'.format(i))
    img1 = cv2.imread("path/{}".format(dosya + uzantı))
    if ("jpg" in uzantı) == True:
        pred_class, pred_idx, outputs = learn.predict(Image(pil2tensor(img1, np.float32).div_(255)))
        if dosya[0]== str(pred_class)[0]:
            dogrulukone+=1


        f.write(
            "pred_class: {}\n".format(pred_class) +
            "outputs :  {}\n".format(outputs) +
            "image name : {}\n".format(dosya+uzantı) +
            "******************\n\n")
f.write(" dogruluk : {}\n".format(dogrulukone))

f.close()
