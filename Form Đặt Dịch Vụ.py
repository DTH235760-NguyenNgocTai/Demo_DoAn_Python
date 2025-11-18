import tkinter as tk
from tkinter import ttk , messagebox    #Dùng combobox, messagebox
from tkcalendar import DateEntry        # Dùng DateEntry
import pyodbc           # Kết nối Database

root = tk.Tk()
root.title("ĐẶT DỊCH VỤ")
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

# ----------------------------- Load Dịch vụ -----------------------------
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

    # ----------------------------- Load Chi tiết dịch vụ -----------------------------
def Load_Database_CTDV():
    conn = Connect_Database()
    if conn is None:
        return
    
    cursor = conn.cursor()
    cursor.execute('''SELECT MaCTDV, MaDatPhong, MaDV, SoLuong 
                      FROM ChiTietDichVu
                   ''')
    rows = cursor.fetchall()

    # Xóa dữ liệu cũ
    for i in ctdv.get_children():
        ctdv.delete(i)

    # Thêm dữ liệu mới
    for row in rows:
        ctdv.insert("", tk.END, values=row)

    conn.close()   

# ============================= Giao diện =============================
# ----------------------------- Tên form Đặt phòng -----------------------------
title_label = tk.Label(root, text="ĐẶT DỊCH VỤ", 
                       font = ("Arial", 20, "bold"), 
                       fg="#FFAA78", 
                       bg = "Black")
title_label.place(x = 450, y = 5, anchor = "n", width = 700, height = 40)
# ----------------------------- Thông tin Đặt phòng (Chứa trong Frame) -----------------------------
group = tk.LabelFrame(root, text = "Thông tin đặt dịch vụ", font = ("Arial", 10),
                    bg = "#000000",
                    fg = "#0DFF00")
group.place(relx = 0.005, rely = 0.23, anchor = "w", width = 300, height = 170)

        # --- Mã đặt dịch vụ ---
tk.Label(group, text = "Mã đặt dịch vụ",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 10, y = 5)
entry_maddv = tk.Entry(group, 
                      state = "disabled",
                      font = ("Arial", 10))
entry_maddv.place(x = 120, y = 5, width = 160, height = 20)

        # --- Mã đặt phòng ---
tk.Label(group, text = "Mã đặt phòng", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 10, y = 35)
entry_madp = tk.Entry(group, 
                      state = "disabled",
                      font = ("Arial", 10))
entry_madp.place(x = 120, y = 35, width = 160, height = 20)

        # --- Mã dịch vụ ---
tk.Label(group, text = "Mã dịch vụ", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 10, y = 65)
entry_madv = tk.Entry(group, font = ("Arial", 10))
entry_madv.place(x = 120, y = 65, width = 160, height = 20)

        # --- Số lượng ---
tk.Label(group, text = "Số lượng", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 10, y = 95)
entry_sl = tk.Entry(group, font = ("Arial", 10))
entry_sl.place(x = 120, y = 95, width = 160, height = 20)

# ----------------------------- Bảng dịch vụ -----------------------------
frame_dv = tk.Frame(root, bg="black")
frame_dv.place(x = 320, y = 62, width = 570, height = 170)

# Tạo Treeview
dichvu = ttk.Treeview(
        frame_dv,
        columns=("MaDV", "TenDV", "GiaDV"),
        show="headings")

# Tạo Scrollbar dọc
scroll_y = tk.Scrollbar(frame_dv, orient="vertical", command=dichvu.yview)
dichvu.configure(yscrollcommand=scroll_y.set)

# Tạo Scrollbar ngang
scroll_x = tk.Scrollbar(frame_dv, orient="horizontal", command=dichvu.xview)
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

# ----------------------------- Bảng Chi tiết dịch vụ -----------------------------
frame_ctdv = tk.Frame(root, bg = "black")
frame_ctdv.place(x = 10, y = 250, width = 880, height = 170)
# Tạo Treeview
ctdv = ttk.Treeview(
        frame_ctdv,
        columns = ("MaCTDV", "MaDatPhong", "MaDV", "SoLuong"),
        show = "headings")

# Tạo Scrollbar dọc
scroll_y = tk.Scrollbar(frame_ctdv, orient = "vertical", command = ctdv.yview)
ctdv.configure(yscrollcommand=scroll_y.set)

# Tạo Scrollbar ngang
scroll_x = tk.Scrollbar(frame_ctdv, orient = "horizontal", command = ctdv.xview)
ctdv.configure(xscrollcommand = scroll_x.set)

# Hiển thị Scrollbar
scroll_y.pack(side = "right", fill = "y")
scroll_x.pack(side = "bottom", fill = "x")

# Hiển thị Treeview rộng hết cả frame chứa và thay đổi theo kích thước frame
ctdv.pack(fill = "both", expand = True)

# Khai báo các cột
ctdv.heading("MaCTDV", text="Mã CTDV")
ctdv.heading("MaDatPhong", text="Mã đặt phòng")
ctdv.heading("MaDV", text="Mã dịch vụ")
ctdv.heading("SoLuong", text="Số lượng")

ctdv.column("MaCTDV", width = 80)
ctdv.column("MaDatPhong", width = 150)
ctdv.column("MaDV", width = 150)
ctdv.column("SoLuong", width = 100)
# Thêm dữ liệu vào bảng
Load_Database_CTDV()

# ============================= Chức năng =============================
        # --- Nhập thông tin ---
btnNhap = tk.Button(root, text = "Nhập thông tin", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnNhap.place(x = 10, y = 440, width = 120, height = 30 )

        # --- Đặt ---
btnDat = tk.Button(root, text = "Đặt", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnDat.place(x = 260, y = 440, width = 120, height = 30)

btnHuy = tk.Button(root, text = "Huỷ", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnHuy.place(x = 510, y = 440, width = 120, height = 30)

        # --- Thoát ---
btnThoat = tk.Button(root, text = "Thoát", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnThoat.place(x =760, y = 440, width = 120, height = 30 )



root.mainloop()