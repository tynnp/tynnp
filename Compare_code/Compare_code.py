import tkinter as tk
from tkinter import filedialog, messagebox
from difflib import SequenceMatcher
from tkinter import scrolledtext

# Bỏ các dòng trống và khoảng trắng trong file code
def filter_code_lines(lines):
    return [line.strip() for line in lines if line.strip()]

# Hàm đọc nội dung file 
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

# Tính toán độ tương đồng 
def calculate_similarity(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()

# So sánh nội dung hai file, trả về tỉ lệ tương đồng
def compare_files(file1_lines, file2_lines):
    filtered_file1 = filter_code_lines(file1_lines)
    filtered_file2 = filter_code_lines(file2_lines)
    similarity_ratio = calculate_similarity("\n".join(filtered_file1), "\n".join(filtered_file2))
    return similarity_ratio

# Hàm mở hộp thoại chọn file 
def open_file():
    file_path = filedialog.askopenfilename(title="Chọn file", filetypes=(("Code files", "*.py;*.cpp;*.txt"), ("All files", "*.*")))
    return file_path

# Hàm tô màu các đoạn code giống nhau 
def color_code(file_text, file1_lines, file2_lines):
    file_text.delete(1.0, tk.END) 
    matcher = SequenceMatcher(None, file1_lines, file2_lines)
    
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        text1 = ''.join(file1_lines[i1:i2])
        
        if tag == "equal":  
            file_text.insert(tk.END, text1, "match")
        else:
            file_text.insert(tk.END, text1)

def compare_code():
    file1_path = open_file()
    file2_path = open_file()

    if not file1_path or not file2_path:
        messagebox.showwarning("Cảnh báo", "Bạn chưa chọn đủ 2 file.")
        return

    file1_lines = read_file(file1_path)
    file2_lines = read_file(file2_path)
    similarity_ratio = compare_files(file1_lines, file2_lines)

    color_code(file1_text, file1_lines, file2_lines)
    color_code(file2_text, file2_lines, file1_lines)

    # Hiển thị tỉ lệ tương đồng
    similarity_percentage = similarity_ratio * 100
    similarity_text = f"Độ tương đồng: "
    percentage_text = f"{similarity_percentage:.2f}%"

    result_label.config(text=similarity_text, fg="black", font=("Arial", 12, "bold"))
    percentage_label.config(text=percentage_text, font=("Arial", 12, "bold"))

    # Đổi màu tỉ lệ tương đồng dựa trên ngưỡng 70%
    if similarity_percentage >= 70:
        percentage_label.config(fg="red")
    else:
        percentage_label.config(fg="green")

root = tk.Tk()
root.title("So sánh code")
root.geometry("1200x700")

top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, pady=10)

compare_button = tk.Button(top_frame, text="Chọn 2 file và so sánh", command=compare_code, height=2, width=20)
compare_button.pack(pady=10)

result_frame = tk.Frame(top_frame)
result_frame.pack(pady=5)

result_label = tk.Label(result_frame, text="Độ tương đồng: ", font=("Arial", 12, "bold"), fg="black")
result_label.pack(side=tk.LEFT)

percentage_label = tk.Label(result_frame, text="", font=("Arial", 12))
percentage_label.pack(side=tk.LEFT)

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

left_frame = tk.Frame(main_frame)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

left_label = tk.Label(left_frame, text="File 1", font=("Arial", 12))
left_label.pack()

file1_scroll = tk.Scrollbar(left_frame, orient=tk.HORIZONTAL)
file1_scroll.pack(side=tk.BOTTOM, fill=tk.X)

file1_text = scrolledtext.ScrolledText(left_frame, height=20, width=50, xscrollcommand=file1_scroll.set, wrap=tk.NONE)
file1_text.pack(fill=tk.BOTH, expand=True)

file1_scroll.config(command=file1_text.xview)

right_frame = tk.Frame(main_frame)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

right_label = tk.Label(right_frame, text="File 2", font=("Arial", 12))
right_label.pack()

file2_scroll = tk.Scrollbar(right_frame, orient=tk.HORIZONTAL)
file2_scroll.pack(side=tk.BOTTOM, fill=tk.X)

file2_text = scrolledtext.ScrolledText(right_frame, height=20, width=50, xscrollcommand=file2_scroll.set, wrap=tk.NONE)
file2_text.pack(fill=tk.BOTH, expand=True)

file2_scroll.config(command=file2_text.xview)

file1_text.tag_configure("match", foreground="red")
file2_text.tag_configure("match", foreground="red")

root.mainloop()
