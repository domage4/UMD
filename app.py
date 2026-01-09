import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="유튜브 음원 추출기", page_icon="🎵")
st.title("🎵 유튜브 음원 다운로더")
st.write("링크만 넣으면 mp3로 바꿔줄게!")

url = st.text_input("유튜브 URL을 입력하세요:", placeholder="https://www.youtube.com/watch?v...")

if st.button("음원 추출하기"):
    if url:
        with st.spinner('베를린 서버에서 열심히 변환 중...'):
            try:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'outtmpl': '%(title)s.%(ext)s',
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                st.success("성공! 파일이 서버(또는 로컬)에 저장되었어.")
            except Exception as e:
                st.error(f"에러 발생: {e}")
    else:
        st.warning("링크를 먼저 입력해줘!")