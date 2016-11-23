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
    height = len(data)
    width = len(data[0])

    # First get points from image
    pts = {x-1j*y for y in range(height) for x in range(width) if max(data[y][x]) < 120}

    # Next centre points.
    pts = {(c.real-width*0.5)+(c.imag+height*0.5)*1j for c in pts}

    # Now rotate by pi/4.
    pts = [c * (e ** complex(0, (pi/4))) for c in pts]

    # Plot.
    plot2(pts, range=280)

else:
    print 'Image path not found. Aborting.'

