import streamlit as st

# 세션 상태 초기화
if 'result' not in st.session_state:
    st.session_state.result = []

# 문제 리스트
questions = [
    {
        "question": "1. 파이썬에서 리스트를 생성하는 방법은?",
        "options": ["a) []", "b) ()", "c) {}", "d) <>"],
        "answer": "a"
    },
    {
        "question": "2. 파이썬의 기본 데이터 타입이 아닌 것은?",
        "options": ["a) int", "b) str", "c) float", "d) char"],
        "answer": "d"
    },
    {
        "question": "3. 파이썬에서 함수 정의 키워드는?",
        "options": ["a) def", "b) function", "c) fun", "d) define"],
        "answer": "a"
    }
]

# 퀴즈 출력
for i, q in enumerate(questions):
    st.write(q["question"])
    user_answer = st.selectbox(f"문제 {i + 1} 선택:", q["options"], key=f"question_{i}")
    if st.button("제출", key=f"submit_{i}"):
        if user_answer[0] == q["answer"]:
            st.session_state.result.append(True)
            st.success("정답입니다!")
        else:
            st.session_state.result.append(False)
            st.error("틀렸습니다.")

# 결과 보기 버튼
if st.button("결과 보기"):
    st.write("당신의 결과는:", st.session_state.result)
