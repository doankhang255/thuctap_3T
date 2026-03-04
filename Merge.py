import pandas as pd
import unidecode

# Bước 1: Đọc dữ liệu từ các file Parquet của CafeF và Vietstock
df_cafef = pd.read_parquet('stock_data_vietstock.parquet')
df_vietstock = pd.read_parquet('stock_data_cafef.parquet')

# Bước 2: Tiền xử lý tên người (bỏ dấu, viết tắt)
def preprocess_name(name):
    # Chuyển sang không dấu
    name = unidecode.unidecode(name)
    # Xử lý danh hiệu (Ông, Bà)
    name = name.replace("Ông", "Ong").replace("Bà", "Ba")
    # Loại bỏ khoảng trắng thừa
    name = name.strip().replace(" ", "")
    return name

df_cafef['person_name_processed'] = df_cafef['person_name'].apply(preprocess_name)
df_vietstock['person_name_processed'] = df_vietstock['person_name'].apply(preprocess_name)

# Bước 3: Merge dữ liệu từ CafeF và Vietstock
df_merged = pd.merge(df_cafef, df_vietstock, on=['ticker', 'person_name_processed'], how='outer', suffixes=('_cafef', '_vietstock'))

# Bước 4: Lựa chọn giá trị tốt nhất giữa các cột
def select_best_value(row, column):
    cafef_value = row[f"{column}_cafef"]
    vietstock_value = row[f"{column}_vietstock"]
    
    if pd.notnull(vietstock_value):  # Ưu tiên Vietstock nếu có dữ liệu
        return vietstock_value
    else:
        return cafef_value


