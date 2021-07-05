# AI 학습 방법



머신러닝의 학습방법은 크게 3가지로 분류 할 수 있습니다.

- 지도학습
- 비지도학습
- 강화학습



### 지도학습(Supervised Learning)

: 정답이 있는 데이터를 활용해서 학습을 하기때문에 정확한 Input과 Output 존재합니다.

1. 분류(classification) 
   - 주어진 데이터를 정해진 라벨(카테고리)에 따라 분류합니다.
     -  ex) Yolo를 활용한 이미지 분류
   - 예, 아니오로 구분 가능한 이진분류(Binary Classification)
   -  강아지다 고양이다의 다중분류(Multi-label Classification)
   - KNN, Naive Bayes, Support Vector Machines, Decision trees
2. 회귀(Regression)
   - feature를 기준으로 연속된 값을 예측하는 문제로 패턴, 트렌드, 경향을 예측합니다.
     - ex) 집 값 구하기
   - Linear Regression, Locally Weighted Linear, Ridge, Lasso



### 비지도학습(Unsupervised Learning)

: 정답이 없는 데이터를 비슷한 특징끼리 군집화하여 새로운 데이터에 대한 결과를 예측합니다.

- ex) 뉴스 기사 그룹핑, 추천시스템
  - Clustering, K Means, Density Estimation, Exception Maximization, Pazwn Window, DBSCAN



### 강화학습(Reinforcement Learning)

: agent, environment, state, action, reword의 개념으로 이루어져있습니다. 즉, 어떤 environment안에서 agent가 state를 관찰하여 선택 할 수 있는 action중에서 가장 최대의 reword를 갖는 행동이 무엇인지를 학습합니다.  

- ex) 자율주행, 알파고, 게임
  - DQN, A3C, MDP

