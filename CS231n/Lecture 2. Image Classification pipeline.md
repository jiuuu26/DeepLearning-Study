# 📝 Lecture 2. Image Classification pipeline <br></br>
## 🔎 Image Classification
 우리는 다음의 사진을 보고 고양이라고 인식을 하지만 컴퓨터는 고양이라고 인식하지 못한다. 컴퓨터에게는 이것이 오직 아주 큰 격자 모양의 숫자 집합으로 보인다. 이 사진에서 카메라의 구도가 조금이라도 바뀌거나 고양이가 자세를 바꾸면 픽셀 값이 아주 크게 달라질 것이다. 그렇지만 이것이 고양이라는 사실은 달라지지 않는다. 그래서 어떠한 상황에 고양이가 있든 이것을 고양이라고 알아차릴 수 있는 알고리즘을 만들어야 한다.  
 ![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/7f698a2d-f64a-4150-a748-d03bee2c56f2)
 
 우리는 Hubel & Wiesel의 연구 덕분에 Edges가 중요하다는 것을 알고 있다. 그래서 알고리즘을 만들 때 우선 이미지에서 edge를 계산하고 다양한 corners와 edges를 각 카테고리로 분류하는 방법을 사용할 수 있다. 하지만 이러한 방식은 잘 작동하지 않는데, 문제는 이 알고리즘이 robust하지 못하다는 것과 다른 객체를 인식해야할 때 별도로 클래스에 맞는 집합을 하나하나 생성해야한다는 것이다. 이 말은 위의 방법이 확장성이 전혀 없다는 것이다.  
![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/3a48fde3-1d8d-4e0b-8156-e9e4ff961c1b)

 
다양한 객체들에게 유연하게 적용가능한 알고리즘을 만들어야 하는데, 이것을 가능하게 하는 것 중 하나는 "Data-Driven Approach(데이터 중심 접근법)"이다. 인터넷에 접속하여 많은 데이터를 수집하고 이것으로 다양한 객체를 인식할 수 있는 모델을 만들어 이 학습 모델로 새 이미지를 테스트 해보는 것이다. 이러한 방법으로 이미지를 올바른 객체로 인식하기 위해서는 2가지 함수가 필요하다. 하나는 train 함수, 다른 하나는 predict 함수이다.  


## 🔎 Nearest Neighbor Classifier
 ![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/83963a63-8e76-4b1c-a068-b12c9c46e572)  
 위의 코드가 아주 단순한 Nearest Neighbor Classfier인데, 보다시피 train에서는 모든 학습 데이터만 기억을 하고 predict에서 새로운 이미지와 기존 학습 데이터를 비교해서 가장 유사한 이미지로 레이블링을 예측하는 것이다. 이는 아주 간단하지만 "Data-driven Approach"의 아주 좋은 알고리즘이다.  
  이제 CIFAR-10 데이터 셋을 이용한 NN 예제를 살펴보겠다. 다음은 이미지를 학습 이미지와 유사한 순으로 정렬을 한 것이다. 이 이미지에 NN 알고리즘을 적용하면 트레이닝 셋에서 가장 가까운 셋을 찾아 내는데, 이 과정에서 테스트 이미지 하나를 모든 학습 이미지들과 비교할 때 여러 비교 방법이 있다. 즉 여러 비교 함수가 있다는 것이다.   

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/d8b0f258-f310-4455-806e-109779775f9e)

앞에서 적용한 방법은 L1 distance(Manhatten distance)를 사용한 것 이다. 이 방법은 이미지를 pixel-wise로 비교한 것인데, 테스트 이미지와 트레이닝 이미지의 같은 위치 픽셀을 서로 빼고 절대값을 취해 이 결과 값들의 합을 모두 더하여 비교하는 함수이다.  
![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/6ae1e5c3-fb54-42e3-a589-5a3d9739ad9b)

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/984b1bde-4890-40a8-898d-d47ca4fc1757)

이 코드를 가지고 train time과 test time을 비교해보면 각각의 시간 복잡도가 O(1), O(n)으로 test time이 더 오래걸린다는 것을 알 수 있다. 하지만 우리는 train이 조금 오래 걸리더라도 test가 빠른 것을 원한다. 이러한 관점으로 보면 이 NN 알고리즘은 좋지 않다. 반면 CNN과 같은 parametic model은 긴 train time과 짧은 test time을 가진다. CNN은 나중 수업에서 알아보기로 하고, 우선 NN 알고리즘을 실제로 적용했을 때 어떠한 결과가 나올지 보자. 다음은 NN의 "decision region"을 그린 것이다. 각 점은 학습 데이터이고, 점의 색은 class label 즉 카테고리이다. 이 예제에는 5개의 클래스가 있고 2차원 평면 내의 좌표에서 각 좌표가 어떤 학습 데이터와 가까운지를 계산한 것이다.  

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/8f6b65f7-7c50-49c2-a310-7f892f72c062)

하지만 이 classifier은 좋지 않다. 위 그림의 가운데를 보면 초록 부분에 노란 부분이 끼어 있는 것을 볼 수 있는데, NN 알고리즘은 이름과 같이 가장 가까운 이웃(Nearest Neighbor)만 보기 때문에 이러한 영역이 생기는 것이다. 그래서 우리는 단순히 가장 가까운 이웃만 찾기보다는 Distance metric을 이용하여 가까운 이웃 K개를 찾고, 이웃끼리 투표하는 방법을 도입할 것이다. 이것이 K-Nearest Neighbors이다. 


## 🔎 K-Nearest Neighbors


## 🔎 Linear Classification


