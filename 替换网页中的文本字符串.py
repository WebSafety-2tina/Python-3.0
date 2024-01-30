import requests

def fetch_and_replace(url, replacements):
    try:
        response = requests.get(url)
        response.raise_for_status()

        content = response.text
        for original, replacement in replacements.items():
            content = content.replace(original, replacement)

        # 输出替换后的内容
        print(content)
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch content from {url}. Error: {e}")

if __name__ == "__main__":
    # 示例网页，替换规则
    webpage_url = "http://guihe.23pqzn.cfd/ddps.php"
    replacement_rules = {"电话号码参数未提供": "1", "Hello": "Hi"}

    # 获取网页内容并进行替换
    fetch_and_replace(webpage_url, replacement_rules)
