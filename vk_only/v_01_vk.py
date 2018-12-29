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
        'Pol': '62940b03fdd79762509c294e614405b9c176115f404541ce1dac6323eab9b6edb0587ff73204dac4a79fc',
        'Kris': '99dd7c6ca91e49521c8ae6272023c0184b21306f34b54eae889505154b06417aa412ee8ec4f763d802b8d',
        'Me': '1cc8e1444fd1bb6858af1a52c88b34543ab64533e357f146a351dace10154a15e7df18557c041a366c149',
        'Sasha': '21644494167a3ea0aa237fdbfb688f4bac1c28770e7ca095140f65f7b9aef8a93a5346a6db1247562bb38'
    }
    all_api = create_sessions(tokens=all_tokens)
    print(all_api)
    pass
