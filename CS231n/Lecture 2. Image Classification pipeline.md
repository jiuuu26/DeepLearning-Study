# 📝 Lecture 2. Image Classification pipeline <br></br>
## 🔎 Image Classification
&nbsp; 우리는 다음의 사진을 보고 고양이라고 인식을 하지만 컴퓨터는 고양이라고 인식하지 못한다. 컴퓨터에게는 이것이 오직 아주 큰 격자 모양의 숫자 집합으로 보인다. 이 사진에서 카메라의 구도가 조금이라도 바뀌거나 고양이가 자세를 바꾸면 픽셀 값이 아주 크게 달라질 것이다. 그렇지만 이것이 고양이라는 사실은 달라지지 않는다. 그래서 어떠한 상황에 고양이가 있든 이것을 고양이라고 알아차릴 수 있는 알고리즘을 만들어야 한다.  
 ![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/7f698a2d-f64a-4150-a748-d03bee2c56f2)
 
&nbsp; 우리는 Hubel & Wiesel의 연구 덕분에 Edges가 중요하다는 것을 알고 있다. 그래서 알고리즘을 만들 때 우선 이미지에서 edge를 계산하고 다양한 corners와 edges를 각 카테고리로 분류하는 방법을 사용할 수 있다. 하지만 이러한 방식은 잘 작동하지 않는데, 문제는 이 알고리즘이 robust하지 못하다는 것과 다른 객체를 인식해야할 때 별도로 클래스에 맞는 집합을 하나하나 생성해야한다는 것이다. 이 말은 위의 방법이 확장성이 전혀 없다는 것이다.  
![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/3a48fde3-1d8d-4e0b-8156-e9e4ff961c1b)

 
&nbsp; 다양한 객체들에게 유연하게 적용가능한 알고리즘을 만들어야 하는데, 이것을 가능하게 하는 것 중 하나는 "Data-Driven Approach(데이터 중심 접근법)"이다. 인터넷에 접속하여 많은 데이터를 수집하고 이것으로 다양한 객체를 인식할 수 있는 모델을 만들어 이 학습 모델로 새 이미지를 테스트 해보는 것이다. 이러한 방법으로 이미지를 올바른 객체로 인식하기 위해서는 2가지 함수가 필요하다. 하나는 train 함수, 다른 하나는 predict 함수이다.  


## 🔎 Nearest Neighbor Classifier
 ![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/83963a63-8e76-4b1c-a068-b12c9c46e572)  
&nbsp; 위의 코드가 아주 단순한 Nearest Neighbor Classfier인데, 보다시피 train에서는 모든 학습 데이터만 기억을 하고 predict에서 새로운 이미지와 기존 학습 데이터를 비교해서 가장 유사한 이미지로 레이블링을 예측하는 것이다. 이는 아주 간단하지만 "Data-driven Approach"의 아주 좋은 알고리즘이다.  
&nbsp;  이제 CIFAR-10 데이터 셋을 이용한 NN 예제를 살펴보겠다. 다음은 이미지를 학습 이미지와 유사한 순으로 정렬을 한 것이다. 이 이미지에 NN 알고리즘을 적용하면 트레이닝 셋에서 가장 가까운 셋을 찾아 내는데, 이 과정에서 테스트 이미지 하나를 모든 학습 이미지들과 비교할 때 여러 비교 방법이 있다. 즉 여러 비교 함수가 있다는 것이다.   

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/d8b0f258-f310-4455-806e-109779775f9e)

&nbsp; 앞에서 적용한 방법은 L1 distance(Manhatten distance)를 사용한 것 이다. 이 방법은 이미지를 pixel-wise로 비교한 것인데, 테스트 이미지와 트레이닝 이미지의 같은 위치 픽셀을 서로 빼고 절대값을 취해 이 결과 값들의 합을 모두 더하여 비교하는 함수이다.  

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/6ae1e5c3-fb54-42e3-a589-5a3d9739ad9b)

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/984b1bde-4890-40a8-898d-d47ca4fc1757)

