#####companyname, day, page를 받음
from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route('/app/users/1/search', methods=['POST'])
def search_handler():
    # POST 요청에서 JSON 데이터 추출
    json_data = request.json

    # JSON 데이터를 데이터프레임으로 변환
    df = pd.DataFrame.from_dict(json_data, orient='index', columns=['Value'])

    searchlist=[]
    for index, i in enumerate(df['Value']):
        searchlist.append(i)


    # 데이터프레임 출력
    print(searchlist)

    return df.to_json()

if __name__ == '__main__':
    app.run(host='localhost', port=3000)
