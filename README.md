<br/>

# OKAY 빅데이터 기반 프린팅 검수 서비스

<br/>

## **프로젝트 결과 시연 영상**
: [OKAY 시연 유튜브 영상 바로가기](https://www.youtube.com/watch?v=LEoapwCI-KA)

<br/>

## **Project Description**

### **❤️ 주제 : OpenCV를 활용한 동영상, 이미지 픽셀 XOR 처리 불량품 검수**

### **❤️ 팀: OKAY (총4명)**

- 팀장 : 윤민지 (백엔드)
- 팀원 : 오송민 (딥러닝, 데이터베이스) , 김형우(딥러닝, 데이터베이스) , 안예지(프론트엔드)
&nbsp;&nbsp;&nbsp;<img width="600" alt="image" src="https://user-images.githubusercontent.com/68888349/175545161-681237f5-6b84-4dc5-bd23-e7920eb00116.png">

### **❤️ 개발 목표**

 - 중소기업 공장의 제조 과정 중 불량품 검수 작업의 기계 자동화를 위한 서비스<br/>
 - 실시간으로 입력되는 제품 이미지 데이터와 DB에 저장된 양품 이미지 데이터의 각 픽셀 값을 XOR 비교하여 불량품을 검수해주는 서비스 제공<br/>
 - 실시간으로 검수된 불량품 이미지를 DB화하고 원하는 기간별로 조회하여 시각화 된 통계 차트로 확인 가능하며 불량품의 상세 정보 열람 가능<br/>
 
### **❤️ 프로젝트의 특장점**
  - 유사 서비스 : LG C&S에서 자체 개발한 DAP-VISION -> 대기업에서 자체 개발한 비전 머신을 이용한 딥러닝 기술, 개발 소스 비공개로 비교 불가<br/>
  - 이미지 픽셀 빅데이터를 활용하여 효율적인 실시간 프린팅 검수 서비스 개발<br/>
  - 과하게 소요되는 검수 인력을 줄이고 검수에 소요되는 시간을 단축<br/>
  
## **Project Process**

### **🙏 시행착오**
- CNN 기반 이미지 객체 검출 모델 YOLOv4를 전이학습한 에러검출 모델 생성 <br/>
   1. 환경 설정<br/>
    &nbsp;- TensorFlow, YOLOv4, YOLO_MARK, CUDA, CUDNN, Visual Studio 등 설치, 환경 구축 및 설정<br/>
   2. 데이터 라벨링<br/>
     &nbsp; - YOLO_MARK를 이용하여 정답 데이터 라벨링<br/>
   3. 모델 학습과 객체 검출<br/>
    &nbsp;  - YOLOv4를 이용하여 전이학습 및 디텍팅<br/>
   4. 테스트 결과<br/>
    &nbsp;  - 이미지 데이터 부족과 라벨링 한 에러의 특징 부족으로 인해 학습과 디텍팅 실패<br/>
   5. 결론<br/>
   &nbsp;   - 본 프로젝트는 모델 학습과는 관계가 멀다고 판단하였고 이미지 픽셀 기반 XOR 처리방식이 적합하다고 결론<br/>
 
### **🙏 진행과정**
- 이미지 픽셀 XOR 기반 실시간 불량품 검수 서비스 개발<br/>
   1. 데이터 수집 및 전처리<br/>
    &nbsp; 1) 현장 답사를 통한 불량품 샘플 확보<br/>
    &nbsp; 2) 불량품 동영상 촬영 및 이미지 캡쳐<br/>
    &nbsp; 3) 불량품 이미지에서 에러 부분 픽셀 값을 변경하여 양품 이미지처럼 수정 전처리<br/>
   2. OpenCV 라이브러리를 활용하여 XOR 비교<br/>
    &nbsp; 1) 불량품 이미지와 수정한 양품 이미지를 XOR 비교하여 에러 검출<br/>
   3. 결과 시각화 서비스<br/>
    &nbsp; 1) 검출한 결과를 DB화하고 실시간으로 웹페이지에 서비스<br/>
    &nbsp; 2) DB에 저장된 정보를 기간별로 조회하여 상세 정보와 통계 시각화 서비스<br/>

<br/>

## **Project Information**

### **😍 DataBase**
 - Oracle DB를 활용한 로그인 사용자 및 제품 데이터 저장<br/>
&nbsp;&nbsp;&nbsp;<img width="400" alt="image" src="https://user-images.githubusercontent.com/68888349/175549347-cf4a1383-207b-42ae-b2c5-ca64cae958ac.png">


### **😍 Web**
 1. 파이썬 Flask를 활용한 웹 개발 및 DB 연동<br/>
 2. Javascript 및 jQuery를 활용한 화면 구성, 차트 구현<br/>
&nbsp;&nbsp;&nbsp;<img width="600" height="300" alt="image" src="https://user-images.githubusercontent.com/68888349/175549595-7425246f-d19b-4d9c-9342-dd9345854a58.png">
&nbsp;&nbsp;&nbsp;<img width="600" alt="image" src="https://user-images.githubusercontent.com/68888349/175549099-3616c533-5b01-4878-a127-1cde5484a662.png">

 
### **😍 machine learning**
 - OpenCV 라이브러리를 활용한 실시간 이미지 가공<br/>
 &nbsp;&nbsp;&nbsp;<img width="496" alt="image" src="https://user-images.githubusercontent.com/68888349/175549145-9dd1b6cf-23df-4315-9557-096cc6f1fdfa.png">

 
