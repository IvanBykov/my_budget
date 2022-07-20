from bs4 import BeautifulSoup

from buy.libs.decoder import decode_str
from buy.models import BuyTmp


def import_buy():
    with open('buy_tmp/new_email.eml', 'r', encoding='UTF-8') as in_file:
        file_text = in_file.read()
    soup = BeautifulSoup(file_text, 'lxml')
    data = soup.find('table', class_='3D"w95"')
    products = list()
    rows = data.find_all('tr')
    for row in rows[20:]:
        split_row = decode_str(row.text).split('\n')
        product = list()
        for col in split_row:
            if col.isspace() or col == '':
                continue
            else:
                try:
                    product.append(float(col.strip()))
                except ValueError:
                    product.append(col.strip())
            if len(product) == 4 and type(product[1]) == float and type(product[2]) == float and type(
                    product[3]) == float:
                products.append(product)
                #BuyTmp(name=product[0], amount=product[1], price_unit=product[2], price_buy=product[3]).save()
    return products
