from PIL import Image
import argparse
import os


def load_image(path_to_original):
    original_img = Image.open(path_to_original)
    return original_img


def get_new_size_in_scale(original_width, original_height, scale):
    new_size = (int(original_width * scale), int(original_height * scale))
    return new_size


def get_new_size_in_width(original_width, original_height, new_width):
    ratio = new_width / original_width
    new_size = (new_width, int(original_height * ratio))
    return new_size


def get_new_size_in_height(original_width, original_height, new_height):
    ratio = new_height / original_height
    new_size = (int(original_width * ratio), new_height)
    return new_size


def get_new_size_in_correct_parameters(
        original_width,
        original_height,
        new_width=None,
        new_height=None,
        scale=None
):
    if new_width and new_height:
        new_size = new_width, new_height
    elif new_width:
        new_size = get_new_size_in_width(
            original_width,
            original_height,
            new_width
        )
    elif new_height:
        new_size = get_new_size_in_height(
            original_width,
            original_height,
            new_height
        )
    elif scale:
        new_size = get_new_size_in_scale(
            original_width,
            original_height,
            scale
        )
    return new_size


def resize_image(original_img, new_size):
    return original_img.resize(new_size, Image.LANCZOS)


def get_new_image_name(new_size, original_image_name):
    new_width, new_height = new_size
    root, ext = os.path.splitext(original_image_name)
    resized_image_name = '{name}__{width}x{height}.{ext}'.format(
        name=root,
        ext=ext,
        width=new_width,
        height=new_height,
    )
    return resized_image_name


def save_image(
        resized_image,
        new_image_name,
        path_to_original,
        dir_to_result=None
):
    if dir_to_result:
        path_to_save = os.path.join(dir_to_result, new_image_name)
    else:
        path_to_save = os.path.join(path_to_original, new_image_name)
    return resized_image.save(path_to_save)


def get_parsed_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('img', type=str, help='path to original image')
    parser.add_argument('-H', type=int, help='resize height')
    parser.add_argument('-W', type=int, help='resize width')
    parser.add_argument('-S', type=float, help='resize scale')
    parser.add_argument(
        '--path_to_save',
        type=str,
        help='directory path to resized image')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_parsed_arguments()
    original_path = args.img
    width = args.W
    height = args.H
    scale = args.S
    result_path = args.path_to_save
    if scale and (width or height):
        exit('incorrect parameters to resize image')
    if result_path and not os.path.isdir(result_path):
        exit('incorrect directory to save')
    try:
        image = load_image(original_path)
    except IOError:
        exit('image cannot be found / image cannot be opened and identified')
    original_width, original_height = image.size
    new_size = get_new_size_in_correct_parameters(
        original_width,
        original_height,
        new_width=width,
        new_height=height,
        scale=scale
    )
    resized_image = resize_image(image, new_size)
    original_image_name = os.path.basename(original_path)
    original_directory = os.path.dirname(original_path)
    new_image_name = get_new_image_name(new_size, original_image_name)
    saved_image = save_image(
        resized_image,
        new_image_name,
        original_path,
        dir_to_result=result_path
    )
