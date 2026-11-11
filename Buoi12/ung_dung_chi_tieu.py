import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_chi_tieu as db
DANH_SACH_HANG_MUC = ["An uong", "Di lai", "Hoc tap", "Mua sam", "Giai tri", "Khac"]
class UngDungChiTieu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Chi tieu Ca nhan")
        self.geometry("620x520")
        self.resizable(False, False)
        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()
    def khoi_tao_giao_dien(self):
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Ngay (DD/MM/YYYY):").grid(row=0, column=0, sticky="w", pady=4)
        self.o_nhap_ngay = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ngay.grid(row=0, column=1, padx=10, pady=4)
        self.o_nhap_ngay.insert(0, "11/11/2026")

        tk.Label(khung_nhap, text="Hang muc:").grid(row=1, column=0, sticky="w", pady=4)
        self.chon_hang_muc = ttk.Combobox(khung_nhap, values=DANH_SACH_HANG_MUC, width=27, state="readonly")
        self.chon_hang_muc.current(0)
        self.chon_hang_muc.grid(row=1, column=1, padx=10, pady=4)

        tk.Label(khung_nhap, text="So tien (VND):").grid(row=2, column=0, sticky="w", pady=4)
        self.o_nhap_so_tien = tk.Entry(khung_nhap, width=30)
        self.o_nhap_so_tien.grid(row=2, column=1, padx=10, pady=4)

        tk.Label(khung_nhap, text="Ghi chu:").grid(row=3, column=0, sticky="w", pady=4)
        self.o_nhap_ghi_chu = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ghi_chu.grid(row=3, column=1, padx=10, pady=4)

        # Nút bấm cơ bản mặc định của Tkinter, không có màu mè
        tk.Button(khung_nhap, text="Them khoan chi", command=self.xu_ly_them).grid(row=4, column=0, columnspan=2, pady=10)

        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_chi_tieu = tk.Listbox(khung_danh_sach, width=82, height=13)
        self.listbox_chi_tieu.pack(side="left", fill="both", expand=True)

        cuon_y = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_chi_tieu.yview)
        cuon_y.pack(side="right", fill="y")
        self.listbox_chi_tieu.config(yscrollcommand=cuon_y.set)

        khung_nut = tk.Frame(self)
        khung_nut.pack(pady=10)

        tk.Button(khung_nut, text="Xoa khoan chi", command=self.xu_ly_xoa).grid(row=0, column=0, padx=10)
        tk.Button(khung_nut, text="Thong ke theo hang muc", command=self.xu_ly_thong_ke).grid(row=0, column=1, padx=10)

    def tai_lai_danh_sach(self):
        self.listbox_chi_tieu.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_chi_tieu()
        for item in self.danh_sach_hien_tai:
            id_ct, ngay, hang_muc, so_tien, ghi_chu = item
            chuoi = f"[{ngay}] {hang_muc}: {int(so_tien)} VND - {ghi_chu}"
            self.listbox_chi_tieu.insert(tk.END, chuoi)

    def xu_ly_them(self):
        ngay = self.o_nhap_ngay.get().strip()
        hang_muc = self.chon_hang_muc.get()
        chuoi_so_tien = self.o_nhap_so_tien.get().strip()
        ghi_chu = self.o_nhap_ghi_chu.get().strip()
        if ngay == "" or chuoi_so_tien == "":
            messagebox.showerror("Loi", "Vui long nhap day du ngay thang va so tien.")
            return
        try:
            so_tien = float(chuoi_so_tien)
            if so_tien <= 0:
                messagebox.showerror("Loi", "So tien chi tieu phai lon hon 0.")
                return
        except ValueError:
            messagebox.showerror("Loi", "So tien phai la mot gia tri so hop le.")
            return

        db.them_khoan_chi(ngay, hang_muc, so_tien, ghi_chu)
        self.o_nhap_so_tien.delete(0, tk.END)
        self.o_nhap_ghi_chu.delete(0, tk.END)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thanh cong", f"Da ghi nhan khoan chi: {hang_muc}")

    def xu_ly_xoa(self):
        lua_chon = self.listbox_chi_tieu.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon mot khoan chi trong danh sach de xoa.")
            return
        id_ct = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_khoan_chi(id_ct)
        self.tai_lai_danh_sach()

    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_theo_hang_muc()
        if not du_lieu:
            messagebox.showinfo("Thong bao", "Chua co du lieu chi tieu de thong ke.")
            return
        hang_muc = [row[0] for row in du_lieu]
        so_tien = [row[1] for row in du_lieu]
        plt.figure(figsize=(7, 4.5))
        bars = plt.bar(hang_muc, so_tien)
        plt.title("Tong chi tieu theo tung hang muc")
        plt.xlabel("Hang muc chi tieu")
        plt.ylabel("So tien (VND)")
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, f"{int(yval)}", ha='center', va='bottom')
        plt.tight_layout()
        plt.show()
if __name__ == "__main__":
    app = UngDungChiTieu()
    app.mainloop()
