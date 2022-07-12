import matplotlib.pyplot as plt
import base64
from io import BytesIO

from django.db.models import QuerySet


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, y, product):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8, 5))
    plt.title(product)
    plt.plot(x, y)
    plt.xticks(rotation=45)
    plt.xlabel('Дата')
    plt.ylabel('Цена')
    plt.tight_layout()
    graph = get_graph()
    return graph


def delta_price(list_buy):
    # возвращает изменение в % между первым и последним элементом списка
    if len(list_buy) > 0:
        first_value = list_buy[0].unit_price()
        last_value = list_buy[len(list_buy)-1].unit_price()
        delta = (last_value - first_value) / first_value * 100
        return delta
    else:
        return 0
