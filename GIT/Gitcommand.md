# Git command

> Git 명령어 정리



### 0. init

- `git init`
- `.git/` 폴더를 생성해준다.
- ![image-20201229151821608](./Gitcommand.assets/image-20201229151821608.png)
=======
- `.git ` 폴더가 생성된 경우 오른쪽에` master`라는 표시가 나온다.
- 최초에 한번만 하면된다.

### 1. config

- `git config --global user. email "myemail@gmail.com"`
  - 이메일의 경우 깃헙에 올릴때 잔디가 심어지는 기준이므로 정확하게 입력!!
- `git config --global user. name "myname"`
- 최초로 한번만 하면 된다.



## 커밋기록

### 1. add

- `git add <추가하고싶은 파일>`	
  - `git add .` : 현재 폴더의 모든 파일과 폴더를 add
- working directory => staging area로 이동

### 2. commit

- `git commit -m "메세지"`
- 스냅샷을 찍는 동작
- add 되어있는 파일들을 하나의 묶음으로 저장
- 메세지에 들어가는 내용은 기능단위로

### 3.remote

- `git remote add origin <주소>`
- 원격 저장소와 현재 로컬 장소를 연결

### 5. push

- `git push origin master`
- 깃아 올려줘 origin master
- 원격 저장소에 로컬 저장소의 데이터를 전송



## 상태확인

### 1. status

- `git status`
- 현재 git 상태를 출력

### 2. log

- `git log`

- 커밋 기록을 전체 다 출력
- 옵션
  - `--online`: author, date 같은 정보를 제외하고 한줄로 출력
  - `--graph`:  커밋들을 점으로 표현하고 그 커밋을 선으로 연결하여 그래프 형태로 출력
- `:wq` : 나가기

### 3. diff

- `git diff`
- 현재 변경사항을 체크 (`git add`하기 전)



# 추가파일

### 1. git ignore

- `git ignore` 파일을 생성 후, git으로 관리하고 싶지 않은 파일들을 저장
- `gitignore.io`



# 브랜치

### 1. 생성

- `git branch<브랜치 이름>`

### 2. 이동

- `git switch<브랜치 이름>`

### 3. 삭제

- `git branch -D<브랜치 이름>`

### 4. 병합

- `git merge<브랜치 이름>`
- base가 되는 branch로 이동해서 명령어 사용
- 충돌이 발생한 경우 해결하고, add-commit-push
  - 꺽새, 언더라인 등 지우기

### 5. git hub 가져오기

- `git pull origin master`
- `git clone<복제할 주소>`
- 오른쪽 상단 위 fork