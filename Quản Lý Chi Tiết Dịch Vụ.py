import tkinter as tk
from tkinter import ttk , messagebox    #Dùng combobox, messagebox
import pyodbc           # Kết nối Database

root = tk.Tk()
root.title("QUẢN LÝ CHI TIẾT DỊCH VỤ")
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
# ----------------------------- Tên form Quản lý phòng -----------------------------
title_label = tk.Label(root, text="QUẢN LÝ CHI TIẾT DỊCH VỤ", 
                       font = ("Arial", 20, "bold"), 
                       fg="#FFAA78", 
                       bg = "Black")
title_label.place(x = 450, y = 5, anchor = "n", width = 700, height = 40)

# ----------------------------- Thông tin Phòng (Chứa trong Frame) -----------------------------
group = tk.LabelFrame(root, text = "Thông tin dịch vụ",font = ("Arial", 10),
                      fg = "#0DFF00",
                      bg = "#000000")
group.place(x = 10, y = 140, anchor = "w", width = 600, height = 180)

        # --- Mã chi tiết dịch vụ ---
tk.Label(group, text = "Mã CTDV", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 5)
entry_mactdv = tk.Entry(group, state = "disabled",
                      font = ("Arial", 10))
entry_mactdv.place(x = 120, y = 5, width = 160, height = 20)

        # --- Mã đặt phòng ---
tk.Label(group, text = "Mã đặt phòng", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 35)
entry_madp = tk.Entry(group, 
                      state = "disabled",
                      font = ("Arial", 10))
entry_madp.place(x = 120, y = 35, width = 160, height = 20)

        # --- Mã phòng ---
tk.Label(group, text = "Mã phòng", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 65)
entry_maphong = tk.Entry(group, font = ("Arial", 10))
entry_maphong.place(x = 120, y = 65, width = 160, height = 20)

        # --- Mã khách hàng ---
tk.Label(group, text = "Mã khách hàng", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 95)
entry_makh = tk.Entry(group, font = ("Arial", 10))
entry_makh.place(x = 120, y = 95, width = 160, height = 20)

        # --- Tên khách hàng ---
tk.Label(group, text = "Tên khách hàng", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 125)
entry_tenkh = tk.Entry(group, font = ("Arial", 10))
entry_tenkh.place(x = 120, y = 125, width = 160, height = 20)

        # --- Mã dịch vụ ---
tk.Label(group, text = "Mã dịch vụ", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 310, y = 5)
entry_madv = tk.Entry(group, font = ("Arial", 10))
entry_madv.place(x = 390, y = 5, width = 160, height = 20)

        # --- Tên dịch vụ ---
tk.Label(group, text = "Tên dịch vụ", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 310, y = 35)
entry_tendv = tk.Entry(group, font = ("Arial", 10))
entry_tendv.place(x = 390, y = 35, width = 160, height = 20)

        # --- Số lượng ---
tk.Label(group, text = "Số lượng", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 310, y = 65)
entry_sl = tk.Entry(group, font = ("Arial", 10))
entry_sl.place(x = 390, y = 65, width = 160, height = 20)

# ----------------------------- Bảng Chi tiết dịch vụ -----------------------------
frame_ctdv = tk.Frame(root, bg = "black")
frame_ctdv.place(x = 10, y = 250, width = 600, height = 150)

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
        # --- Xem chi tiết ---
btnXemchitiet = tk.Button(root, text = "Xem chi tiết", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnXemchitiet.place(x = 10, y = 420, width = 100, height = 30)

        # --- Thoát ---
btnThoat = tk.Button(root, text = "Thoát", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnThoat.place(x = 510, y = 420, width = 100, height = 30 )

root.mainloop()