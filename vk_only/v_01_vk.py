from vk import API, Session


def create_sessions(tokens):
    for token in tokens:
        session = Session(access_token=tokens[token])
        vk_api = API(session)
        tokens[token] = vk_api
    print('All sessions created successfully.')
    return tokens


def saver(function, arguments):
    pass


if __name__ == '__main__':
    all_tokens = {
        # 'name': 'token',
        'Sasha': '21644494167a3ea0aa237fdbfb688f4bac1c28770e7ca095140f65f7b9aef8a93a5346a6db1247562bb38'
    }
    all_api = create_sessions(tokens=all_tokens)
    print(all_api)
    pass
