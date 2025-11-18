import tkinter as tk
from tkinter import ttk , messagebox    #Dùng combobox, messagebox
import pyodbc           # Kết nối Database

root = tk.Tk()
root.title("QUẢN LÝ DỊCH VỤ")
# Kích thước form
window_width = 900
window_height = 600

# Lấy kích thước màn hình
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Lấy vị trí ở giữa
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Đặt kích thước và vị trí
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
# Chỉnh màu nền của form
root.configure(bg = "#000000")
# ============================= Kết nối Cơ Sở Dữ Liệu =============================
# ----------------------------- Liên kết CSDL -----------------------------
def Connect_Database():
    try: 
        conn = pyodbc.connect(
                r"DRIVER={ODBC Driver 17 for SQL Server};"
                r"SERVER=LAPTOP-VO3C4ONL;"
                r"DATABASE=Quan_Ly_Khach_San_python;"
                r"Trusted_Connection=yes;"               
        )
        return conn
    except Exception as e:
        messagebox.showerror("Lỗi kết nối", f"Không thể kết nối CSDL:\n{e}")
        return None

# ----------------------------- Load CSDL -----------------------------
def Load_Database_DichVu():
    conn = Connect_Database()
    if conn is None:
        return
    
    cursor = conn.cursor()
    cursor.execute('''SELECT MaDV, TenDV, GiaDV 
                      FROM DichVu
                   ''')
    rows = cursor.fetchall()

    # Xóa dữ liệu cũ
    for i in dichvu.get_children():
        dichvu.delete(i)

    # Thêm dữ liệu mới
    for row in rows:
        dichvu.insert("", tk.END, values=row)

    conn.close()    

# ============================= Giao diện =============================
# ----------------------------- Tên form Quản lý phòng -----------------------------
title_label = tk.Label(root, text="QUẢN LÝ DỊCH VỤ", 
                       font = ("Arial", 20, "bold"), 
                       fg="#FFAA78", 
                       bg = "Black")
title_label.place(x = 450, y = 5, anchor = "n", width = 700, height = 40)

# ----------------------------- Thông tin Phòng (Chứa trong Frame) -----------------------------
group = tk.LabelFrame(root, text = "Thông tin dịch vụ",font = ("Arial", 10),
                      fg = "#0DFF00",
                      bg = "#000000")
group.place(x = 10, y = 130, anchor = "w", width = 300, height = 150)

        # ---Mã dịch vụ ---
tk.Label(group, text = "Mã dịch vụ",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 5)
entry_maphong = tk.Entry(group, font = ("Arial", 10))
entry_maphong.place(x = 110, y = 5, width = 160, height = 20)

        # --- Tên dịch vụ ---
tk.Label(group, text = "Tên dịch vụ",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 35)
entry_maphong = tk.Entry(group, font = ("Arial", 10))
entry_maphong.place(x = 110, y = 35, width = 160, height = 20)

        # --- Tiền dịch vụ ---
tk.Label(group, text = "Tiền dịch vụ",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 65)
entry_maphong = tk.Entry(group, font = ("Arial", 10))
entry_maphong.place(x = 110, y = 65, width = 160, height = 20)

# ----------------------------- Bảng dịch vụ -----------------------------
frame_table = tk.Frame(root, bg="black")
frame_table.place(x=320, y=65, width=550, height=230)

# Tạo Treeview
dichvu = ttk.Treeview(
        frame_table,
        columns=("MaDV", "TenDV", "GiaDV"),
        show="headings")

# Tạo Scrollbar dọc
scroll_y = tk.Scrollbar(frame_table, orient="vertical", command=dichvu.yview)
dichvu.configure(yscrollcommand=scroll_y.set)

# Tạo Scrollbar ngang
scroll_x = tk.Scrollbar(frame_table, orient="horizontal", command=dichvu.xview)
dichvu.configure(xscrollcommand=scroll_x.set)

# Hiển thị Scrollbar
scroll_y.pack(side="right", fill="y")
scroll_x.pack(side="bottom", fill="x")

# Hiển thị Treeview rộng hết cả frame chứa và thay đổi theo kích thước frame
dichvu.pack(fill="both", expand=True)

# Khai báo các cột
dichvu.heading("MaDV", text="Mã dịch vụ")
dichvu.heading("TenDV", text="Tên dịch vụ")
dichvu.heading("GiaDV", text="Giá dịch vụ")

dichvu.column("MaDV", width=50)
dichvu.column("TenDV", width=150)
dichvu.column("GiaDV", width=100)
# Thêm dữ liệu vào bảng
Load_Database_DichVu()

# ============================= Chức năng (Thêm Xoá Sửa ...) =============================
        # --- Thêm ---
btnThem = tk.Button(root, text = "Thêm", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnThem.place(x = 10, y = 210, width = 90, height = 30 )

        # --- Xoá ---
btnXoa = tk.Button(root, text = "Xoá", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnXoa.place(x = 115, y = 210, width = 90, height = 30)

        # --- Sửa ---
btnSua = tk.Button(root, text = "Sửa", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnSua.place(x =220, y = 210, width = 90, height = 30 )

        # --- Huỷ ---
btnHuy = tk.Button(root, text = "Huỷ", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnHuy.place(x = 10, y = 250, width = 90, height = 30 )

        # --- Lưu ---
btnLuu = tk.Button(root, text = "Lưu", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnLuu.place(x = 115, y = 250, width = 90, height = 30)

        # --- Thoát ---
btnThoat = tk.Button(root, text = "Thoát", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnThoat.place(x =220, y = 250, width = 90, height = 30 )


root.mainloop()