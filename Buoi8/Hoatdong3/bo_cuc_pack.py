import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Bố cục bảng pack()")
cua_so.geometry("300x250")
tk.Label(cua_so, text="Họ tên:").pack(pady=5)
tk.Label(cua_so, text="Tuổi:").pack(pady=5)
tk.Label(cua_so, text="Email:").pack(pady=5)
tk.Button(cua_so, text="Đồng ý").pack(side="left", padx=20, pady=15)
tk.Button(cua_so, text="Hủy").pack(side="right", padx=20, pady=15)
cua_so.mainloop()