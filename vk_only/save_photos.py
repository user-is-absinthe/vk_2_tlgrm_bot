import sys
import re
import os

import vk

PATH_TO_TOKENS = 'C:/Users/Worker/Pycharm/Pycharm_project/me.txt'

PATH_TO_PHOTOS_WIN = 'C:/Users/Worker/Pycharm/Pycharm_project/vk_2_tlgrm_bot/photos'
PATH_TO_PHOTOS_OSX = ''
PATH_TO_PHOTOS_LIN = ''


if sys.platform == 'win32':
    PATH_TO_PHOTOS = PATH_TO_PHOTOS_WIN
else:
    print('Check system.')
    sys.exit(1)


def main():
    test_url = 'https://vk.com/wall-110373564_275376'
    """
    https://vk.com/wall-88616456_69199
    https://vk.com/wall-144853097_31924
    https://vk.com/wall-144853097_31876
    https://vk.com/wall-144853097_31863
    
    https://vk.com/wall-164153727_61513
    """
    check_path()
    tokens_list = load_tokens()
    api_list = create_sesion(tokens=tokens_list)
    group_id, post_id = get_posts_ids(test_url)
    # TODO: save photo & description

    pass


def check_path():
    global PATH_TO_PHOTOS
    if os.path.isdir(PATH_TO_PHOTOS):
        os.makedirs(PATH_TO_PHOTOS)


def get_posts_ids(url):
    ids = url[re.search('wall-', url).end():].replace('/', '')
    ids = ids.split('_')
    return ids[0], ids[1]  # return group id, post id


def create_sesion(tokens):
    api_list = list()
    for index, token in enumerate(tokens):
        session = vk.Session(access_token=token)
        vk_api = vk.API(session)
        api_list.append(vk_api)
    return api_list


def load_tokens(path=PATH_TO_TOKENS):
    with open(path, 'r') as file:
        lines = file.readlines()
    lines = set([i.strip() for i in lines])
    return list(lines)


if __name__ == '__main__':
    main()
