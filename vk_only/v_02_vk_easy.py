from sys import exit
from urllib.request import urlretrieve
from re import search
from traceback import format_exc

from vk import API, Session


def create_sessions(tokens):
    for token in tokens:
        session = Session(access_token=tokens[token])
        vk_api = API(session)
        tokens[token] = vk_api
    print('All sessions created successfully.')
    return tokens


def to_wall(api_by_user, post_id):
    all_post_info = api_by_user.wall.getById(posts=post_id, v=5.60)
    try:
        text = all_post_info[0]['text']
        photos = []
        for attachment in all_post_info[0]['attachments']:
            if attachment['type'] == 'photo':
                # print(attachment)

                all_keys = list(attachment['photo'].keys())
                all_photo_size = []
                for key in all_keys:
                    if 'photo_' in key:
                        all_photo_size.append(key)
                max_photo_size = all_photo_size[-1]

                photos.append(attachment['photo'][max_photo_size])

        # print('lll', photos)
    except:
        print('LoL, ошибка!\n', format_exc())
        exit(20)

    return text, photos


def img_saver(urls):
    for url in urls:
        name = 'save_pic/' + url.replace('/', '')
        urlretrieve(url, name)
    print('All images saved successfully.')


def post_url_to_post_id(url):
    position = search(r'wall-', url)
    position = position.end() - 1
    tail = url[position::]
    if tail[-1].isdigit():
        return tail
    else:
        return tail[:len(tail) - 1]


if __name__ == '__main__':
    all_tokens = {
        'Me': '1cc8e1444fd1bb6858af1a52c88b34543ab64533e357f146a351dace10154a15e7df18557c041a366c149',
    }
    post_url = 'https://vk.com/wall-110373564_275376/'

    all_api = create_sessions(tokens=all_tokens)

    post_id = post_url_to_post_id(url=post_url)
    post_text, links_photos = to_wall(api_by_user=all_api['Me'], post_id=post_id)
    print('Post description:\n' + post_text if len(post_text) != 0 else 'No post description.')
    img_saver(urls=links_photos)
