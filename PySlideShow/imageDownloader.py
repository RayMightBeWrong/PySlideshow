from bing_image_downloader import downloader
import cv2
import os
import imutils

def downloadImg(query,presentChoice=True):
    flag = True
    while (flag):
        downloader.download(query, limit=10,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=False)
        images = []
        for f in os.listdir("./dataset/"+query):
            if f.endswith("jpg"):
                images.append(f)
            else:
                os.remove(os.path.join("./dataset/"+query, f))
        chosen=""
        for image in images:
            image_path = os.path.join("./dataset/"+query, image)
            if presentChoice:
                frame = cv2.imread(image_path)
                height, width, channels = frame.shape
                frame = imutils.resize(frame,width=min(1280,width),height=min(720,height))
                cv2.imshow('video',frame)
                print("Is this what you were looking for? [Y/n]")
                key = (cv2.waitKey() & 0xFF)
                if key == ord('y'): # Hit `q` to exit
                    flag=False
                    chosen=image
                    break
                else:
                    cv2.destroyAllWindows()
            else:
                chosen=image
                flag=False
                break

        for image in images:
            if image!= chosen:
                image_path = os.path.join("./dataset/"+query, image)
                os.remove(image_path)
        