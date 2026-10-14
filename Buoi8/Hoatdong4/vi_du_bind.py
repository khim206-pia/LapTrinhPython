import tkinter as tk

def khi_go_phim(event):
    nhan_thong_bao.config(text=f"Bạn vừa nhấn phím: {event.char}")
def khi_click_chuot(event):
    nhan_thong_bao.config(text=f"Bạn vừa click tại tọa độ: ({event.x}, {event.y})")
cua_so = tk.Tk()
cua_so.title("Ví dụ bind()")
cua_so.geometry("400x250")
nhan_thong_bao = tk.Label(cua_so, text="Hay nhấn phím hoặc click chuột", font=("Arial", 12))
nhan_thong_bao.pack(pady=30)
cua_so.bind("<Key>", khi_go_phim)
cua_so.bind("<Button-1>", khi_click_chuot)
cua_so.mainloop()