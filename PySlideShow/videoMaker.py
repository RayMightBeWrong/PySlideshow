import cv2

def videoMaker(slideshow,outputfile):
    width = slideshow["config"]["width"]       
    height = slideshow["config"]["height"]       
    outputFile = outputfile 
    fps = 1         

    fourcc = cv2.VideoWriter_fourcc(*'XVID') # Be sure to use lower case
    out = cv2.VideoWriter(outputFile, fourcc, fps, (width, height))
    counter =1
    for slide in slideshow["slides"]:
        slidePath = """./slides/slide{counter}.png""".format(counter=counter)
        slideDuration=5
        for elem in slide:
            
            if elem[0]=="duration": slideDuration = elem[1]["time"]
       
        for j in range(fps*slideDuration):
            frame = cv2.imread(slidePath)
            out.write(frame) # Write out frame to video   
        counter+=1   
    out.release()

