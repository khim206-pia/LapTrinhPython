import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Bố cục bảng place()")
cua_so.geometry("300x250")
tk.Label(cua_so, text="Họ tên:").place(x=20, y=20)
tk.Label(cua_so, text="Tuổi:").place(x=20, y=60)
tk.Label(cua_so, text="Email:").place(x=20, y=100)
tk.Button(cua_so, text="Đồng ý").place(x=40, y=160)
tk.Button(cua_so, text="Hủy").place(x=150, y=160)
cua_so.mainloop()