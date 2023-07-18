# 📝 Lecture 3. Loss Functions and Optimization <br></br>
## 🔎 Loss function
&nbsp; 손실함수란 W를 입력으로 받아, 이 W가 얼마나 좋은지, 좋지 않은지 정량적으로 말해주는 것이다. x는 입력인 이미지이고 Y는 예측하고자 하는 레이블인 정수 값이다. 그러고 앞에서 말한 예측함수 f와 정답 값 y를 입력으로 받아서, 이 예측 정확도를 정량화 시키고 최종 Loss인 L은 데이터 셋에서 N개 샘플들의 Loss 평균이 된다. 딥러닝 알고리즘에서 가장 일반적으로 진행되는 일은 W가 얼마나 좋은지 정량화하는 손실 함수를 만드는 것이다. 
&nbsp; 손실 함수의 종류 중 하나인 multiclass SVM(Support Vector Machine) loss에 대해 알아보자. Loss L_i를 구하기 위해 "true인 카테고리"를 제외한 나머지 카테고리 Y의 합을 구한다. 즉 맞지 않는 카테고리를 전부 합치는 것이다. 그리고 "true 카테고리"와 "나머지 카테고리"의 스코어를 비교한 후 이 격차가 safety margin 이상이라면 loss가 0이 된다. 다음의 수식은 safety margin이 1인 예시이다. 이미지 내 "나머지 카테고리"의 모든 값을 합치면 그 값이 한 이미지의 최종 loss가 되고, 전체 트레이닝 데이터 셋에서 그 loss들의 평균을 구하면 된다. 

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/ef7b3563-6210-4fe0-97d7-48fec554781f)

&nbsp; 그리고 위와 같은 식으로 손실 함수를 만드는데, 이런 손실 함수를 "hinge loss"(경첩)이라고 부르기도 한다. 아래의 그래프에서 x축은 실제 정답 클래스의 스코어인 S_Yi이고, y축은 Loss이다. 정답 카테괴의 점수가 증가할수록 Loss가 선형적으로 줄어드는 것을 확인할 수 있다. 이 loss는 0이 된 이후에도 safety margin을 넘어설 때까지 줄어든다. 여기서 loss의 값이 0이 되었다는 것은 클래스를 잘 분류했다는 의미이다. 

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/cc46563d-6a9b-4f27-8944-20280fc29ec2)

&nbsp; 분류기가 트레이닝 데이터에 핏하게 된다면 모든 트레이닝 데이터를 분류해내기 위해 구불한 곡선을 만들 것이다. 하지만 이렇게 된다면 테스트 데이터에 대한 성능이 좋지 않을 것이다. 이를 해결하기 위한 방법은 regularization을 사용하는 것인데, 손실 함수에 하나의 항을 추가해주는 방법이다. 이것은 좀 더 단순한 W를 선택할 수 있도록 도와준다. 과학계에서 유명한 "Occam's Razor"이라는 말이 있는데, 이것은 우리가 다양한 가설들을 가지고 있고 이 가설들 모두가 어떤 현상에 대해 설명 가능하다면 우리는 일반적으로 더 단순한 것을 선호해야한다는 뜻이다. 단순한 것이 미래에 일어날 현상을 더 잘 설명할 가능성이 높기 때문이다. 위에서 regularization을 사용하는 이유도 이것과 같은 것이다. 

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/23be967b-b608-4f55-87b4-6af4fd919f7f)

&nbsp; Regularization에는 여러 종류가 있는데, 가장 보편적인 것은 L2 regularization이다. weight decay라고도 하며, 이것은 가중치 행렬 W의 euclidean norm에 패널티를 주는 것이다. 다음으로 L1 regularization은 L1 norm으로 w에 패널티를 주는 것이고, L1에서는 행렬 W가 희소 행렬이 되도록 한다. 그리고 Elastic net regularization이라는 것도 있는데, 이것은 L1과 L2를 섞어놓은 것이다. 또, max norm regulatization이라는 것도 있는데 이것은 L1과 L2 대신에 max norm을 사용하는 것이다. 정리하자면 regularization은 모델이 트레이닝 데이터셋에 완벽히 핏하지 못하도록 복잡도에 패널티를 부여하는 방법이다. 

![image](https://github.com/jiuuu26/DeepLearning-Study/assets/110098218/109d251c-d056-4785-9960-87d1cd44e39e)

1695

## 🔎 Optimization


## 🔎 기존 이미지 추출 방식
