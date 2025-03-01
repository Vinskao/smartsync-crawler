from flask import Flask
import os

def setup_environment():
    app = Flask(__name__)
    
    # 設定圖片儲存路徑
    app.config['IMAGE_FOLDER'] = os.path.join(os.path.dirname(__file__), '../data/raw/images')
    app.config['PROCESSED_IMAGE_FOLDER'] = os.path.join(os.path.dirname(__file__), '../data/processed/images')
    
    # 確保目錄存在
    os.makedirs(app.config['IMAGE_FOLDER'], exist_ok=True)
    os.makedirs(app.config['PROCESSED_IMAGE_FOLDER'], exist_ok=True)
    
    return app