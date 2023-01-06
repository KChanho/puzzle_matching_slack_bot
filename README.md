# puzzle_matching_slack_bot

<img src="https://user-images.githubusercontent.com/94108712/209671125-9119d237-dc9a-4e70-afbf-25fb0a6614f8.png"  width="400" height="400"/>
                                                                                                                                         
안녕하세요, 지역 기반 매칭 봇, **매칭박사 퍼즈리**입니다!

매칭박사 퍼즈리는 캠퍼 분들에게 다양한 교류의 장을 열어드리기 위해 제작된 지역 기반 매칭 봇입니다.
퍼즈리는 수도권의 활발한 오프라인 모임이 부러웠던 한 지방 캠퍼의 소망 에서 탄생했는데요.
퍼즈리는 퍼즐 조각들을 맞추어 하나의 작품이 되듯, 캠퍼분들을 이어드립니다.

아래는 매칭박사 퍼즈리의 가이드라인 입니다.

---
1. 슬랙 숏컷에서 바로가기 검색으로 퍼즈리를 찾아보세요.

![연말1](https://user-images.githubusercontent.com/94108712/209671136-0c7dba15-65b0-4faa-b552-78f62fb4589c.png)

2. 퍼즈리 매칭 등록을 신청합니다.

![연말2](https://user-images.githubusercontent.com/94108712/209671139-0974c547-f889-4112-b23f-0834d89c0d2f.png)

3. 매칭 결과에 따라 매칭 상대와 그룹 채팅방이 생성됩니다.

![연말3](https://user-images.githubusercontent.com/94108712/209671141-ab8c6b0f-069b-4c78-8ccd-75fe166b11b5.png)
---

# 퍼즈리 기능

- 슬랙 채팅에서 사용자의 멘션에 반응하여 퍼즈리 자기소개글과 가이드라인 출력
- 슬랙 숏컷 기능을 통해 매칭 신청과 매칭 취소 신청 접수
- 위에서 받은 매칭 신청과 매칭 취소 신청 기록을 csv 파일로 저장
- 퍼즈리 봇을 통해 채팅창에 메세지 전송
- 매칭된 사용자들을 모아 그룹 채팅방 생성

---

# 프로젝트 타임라인

- 2022.12.17: 오프라인 모임에 소외된 지방 캠퍼들을 위한 서비스의 필요성 인식
- 2022.12.18: 구현할 서비스의 초안 계획
- 2022.12.19: 부스트캠프 슬랙 내 랜덤 채널을 활용하여 수요 설문조사 진행
- 2022.12.23: 슬랙 봇 퍼즈리를 구현하여 연말 연휴 오프라인 모임 매칭 신청받기
- 2022.12.26: 접수된 매칭 신청들을 종합하여 매칭 진행 후 그룹채팅방 생성

---

# 코드 사용 가이드

```
.
|-- json  # contains config and forms
|   |-- _config.json
|   |-- close_form.json
|   |-- config.json
|   |-- mention_form.json
|   |-- open_form.json
|   `-- test_message.json
|-- utils
|   |-- data.ipynb
|   |-- open_chat.py
|   `-- send_message.py
|-- key_manager.py
|-- main_background.py
|-- make_csv.py
|-- requirements.txt
`-- README.md
```

1. _config.json 파일의 이름을 config.json으로 수정하고, app token과 bot token 값을 입력한다. (key_manager.py를 통해 token 값 관리)
2. make_csv.py로 데이터를 저장할 csv 파일을 생성한다.
3. main_background.py를 통해 매칭 신청과 매칭 취소 신청을 접수한다.
4. 필요에 따라 send_message.py를 통해 퍼즈리의 형태로 채팅을 전달한다.
5. 매칭 결과에 따라 open_chat.py을 통해 그룹 채팅방을 생성한다.
