from sys import exit
from urllib.request import urlretrieve

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

                all_keys = list(attachment['photo'].keys())
                all_photo_size = []
                for key in all_keys:
                    if 'photo_' in key:
                        all_photo_size.append(key)
                max_photo_size = all_photo_size[-1]

                photos.append(attachment['photo'][max_photo_size])

    except:
        print('лолшибка!')
        exit(20)

    return text, photos


def img_saver(urls):
    for url in urls:
        name = url.replace('/', '')
        urlretrieve(url, name)
    pass


if __name__ == '__main__':
    all_tokens = {
        'Me': 'a',
    }

    all_api = create_sessions(tokens=all_tokens)

    post = input('\nВведите id записи.\nПример для https://vk.com/wall-110373564_275376:\n-110373564_275376\n')

    post_text, links_photos = to_wall(api_by_user=all_api['Me'], post_id=post)
    print(post_text if len(post_text) != 0 else 'No description.')
    img_saver(urls=links_photos)
