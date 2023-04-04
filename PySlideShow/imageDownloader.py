from bing_image_downloader import downloader
import cv2
import os
import imutils

def treatImgQueries(slideshow):
    for slide in slideshow["slides"]:
        for elem in slide:
            if elem[0]=="img":
                if "query" in elem[1]:
                    elem[1]["src"]=downloadImg(elem[1]["query"])
    return slideshow


def downloadImg(query,presentChoice=True):
    flag = True
    while (flag):
        downloader.download(query, limit=10,  output_dir='tempDS', adult_filter_off=False, force_replace=False, timeout=60, verbose=False)
        images = []
        for f in os.listdir("./tempDS/"+query):
            if f.endswith("jpg"):
                images.append(f)
            else:
                os.remove(os.path.join("./tempDS/"+query, f))
        chosen=""
        for image in images:
            image_path = os.path.join("./tempDS/"+query, image)
            if presentChoice:
                frame = cv2.imread(image_path)
                height, width, channels = frame.shape
                frame = imutils.resize(frame,width=min(1280,width),height=min(720,height))
                cv2.imshow('Is this what you were looking for? [Y/n]',frame)
                print("Is this what you were looking for? [Y/n]")
                key = (cv2.waitKey() & 0xFF)
                if key == ord('y'): # Hit `q` to exit
                    flag=False
                    chosen= os.path.join("./dataset/" + str(hash(query+image))+".jpg")
                    cv2.imwrite(chosen,frame)
                    cv2.destroyAllWindows()
                    break
                else:
                    cv2.destroyAllWindows()
            else:
                chosen=image
                flag=False
                break

        for image in images:
            image_path = os.path.join("./tempDS/"+query, image)
            os.remove(image_path)
    return chosen
