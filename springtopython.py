# import org.springframework.http.HttpEntity;
# import org.springframework.http.HttpHeaders;
# import org.springframework.http.MediaType;
# import org.springframework.http.ResponseEntity;
# import org.springframework.web.client.RestTemplate;
#
# import java.util.HashMap;
# import java.util.Map;
#
# public class DataSender {
#
#     public static void main(String[] args) {
#         // 파이썬으로 전송할 값 설정
#         String text1 = "Hello";
#         String text2 = "world";
#         String text3 = "!";
#
#         // 파이썬으로 전송할 엔드포인트 URL
#         String url = "http://localhost:5000/process-values";
#
#         // 전송할 데이터를 Map에 담기
#         Map<String, String> requestData = new HashMap<>();
#         requestData.put("text1", text1);
#         requestData.put("text2", text2);
#         requestData.put("text3", text3);
#
#         // HTTP 요청 헤더 설정
#         HttpHeaders headers = new HttpHeaders();
#         headers.setContentType(MediaType.APPLICATION_JSON);
#
#         // HTTP 요청 본문에 데이터와 헤더를 포함하여 요청 엔티티 생성
#         HttpEntity<Map<String, String>> requestEntity = new HttpEntity<>(requestData, headers);
#
#         // RestTemplate을 사용하여 POST 요청 보내기
#         RestTemplate restTemplate = new RestTemplate();
#         ResponseEntity<String> response = restTemplate.postForEntity(url, requestEntity, String.class);
#
#         // 응답 받은 결과 출력
#         String responseBody = response.getBody();
#         System.out.println("Response: " + responseBody);
#     }
# }


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process-values', methods=['POST'])
def process_values():
    data = request.get_json()
    text1 = data.get('text1')
    text2 = data.get('text2')
    text3 = data.get('text3')

    return jsonify({
        'message': 'Values processed successfully',
        'processed_values': f'{text1}, {text2}, {text3} processed'
    })

if __name__ == '__main__':
    app.run(debug=True)
