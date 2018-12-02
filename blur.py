# Import packages
from imutils import paths
import cv2

def varianceofLap(image):
    # Variance of Laplacian as a focus metric
    return cv2.Laplacian(image,cv2.CV_64F).var()

# Loop over images in directory
for imagePaths in paths.list_images('images'):

    image = cv2.imread(imagePaths)
    imageGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


    if varianceofLap(imageGray) > 100 :
        print(imagePaths+' is blurry')

    else :
        print(imagePaths + ' is not blurry')

