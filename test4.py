import pandas as pd

# Dữ liệu mẫu
data = [
    {'ticker': 'FPT', 'exchange': 'HOSE', 'person_name': 'Nguyễn Văn Quang', 'role': 'Chủ tịch HĐQT', 'source': 'cafef', 'scraped_at': '2026-03-04T12:00:00'},
    {'ticker': 'PIT', 'exchange': 'HOSE', 'person_name': 'Nguyễn Tuấn Quỳnh', 'role': 'Chủ tịch HĐQT', 'source': 'cafef', 'scraped_at': '2026-03-04T12:10:00'},
    {'ticker': 'HRC', 'exchange': 'HOSE', 'person_name': 'Lê Thanh Bình', 'role': 'Giám đốc điều hành', 'source': 'cafef', 'scraped_at': '2026-03-04T12:20:00'}
]

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Chuyển tất cả các cột thành string, ngoại trừ cột scraped_at

# Lưu vào file Parquet (dùng pyarrow hoặc fastparquet)
df.to_parquet('stock_data.parquet', engine='pyarrow', index=False)

# Đọc lại dữ liệu từ file Parquet
df_read = pd.read_parquet('stock_data.parquet')

# In ra dữ liệu để kiểm tra
print(df_read)