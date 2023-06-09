import argparse
from parser.pssParser import parsePSS
from imageDownloader import treatImgQueries
from slideGen import generateSlides
from videoMaker import videoMaker


def main():
    parser = argparse.ArgumentParser(
                prog='PySlideShow',
                description='Python tool capable of creating a slideshow based on .pss file')

    parser.add_argument("filename",help="Name .pss file, that describes the slideshow to be created")    # positional argument
    parser.add_argument("-o","--outputFile",help="Name of the output file, without extension",default="output")
    args = parser.parse_args()

    # Read input file
    f = open(args.filename)
    text = f.read()

    # parse the input file
    parsedData=parsePSS(text)

    # download images needed
    treatImgQueries(parsedData)
    
    # create slides
    generateSlides(parsedData)

    # compose video
    videoMaker(parsedData,args.outputFile)


    


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()