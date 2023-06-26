import functions as f

# данные для авторизации
user = 'login'
passwd = 'password'
mail_to = 'mail_to'

f.create_report('file.xlsx')  # обрабатываем файл, отбирая только свежие (вчерашние) данные и создаем новый файл Datas.xlsx
f.send_file('Datas.xlsx', user, passwd, mail_to)  # отправляем файл с почты user на почту mail_to
