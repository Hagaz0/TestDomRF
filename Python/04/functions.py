import datetime
import pandas as pd
import openpyxl
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email import encoders

def create_report(file):
    df = pd.read_excel(file)

    # Создаем новый xlsx файл
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Datas"
    symbol = 65
    date = 0
    count = 2
    yesterday = datetime.datetime.today().date() - datetime.timedelta(days=1)

    # В новом файле прописываем имена столбцов из исходного файла
    for i in df.columns:
        sheet[f"{chr(symbol)}1"] = i
        symbol += 1
        if i == 'upd_date':
            date = symbol - 66

    # Заполняем новый файл. Если запись была добавлена вчера, добавляем ее в отчет
    for i in df.values:
        if i[date].date() == yesterday:
            symbol = 65
            for k in range(len(df.columns)):
                if k == date:
                    sheet[f"{chr(symbol)}{count}"] = i[k].date()
                else:
                    sheet[f"{chr(symbol)}{count}"] = i[k]
                symbol += 1
            count += 1

    # Сохраняем файл
    workbook.save("Datas.xlsx")

def send_file(file_to_attach, user, passwd, mail_to):
    # Данные почтового сервиса
    server = "smtp.mail.ru"
    port = 587

    # Текст письма
    text = "Отчет с записями вчерашнего дня"

    msg = MIMEMultipart()
    msg["From"] = user
    msg["Subject"] = "Тестовое письмо"
    if text:
        # Текст письма отправляем как вложение
        msg.attach(MIMEText(text))
    msg["To"] = mail_to

    attachment = MIMEBase('application', "octet-stream")
    header = 'Content-Disposition', f'attachment; filename="{file_to_attach}"'

    # Добавляем файл в письмо
    with open(file_to_attach, "rb") as f:
        data = f.read()
    attachment.set_payload(data)
    encoders.encode_base64(attachment)
    attachment.add_header(*header)
    msg.attach(attachment)

    try:
        # Подключаемся к почтовому сервису
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()

        # Логинимся на почтовом сервере
        smtp.login(user, passwd)

        # Пробуем послать письмо
        smtp.sendmail(user, msg["To"], msg.as_string())
    except smtplib.SMTPException as err:
        print('Что - то пошло не так...')
        raise err
    finally:
        smtp.quit()