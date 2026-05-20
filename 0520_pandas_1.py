import pandas as pd

# 1. 先用 list 建立 stock1 (Pandas 會自動將 None 轉為 float 類型的 NaN)
stock1 = pd.Series([120, 80, None, 60, 95, None, 110])

# 2. 加入索引建立 stock2
index_labels = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Peach', 'Melon']
stock2 = pd.Series([120, 80, None, 60, 95, None, 110], index=index_labels)

# 3. 將 stock2 轉為字典 stock3
stock3 = stock2.to_dict()

# --- 開始輸出結果 (嚴格符合範例格式) ---

print("stock1")
print(stock1)
print() # 空一行

print("stock2")
print(stock2)
print() # 空一行

print("stock3")
print(stock3)
print() # 空一行

# 輸出 Banana 的庫存值
print(f"Banana 庫存： {stock2['Banana']}")
print() # 空一行

# 計算與檢查缺失值
print("缺失值檢查：")
missing_check = stock2.isna()
print(missing_check)
print() # 空一行

print(f"缺失值數量： {missing_check.sum()}")

# 4. 把 stock2 存檔為 0520_stock.csv
stock2.to_csv('0520_stock.csv', header=False)