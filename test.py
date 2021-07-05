import currency, requests, json

cur = currency.Currency()

cur.first_currency = 'BRL'
cur.second_currency = 'USD'
print(cur.get_url())

request = requests.get(cur.get_url())
resposta_json = request.json()
print(resposta_json[cur.first_currency + cur.second_currency]["high"])
