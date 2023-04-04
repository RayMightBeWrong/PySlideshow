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
    args = parser.parse_args()

    # Read input file
    f = open(args.filename)
    text = f.read()

    # parse the input file
    parsedData=parsePSS(text)

    # download images needed
    treatImgQueries(parsedData)
    
    print(parsedData)
    # create slides
    generateSlides(parsedData)

    # compose video
    videoMaker(parsedData,"output.avi")


    


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()