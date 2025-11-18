import tkinter as tk
from tkinter import ttk , messagebox    #Dùng combobox, messagebox
from PIL import Image, ImageTk      #Chèn hình ảnh

root = tk.Tk()
root.title("TRANG CHỦ _ ADMIN")
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


# ============================= Chèn background =============================
hinhnen = Image.open("E:\Hình ảnh khách sạn_DotNet\Ảnh-trang-chủ.png")
size_nen = hinhnen.resize((900, 600))  # Bằng với kích thước form
hinhnen_photo = ImageTk.PhotoImage(size_nen)

bg_label = tk.Label(root, image=hinhnen_photo)
bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# =================== Tạo Frame chứa các thông tin (Nút Sign in, Combobox, Nút xem) ===================
top_frame = tk.Frame(root, bg = "#001f4d")  # màu xanh đậm nền cho header
top_frame.place(x = 0, y = 0, width = 900, height = 50)

# Icon user
icon_user = Image.open("E:\Hình ảnh khách sạn_DotNet\Icon Sign in.png")
size_icon = icon_user.resize((50, 30))
icon_photo = ImageTk.PhotoImage(size_icon)

user_icon = tk.Label(top_frame, image = icon_photo, bg = "#001f4d", fg = "white")
user_icon.place(x = 10, y = 5, width = 40, height = 40)

# Label Admin để phân biệt form admin vs form nhân viên
tk.Label(top_frame, text = "Bạn đang là Admin", font = ("Arial", 10),
        bg = "#001f4d", fg = "#FF0000").place(relx = 0.5, rely = 0.5, anchor = "center")

# Nút SIGN OUT
btnsign_out = tk.Button(top_frame, text = "SIGN OUT", bg = "blue", fg = "white", font = ("Arial", 12, "bold"))
btnsign_out.place(x = 60, y = 12, width = 100, height = 30)

# Combobox Lựa chọn
combo_values = ["Quản lý phòng", "Quản lý nhân sự", "Quản lý khách hàng", "Quản lý dịch vụ", "Cập nhật nhân sự"]
combo = ttk.Combobox(top_frame,text = " ", values=combo_values, state = "readonly", font = ("Arial", 12))
combo.place(x = 610, y = 12, width = 200, height = 30)

# Nút Xem góc phải
btn_xem = tk.Button(top_frame, text="Xem", bg="blue", fg="white", font=("Arial", 12, "bold"))
btn_xem.place(x = 820, y = 12, width = 70, height = 30)

# --- Tên khách sạn ---
tk.Label(root, text="ONE THOUSAND AND ONE NIGHTS HOTEL", font=("Segoe Script", 20, "italic"),
        fg="yellow", bg="#001f4d").place(relx=0.5, y=60, anchor="n", width=700, height=40)

root.mainloop()