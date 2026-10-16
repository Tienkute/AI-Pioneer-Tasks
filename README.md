# AI Pioneer – Tasks 4–7

Repo này lưu lại phần mình thực hành từ Task 4 đến Task 7 trong hoạt động AI Pioneer của CLB. Nội dung đi từ Python cơ bản, thiết lập môi trường, NumPy đến xử lý dữ liệu bằng Pandas.

---

## Task 4 – Python cơ bản

- Ôn lại variables, data types, if/else, loop, list, tuple, dictionary, function, exception.
- Thực hành đọc/ghi file TXT và CSV.
- Với `student.csv`, đọc dữ liệu thành list dictionary, tính điểm trung bình, tìm sinh viên điểm cao nhất và đếm số sinh viên có score >= 8.

Phần mình thấy hữu ích nhất ở task này là ghép các kiến thức Python cơ bản lại để xử lý một file CSV hoàn chỉnh.

---

## Task 5 – Python Environment

- Tạo virtual environment.
- Cài NumPy, Pandas, Matplotlib, scikit-learn.
- Kiểm tra environment và Jupyter kernel.
- Xuất requirements.txt.

Trước task này mình thường cài thư viện trực tiếp, nên phần virtual environment giúp mình hiểu rõ hơn cách tách dependencies giữa các project.

---

## Task 6 – NumPy

- Array 1D / 2D / 3D
- shape, ndim, size, dtype
- indexing, slicing, reshape
- mean, std, min, max
- dot product
- broadcasting
- random
- vectorization

Điểm mình chú ý nhất là vectorization, vì NumPy có thể xử lý cả mảng thay vì phải loop từng phần tử.

---

## Task 7 – Pandas

- Đọc Titanic CSV thành DataFrame.
- Xem .shape, .info(), .describe(), .value_counts().
- Xử lý missing values.
- Filter, sort, groupby, agg.
- Làm mini EDA.

Kết quả thực hành:
- Titanic: 891 rows × 12 columns
- Age missing: 177 → fill median
- Embarked missing: 2 → fill mode
- Cabin missing: 687 → drop
- Duplicate rows: 0
- Survival rate: 38.38%
- Female survival: 74.20%
- Male survival: 18.89%

Task này dễ hình dung nhất với mình vì được làm trực tiếp trên một dataset thực và nhìn được kết quả sau khi làm sạch, groupby và thống kê.

---

## Cấu trúc thư mục

```text
├── task4_python/             # Script ôn tập Python và đọc/ghi file student.csv
│   ├── student.csv
│   ├── result.txt
│   ├── task4.py
│   └── test.py
├── task5_environment/        # Kiểm tra virtual environment và Jupyter kernel
│   ├── test_environment.py
│   └── task5_test.ipynb
├── task6_numpy/              # Notebook thực hành mảng NumPy và mini project
│   └── task6_numpy.ipynb
├── task7_pandas/             # Notebook làm sạch & EDA dữ liệu Titanic
│   ├── data/
│   │   └── titanic.csv
│   └── task7_pandas.ipynb
├── requirements.txt
└── README.md
```

## Cách chạy

1. Kích hoạt môi trường ảo:
   - Windows: `.\.venv\Scripts\Activate.ps1`
   - Linux/macOS: `source .venv/bin/activate`
2. Cài dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Chạy script Task 4 & 5:
   ```bash
   python task4_python/task4.py
   python task5_environment/test_environment.py
   ```
4. Mở Jupyter Notebook cho Task 6 & 7:
   ```bash
   jupyter notebook
   ```

---

Sau Task 4–7, mình đã quen hơn với workflow cơ bản: viết Python → tạo môi trường → xử lý mảng bằng NumPy → xử lý dataset bằng Pandas. Phần tiếp theo mình sẽ học preprocessing và Machine Learning.
