from PIL import Image,ImageDraw,ImageFont
import re
import os

def translatePos(pos,mWidth,mHeight):
    posL = re.findall("([tmb][lcr])",pos)
    base = (0,0,0)
    for i in range(len(posL)):
        if i==0:
            match posL[i]:
                case "tl":
                    base=(0,0,mWidth/3,mHeight/3)
                case "tc":
                    base=(mWidth/3,0,2*mWidth/3,mHeight/3)
                case "tr":
                    base=(2*mWidth/3,0,mWidth,mHeight/3)
                case "ml":
                    base=(0,mHeight/3,mWidth/3,2*mHeight/3)
                case "mc":
                    base=(mWidth/3,mHeight/3,2*mWidth/3,2*mHeight/3)
                case "mr":
                    base=(2*mWidth/3,mHeight/3,mWidth,2*mHeight/3)
                case "bl":
                    base=(0,2*mHeight/3,mWidth/3,mHeight)
                case "bc":
                    base=(mWidth/3,2*mHeight/3,2*mWidth/3,mHeight)
                case "br":
                    base=(2*mWidth/3,2*mHeight/3,mWidth,mHeight)
        else:
            match posL[i]:
                case "tl":
                    base=(min(0,base[0]),min(0,base[1]),max(mWidth/3,base[2]),max(mHeight/3,base[3]))
                case "tc":
                    base=(min(mWidth/3,base[0]),min(0,base[1]),max(2*mWidth/3,base[2]),max(mHeight/3,base[3]))
                case "tr":
                    base=(min(2*mWidth/3,base[0]),min(0,base[1]),max(mWidth,base[2]),max(mHeight/3,base[3]))
                
                case "ml":
                    base=(min(0,base[0]),min(mHeight/3,base[1]),max(mWidth/3,base[2]),max(2*mHeight/3,base[3]))

                case "mc":
                    base=(min(mWidth/3,base[0]),min(mHeight/3,base[1]),max(2*mWidth/3,base[2]),max(2*mHeight/3,base[3]))
                
                case "mr":
                    base=(min(2*mWidth/3,base[0]),min(mHeight/3,base[1]),max(mWidth,base[2]),max(2*mHeight/3,base[3]))
                    
                case "bl":
                    base=(min(0,base[0]),min(2*mHeight/3,base[1]),max(mWidth/3,base[2]),max(mHeight,base[3]))
                    
                case "bc":
                    base=(min(mWidth/3,base[0]),min(2*mHeight/3,base[1]),max(2*mWidth/3,base[2]),max(mHeight,base[3]))
                
                case "br":
                    base=(min(2*mWidth/3,base[0]),min(2*mHeight/3,base[1]),max(mWidth,base[2]),max(mHeight,base[3]))

    return base



def generateSlides(slideshow):
    width = slideshow["config"]["width"]
    height =  slideshow["config"]["height"]
    counter=0
    for slide in slideshow["slides"]:
        counter+=1
        newSlide =  Image.new('RGB', (width,height), "white")
        for elements in slide:
            elType= elements[0]
            elConfig = elements[1]
            if elType == "text":
                draw = ImageDraw.Draw(newSlide)
                #TODO FIX fonts
                font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/"+"LiberationMono-Bold"+".ttf", elConfig["size"])
                left, top, right, bottom = font.getbbox(elConfig["text"])
                container = translatePos(elConfig["cont"],width,height)
                tWidth = right-left
                tHeight = bottom-top
                
                if elConfig["center"]:
                    posx = container[0] + (container[2]-container[0])/2 - tWidth/2
                    posy = container[1] + (container[3]-container[1])/2 - tHeight/2
                else:
                    posx = container[0]
                    posy = container[1]

                draw.text((posx,posy), elConfig["text"],"black", font)

            elif elType == "img":
                img = Image.open(elConfig["src"])
                iwidth, iheight = img.size
                flag1 = True
                flag2 = True

                container = translatePos(elConfig["cont"],width,height)
                while(flag1 or flag2):
                    
                    if min(container[2] - container[0],iwidth) != iwidth:
                        iwidth= iwidth*0.99
                        iheight= iheight*0.99
                    else:
                        flag1=False
                    
                    if min(container[3] - container[1],iheight) != iheight:
                        iwidth= iwidth*0.99
                        iheight= iheight*0.99
                    else:
                        flag2=False

                

                img = img.resize((int(iwidth),int(iheight)))
                

                if elConfig["center"]:
                    posx = container[0] + (container[2]-container[0])/2 - iwidth/2
                    posy = container[1] + (container[3]-container[1])/2 - iheight/2
                else:
                    posx = container[0]
                    posy = container[1]

                newSlide.paste(img, (int(posx),int(posy)))
                os.remove(elConfig["src"])
    
        newSlide.save("./slides/slide"+str(counter)+".png")





