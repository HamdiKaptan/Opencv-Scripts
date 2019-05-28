from PIL import Image
import os
def mirror_image(image_path, saved_location):

    image_obj = Image.open(image_path)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(saved_location)
a=26
if __name__ == '__main__':
    for i in (os.listdir("path/")):
        dosya, uzantı = os.path.splitext('{}'.format(i))
        image = 'path/{}'.format(dosya+uzantı)
        mirror_image(image, 'path/{}'.format(dosya+str(a)+uzantı))
        a+=1
