from PIL import Image,ImageDraw,ImageFont
import re
import matplotlib.font_manager as fontM

import textwrap


def translateCont(Cont, mWidth,mHeight):
    ContL = re.findall("([tmb][lcr])",Cont)
    base = (mWidth,mHeight,0,0)
    for i in range(len(ContL)):
         match ContL[i]:
                case "tl":
                    base=(
                        min(mWidth/20,base[0]),
                        min(mHeight/20,base[1]),
                        max(7*mWidth/20,base[2]),
                        max(7*mHeight/20,base[3])
                        )
                case "tc":
                    base=(
                        min(7*mWidth/20,base[0]),
                        min(mHeight/20,base[1]),
                        max(13*mWidth/20,base[2]),
                        max(7*mHeight/20,base[3])
                    )
                case "tr":
                    base=(
                        min(13*mWidth/20,base[0]),
                        min(mHeight/20,base[1]),
                        max(19*mWidth/20,base[2]),
                        max(7*mHeight/20,base[3]))
                
                case "ml":
                    base=(
                        min(mWidth/20,base[0]),
                        min(7*mHeight/20,base[1]),
                        max(7*mWidth/20,base[2]),
                        max(13*mHeight/20,base[3]))

                case "mc":
                    base=(
                        min(7*mWidth/20,base[0]),
                        min(7*mHeight/20,base[1]),
                        max(13*mWidth/20,base[2]),
                        max(13*mHeight/20,base[3]))
                
                case "mr":
                    base=(
                        min(13*mWidth/20,base[0]),
                        min(7*mHeight/20,base[1]),
                        max(19*mWidth/20,base[2]),
                        max(13*mHeight/20,base[3]))
                    
                case "bl":
                    base=(
                        min(mWidth/20,base[0]),
                        min(13*mHeight/20,base[1]),
                        max(7*mWidth/20,base[2]),
                        max(19*mHeight/20,base[3]))
                    
                case "bc":
                    base=(
                        min(7*mWidth/20,base[0]),
                        min(13*mHeight/20,base[1]),
                        max(13*mWidth/20,base[2]),
                        max(19*mHeight/20,base[3]))
                
                case "br":
                    base=(
                        min(13*mWidth/20,base[0]),
                        min(13*mHeight/20,base[1]),
                        max(19*mWidth/20,base[2]),
                        max(19*mHeight/20,base[3]))

    return base

def findFont(font,size):
    fonts = fontM.FontProperties(family=font)
    return ImageFont.truetype(fontM.findfont(fonts), size)

def resizeIMG(container,img):
    iwidth, iheight = img.size
    flag1 = True
    flag2 = True

    while(flag1 or flag2):
        if min(container[2] - container[0],iwidth) != iwidth:
            iwidth= iwidth*0.98
            iheight= iheight*0.98
        else:
            flag1=False
                    
        if min(container[3] - container[1],iheight) != iheight:
            iwidth= iwidth*0.98
            iheight= iheight*0.98
        else:
            flag2=False

    return  img.resize((int(iwidth),int(iheight)))


def centerELEM(container,width,height):
        posx = container[0] + (container[2]-container[0])/2 - width/2
        posy = container[1] + (container[3]-container[1])/2 - height/2
        return posx,posy
                  

def generateSlides(slideshow):
    window_width = slideshow["config"]["width"]
    window_height= slideshow["config"]["height"]
    counter =1

    for slide in slideshow["slides"]:
        
        new_slide = Image.new("RGB",(window_width,window_height),"white")

        for element in slide:
            type = element[0]
            elemConf = element[1]
            match type:
                case "text":
                    draw = ImageDraw.Draw(new_slide)
                    container = translateCont(elemConf["cont"],window_width,window_height)
                    font = findFont(elemConf["font"],elemConf["size"])
                    elemConf["text"]=textwrap.fill(elemConf["text"],int(((container[2]-container[0]) * 2) /elemConf["size"]))
                    left, top, right, bottom = font.getbbox(elemConf["text"])
                    tWidth = right-left
                    tHeight = bottom-top            

                    if elemConf["center"]:
                        posx,posy=centerELEM(container,tWidth,tHeight)
                    else:
                        posx=container[0]
                        posy=container[1]

                    draw.text((posx,posy), elemConf["text"],elemConf["color"], font)

                case "img":
                    img = Image.open(elemConf["src"])
                    
                    container = translateCont(elemConf["cont"],window_width,window_height)
                    if container == (window_width/20,window_height/20,19*window_width/20,19*window_height/20):
                        container=(0,0,window_width,window_height)
                    img = resizeIMG(container,img)
                    if elemConf["center"]:
                        iwidth, iheight = img.size
                        posx,posy=centerELEM(container,iwidth,iheight)
                    else:
                        posx=container[0]
                        posy=container[1]

                    new_slide.paste(img, (int(posx),int(posy)))

        new_slide.save("./slides/slide"+str(counter)+".png")
        counter+=1





