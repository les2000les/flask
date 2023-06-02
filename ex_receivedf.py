from flask import Flask, request
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/receive-dataframe', methods=['POST'])
def receive_dataframe():
    # DataFrame 수신
    serialized_df = request.data

    # DataFrame 역직렬화
    df = pickle.loads(serialized_df)

    # DataFrame 처리 로직 수행
    # TODO: DataFrame 처리 로직을 구현하세요

    return 'DataFrame received successfully'

if __name__ == '__main__':
    app.run(debug=True)
