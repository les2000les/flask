import requests

url = 'http://스프링부트_서버_주소/이미지_업로드_엔드포인트'

# 이미지 파일 경로
image_path = '/경로/이미지파일.jpg'

# 이미지 파일 열기
with open(image_path, 'rb') as file:
    # 파일을 FormData 형식으로 전송
    files = {'file': file}
    response = requests.post(url, files=files)

# 응답 확인
if response.status_code == 200:
    print('이미지 전송 성공')
else:
    print('이미지 전송 실패')
