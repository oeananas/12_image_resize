from PIL import Image
import argparse


def load_image(path_to_original):
    original_img = Image.open(path_to_original)
    return original_img


def get_new_size(original_img, width=None, height=None, scale=None):
    orig_width, orig_height = original_img.size
    if width and height and not scale:
        new_size = (width, height)
        return new_size
    elif (width or height) and not scale:
        if width:
            ratio = float(width / orig_width)
            new_size = (width, int(orig_height * ratio))
            return new_size
        elif height:
            ratio = float(height / orig_height)
            new_size = (int(orig_width * ratio), height)
            return new_size
    elif scale and not (width and height):
        new_size = (scale * orig_width, scale * orig_height)
        return new_size


def resize_image(original_img, new_size):
    return original_img.resize(new_size, Image.ANTIALIAS)


def rename_and_save_image(new_size, path_to_original, path_to_result=None):
    orig_image_name = path_to_original.split('/')[-1]
    orig_dir_path = '/'.join(path_to_original.split('/')[:-1])
    resized_image_name = '{name}__{width}x{height}.{exp}'.format(
        name=orig_image_name.split('.')[0],
        exp=orig_image_name.split('.')[1],
        width=new_size[0],
        height=new_size[1],
    )
    if path_to_result:
        return resized_image.save('{}/{}'.format(
            path_to_result,
            resized_image_name
        ))
    else:
        return resized_image.save('{}/{}'.format(
            orig_dir_path,
            resized_image_name
        ))


def get_parsed_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('img', type=str, help='path to original image')
    parser.add_argument('-W', type=int, help='resize width')
    parser.add_argument('-H', type=int, help='resize height')
    parser.add_argument('-S', type=int, help='resize scale')
    parser.add_argument('--resp', type=str, help='path to resized image')
    return vars(parser.parse_args())


if __name__ == '__main__':
    args = get_parsed_arguments()
    original_path = args['img']
    width = args['W']
    height = args['H']
    scale = args['S']
    result_path = args['resp']
    if not original_path:
        exit('You did not enter file path as parameter')
    try:
        image = load_image(original_path)
    except(FileNotFoundError, PermissionError):
        exit('File not found, incorrect path')
    new_size = get_new_size(image, width=width, height=height, scale=scale)
    if not new_size:
        exit('no parameters for resizing')
    try:
        resized_image = resize_image(image, new_size)
        rename_and_save_image(
            new_size,
            original_path,
            path_to_result=result_path
        )
    except FileNotFoundError:
        exit('incorrect directory path to save image')