&nbsp; 이 코드를 가지고 train time과 test time을 비교해보면 각각의 시간 복잡도가 O(1), O(n)으로 test time이 더 오래걸린다는 것을 알 수 있다. 하지만 우리는 train이 조금 오래 걸리더라도 test가 빠른 것을 원한다. 이러한 관점으로 보면 이 NN 알고리즘은 좋지 않다. 반면 CNN과 같은 parametic model은 긴 train time과 짧은 test time을 가진다. CNN은 나중 수업에서 알아보기로 하고, 우선 NN 알고리즘을 실제로 적용했을 때 어떠한 결과가 나올지 보자. 다음은 NN의 "decision region"을 그린 것이다. 각 점은 학습 데이터이고, 점의 색은 class label 즉 카테고리이다. 이 예제에는 5개의 클래스가 있고 2차원 평면 내의 좌표에서 각 좌표가 어떤 학습 데이터와 가까운지를 계산한 것이다.  

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/8f6b65f7-7c50-49c2-a310-7f892f72c062)

&nbsp; 하지만 이 classifier은 좋지 않다. 위 그림의 가운데를 보면 초록 부분에 노란 부분이 끼어 있는 것을 볼 수 있는데, NN 알고리즘은 이름과 같이 가장 가까운 이웃(Nearest Neighbor)만 보기 때문에 이러한 영역이 생기는 것이다. 그래서 우리는 단순히 가장 가까운 이웃만 찾기보다는 Distance metric을 이용하여 가까운 이웃 K개를 찾고, 이웃끼리 투표하는 방법을 도입할 것이다. 그러고 가장 많은 투표수를 획득한 레이블로 예측한다. 이것이 K-Nearest Neighbors이다. 


## 🔎 K-Nearest Neighbors
&nbsp; 투표를 하는 방법은 거리별 가중치를 고려하는 등 매우 다양하다. 하지만 가장 간단한 방법은 득표수만 고려하는 것이다. 다음 세 그림은 동일한 데이터를 사용한 k-NN classifier이다. 위의 NN 알고리즘에서 발생했던 노란 영역 문제와 빨-파 사이 뾰족한 경계 문제도 어느 정도 해결이 된 것을 볼 수 있다.

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/4f5052d5-5296-42a9-986d-6e3dcb48b559)

&nbsp; 이미지를 다룰 때 다양한 관점을 유연하게 다루는 것은 매우 중요한데, 
1. 이미지를 고차원 공간에 존재하는 하나의 점이라고 생각하거나
2. 이미지를 이미지 자체로 보는 것
이 두 관점을 유연하게 오가는 능력이 중요하다는 것이다.

하지만 k-nn은 이미지를 다룰 때 그다지 좋은 방법은 아니다.

&nbsp; 더하여 k-nn을 사용할 때 서로 다른 점을 어떻게 비교하는지를 결정해야하는데, 지금까지는 픽셀 간 차이의 절대값 합인 "L1 distance"를 이용하였다. 이 방법 말고 제곱 합의 제곱근을 이용하는 "L2 (Euclidean) distance"를 이용해도 된다. 아래에 보이는 L1의 사각형은 L1 distance 관점에서는 원이고, L2는 L2 distance 관점에서도 원이고, 실제로도 원이다. 이 둘의 차이는 L1은 좌표계를 회전시키면 L1 distance가 변하고, L2는 좌표계와 아무런 연관이 없다는 것이다. 따라서 만약 특징 벡터의 각 요소들이 개별적 의미를 가지고 있을 때는 L1이 유용하고, 그렇지 않을 때는 L2가 유용할 것이다. 

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/2f337b77-f88b-4064-ac9b-7ebe8e64d474)

&nbsp; k-nn을 사용할 때 이와 같은 거리 척도를 정해주면 어떤 종류의 데이터도 다룰 수 있다. 아래 그림을 보면 거리 척도에 따라 dicision region의 모양이 달라지는 것을 알 수 있다. 앞서 말한 것과 마찬가지로, L1은 좌표 축에 영향을 받는 경향이 있고 L2는 영향을 받지 않아 조금 더 자연스러운 decision region이 만들어지는 것을 볼 수 있다. 

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/88f3e759-54de-4754-a5d6-af5ac83cc412)

