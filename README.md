# AI Pioneer - Tasks 4 to 7

Repository lưu trữ các bài tập thực hành từ Task 4 đến Task 7 trong lộ trình học **AI Pioneer**, bao gồm nền tảng Python, thiết lập môi trường, tính toán mảng đa chiều với NumPy và làm sạch, khai phá dữ liệu với Pandas.

---

## Completed Tasks

- **Task 4 - Python Basics for AI:** Nền tảng lập trình Python (biến, kiểu dữ liệu, vòng lặp, hàm, xử lý ngoại lệ, đọc/ghi file text và CSV).
- **Task 5 - Python Environment Setup:** Thiết lập môi trường ảo (`venv`), quản lý dependency với `pip` và cấu hình Jupyter Kernel.
- **Task 6 - NumPy Multidimensional Arrays:** Thao tác mảng đa chiều (1D, 2D, 3D), indexing, slicing, phép toán ma trận, cơ chế Axis, Broadcasting, Vectorization và Mini Project chuẩn hóa dữ liệu Z-score.
- **Task 7 - Data Cleaning and EDA with Pandas:** Làm việc với DataFrame & Series, xử lý missing values (NaN), lọc điều kiện, `groupby` kết hợp `agg`, và Mini Project EDA hoàn chỉnh trên dataset Titanic.

---

## Environment & Tech Stack

- **Python:** 3.11+
- **NumPy:** 2.4+
- **Pandas:** 3.0+
- **Matplotlib:** 3.11+
- **Scikit-learn:** 1.9+
- **Jupyter Notebook / ipykernel**

---

## Project Structure

```text
├── task4_python/             # Task 4: Python cơ bản cho AI
│   ├── student.csv           # Dữ liệu CSV mẫu
│   ├── result.txt            # Kết quả đọc/ghi file text
│   ├── task4.py              # Script thực hành chính Task 4
│   └── test.py               # Script test try/except
├── task5_environment/        # Task 5: Kiểm tra môi trường
│   ├── test_environment.py   # Script kiểm tra version các thư viện
│   └── task5_test.ipynb      # Notebook kiểm tra kernel Jupyter
├── task6_numpy/              # Task 6: Thao tác mảng với NumPy
│   └── task6_numpy.ipynb     # Notebook lý thuyết, bài tập & mini project
├── task7_pandas/             # Task 7: Làm sạch & EDA với Pandas
│   ├── data/
│   │   └── titanic.csv       # Dataset Titanic
│   └── task7_pandas.ipynb    # Notebook lý thuyết, bài tập & mini EDA Titanic
├── .gitignore                # File cấu hình bỏ qua file rác khi commit Git
├── requirements.txt          # Danh sách dependency của dự án
└── README.md                 # Tài liệu giới thiệu dự án
```

---

## Installation & Setup

1. **Clone repository về máy:**
   ```bash
   git clone <URL_REPOSITORY_CỦA_BẠN>
   cd "Al pioneer"
   ```

2. **Tạo và kích hoạt môi trường ảo Python:**
   - Trên Windows:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - Trên Linux / macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Cài đặt các thư viện cần thiết:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Chạy các bài thực hành:**
   - Chạy script Python:
     ```bash
     python task4_python/task4.py
     python task5_environment/test_environment.py
     ```
   - Mở Jupyter Notebook để xem Task 6 & 7:
     ```bash
     jupyter notebook
     ```
     *(Chọn kernel là `.venv` khi chạy notebook)*
