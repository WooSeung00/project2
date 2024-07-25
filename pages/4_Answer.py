import streamlit as st

# 세션 상태 초기화
if 'result' not in st.session_state:
    st.session_state.result = []

# 결과 출력
st.title("퀴즈 결과")

if st.session_state.result:
    correct_count = sum(st.session_state.result)
    total_count = len(st.session_state.result)
    
    st.write(f"정답 개수: {correct_count} / {total_count}")
    
    if correct_count == total_count:
        st.success("모든 문제를 정답으로 맞추셨습니다!")
    elif correct_count > 0:
        st.warning("잘 하셨습니다! 더 열심히 해보세요.")
    else:
        st.error("모든 문제를 틀리셨습니다. 다음에는 더 잘 해보세요!")
else:
    st.write("아직 퀴즈를 풀지 않았습니다.")
