import sqlite3

TEN_FILE_CSDL = "chi_tieu.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
    CREATE TABLE IF NOT EXISTS chi_tieu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ngay TEXT NOT NULL,
        hang_muc TEXT NOT NULL,
        so_tien REAL NOT NULL,
        ghi_chu TEXT
    )
    """)
    ket_noi.commit()
    ket_noi.close()

def them_khoan_chi(ngay, hang_muc, so_tien, ghi_chu):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO chi_tieu (ngay, hang_muc, so_tien, ghi_chu) VALUES (?, ?, ?, ?)",
        (ngay, hang_muc, so_tien, ghi_chu)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_chi_tieu():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, ngay, hang_muc, so_tien, ghi_chu FROM chi_tieu ORDER BY id DESC")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_khoan_chi(id_chi_tieu):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM chi_tieu WHERE id = ?", (id_chi_tieu,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_theo_hang_muc():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT hang_muc, SUM(so_tien) FROM chi_tieu GROUP BY hang_muc")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua