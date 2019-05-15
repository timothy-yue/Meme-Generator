#! /usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import sys


def generate_meme(imgPath, botString, topString):
    # get an image
    try:
        base = Image.open(imgPath)
    except Exception as e:
        print(e)
        sys.exit()

    # Find the image size
    imgSize = base.size

    # Guess best font -- imgSize[1] refers to the X dimension
    # Create font
    botFontSize = topFontSize = int(imgSize[1] / 4)
    bottomft = ImageFont.truetype('./Roboto/Roboto-Black.ttf', botFontSize)
    topft = ImageFont.truetype('./Roboto/Roboto-Black.ttf', topFontSize)

    # Get the size of the incoming text
    bottomTextSize = bottomft.getsize(botString)
    topTextSize = topft.getsize(topString)

    acceptableTextSize = imgSize[0] - 30

    while bottomTextSize[0] > acceptableTextSize:
        botFontSize = botFontSize - 2
        bottomft = ImageFont.truetype('./Roboto/Roboto-Black.ttf', botFontSize)
        bottomTextSize = bottomft.getsize(botString)

    while topTextSize[0] > acceptableTextSize:
        topFontSize = topFontSize - 2
        topft = ImageFont.truetype('./Roboto/Roboto-Black.ttf', topFontSize)
        topTextSize = topft.getsize(topString)

    bottomPosition = (imgSize[0]/2 - bottomTextSize[0]/2,
                      imgSize[1] - bottomTextSize[1] - 10)
    topPosition = (imgSize[0]/2 - topTextSize[0]/2, 0)

    # make a blank image for the text, initialized to transparent text color
    textImg = Image.new('RGBA', base.size, (255, 255, 255, 0))

    # get a drawing context
    d = ImageDraw.Draw(textImg)

    # Write text to the textImg
    d.text(bottomPosition, botString, font=bottomft,  fill=(255, 255, 255, 255))
    d.text(topPosition, topString, font=topft, fill=(255, 255, 255, 255))

    # combine base image with the text overlay
    out = Image.alpha_composite(base, textImg)

    out.save("meme.png")


if __name__ == "__main__":

    if len(sys.argv) == 3 or len(sys.argv) == 4:
        img = sys.argv[1]
        botString = sys.argv[2]
        topString = sys.argv[3] if len(sys.argv) == 4 else ""

        generate_meme(img, botString, topString)

    elif len(sys.argv) == 1:
        imgPath = input("Please enter image path: ")
        topText = input("Please enter top text: ")
        bottomText = input("Please enter bottom text: ")

        generate_meme(imgPath, bottomText, topText)

    else:
        print("Invalid number of arguments.\nUsuage: ./memegenerator.py imgPath bottomText topText")
        print("Alt Usuage: ./memegenerator.py \nAnd follow walk through")
        sys.exit()
