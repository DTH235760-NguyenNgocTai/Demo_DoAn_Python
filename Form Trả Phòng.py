import tkinter as tk
from tkinter import ttk , messagebox    #Dùng combobox, messagebox
from tkcalendar import DateEntry        # Dùng DateEntry
import pyodbc           # Kết nối Database

root = tk.Tk()
root.title("TRẢ PHÒNG")
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

# ----------------------------- Load Phòng -----------------------------
def Load_Database_Phong():
    conn = Connect_Database()
    if conn is None:
        return
    
    cursor = conn.cursor()
    cursor.execute('''SELECT MaPhong, LoaiPhong, TrangThai, GiaTien
                      FROM Phong
                   ''')
    rows = cursor.fetchall()

    # Xóa dữ liệu cũ
    for i in phong.get_children():
        phong.delete(i)

    # Thêm dữ liệu mới
    for row in rows:
        phong.insert("", tk.END, values = row)

    conn.close() 

# ----------------------------- Load Đặt Phòng ----------------------------- 
def Load_Database_DatPhong():
    conn = Connect_Database()
    if conn is None:
        return
    
    cursor = conn.cursor()
    cursor.execute('''SELECT *
                      FROM DatPhong
                   ''')
    rows = cursor.fetchall()

    # Xoá dữ liệu cũ
    for i in datphong.get_children():
        datphong.delete(i)

    # Thêm dữ liệu mới
    for row in rows:
        datphong.insert("",tk.END, values = row)

    conn.close()

# ============================= Giao diện =============================
# ----------------------------- Tên form Trả phòng -----------------------------
title_label = tk.Label(root, text = "TRẢ PHÒNG", 
                       font = ("Arial", 20, "bold"), 
                       fg = "#FFAA78", 
                       bg = "Black")
title_label.place(x = 450, y = 5, anchor = "n", width = 700, height = 40)
# ----------------------------- Thông tin Trả phòng (Chứa trong Frame) -----------------------------
group = tk.LabelFrame(root, text = "Thông tin trả phòng", font = ("Arial", 10),
                    bg = "#000000",
                    fg = "#0DFF00")
group.place(relx = 0.005, rely = 0.23, anchor = "w", width = 570, height = 170)

        # --- Mã đặt phòng ---
tk.Label(group, text = "Mã đặt phòng", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 5)
entry_madp = tk.Entry(group, state = "disabled",
                      font = ("Arial", 10))
entry_madp.place(x = 120, y = 5, width = 160, height = 20)

        # --- Mã phòng ---
tk.Label(group, text = "Mã phòng", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 35)
entry_maphong = tk.Entry(group,
                      font = ("Arial", 10))
entry_maphong.place(x = 120, y = 35, width = 160, height = 20)

        # --- Mã khách hàng ---
tk.Label(group, text = "Mã khách hàng", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 65)
entry_makh = tk.Entry(group,
                      font = ("Arial", 10))
entry_makh.place(x = 120, y = 65, width = 160, height = 20)

        # --- Tên khách hàng ---
tk.Label(group, text = "Tên khách hàng", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 95)
entry_tenkh = tk.Entry(group,
                      font = ("Arial", 10))
entry_tenkh.place(x = 120, y = 95, width = 160, height = 20)


        # --- Ngày đặt ---
tk.Label(group, text = "Ngày đặt",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 310, y = 5)
ngaydat = DateEntry(group, date_pattern = "dd/mm/yyyy")
ngaydat.place(x = 380, y = 5, width = 160, height = 20)

        # --- Ngày nhận ---
tk.Label(group, text = "Ngày nhận",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 310, y = 35)
ngaynhan = DateEntry(group, date_pattern = "dd/mm/yyyy")
ngaynhan.place(x = 380, y = 35, width = 160, height = 20)

        # --- Ngày trả ---
tk.Label(group, text = "Ngày trả",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 310, y = 65)
ngaytra = DateEntry(group, date_pattern = "dd/mm/yyyy")
ngaytra.place(x = 380, y = 65, width = 160, height = 20)

# ----------------------------- Bảng phòng -----------------------------
frame_phong = tk.Frame(root, bg = "black")
frame_phong.place(x = 5, y = 230, width = 880, height = 150)

