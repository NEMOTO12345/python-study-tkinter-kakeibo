import tkinter as tk
import tkinter.ttk as ttk
import datetime

root = tk.Tk()

root.title("家計簿")
root.minsize(400,300)


static1 = tk.Label(text="日付")
static1.pack()
entry1 =tk.Entry(width=30)
entry1.pack()

static2 = tk.Label(text="用途")
static2.pack()
entry2 = ttk.Combobox(root,state="readonly")
entry2["values"] = ("食費","住居費","光熱費")
# デフォルトの値をA(index=0)に設定
entry2.current(0)
# コンボボックスの配置
entry2.pack()

static3 = tk.Label(text="金額")
static3.pack()
entry3 =tk.Entry(width=30,justify=tk.RIGHT)
entry3.pack()

button = tk.Button(text="登録")

def get_value(event):
    val1 = entry1.get()
    if val1 == '':
        val1 = datetime.date.today()
    val2 = entry2.get()
    val3 = entry3.get()
    total = f"{val1},{val2},{val3}"   
    with open("kakeibo.csv","w") as f:
        f.write(total)
    entry1.delete(0,tk.END)
    entry2.current(0)
    entry3.delete(0,tk.END)

button.bind('<1>',get_value)
button.pack()

root.mainloop()