from flask import Flask, request
import pandas as pd
import pickle
import os

app = Flask(__name__)

@app.route('/receive-dataframe', methods=['POST'])
def receive_dataframe():
    # DataFrame 수신
    serialized_df = request.data

    # DataFrame 역직렬화
    df = pickle.loads(serialized_df)

    # DataFrame 처리 로직 수행
    # TODO: DataFrame 처리 로직을 구현하세요
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)  # output 폴더가 없으면 생성
    output_path = os.path.join(output_dir, 'output.csv')
    df.to_csv(output_path, index=False)

    return 'DataFrame received successfully'

if __name__ == '__main__':
    app.run(debug=True)
