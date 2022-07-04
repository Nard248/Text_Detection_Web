def search_for_text(word, path, name):
    import easyocr
    import cv2
    from matplotlib import pyplot as plt
    import numpy as np
    import os
    reader = easyocr.Reader(['en'])
    result = reader.readtext(path)
    print(result[0])
    for detection in result:
        text = detection[1]
        if word in text:
            top_left = tuple(detection[0][0])
            bottom_right = tuple(detection[0][2])
            font = cv2.FONT_HERSHEY_SIMPLEX
            img = cv2.imread(path)
            img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
            img = cv2.putText(img, text, top_left, font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            plt.imshow(img)
            plt.show()
            plt.savefig('C:\\Users\\User\Desktop\Projects\Vision_web\media\Image_folder\Processed_image\\' + name)
            print('C:\\Users\\User\Desktop\Projects\Vision_web\media\Image_folder\Processed_image\\' + name)
            return 'C:\\Users\\User\Desktop\Projects\Vision_web\media\Image_folder\Processed_image\\' + name
