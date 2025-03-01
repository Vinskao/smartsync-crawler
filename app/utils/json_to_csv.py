import csv
import json

def json_to_csv(json_path, csv_path):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # 定義 CSV 欄位
    fieldnames = [
        '代碼', '類型', '貨號', '名稱', '已發佈', '是特色商品？', '目錄的可見度', '簡短內容說明', '描述',
        '折扣價開始日期', '折扣價結束日期', '稅金狀態', '稅率類別', '有庫存？', '庫存', '低庫存量',
        '允許無庫存下單嗎？', '單獨銷售?', '重量 (公斤)', '長 (公分)', '寬 (公分)', '高 (公分)',
        '允許客戶評論嗎？', '購買備註', '特價', '原價', '分類', '標籤', '運送類別', '圖片',
        '下載限制', '下載點過期天數', '上層', '組合商品', '追加銷售', '交叉銷售', '外部網址',
        '按鈕文字', '位置', 'Blocksy Variation Images'
    ]
    
    # 寫入 CSV 檔案，w是寫入模式writer，f是檔案
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        # data 格式為 list of dicts，list資料結構，dict是key-value的資料結構
        for item in data:
            writer.writerow({
                '名稱': item['title'],
                '簡短內容說明': item['note'],
                '原價': item['price'],
                '特價': item['price_actual'],
                '描述': f"{item['intro_text']}\n\n{item['qa_text']}",
                '圖片': item['product_image'],
                '外部網址': item['videolink_text'],
                '購買備註': item['spec_image']
            })        
        
    