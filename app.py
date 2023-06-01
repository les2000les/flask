from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query1 = request.form.get('searchQuery1')
        search_query2 = request.form.get('searchQuery2')
        search_query3 = request.form.get('searchQuery3')

        # 여기에서 검색 결과를 처리하는 로직을 구현합니다.
        # 예를 들어, 검색 쿼리를 기반으로 데이터베이스에서 결과를 조회하거나 외부 API에 요청하여 결과를 가져올 수 있습니다.
        # 가져온 결과를 result 변수에 저장합니다.

        return render_template('result.html', search_query1=search_query1, search_query2=search_query2, search_query3=search_query3)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
