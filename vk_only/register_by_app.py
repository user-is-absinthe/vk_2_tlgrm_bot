import lxml.html
import requests

login = 'твой логин'
password = 'твой пароль'
url = 'https://vk.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/61.0.3163.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'DNT': '1'
}
session = requests.session()
data = session.get(url, headers=headers)
page = lxml.html.fromstring(data.content)

form = page.forms[0]
form.fields['email'] = login
form.fields['pass'] = password

response = session.post(form.action, data=form.form_values())
print('onLoginDone' in response.text)
