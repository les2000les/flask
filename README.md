# flask

Flask를 사용하여 REST API를 개발

라우팅: Flask는 @app.route() 데코레이터를 사용하여 URL 경로와 HTTP 메서드에 따른 핸들러 함수를 정의. 예를 들어, @app.route('/users', methods=['GET'])는 /users 경로로 GET 요청이 들어왔을 때 실행할 핸들러 함수를 정의.

요청 처리: Flask는 request 객체를 통해 클라이언트로부터 전송된 요청 데이터에 접근 가능. request 객체를 사용하여 파라미터, 헤더, 바디 등의 요청 데이터를 추출 가능.

응답 생성: Flask는 Response 객체를 통해 응답을 생성. Response 객체는 JSON, XML, 텍스트, 파일 등 다양한 형식의 응답을 생성할 수 있습니다. 일반적으로 JSON 형식을 사용하여 API 응답을 생성.

에러 처리: Flask는 @app.errorhandler() 데코레이터를 사용하여 특정 상태 코드에 대한 에러 핸들러를 정의. 이를 통해 예외 처리, 사용자 정의 에러 응답 등을 처리.

인증과 권한 부여: Flask는 인증과 권한 부여를 위한 확장 기능을 제공. 예를 들어, Flask-Login, Flask-JWT 등의 확장을 사용하여 사용자 인증과 권한 부여를 구현.

REST API 개발을 위해 Flask를 사용하는 경우, 위의 요소들을 활용하여 API 엔드포인트를 정의하고 요청을 처리하며, 데이터를 응답 형식에 맞게 생성하여 클라이언트에 반환.
