from PIL import Image
import sys
from pathlib import Path

def get_luminance(rgb):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    luminance = 0.299 * r + 0.587 * g + 0.114 * b

    # Normalize to 0-1
    return luminance / 255;

def filter_file(filename):
    image = Image.open(filename)

    image_size = image.size
    image_width = image_size[0]
    image_height = image_size[1]

    output = Image.new('RGB', (image_width, image_height), (255, 255, 255))
    output_pixels = output.load()

    # Convert to RGB just in case file is in different format?
    rgb_image = image.convert('RGB')

    brightness = 0
    for h in range(image_height):
        for w in range(image_width):
            color = (0, 0, 0)
            brightness += get_luminance(rgb_image.getpixel((w, h)))
            if brightness >= 1:
                color = (255, 255, 255)
                brightness -= 1

            output_pixels[w, h] = color

    output.save('output.png', 'PNG')

def open_and_filter(filename):
    file = Path(filename)
    if (file.is_file()):
        filter_file(filename)
    else:
        print('Given file does not exist.')

def main():
    if len(sys.argv) > 1:
        open_and_filter(sys.argv[1])
    else:
        print('Provide file name as argument!')

if __name__ == '__main__':
    main()
