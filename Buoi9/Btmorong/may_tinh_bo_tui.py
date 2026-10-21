import tkinter as tk
from tkinter import messagebox

def bam(ky_tu):
    bien_phep_tinh.set(bien_phep_tinh.get() + ky_tu)
def xoa():
    bien_phep_tinh.set("")
    bien_ket_qua.set("")
def xoa_ky_tu():
    bien_phep_tinh.set(bien_phep_tinh.get()[:-1])
def tinh():
    try:
        ket_qua = eval(bien_phep_tinh.get())
        bien_ket_qua.set(str(ket_qua))
    except:
        messagebox.showerror("Loi", "Phep tinh khong hop le")
        bien_ket_qua.set("")
cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("260x370")
bien_phep_tinh = tk.StringVar()
bien_ket_qua = tk.StringVar()

tk.Label(cua_so, text="Phep tinh:").grid(row=0, column=0, columnspan=4, sticky="w", padx=10)
tk.Entry(cua_so, textvariable=bien_phep_tinh, font=("Arial", 14), width=20).grid(row=1, column=0, columnspan=4, padx=10, pady=2)

tk.Label(cua_so, text="Ket qua:").grid(row=2, column=0, columnspan=4, sticky="w", padx=10)
tk.Entry(cua_so, textvariable=bien_ket_qua, font=("Arial", 14), width=20).grid(row=3, column=0, columnspan=4, padx=10, pady=5)

tk.Button(cua_so, text="7", width=5, command=lambda: bam("7")).grid(row=4, column=0, pady=5)
tk.Button(cua_so, text="8", width=5, command=lambda: bam("8")).grid(row=4, column=1, pady=5)
tk.Button(cua_so, text="9", width=5, command=lambda: bam("9")).grid(row=4, column=2, pady=5)
tk.Button(cua_so, text="/", width=5, command=lambda: bam("/")).grid(row=4, column=3, pady=5)

tk.Button(cua_so, text="4", width=5, command=lambda: bam("4")).grid(row=5, column=0, pady=5)
tk.Button(cua_so, text="5", width=5, command=lambda: bam("5")).grid(row=5, column=1, pady=5)
tk.Button(cua_so, text="6", width=5, command=lambda: bam("6")).grid(row=5, column=2, pady=5)
tk.Button(cua_so, text="*", width=5, command=lambda: bam("*")).grid(row=5, column=3, pady=5)

tk.Button(cua_so, text="1", width=5, command=lambda: bam("1")).grid(row=6, column=0, pady=5)
tk.Button(cua_so, text="2", width=5, command=lambda: bam("2")).grid(row=6, column=1, pady=5)
tk.Button(cua_so, text="3", width=5, command=lambda: bam("3")).grid(row=6, column=2, pady=5)
tk.Button(cua_so, text="-", width=5, command=lambda: bam("-")).grid(row=6, column=3, pady=5)

tk.Button(cua_so, text="C", width=5, command=xoa).grid(row=7, column=0, pady=5)
tk.Button(cua_so, text="0", width=5, command=lambda: bam("0")).grid(row=7, column=1, pady=5)
tk.Button(cua_so, text="=", width=5, command=tinh).grid(row=7, column=2, pady=5)
tk.Button(cua_so, text="+", width=5, command=lambda: bam("+")).grid(row=7, column=3, pady=5)

tk.Button(cua_so, text="DELETE", width=25, command=xoa_ky_tu).grid(row=8, column=0, columnspan=4, pady=5)

cua_so.mainloop()