from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Khởi tạo trình duyệt (ở đây dùng Chrome)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Chạy ngầm (headless)
driver = webdriver.Chrome(options=options)

data = []

tickers_hose = ["FPT","PIT","HRC","PNC","PMG","ADG","UIC","DXV","PLX","MCH","SVD","SHB","TCB","MBB","HPG","VIC"]

for ticker in tickers_hose:
    retry = 5
    while retry > 0:
        try:

            driver.get(f"https://finance.vietstock.vn/{ticker}/ban-lanh-dao.htm")

            wait = WebDriverWait(driver, 30)

            # Lấy CSRF Token
            csrf_token = wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='__RequestVerificationToken']"))
            ).get_attribute("value")

            # Lấy thông tin người đứng đầu 
            first_row = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//table[@class='table m-b table-striped table-hover b-b']/tbody/tr[1]"))
            )

            name = first_row.find_element(By.XPATH, ".//td[2]").text  # Cột tên
            role = first_row.find_element(By.XPATH, ".//td[3]").text  # Cột chức vụ
            year_of_birth = first_row.find_element(By.XPATH, ".//td[4]").text  # Cột năm sinh
            year_of_appointment = first_row.find_element(By.XPATH, ".//td[7]").text  # Cột năm bổ nhiệm

            source = "vietstock"
            scraped_at = datetime.now().isoformat()

            print(f"ticker: {ticker}, exchange: HOSE, person_name: {name}, role: {role}, "
                f"year_of_birth: {year_of_birth}, year_of_appointment: {year_of_appointment}, "
                f"source: {source}, scraped at: {scraped_at}")
            print()

            data.append(
                {
                    'ticker':ticker,
                    'exchange': "HOSE",
                    'person_name': name,
                    'role': role,
                    'year_of_birth': year_of_birth,
                    'year_of_appointment': year_of_appointment,
                    'source': source,
                    'scraped_at': scraped_at
                }
            )

            break

        except Exception as e:
            retry -= 1
            print(f"{ticker} retry: {retry}")

print("Đã hoàn thành việc lấy dữ liệu cho các mã chứng khoán trên sàn HOSE.")
print("-----------------------------------------------------------------------------")
print()

#HNX
tickers_hnx = ["SHS","PVS","CEO","PVC","MST","MBS","IDC","TNG","LAS","HUT","HMH","HLC","NBC","TVD","ALT","TMB","THT","MEL"]  

for ticker in tickers_hnx:
    retry1 = 5
    while retry1 > 0:
        try:

            driver.get(f"https://finance.vietstock.vn/{ticker}/ban-lanh-dao.htm")

            wait = WebDriverWait(driver, 30)

            # Lấy CSRF Token
            csrf_token = wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='__RequestVerificationToken']"))
            ).get_attribute("value")

            # Lấy thông tin người đứng đầu 
            first_row = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//table[@class='table m-b table-striped table-hover b-b']/tbody/tr[1]"))
            )

            name = first_row.find_element(By.XPATH, ".//td[2]").text  # Cột tên
            role = first_row.find_element(By.XPATH, ".//td[3]").text  # Cột chức vụ
            year_of_birth = first_row.find_element(By.XPATH, ".//td[4]").text  # Cột năm sinh
            year_of_appointment = first_row.find_element(By.XPATH, ".//td[7]").text  # Cột năm bổ nhiệm

            source = "vietstock"
            scraped_at = datetime.now().isoformat()

            print(f"ticker: {ticker}, exchange: HNX, person_name: {name}, role: {role}, "
                f"year_of_birth: {year_of_birth}, year_of_appointment: {year_of_appointment}, "
                f"source: {source}, scraped at: {scraped_at}")
            print()

            data.append(
                {
                    'ticker':ticker,
                    'exchange': "HNX",
                    'person_name': name,
                    'role': role,
                    'year_of_birth': year_of_birth,
                    'year_of_appointment': year_of_appointment,
                    'source': source,
                    'scraped_at': scraped_at
                }
            )

            break

        except Exception as e:
            retry1 -= 1
            print(f"{ticker} retry: {retry1}")

print("Đã hoàn thành việc lấy dữ liệu cho các mã chứng khoán trên sàn HNX.")
print("-----------------------------------------------------------------------------")
print()

#upcom
tickers_upcom = ["A32", "AAH", "AAS", "ABB", "ABC", "ABI", "ABW", "ACE", "ACM", "ACS", "ACV", "AG1", "AGF", "AGM", "AGP", "AGX", "AIC", "AIG", "ALC", "ALV"]
for ticker in tickers_upcom:
    retry2 = 5
    while retry2 > 0:
        try:

            driver.get(f"https://finance.vietstock.vn/{ticker}/ban-lanh-dao.htm")

            wait = WebDriverWait(driver, 30)

            # Lấy CSRF Token
            csrf_token = wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='__RequestVerificationToken']"))
            ).get_attribute("value")

            # Lấy thông tin người đứng đầu 
            first_row = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//table[@class='table m-b table-striped table-hover b-b']/tbody/tr[1]"))
            )

            name = first_row.find_element(By.XPATH, ".//td[2]").text  # Cột tên
            role = first_row.find_element(By.XPATH, ".//td[3]").text  # Cột chức vụ
            year_of_birth = first_row.find_element(By.XPATH, ".//td[4]").text  # Cột năm sinh
            year_of_appointment = first_row.find_element(By.XPATH, ".//td[7]").text  # Cột năm bổ nhiệm

            source = "vietstock"
            scraped_at = datetime.now().isoformat()

            print(f"ticker: {ticker}, exchange: UPCom, person_name: {name}, role: {role}, "
                f"year_of_birth: {year_of_birth}, year_of_appointment: {year_of_appointment}, "
                f"source: {source}, scraped at: {scraped_at}")
            print()

            data.append(
                {
                    'ticker':ticker,
                    'exchange': "UPCom",
                    'person_name': name,
                    'role': role,
                    'year_of_birth': year_of_birth,
                    'year_of_appointment': year_of_appointment,
                    'source': source,
                    'scraped_at': scraped_at
                }
            )

            break

        except Exception as e:
            retry2 -= 1
            print(f"{ticker} retry: {retry2}")

print("Đã hoàn thành việc lấy dữ liệu cho các mã chứng khoán trên sàn upcom.")
print("-----------------------------------------------------------------------------")
print()

# Đóng trình duyệt
driver.quit()

df = pd.DataFrame(data)

df.to_parquet('stock_data_vietstock.parquet', engine = 'pyarrow', index = False)

df_read = pd.read_parquet('stock_data_vietstock.parquet')

print(df_read)