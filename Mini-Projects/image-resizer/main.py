import cv2

source="C:\\Users\\USER\\OneDrive\\Desktop\\uploads\\Mini-Projects\\image-resizer\\sign.jpeg"
destination="C:\\Users\\USER\\OneDrive\\Desktop\\uploads\\Mini-Projects\\image-resizer\\newsign.jpeg"
scale_percent = 30

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",src)

new_width= int(src.shape[1] * scale_percent/100)
new_height= int(src.shape[0] * scale_percent/100)

# dsize =(width, height)

output = cv2.resize(src, (new_width , new_height))
cv2.imwrite(destination,output)
cv2.waitKey(0)