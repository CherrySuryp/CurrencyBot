import requests

"""GETTING INFORMATION FROM API"""


def EUR():
    url = 'https://api.exchangeratesapi.io/latest?base=EUR'
    values = dict(eval(requests.get(url).text))["rates"]
    return str("Курс EUR равен " + str(round(values["RUB"], 2)) + " рубля")


def USD():
    url = 'https://api.exchangeratesapi.io/latest?base=USD'
    values = dict(eval(requests.get(url).text))["rates"]
    return str("Курс USD равен " + str(round(values["RUB"], 2)) + " рубля")

def own(text, cot):
    url = 'https://api.exchangeratesapi.io/latest?base=' + cot
    values = dict(eval(requests.get(url).text))["rates"]
    return str("1 " + text + " стоит " + str(round(values["RUB"], 2)) + " рубля")




