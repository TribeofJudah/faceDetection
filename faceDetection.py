#%%
import cv2 
import matplotlib.pyplot as plt 
import cvlib as cv 


img_path = 'couple-image.jpg'
image = cv2.imread(img_path)

plt.imshow(image)
plt.show()

faces, confidences = cv.detect_face(image)

#Loop through detected faces and add bounding box 

for face in faces:
    (startX, startY) = face[0],face[1]
    (endX,endY) = face[2],face[3]

    #draw rectangle over face
    cv2.rectangle(image, (startX,startY), (endX, endY), (0,255,0), 2)



#display output 
plt.imshow(image)
plt.show()
#%%
