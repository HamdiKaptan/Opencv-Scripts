import os

a = 1

for i in os.listdir():

    dosya, uzantı = os.path.splitext('{}'.format(i))

    

        dosya = 'More_' + str(a) + ''
        a += 1
        os.rename(i,dosya+uzantı)
   