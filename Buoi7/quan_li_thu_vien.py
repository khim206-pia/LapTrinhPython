danh_sach_sach = [
    {"ma_sach": "A101", "ten_sach": "Nha Gia Kim", "gia": 30000, "trang_thai": "Co san", "nguoi_muon": ""},
    {"ma_sach": "A102", "ten_sach": "Dac Nhan Tam", "gia": 25000, "trang_thai": "Co san", "nguoi_muon": ""},
    {"ma_sach": "A103", "ten_sach": "Tieu Thuyet Bo Gia", "gia": 17000, "trang_thai": "Co san", "nguoi_muon": ""},
    {"ma_sach": "A104", "ten_sach": "Thoi Quen De Thanh Dat", "gia": 10000, "trang_thai": "Co san", "nguoi_muon": ""},
]
lich_su_doanh_thu = []

def hien_thi_danh_sach_sach():
    print("\n" + "=" * 80)
    print(f"{'Ma sach':<10}{'Ten sach':<26}{'Gia/ngay':<16}{'Trang thai':<14}{'Nguoi muon':<14}")
    print("-" * 80)
    for sach in danh_sach_sach:
        gia_str = f"{sach['gia']:,} VND"
        print(f"{sach['ma_sach']:<10}{sach['ten_sach']:<26}{gia_str:<16}{sach['trang_thai']:<14}{sach['nguoi_muon']:<14}")
    print("=" * 80)

def tim_sach_theo_ma(ma_sach):
    for sach in danh_sach_sach:
        if sach["ma_sach"] == ma_sach:
            return sach
    return None

def xem_sach_co_san():
    sach_co_san = [sach for sach in danh_sach_sach if sach["trang_thai"] == "Co san"]
    if len(sach_co_san) == 0:
        print("-> Hien khong con dau sach nao co san de muon.")
        return
    print("\nCAC SACH DANG CO SAN:")
    for sach in sach_co_san:
        print(f"- {sach['ma_sach']} | {sach['ten_sach']} | {sach['gia']:,} VND/ngay")

def them_sach(ma_sach, ten_sach, gia):
    if tim_sach_theo_ma(ma_sach) is not None:
        print(f"-> Ma sach {ma_sach} da ton tai, khong the them.")
        return
    danh_sach_sach.append({
        "ma_sach": ma_sach,
        "ten_sach": ten_sach,
        "gia": gia,
        "trang_thai": "Co san",
        "nguoi_muon": ""
    })
    print(f"-> Da them sach {ma_sach} thanh cong.")

def muon_sach(ma_sach, nguoi_muon):
    sach = tim_sach_theo_ma(ma_sach)
    if sach is None:
        print(f"-> Khong tim thay sach {ma_sach}.")
        return
    if sach["trang_thai"] == "Dang muon":
        print(f"-> Sach {ma_sach} da co nguoi muon, khong the muon tiep.")
        return
    sach["trang_thai"] = "Dang muon"
    sach["nguoi_muon"] = nguoi_muon
    print(f"-> Cho nguoi muon {nguoi_muon} muon sach {ma_sach} thanh cong.")

def tra_sach(ma_sach, so_ngay):
    sach = tim_sach_theo_ma(ma_sach)
    if sach is None:
        print(f"-> Khong tim thay sach {ma_sach}.")
        return
    if sach["trang_thai"] == "Co san":
        print(f"-> Sach {ma_sach} dang co san tai thu vien, khong co nguoi muon muon de tra.")
        return
    thanh_tien = sach["gia"] * so_ngay
    lich_su_doanh_thu.append({
        "ma_sach": ma_sach,
        "nguoi_muon": sach["nguoi_muon"],
        "so_ngay": so_ngay,
        "thanh_tien": thanh_tien
    })
    print(f"-> nguoi muon {sach['nguoi_muon']} tra sach {ma_sach} sau {so_ngay} ngay.")
    print(f"-> Tong tien phai thanh toan: {thanh_tien:,} VND")
    sach["trang_thai"] = "Co san"
    sach["nguoi_muon"] = ""

def thong_ke_doanh_thu():
    if len(lich_su_doanh_thu) == 0:
        print("-> Chua co giao dich tra sach nao.")
        return
    tong_doanh_thu = 0
    print("\nLICH SU GIAO DICH:")
    for gd in lich_su_doanh_thu:
        print(f"- {gd['ma_sach']} | {gd['nguoi_muon']} | {gd['so_ngay']} ngay | {gd['thanh_tien']:,} VND")
        tong_doanh_thu += gd["thanh_tien"]
    print(f"\n>>> TONG DOANH THU: {tong_doanh_thu:,} VND")

def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            gia_tri = int(input(loi_nhac))
            if gia_tri > 0:
                return gia_tri
            print("-> Gia tri phai lon hon 0, vui long nhap lai.")
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")

def hien_thi_menu():
    print("\n===== QUAN LY THU VIEN MUON/TRA SACH =====")
    print("1. Hien thi danh sach tat ca sach")
    print("2. Xem cac sach dang co san")
    print("3. Them sach moi")
    print("4. Muon sach cho nguoi muon")
    print("5. Tra sach / Thanh toan")
    print("6. Thong ke doanh thu")
    print("0. Thoat chuong trinh")

def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()
        if lua_chon == "1":
            hien_thi_danh_sach_sach()
        elif lua_chon == "2":
            xem_sach_co_san()
        elif lua_chon == "3":
            ma_sach = input("Nhap ma sach moi: ").strip().upper()
            ten_sach = input("Nhap ten sach: ").strip().title()
            gia = nhap_so_nguyen("Nhap gia muon/ngay: ")
            them_sach(ma_sach, ten_sach, gia)
        elif lua_chon == "4":
            ma_sach = input("Nhap ma sach can muon: ").strip().upper()
            nguoi_muon = input("Nhap ten nguoi muon: ").strip().title()
            muon_sach(ma_sach, nguoi_muon)
        elif lua_chon == "5":
            ma_sach = input("Nhap ma sach can tra: ").strip().upper()
            so_ngay = nhap_so_nguyen("Nhap so ngay da muon: ")
            tra_sach(ma_sach, so_ngay)
        elif lua_chon == "6":
            thong_ke_doanh_thu()
        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")

if __name__ == "__main__":
    chay_chuong_trinh()