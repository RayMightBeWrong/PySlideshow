import cv2

def videoMaker(slideshow):
    width = 0       # TODO
    height = 0      # TODO
    outputFile = "" # TODO
    fps = 1         # TODO

    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
    out = cv2.VideoWriter(outputFile, fourcc, fps, (width, height))

    slides = {} # TODO

    for slide in slides:
        slidePath = slide["path"]
        slideDuration = slide["duration"]
        for j in range(fps*slideDuration):
            frame = cv2.imread(slidePath)
            out.write(frame) # Write out frame to video      
    out.release()

