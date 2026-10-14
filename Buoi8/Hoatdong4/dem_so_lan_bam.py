import tkinter as tk

so_lan_bam = 0
def tang_so_lan_bam():
    global so_lan_bam
    so_lan_bam += 1
    nhan_dem.config(text=f"Số lần đã bấm: {so_lan_bam}")
cua_so = tk.Tk()
cua_so.title("Đếm số lần bấm nút")
cua_so.geometry("350x200")
nhan_dem = tk.Label(cua_so, text="Số lần đã bấm: 0", font=("Arial", 14))
nhan_dem.pack(pady=20)
nut_bam = tk.Button(cua_so, text="Bấm vào đây", command=tang_so_lan_bam)
nut_bam.pack(pady=10)
cua_so.mainloop()