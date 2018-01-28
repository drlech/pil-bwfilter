from PIL import Image
import sys
from pathlib import Path

def get_luminance(rgb):
    """
    Get the normalized (0-1) luminance based on RBG values of the color.

    Args:
        rgb (tuple): RGB colors to find luminance for.

    Returns:
        int: Pixel luminence.
    """

    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    luminance = 0.299 * r + 0.587 * g + 0.114 * b

    # Normalize to 0-1
    return luminance / 255;

def filter_file(filename):
    """
    Process the image file.

    Args:
        filename (string): Name of the file to process.
    """

    image = Image.open(filename)

    image_size = image.size
    image_width = image_size[0]
    image_height = image_size[1]

    # Output file
    output = Image.new('RGB', (image_width, image_height), (255, 255, 255))
    output_pixels = output.load()

    # Convert to RGB just in case file is in different format?
    rgb_image = image.convert('RGB')

    # Convert each pixel to either black or white color.
    # That is based on pixel luminance (normalized to 0-1). We sum the luminance of the pixels
    # as we go, as long as it's below 1 we print a white pixel, when it goes over one
    # we print a black pixel.
    brightness = 0
    for h in range(image_height):
        for w in range(image_width):
            color = (0, 0, 0)
            brightness += get_luminance(rgb_image.getpixel((w, h)))
            if brightness >= 1:
                color = (255, 255, 255)
                brightness -= 1

            output_pixels[w, h] = color

    # Save output file
    output.save('output.png', 'PNG')

def open_and_filter(filename):
    """
    Check if file exists, and if it does - run the filter.

    Args:
        filename (string): Name of the file to process.
    """

    file = Path(filename)
    if (file.is_file()):
        filter_file(filename)
    else:
        print('Given file does not exist.')

def main():
    """
    Input file should be passed as a first argument.
    """

    if len(sys.argv) > 1:
        open_and_filter(sys.argv[1])
    else:
        print('Provide file name as argument!')

if __name__ == '__main__':
    main()
