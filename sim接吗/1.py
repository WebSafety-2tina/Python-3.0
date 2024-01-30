import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout

# 设置5sim API密钥
API_KEY = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzgwNzcyNjUsImlhdCI6MTcwNjU0MTI2NSwicmF5IjoiODc3ZmVhM2M2OWFlYzIyOTBkYzc1OWNlMTMxMzM4NjUiLCJzdWIiOjcyNDEzOX0.h5s_stLXVJrUkwf026-hBenwqN8GXRxiIlfrwQ7Cak-bYjXB97SupFYRmMdVhAE6wW55CibQTY-8-F3MPVfLOA1gq3QnTUIFUnpA7KqdTL813bDz3iKs3D4CD6QV2kW79LvqEOEYt5GMxFQuZE14wi3w-1Ra2lO5wgivjEfnWqGrT4ScSwUFuKXPPgoAkQ6oO-eXVp7RRbj3GtgszhkdhD9499hFRKITXufdl6cNij_n5libtqCqXIHwtq83IOGuFoeiN02v49twok5YY6Lq11ERGkXQuxQd3EMr4sJxjeJ_X_WIAKjQa5X0SYGcVmxlAcBXS0AKseBBwvztyCI_jg'

# 设置API基本URL
BASE_URL = 'https://api.5sim.net/v1/'

def get_countries():
    """获取支持的国家列表"""
    url = BASE_URL + 'countries'
    headers = {'Authorization': 'Bearer ' + API_KEY}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查响应是否成功
        countries = response.json()
        return countries
    except (HTTPError, ConnectionError, Timeout) as e:
        print(f"获取国家列表失败: {e}")
        return []

def get_products(country_code):
    """获取指定国家支持的产品列表"""
    url = BASE_URL + f'countries/{country_code}/products'
    headers = {'Authorization': 'Bearer ' + API_KEY}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查响应是否成功
        products = response.json()
        return products
    except (HTTPError, ConnectionError, Timeout) as e:
        print(f"获取产品列表失败: {e}")
        return []

def get_phone_number(country_code, product_id):
    """获取指定国家和产品的手机号"""
    url = BASE_URL + f'countries/{country_code}/products/{product_id}/numbers'
    headers = {'Authorization': 'Bearer ' + API_KEY}
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()  # 检查响应是否成功
        number = response.json()
        return number['phone']
    except (HTTPError, ConnectionError, Timeout) as e:
        print(f"获取手机号失败: {e}")
        return None

def main():
    # 获取国家列表
    countries = get_countries()
    if not countries:
        print("无法获取国家列表。程序退出。")
        return

    for country in countries:
        print(country['code'], country['name'])

    # 用户选择国家
    selected_country_code = input('请选择国家代码: ')

    # 获取选定国家支持的产品列表
    products = get_products(selected_country_code)
    if not products:
        print("无法获取产品列表。程序退出。")
        return

    for product in products:
        print(product['id'], product['name'])

    # 用户选择产品
    selected_product_id = input('请选择产品ID: ')

    # 获取手机号
    phone_number = get_phone_number(selected_country_code, selected_product_id)
    if phone_number:
        print(f'您的手机号是: {phone_number}')
    else:
        print("无法获取手机号。程序退出。")

if __name__ == '__main__':
    main()
