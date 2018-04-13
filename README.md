# Image Resizer

A script for working with images.
The input is a required argument (img) - the full path to the image file, the size of which must be changed.
then at startup the optional parameters are transmitted:
the desired image width (-W), the desired height (-H), or the scaling factor (-S).
At start it is necessary to specify either only the scaling factor or the width / height (you can specify only the width or only the height, then the picture will change in size in proportion to the specified parameter)
the last parameter (--resp) is the path to the directory where the modified picture will be saved. If this parameter is not specified, the picture will be saved to the current directory.
When the script is running, the original files are not changed and are not deleted. A new file with a formatted name and a new size is created (name__'width'x'height'.exp).

# Quickstart
Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```
```bash
oeananas@oeananas-PC:~/12_image_resize$ ls
image_resize.py  me.jpg  README.md  requirements.txt
python3 image_resize.py /home/oeananas/12_image_resize/me.jpg -W=800 --resp=/home/oeananas/
python3 image_resize.py /home/oeananas/12_image_resize/me.jpg -S=2 --resp=/home/oeananas/
python3 image_resize.py /home/oeananas/12_image_resize/me.jpg -S=2
oeananas@oeananas-PC:~/12_image_resize$ ls
image_resize.py  me__1384x2036.jpg  me.jpg  README.md  requirements.txt
oeananas@oeananas-PC:~$ ls
11_duplicates        8_vk_friends_online  SecLists     Музыка
12_image_resize      Downloads            snap         Общедоступные
3_bars               examples.desktop     Видео        Рабочий стол
4_json               me__1384x2036.jpg    Документы    Шаблоны
5_lang_frequency     me__800x1176.jpg     Загрузки
6_password_strength  PycharmProject       Изображения

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
