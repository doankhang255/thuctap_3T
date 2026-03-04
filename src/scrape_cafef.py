from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Khởi tạo trình duyệt
options = webdriver.ChromeOptions()
options.add_argument('--headless') # Bỏ dấu # ở đầu dòng này nếu muốn chạy ngầm
driver = webdriver.Chrome(options=options)

data = []

tickers_hose = ["FPT","PIT","HRC","PNC","PMG","ADG","UIC","DXV","PLX","MCH","SVD","SHB","TCB","MBB","HPG","VIC"]

for ticker in tickers_hose:
    retry = 5
    while retry > 0:
        try:
            url = f'https://cafef.vn/du-lieu/hose/{ticker}-ban-lanh-dao-so-huu.chn'
            driver.get(url)

            wait = WebDriverWait(driver, 30)

            name_element = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "directorandonwer_name-top"))
            )
            role_element = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "directorandonwer_position-top"))
            )
            exchange = "HOSE"
            source = "cafef"
            scraped_at = datetime.now().isoformat()
            print(f"ticker: {ticker}, exchange: {exchange}, person_name: {name_element.text}, role: {role_element.text}, source: {source}, scraped at: {scraped_at}")
            print()
            data.append(
                {
                    'ticker':ticker,
                    'exchange':exchange,
                    'person_name': name_element.text,
                    'role':role_element.text,
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
            url = f'https://cafef.vn/du-lieu/hnx/{ticker}-ban-lanh-dao-so-huu.chn'
            driver.get(url)
                
            wait = WebDriverWait(driver, 30)

            name_element = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "directorandonwer_name-top"))
            )
            role_element = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "directorandonwer_position-top"))
            )
            exchange = "HNX"
            source = "cafef"
            scraped_at = datetime.now().isoformat()
            print(f"ticker: {ticker}, exchange: {exchange}, name: {name_element.text}, role: {role_element.text}, source: {source}, scraped at: {scraped_at}")
            print() 
            data.append(
                {
                    'ticker':ticker,
                    'exchange':exchange,
                    'person_name': name_element.text,
                    'role':role_element.text,
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

#UPCOM
tickers_upcom = ["AAS","ABW","ART","BMS","CSI","PHS","SBS","VUA"]

for ticker in tickers_upcom:
    retry2 = 5 
    while retry2 > 0:
        try:
            url = f'https://cafef.vn/du-lieu/upcom/{ticker}-ban-lanh-dao-so-huu.chn'
            driver.get(url)
                
            wait = WebDriverWait(driver, 30)

            name_element = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "directorandonwer_name-top"))
            )
            role_element = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "directorandonwer_position-top"))
            )
            exchange = "UPCOM"
            source = "cafef"
            scraped_at = datetime.now().isoformat()
            print(f"ticker: {ticker}, exchange: {exchange}, name: {name_element.text}, role: {role_element.text}, source: {source}, scraped at: {scraped_at}")
            print() 
            data.append(
                {
                    'ticker':ticker,
                    'exchange':exchange,
                    'person_name': name_element.text,
                    'role':role_element.text,
                    'source': source,
                    'scraped_at': scraped_at
                }
            )

            break

        except Exception as e:
            retry2 -= 1
            print(f"{ticker} retry: {retry2}")

print("Đã hoàn thành việc lấy dữ liệu cho các mã chứng khoán trên sàn UPCom.")
print("-----------------------------------------------------------------------------")
print()

driver.quit()

df = pd.DataFrame(data)

df.to_parquet('stock_data_cafef.parquet', engine = 'pyarrow', index = False)

df_read = pd.read_parquet('stock_data_cafef.parquet')

print(df_read)