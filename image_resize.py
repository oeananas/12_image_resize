from PIL import Image
import argparse
import os


def load_image(path_to_original):
    original_img = Image.open(path_to_original)
    return original_img


def get_original_size(original_img):
    orig_width, orig_height = original_img.size
    return orig_width, orig_height


def get_new_size_in_sides(new_width, new_height):
    return new_width, new_height


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


def validate_new_size(
        original_width,
        original_height,
        new_width=None,
        new_height=None,
        scale=None
):
    if new_width and new_height and not scale:
        valid_new_size = get_new_size_in_sides(new_width, new_height)
        return valid_new_size
    elif (new_width or new_height) and not scale:
        if new_width:
            valid_new_size = get_new_size_in_width(
                original_width,
                original_height,
                new_width
            )
            return valid_new_size
        elif new_height:
            valid_new_size = get_new_size_in_height(
                original_width,
                original_height,
                new_height
            )
            return valid_new_size
    elif scale and not new_width and not new_height:
        valid_new_size = get_new_size_in_scale(
            original_width,
            original_height,
            scale
        )
        return valid_new_size


def resize_image(original_img, new_size):
    return original_img.resize(new_size, Image.LANCZOS)


def get_original_image_name(path_to_original):
    orig_image_path, orig_image_name = os.path.split(path_to_original)
    return orig_image_name


def get_original_directory(path_to_original):
    orig_image_path, orig_image_name = os.path.split(path_to_original)
    return orig_image_path


def get_new_image_name(new_size, original_image_name):
    new_width, new_height = new_size
    root, exp = os.path.splitext(original_image_name)
    resized_image_name = '{name}__{width}x{height}.{exp}'.format(
        name=root,
        exp=exp,
        width=new_width,
        height=new_height,
    )
    return resized_image_name


def save_image(
        resized_image,
        new_image_name,
        path_to_original,
        path_to_result=None
):
    if path_to_result:
        return resized_image.save(
            os.path.join(path_to_result, new_image_name)
        )
    else:
        return resized_image.save(
            os.path.join(path_to_original, new_image_name)
        )


def get_parsed_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('img', type=str, help='path to original image')
    parser.add_argument('-W', type=int, help='resize width')
    parser.add_argument('-H', type=int, help='resize height')
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
    if result_path and not os.path.isdir(result_path):
        exit('incorrect directory to save')
    try:
        image = load_image(original_path)
    except IOError:
        exit('image cannot be found / image cannot be opened and identified')
    original_width, original_height = get_original_size(image)
    new_valid_size = validate_new_size(
            original_width,
            original_height,
            new_width=width,
            new_height=height,
            scale=scale
    )
    if not new_valid_size:
        exit('incorrect parameters to resize image')
    resized_image = resize_image(image, new_valid_size)
    original_image_name = get_original_image_name(original_path)
    original_directory = get_original_directory(original_path)
    new_image_name = get_new_image_name(new_valid_size, original_image_name)
    saved_image = save_image(
        resized_image,
        new_image_name,
        original_path,
        path_to_result=result_path
    )