# Tạo Treeview
phong = ttk.Treeview(
        frame_phong,
        columns = ("MaPhong", "LoaiPhong", "TrangThai", "GiaTien"),
        show = "headings")

# Tạo Scrollbar dọc
scroll_y = tk.Scrollbar(frame_phong, orient = "vertical", command = phong.yview)
phong.configure(yscrollcommand=scroll_y.set)

# Tạo Scrollbar ngang
scroll_x = tk.Scrollbar(frame_phong, orient = "horizontal", command = phong.xview)
phong.configure(xscrollcommand = scroll_x.set)

# Hiển thị Scrollbar
scroll_y.pack(side = "right", fill = "y")
scroll_x.pack(side = "bottom", fill = "x")

# Hiển thị Treeview rộng hết cả frame chứa và thay đổi theo kích thước frame
phong.pack(fill = "both", expand = True)

# Khai báo các cột
phong.heading("MaPhong", text="Mã phòng")
phong.heading("LoaiPhong", text="Loại phòng")
phong.heading("TrangThai", text="Trạng thái")
phong.heading("GiaTien", text="Giá tiền")

phong.column("MaPhong", width = 80)
phong.column("LoaiPhong", width = 150)
phong.column("TrangThai", width = 150)
phong.column("GiaTien", width = 100)
# Thêm dữ liệu vào bảng
Load_Database_Phong()

# ----------------------------- Bảng Đặt phòng -----------------------------
frame_datphong = tk.Frame(root, bg = "black")
frame_datphong.place(x = 5, y = 390, width = 880, height = 200)

# Tạo Treeview
datphong = ttk.Treeview(
        frame_datphong,
        columns = ("MaDatPhong", "MaPhong", "MaKH", "TenKH", "NgayDat", "NgayNhan", "NgayTra"),
        show = "headings")

# Tạo Scrollbar dọc
scroll_y = tk.Scrollbar(frame_datphong, orient = "vertical", command = datphong.yview)
datphong.configure(yscrollcommand = scroll_y.set)

# Tạo Scrollbar ngang
scroll_x = tk.Scrollbar(frame_datphong, orient = "horizontal", command = datphong.xview)
datphong.configure(xscrollcommand = scroll_x.set)

# Hiển thị Scrollbar
scroll_y.pack(side = "right", fill = "y")
scroll_x.pack(side = "bottom", fill = "x")

# Hiển thị Treeview rộng hết cả frame chứa và thay đổi theo kích thước frame
datphong.pack(fill = "both", expand = True)

# Khai báo các cột
datphong.heading("MaDatPhong", text = "Mã đặt phòng")
datphong.heading("MaPhong", text = "Mã phòng")
datphong.heading("MaKH", text = "Mã khách hàng")
datphong.heading("TenKH", text = "Tên khách hàng")
datphong.heading("NgayDat", text = "Ngày đặt")
datphong.heading("NgayNhan", text = "Ngày nhận")
datphong.heading("NgayTra", text = "Ngày trả")

datphong.column("MaDatPhong", width = 100)
datphong.column("MaPhong", width = 100)
datphong.column("MaKH", width = 100)
datphong.column("TenKH", width = 150)
datphong.column("NgayDat", width = 120)
datphong.column("NgayNhan", width = 120)
datphong.column("NgayTra", width = 120)
# Thêm dữ liệu vào bảng
Load_Database_DatPhong()

# ============================= Chức năng =============================
        # --- Nhập thông tin ---
btnNhap = tk.Button(root, text = "Nhập thông tin", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnNhap.place(x = 580, y = 62, width = 150, height = 30 )

        # --- Huỷ ---
btnHuy = tk.Button(root, text = "Huỷ", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnHuy.place(x = 740, y = 62, width = 150, height = 30)

        # --- Trả phòng ---
btnTraphong = tk.Button(root, text = "Xem phòng", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnTraphong.place(x =580, y = 110, width = 150, height = 30 )

        # --- Thoát ---
btnThoat = tk.Button(root, text = "Thoát", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnThoat.place(x =740, y = 110, width = 150, height = 30 )




root.mainloop()