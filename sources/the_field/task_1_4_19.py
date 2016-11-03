import image
import os
from math import pi, e
from plotting import plot2

curr_dir = os.getcwd()
image_path = '%s/img01.png' % curr_dir

print 'Checking...%s' % image_path
if os.path.isfile(image_path):

    print 'Using png image...'
    

    data = image.file2image(image_path)
    width = len(data)
    height = len(data[0])
    pts = {-1j*x+y for x in range(width) for y in range(height) if max(data[x][y]) < 120}

    a = pi / 4.0
    pts = [c * (e ** complex(0, (pi/4))) for c in pts]
    plot2(pts, range=280)

else:
    print 'Image path not found. Aborting.'

