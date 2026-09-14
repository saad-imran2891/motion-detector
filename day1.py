'''import cv2

img = cv2.imread('test.jpg')
if img is None:
    print('Failed to load the image.')
else:
    print("shape:",img.shape)
    cv2.imshow('Frame',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
    
import cv2

img = cv2.imread('test.jpg')
if img is None:
    print('Failed to load the image.')
else:  
    h,w = img.shape[:2]
    resized = cv2.resize(img,(w//2, h//2))
    cv2.imwrite('resized_test.jpg', resized)
    cv2.destroyAllWindows()
    print(f"Original: {w}x{h} -> Resized: {w//2}x{h//2}, saved as 'resized_test.jpg'")


