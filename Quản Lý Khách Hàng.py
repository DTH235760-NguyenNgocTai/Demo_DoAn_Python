import tkinter as tk
from tkinter import ttk , messagebox    #Dùng combobox, messagebox
from tkcalendar import DateEntry
import pyodbc           # Kết nối Database

root = tk.Tk()
root.title("QUẢN LÝ KHÁCH HÀNG")
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
                r"SERVER=(localdb)\MSSQLLocalDB;"
                r"DATABASE=Quan_Ly_Khach_San_Python;"
                r"Trusted_Connection=yes;"                         
        )
        return conn
    except Exception as e:
        messagebox.showerror("Lỗi kết nối", f"Không thể kết nối CSDL:\n{e}")
        return None

# ----------------------------- Load CSDL -----------------------------
def Load_Database_KhachHang():
    conn = Connect_Database()
    if conn is None:
        return
    
    cursor = conn.cursor()
    cursor.execute('''SELECT MaKH, TenKH, CCCD, GioiTinh, SoDienThoai, QuocTich
                      FROM KhachHang
                   ''')
    rows = cursor.fetchall()

    # Xóa dữ liệu cũ
    for i in khachhang.get_children():
        khachhang.delete(i)

    # Thêm dữ liệu mới
    for row in rows:
        khachhang.insert("", tk.END, values=row)

    conn.close()    
  
# ============================= Giao diện =============================  
# ----------------------------- Tên form Quản lý khách hàng -----------------------------
title_label = tk.Label(root, text="QUẢN LÝ KHÁCH HÀNG", 
                       font = ("Arial", 20, "bold"), 
                       fg="#FFAA78", 
                       bg = "Black")
title_label.place(x = 450, y = 5, anchor = "n", width = 700, height = 40)

# ----------------------------- Thông tin Khách hàng (Chứa trong Frame) -----------------------------
group = tk.LabelFrame(root, text = "Thông tin khách hàng", font = ("Arial", 10),
                      fg = "#0DFF00",
                      bg = "#000000")
group.place(relx = 0.005, rely = 0.22, anchor = "w", width = 560, height = 140)

        # --- Mã nhân viên ---
tk.Label(group, text = "Mã khách hàng",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 5)
entry_makh = tk.Entry(group, font = ("Arial", 10))
entry_makh.place(x = 115, y = 5, width = 160, height = 20)

        # --- Họ tên nhân viên ---
tk.Label(group, text = "Họ tên",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 35)
entry_tenkh = tk.Entry(group, font = ("Arial", 10))
entry_tenkh.place(x = 115, y = 35, width = 160, height = 20)

        # --- CCCD ---
tk.Label(group, text = "CCCD",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 20, y = 65)
entry_cccd = tk.Entry(group, font = ("Arial", 10))
entry_cccd.place(x = 115, y = 65, width = 160, height = 20)

        # --- Giới tính khách hàng ---
tk.Label(group, text = "Giới tính",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 300, y = 5)
selected_option = tk.StringVar()
rdbNam = tk.Radiobutton(group, text = "Nam", variable = selected_option, value = "Nam", 
                        font = ("Arial", 10), fg = "#FCBD00", bg = "#000000")
rdbNu = tk.Radiobutton(group, text = "Nữ", variable = selected_option, value = "Nữ", 
                        font = ("Arial", 10), fg = "#FCBD00", bg = "#000000")
rdbNam.place(x = 370, y = 5)
rdbNu.place(x = 440, y = 5)

        # --- Số điện thoại khách hàng ---
tk.Label(group, text = "SĐT",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 300, y = 35)
entry_sdt = tk.Entry(group, font = ("Arial", 10))
entry_sdt.place(x = 370, y = 35, width = 160, height = 20)

        # --- Quốc tịch ---
tk.Label(group, text = "Quốc tịch",
        font = ("Arial", 10),
        fg = "#FCBD00",
        bg = "#000000").place(x = 300, y = 65)
entry_quoctich = tk.Entry(group, font = ("Arial", 10))
entry_quoctich.place(x = 370, y = 65, width = 160, height = 20)

# ----------------------------- Bảng phòng -----------------------------
frame_table = tk.Frame(root, bg="black")
frame_table.place(x=10, y=220, width=880, height=250)

# Tạo Treeview
khachhang = ttk.Treeview(
        frame_table,
        columns=("MaKH", "TenKH", "CCCD", "GioiTinh", "SoDienThoai", "QuocTich"),
        show="headings")

# Tạo Scrollbar dọc
scroll_y = tk.Scrollbar(frame_table, orient="vertical", command=khachhang.yview)
khachhang.configure(yscrollcommand=scroll_y.set)

# Tạo Scrollbar ngang
scroll_x = tk.Scrollbar(frame_table, orient="horizontal", command=khachhang.xview)
khachhang.configure(xscrollcommand=scroll_x.set)

# Hiển thị Scrollbar
scroll_y.pack(side="right", fill="y")
scroll_x.pack(side="bottom", fill="x")

# Hiển thị Treeview rộng hết cả frame chứa và thay đổi theo kích thước frame
khachhang.pack(fill="both", expand=True)

# Khai báo các cột
khachhang.heading("MaKH", text = "Mã khách hàng")
khachhang.heading("TenKH", text = "Tên khách hàng")
khachhang.heading("CCCD", text = "CCCD")
khachhang.heading("GioiTinh", text = "Giới tính")
khachhang.heading("SoDienThoai", text = "Số điện thoại")
khachhang.heading("QuocTich", text = "Quốc tịch")

khachhang.column("MaKH", width = 100)
khachhang.column("TenKH", width = 210)
khachhang.column("CCCD", width = 140)
khachhang.column("GioiTinh", width = 70)
khachhang.column("SoDienThoai", width = 140)
khachhang.column("QuocTich", width = 200)
# Thêm dữ liệu vào bảng
Load_Database_KhachHang()

# ============================= Chức năng (Thêm Xoá Sửa ...) =============================
        # --- Thêm ---
btnThem = tk.Button(root, text = "Thêm", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnThem.place(x = 580, y = 70, width = 90, height = 30 )

        # --- Xoá ---
btnXoa = tk.Button(root, text = "Xoá", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnXoa.place(x = 680, y = 70, width = 90, height = 30)

        # --- Sửa ---
btnSua = tk.Button(root, text = "Sửa", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnSua.place(x =780, y = 70, width = 90, height = 30 )

        # --- Huỷ ---
btnHuy = tk.Button(root, text = "Huỷ", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnHuy.place(x = 580, y = 110, width = 90, height = 30 )

        # --- Lưu ---
btnLuu = tk.Button(root, text = "Lưu", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnLuu.place(x = 680, y = 110, width = 90, height = 30)

        # --- Thoát ---
btnThoat = tk.Button(root, text = "Thoát", font = ("Arial", 12),
                    fg = "white",
                    bg = "#001f4d")
btnThoat.place(x =780, y = 110, width = 90, height = 30 )




root.mainloop()