import requests

username = 'you_login'
password = 'you_pass'

url = 'https://moscow.hh.ru/account/login'

#  Создаем юзер-агента - имитацию пользователя, ибо сайт не пропускает бота и возвращает ошибку
user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

session = requests.Session()
r = session.get(url, headers = {
    'User-Agent': user_agent_val
})

session.headers.update({'Referer':url})
session.headers.update({'User-Agent':user_agent_val})
_xsrf = session.cookies.get('_xsrf', domain=".hh.ru")

# Осуществляем вход с помощью метода POST с указанием необходимых данных
post_request = session.post(url, {
     'backUrl': 'https://moscow.hh.ru/',
     'username': username,
     'password': password,
     '_xsrf':_xsrf,
     'remember':'yes',
})

if post_request == 200:
    print("Авторизация прошла успешно!")
else:
    print(f'Авторизация провалена. Код ошибки: {post_request.status_code}')