&nbsp; 여기서 K와 거리 척도를 <b>"hyperparameters"</b>라고 부르는데, 이것은 학습 전 미리 선택해주어야 하는 것이다. 그렇다면 어떻게 hyperparameter을 정해야하는지 궁금해지는데, 이것은 problem-dependent하게 정해주어야 한다. 가장 간단히 이를 결정하는 법은 다양한 hyperparameter을 시도해보고 가장 좋은 값을 찾는 것이다. 가장 최고의 hyperparmeter을 선택하는 방법 중 가장 먼저 떠올릴 수 있는 것은 "학습 데이터의 정확도와 성능을 최대화"하는 hyperparameter을 선택하는 것이다.(Idea #1) 하지만 이것은 아주 좋지 않은 방법이고, 이를 선택해서는 안된다. 이를 선택한다면 항상 k=1일 때가 최고라는 결과가 나온다. 이렇게 되어선 안되는 이유는 k를 1이 아닌 큰 값으로 선택했을 때 학습 데이터에서 몇 가지를 잘못 분류할 수는 있지만, unseen data에서는 대부분 더 좋은 성능을 보이기 때문이다. 

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/4ff7eb1c-ca81-435e-979b-1cfe43d42ea9)

&nbsp; 두번째로는 전체 데이터 셋 중 학습 데이터를 train data와 test data로 쪼개어 일부를 test data로 사용하는 것이다.(Idea #2) 학습 데이터로 다양한 hyperparameter 값들을 학습시키고 test data에 적용시켜 본 다음 hyperparameter을 선택하는 것이다. 이것도 아주 좋지 않은 방법이고, 이를 선택해서는 안된다. machine learning의 궁극적인 목표는 unseen data에서 잘 작동해야하므로, 테스트 셋으로는 unseen data에서의 알고리즘 성능을 측정할 수 있어야한다. 여기서 학습시킨 모델 중 test data에 잘 맞는 hyperparameter을 선택한다면, unseen이 아닌 단지 그 test set에서만 잘 작동하는 hyperparameter을 고른 것이다. 

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/39282980-b9c4-4e0e-930b-8fb23ca738e9)

&nbsp; 세번째 방법으로는 데이터 셋을 세 부분으로 나누는 것이다. 데이터 셋의 대부분은 train, 일부는 validation, test로 나누는 것이다.(Idea #3) 그 후 다양한 hyperparameter로 training set을 학습시키고 validation으로 검증을 한 후, validation에서 가장 좋은 결과를 낸 hyperparameter을 선택한다. test에서는 이것을 가지고 딱 한 번만 수행을 한다. 우리가 정직하고 공정하게 수치를 측정했다는 것을 보장하기 위해서는 test를 마지막 쯤에 한 번 사용해야한다. 그래서 validation data와 test data를 엄격하게 나누는 것은 아주 중요하다. 

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/b2988b5d-a227-4a18-89e6-755181b460a9)

&nbsp; 추가로 또 다른 hyperparameter 선택 방법은 cross-validation(교차 검증)이라는 방법이다.(Idea #4) 이것은 data set이 작을 때 주로 사용하고 딥러닝에서는 많이 사용하지 않는다. 이 방법에서는 우선 test data를 정한 후 나머지를 train 여러 부분으로 나누어 주고나서, 번갈아가면서 하나씩 validation으로 지정해준다. 이렇게 순환하면서 알고리즘을 평가하고 최적의 hyperparameter을 찾아주는 방법이다. 딥러닝은 학습 자체의 계산량이 많기 때문에 실제로 이 방법을 잘 쓰지 않는다.

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/cefa9c7b-3ae2-4377-81ef-b61921b9520f)

✔️ 참고로 training과 validation의 차이는 전자의 레이블은 볼 수 있지만, 후자의 레이블은 볼 수 없다는 것이다. validation의 레이블은 알고리즘이 얼마나 잘 동작하는지를 확인할 때만 사용한다. 

&nbsp; 앞서 말했다시피 실제로 입력이 이미지일 때 k-NN classifier을 잘 사용하지 않는다. 첫번째 이유는 k-nn이 너무 느리기 때문이다. 그리고 두번째 이유는 L1/L2 distance가 이미지 간의 거리를 측정하기에 적절하지 않기 때문이다. L1/L2와 같은 벡터 간 거리 측정 관련 함수들은 이미지 간의 "지각적 유사성"을 측정하는 척도로는 적정하지 않다. 다음의 이미지들의 Euclidean Distance을 측정해보면 모두 동일한 L2 Distance을 가지는데, 이는 이것이 지각적 유사성을 측정하기에 적합하지 않다는 것을 뜻한다.

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/67ce4f18-9770-4ccd-a4a4-3cd2ba5481b0)


