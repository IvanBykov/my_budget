from bs4 import BeautifulSoup

from buy.libs.decoder import decode_str


def import_buy():
    with open('buy_tmp/new_email.eml', 'r', encoding='UTF-8') as in_file:
        file_text = in_file.read()
    soup = BeautifulSoup(file_text, 'lxml')
    data = soup.find('table', class_='3D"w95"')
    products = list()
    rows = data.find_all('tr')
    string_with_date = decode_str(rows[8].text).split('\n')
    check_date = string_with_date[1][:10]
    # for row in rows[20:]:
    for row in rows:
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
                product.append(check_date)
                products.append(product)
    return products


def parse_name(input_str: str):
    words = input_str.split()
    brand = ''
    step = 0
    for word in words:
        if word.isupper():
            brand += word + ' '
            step += 1
        else:
            break
    name = words[step]
    weight = ''
    unit = ''
    for word in words[step:]:
        if word[0].isdigit() and word[-1].isalpha():
            for w in word[::-1]:
                if w.isalpha():
                    unit = w + unit
                else:
                    break
            weight = word[:-len(unit)]
    weight = weight.replace(',', '.')
    try:
        weight = float(weight)
    except Exception:
        weight = 1
    if unit == 'мл':
        unit = 'л'
        weight /= 1000
    elif unit == 'г':
        unit = 'кг'
        weight /= 1000
    result = {
        'brand': brand.strip(),
        'name': name.strip(),
        'weight': weight,
        'unit': unit
    }
    return result
