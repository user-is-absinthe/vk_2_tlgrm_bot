# import vk
#
#
# token = '1cc8e1444fd1bb6858af1a52c88b34543ab64533e357f146a351dace10154a15e7df18557c041a366c149'
#
#
# session = vk.Session(access_token=token)
# vk_api = vk.API(session)

from requests import get

# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

# site = 'ya.ru'
site = 'vk.com'

full_url = 'https://vk.com/wall-164153727_8263'

# r = get('https://ya.ru')#, auth=('user', 'pass'))

r = get('https://api.github.com/events')

print(r.status_code)
print(r)
