import requests

base = 'USD'

to = 'VND'

url = f'https://api.exchangerate.host/lastest?base={base}&symbols={to}'

response = requests.get(url)

data = response.json()

rate = data.get('rates').get(to)

print('Tỉ giá chuyển đổi $ -> VND:', rate)
dollar = input('Số tiền bạn đang có ($): ')

try:
    dollar = float(dollar)
    if dollar < 0:
        raise Exception()
    vnd = dollar * rate
    print('Số tiền của bạn (VND): ', vnd)
    print('=>', end=' ')
    if vnd >= 10**9:
        print('Bạn là tỉ phú VND')
    elif vnd >= 10**6:
        print('Bạn là triệu phú VND')
    else:
        print('Bạn rất nghèo')
except Exception:
    print('Input chỉ có thể là số và không âm')


