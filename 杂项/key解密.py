import base64

encoded_str = "JDJ5JDEwJHUzc2V5cG9qYW5seWVRS1pkRGtXTS5pRkVOUlg1VW9XRkptZm5wQVN6UHBEZzN1am1WVXoy"
decoded_bytes = base64.b64decode(encoded_str.encode('utf-8'))
decoded_str = decoded_bytes.decode('utf-8')

print(decoded_str)