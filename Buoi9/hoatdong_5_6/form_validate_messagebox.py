#Hoạt động 6: messagebox – validate
import tkinter as tk
from tkinter import messagebox

def xu_ly_submit():
    ho_ten = entry_ho_ten.get().strip()
    tuoi_nhap = entry_tuoi.get().strip()
    email = entry_email.get().strip()
    if ho_ten == "":
        messagebox.showerror("Loi", "Ho ten khong duoc de trong.")
        return
    try:
        tuoi = int(tuoi_nhap)
        if tuoi <= 0:
            messagebox.showerror("Loi", "Tuoi phai lon hon 0.")
            return
    except ValueError:
        messagebox.showerror("Loi", "Tuoi phai la mot so nguyen.")
        return
    if "@" not in email:
        messagebox.showerror("Loi", "Email khong hop le (thieu ky tu @).")
        return
    thong_tin = f"Da nhan: {ho_ten} - {tuoi} tuoi - {email}"
    nhan_ket_qua.config(text=thong_tin)
    messagebox.showinfo("Thanh cong", thong_tin)
def xu_ly_xoa():
    entry_ho_ten.delete(0, tk.END)
    entry_tuoi.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    nhan_ket_qua.config(text="")
cua_so = tk.Tk()
cua_so.title("Form co validate")
cua_so.geometry("400x300")
cua_so.resizable(False, False)
tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_ho_ten = tk.Entry(cua_so, width=25)
entry_ho_ten.grid(row=0, column=1, padx=10, pady=10)
tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_tuoi = tk.Entry(cua_so, width=25)
entry_tuoi.grid(row=1, column=1, padx=10, pady=10)
tk.Label(cua_so, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(cua_so, width=25)
entry_email.grid(row=2, column=1, padx=10, pady=10)
nut_submit = tk.Button(cua_so, text="Submit", command=xu_ly_submit)
nut_submit.grid(row=3, column=0, pady=15)
nut_xoa = tk.Button(cua_so, text="Xoa", command=xu_ly_xoa)
nut_xoa.grid(row=3, column=1, pady=15)
nhan_ket_qua = tk.Label(cua_so, text="", font=("Arial", 11), fg="blue")
nhan_ket_qua.grid(row=4, column=0, columnspan=2, pady=10)
cua_so.mainloop()