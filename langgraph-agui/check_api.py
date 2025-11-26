from dotenv import load_dotenv
import os

# .env ファイルを読み込む
load_dotenv()

# 環境変数を取得
api_key = os.getenv("OPENAI_API_KEY")
print(f"OPENAI_API_KEY: {api_key}")
