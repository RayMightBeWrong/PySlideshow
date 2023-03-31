import argparse
import pssParser
import imageDownloader

def main():
    parser = argparse.ArgumentParser(
                prog='PySlideShow',
                description='Python tool capable of creating a slideshow based on .pss file')

    parser.add_argument("filename",help="Name .pss file, that describes the slideshow to be created")    # positional argument
    args = parser.parse_args()

    # parse the input file
    
    # download images needed
    imageDownloader.downloadImg("balls")

    # create slides

    # compose video


    




if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()