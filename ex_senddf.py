import pandas as pd
import pickle
import requests

# 전송할 DataFrame 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)

# DataFrame 직렬화
serialized_df = pickle.dumps(df)

# DataFrame 전송
response = requests.post('http://localhost:9999/receive-dataframe', data=serialized_df)
print(response.text)
