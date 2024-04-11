import tkinter as tk
import requests

def fetch_data():
    choice = choice_var.get()
    user_input = entry_var.get()

    if choice == '1':
        url = f"https://zy.xywlapi.cc/qqapi?qq={user_input}"
    elif choice == '2':
        url = f"https://zy.xywlapi.cc/lolname?name={user_input}"
    elif choice == '3':
        url = f"https://zy.xywlapi.cc/wbapi?id={user_input}"
    else:
        output_label.config(text="无效选择，请输入1、2、3或4以选择操作。")
        return

    response = requests.get(url)
    if response.status_code == 200:
        output_label.config(text=response.text)
    else:
        output_label.config(text=f"请求失败，状态码: {response.status_code}")

# Create main window
root = tk.Tk()
root.title("API查询工具")
root.geometry("400x300")  # Set the size of the window

# Create input widgets
choice_label = tk.Label(root, text="请选择操作:")
choice_label.pack()

choice_var = tk.StringVar()
choice_var.set('1')
choices = [("QQ查询phone", '1'), ("LOL名称查询QQ", '2'), ("微博查询phone", '3')]
for text, value in choices:
    radio = tk.Radiobutton(root, text=text, variable=choice_var, value=value)
    radio.pack()

entry_label = tk.Label(root, text="请输入查询内容:")
entry_label.pack()

entry_var = tk.StringVar()
entry_entry = tk.Entry(root, textvariable=entry_var)
entry_entry.pack()

fetch_button = tk.Button(root, text="查询", command=fetch_data)
fetch_button.pack()

# Create output widget
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