&nbsp; k-nn의 또 다른 세번째 문제는 k-nn이 잘 동작하기 위해서는 전체 공간을 조밀하게 커버할 만큼의 충분한 training sample이 필요하다는 것인데, 이 샘플의 양은 차원이 증가하면서 기하급수적으로 증가하기 때문에 좋지 않다. 

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/a765ab69-86fc-4704-8078-056e10306591)


## 🔎 Linear Classification
&nbsp; Linear Classification은 아주 간단한 알고리즘이지만, 굉장히 중요한 NN & CNN의 기반 알고리즘이다. Linear Classification은 "parametic model"의 가장 단순한 형태이다. parametic model에는 두 가지 요소 x, W가 있다. 입력 이미지 x와 가중치를 뜻하는 W이다. 우리는 50,000여개의 샘플을 가진 CIFAR-10과 3가지 컬러의 32x32 픽셀에 Linear Classification으로 접근해볼 것이다. 그러기 위해서 우리는 함수를 작성해야하는데, 앞서 말한 x와 W를 가지고 CIFAR-10의 카테고리인 10개의 숫자를 출력해야한다. 여기서 출력하는 숫자는 각 카테고리의 스코어인데, 한 카테고리의 스코어가 높다면 이미지 x가 해당 카테고리일 확률이 크다는 것을 의미한다. 

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/5c13a059-4f02-4156-9281-44459522dd92)

&nbsop; parametic approach에서는 training data의 정보를 요약하여 이것을 parameter인 W에 모아준다. 이러한 방식을 이용하면 test time에서 training data가 필요하지 않고 W만 있으면 된다. 이 방법은 스마트폰 같은 작은 디바이스에서 모델을 동작시킬 때 효율적이다. 따라서 딥러닝은 어떤 식으로 가중치 W와 데이터 x를 잘 조합할지 함수 F를 적절히 잘 설계하는 일이라고 할 수 있다. 이렇게 F를 설계하는 일이 모두 NN 아키텍처를 설계하는 과정이고, F 설계법 중 가장 간단한 방법은 W와 x를 단순히 곱하는 것이다. 이것이 바로 F(x,W) = Wx, 즉 Linear Classification이다.  
&nbsop; 다음으로 이것의 차원을 살펴보면, 입력 이미지 X는 32 x 32 x 3이다. 이 값을 길게 펴서 열 벡터로 만들면 3,072-dim 벡터가 된다. 그리고 이 3072-dim 벡터가 10 classes 스코어가 되어야 한다. 따라서 행렬 W는 10 x 3072이 되어야 하는 것이다. 그러고 W와 x를 곱하면 10 x 1 짜리 하나의 열 벡터를 얻게 된다. 여기서 가끔 10-dim 벡터인 "Bias"를 더해주어야 하는데, 이것은 입력과 직접 연결되지 않고 데이터와 무관하게 특정 클래스에 우선권을 부여하는 역할을 한다. 예를 들어 고양이 데이터가 개 데이터보다 훨씬 많은 상황에서 고양이 클래스에 해당하는 Bias가 커지고, 이를 더해주는 것이다. 아래는 위의 설명을 전체 4개 픽셀의 2x2 이미지에 고양이, 강아지, 배 총 3가지 클래스가 있다고 가정한 뒤 함수가 어떻게 작동하는지를 나타낸 것이다. 가중치 행렬 W는 4x3 행렬이 되며, 3-dim bias 벡터가 있다. 

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/3b007293-91d9-4f2a-8ca5-e2ace4858588)

&nbsp; 가중치 행렬 W의 행 벡터와 이미지 X 열벡터 간의 내적을 계산하는 것인데, 여기서 내적은 결국 클래스 간 템플릿의 유사도를 측정하는 것과 비슷하다. 

&nbsp; Linear Classifier의 문제점은 다양한 특징을 평균화시켜 한 클래스에 대해서 단 하나의 템플릿만을 학습한다는 것이다. 다음으로 Linear Classifier을 또 다른 관점으로 해석할 수 있는데, 각 이미지를 고차원 공간의 한 점이라고 생각하고 Linear Classifier을 각 클래스를 구분시켜 주는 선형 결정 경계로 해석하는 것이다. 하지만 이것으로 다음의 데이터를 선 하나로 분류하기는 힘들다. 또 맨 오른쪽 그림과 같이 한 클래스가 다양한 공간에 분포하는 Multimodal data라면 linear classifier로 해결하기 힘들어진다. 

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/dea7b1a8-e82b-451e-9277-52e125c1692d)

