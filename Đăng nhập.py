import tkinter as tk

root = tk.Tk()
root.title("ĐĂNG NHẬP")
# Kích thước form
window_width = 300
window_height = 200

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

# ============================= Giao diện =============================
# ----------------------------- Log in -----------------------------
tk.Label(root, text = "LOG IN", font = ("Arial", 15, "bold"),
         bg = "#000000", fg = "#00B3FF").place(relx = 0.5, rely = 0.1, anchor = "center")
# ----------------------------- User -----------------------------
tk.Label(root, text = "Username", font = ("Arial", 12),
         bg = "#000000", fg = "#FFA200").place(relx = 0.025, rely = 0.27, anchor = "w")
entry_user = tk.Entry(root, font = ("Arial", 12), fg = "#000000")
entry_user.place(relx = 0.35, rely = 0.27, anchor = "w")

# ----------------------------- Pass -----------------------------
tk.Label(root, text = "Password", font = ("Arial", 12),
         bg = "#000000", fg = "#FFA200").place(relx = 0.025, rely = 0.47, anchor = "w")
entry_user = tk.Entry(root, font = ("Arial", 12), fg = "#000000")
entry_user.place(relx = 0.35, rely = 0.47, anchor = "w")
                      
# ============================= Chức năng (Đăng nhập) =============================
# --- Nút Đăng nhập ---
btnDangnhap = tk.Button(root, text = "Đăng nhập", font = ("Arial", 12),
                        bg = "#001f4d", fg = "white")
btnDangnhap.place(relx = 0.025, rely = 0.7, width = 90, anchor = "w")

# --- Nút Xoá ---
btnXoa = tk.Button(root, text = "Xoá", font = ("Arial", 12),
                        bg = "#001f4d", fg = "white")
btnXoa.place(relx = 0.5, rely = 0.7, width = 90, anchor = "center")

# --- Nút Thoát ---
btnXoa = tk.Button(root, text = "Thoát", font = ("Arial", 12),
                        bg = "#001f4d", fg = "white")
btnXoa.place(relx = 0.975, rely = 0.7, width = 90, anchor = "e")

root.mainloop()