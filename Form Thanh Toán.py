import tkinter as tk
from tkinter import ttk , messagebox    #Dùng combobox, messagebox
from tkcalendar import DateEntry        # Dùng DateEntry
import pyodbc           # Kết nối Database

root = tk.Tk()
root.title("ĐẶT PHÒNG")
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
    
    # ----------------------------- Load Chi tiết dịch vụ -----------------------------
def Load_Database_CTDV():
    conn = Connect_Database()
    if conn is None:
        return
    
    cursor = conn.cursor()
    cursor.execute('''SELECT MaCTDV, MaDatPhong, MaDV, SoLuong 
                      FROM ChiTietDichVu ct
                      JOIN DatPhong dp ON ct.MaDatPhong = dp.MaDatPhong
                      WHERE ct.MaDatPhong = @MaDatPhong
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
# ----------------------------- Tên form Thanh toán -----------------------------
title_label = tk.Label(root, text = "THANH TOÁN", 
                       font = ("Arial", 20, "bold"), 
                       fg = "#FFAA78", 
                       bg = "Black")
title_label.place(x = 450, y = 5, anchor = "n", width = 700, height = 40)
# ----------------------------- Thông tin Thanh toán (Chứa trong Frame) -----------------------------
group_thongtin = tk.LabelFrame(root, text = "Thông tin thanh toán", font = ("Arial", 10),
                    bg = "#000000",
                    fg = "#0DFF00")
group_thongtin.place(relx = 0.005, rely = 0.22, anchor = "w", width = 570, height = 150)

        # --- Mã đặt phòng ---
tk.Label(group_thongtin, text = "Mã đặt phòng", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 5)
entry_madp = tk.Entry(group_thongtin, state = "disabled",
                      font = ("Arial", 10))
entry_madp.place(x = 120, y = 5, width = 160, height = 20)

        # --- Mã phòng ---
tk.Label(group_thongtin, text = "Mã phòng", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 35)
entry_maphong = tk.Entry(group_thongtin,
                      font = ("Arial", 10))
entry_maphong.place(x = 120, y = 35, width = 160, height = 20)

        # --- Mã khách hàng ---
tk.Label(group_thongtin, text = "Mã khách hàng",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 65)
entry_makh = tk.Entry(group_thongtin, font = ("Arial", 10))
entry_makh.place(x = 120, y = 65, width = 160, height = 20)

        # --- Họ tên nhân viên ---
tk.Label(group_thongtin, text = "Tên khách hàng",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 95)
entry_tenkh = tk.Entry(group_thongtin, font = ("Arial", 10))
entry_tenkh.place(x = 120, y = 95, width = 160, height = 20)

tk.Label(group_thongtin, text = "Loại phòng",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 310, y = 5)
entry_loaiphong = tk.Entry(group_thongtin, font = ("Arial", 10))
entry_loaiphong.place(x = 380, y = 5, width = 160, height = 20)

tk.Label(group_thongtin, text = "Tiền phòng",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 310, y = 35)
entry_loaiphong = tk.Entry(group_thongtin, font = ("Arial", 10))
entry_loaiphong.place(x = 380, y = 35, width = 160, height = 20)

        # --- Ngày nhận ---
tk.Label(group_thongtin, text = "Ngày nhận",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 310, y = 65)
ngaynhan = DateEntry(group_thongtin, date_pattern = "dd/mm/yyyy")
ngaynhan.place(x = 380, y = 65, width = 160, height = 20)

        # --- Ngày trả ---
tk.Label(group_thongtin, text = "Ngày trả",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 310, y = 95)
ngaytra = DateEntry(group_thongtin, date_pattern = "dd/mm/yyyy")
ngaytra.place(x = 380, y = 95, width = 160, height = 20)

# ----------------------------- Phương thức thanh toán (Chuyển khoản or tiền mặt) -----------------------------
group_phuongthuc = tk.LabelFrame(root, text = "Phương thức thanh toán",  font = ("Arial", 10),
                    bg = "#000000",
                    fg = "#0DFF00")
group_phuongthuc.place(x = 5, y = 220, width = 200, height = 100)
        # --- Lựa chọn chuyển khoản / tiền mặt ---
selected_option = tk.StringVar()
rdbtienmat = tk.Radiobutton(group_phuongthuc, text = "Tiền mặt", variable = selected_option, value = "Tiền mặt", 
                        font = ("Arial", 10), fg = "#FCBD00", bg = "#000000")
rdbchuyenkhoan = tk.Radiobutton(group_phuongthuc, text = "Chuyển khoản", variable = selected_option, value = "Chuyển khoản", 
                        font = ("Arial", 10), fg = "#FCBD00", bg = "#000000")
rdbtienmat.grid(column = 0, row = 0, sticky = "w")
rdbchuyenkhoan.grid(column = 0, row = 1, sticky = "w")

btnChon = btnThem = tk.Button(group_phuongthuc, text = "Chọn", font = ("Arial", 12),
                    fg = "#000000",
                    bg = "#0DFF00")
btnChon.place(x = 120, y = 7, width =70, height = 40)

# ----------------------------- Chi phí -----------------------------
group_chiphi = tk.LabelFrame(root, text = "Thông tin chi phí",  font = ("Arial", 10),
                    bg = "#000000",
                    fg = "#0DFF00")
group_chiphi.place(x = 250, y = 220, width = 325, height = 120)

        # --- Tổng tiền phòng ---
tk.Label(group_chiphi, text = "Tổng tiền phòng", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 10, y = 5)
entry_tongtienphong = tk.Entry(group_chiphi,
                      font = ("Arial", 10))
entry_tongtienphong.place(x = 120, y = 5, width = 160, height = 20)

        # --- Tổng tiền dịch vụ ---
tk.Label(group_chiphi, text = "Tổng tiền dịch vụ", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 10, y = 35)
entry_tongtiendv = tk.Entry(group_chiphi,
                      font = ("Arial", 10))
entry_tongtiendv.place(x = 120, y = 35, width = 160, height = 20)

        # --- Thành tiền ---
tk.Label(group_chiphi, text = "Thành tiền", 
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 10, y = 65)
entry_thanhtien = tk.Entry(group_chiphi,
                      font = ("Arial", 10))
entry_thanhtien.place(x = 120, y = 65, width = 160, height = 20)

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
        # --- Thanh toán ---
btnThanhtoan = tk.Button(root, text = "Thanh toán", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnThanhtoan.place(x = 580, y = 70, width = 120, height = 30 )

        # --- Đã thanh toán ---
btnDathanhtoan = tk.Button(root, text = "Đã thanh toán", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnDathanhtoan.place(x = 580, y = 110, width = 120, height = 30)

        # --- Thoát ---
btnThoat = tk.Button(root, text = "Thoát", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnThoat.place(x =580, y = 150, width = 120, height = 30 )



root.mainloop()