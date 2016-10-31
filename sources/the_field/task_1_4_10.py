import image
import os
from pprint import pprint
from plotting import plot
import matplotlib.pyplot as plt

curr_dir = os.getcwd()
image_path = '%s/img01.png' % curr_dir

print 'Checking...%s' % image_path
if os.path.isfile(image_path):

    print 'Using png image...'

    data = image.file2image(image_path)
    width = len(data)
    height = len(data[0])
    #pts = {1j*y+x for x in range(width) for y in range(height) if max(data[x][y]) < 120}
    pts = [(-x, y) for x in range(width) for y in range(height) if max(data[x][y]) < 120]
    xs = [x[0] for x in pts]
    ys = [x[1] for x in pts]
    #plot(pts, 4.0, dir=curr_dir)
    plt.scatter(ys, xs)
    plt.show()


else:
    print 'Image path not found. Aborting.'

