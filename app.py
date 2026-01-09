import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="신대방 UMD", page_icon="🎵")
st.title("🎵 신대방 유튜브 다운로더 (UMD)")
st.write("친구들아, 링크 넣고 변환 버튼 눌러봐!")

url = st.text_input("유튜브 URL 입력:", placeholder="https://www.youtube.com/watch?v...")

if st.button("음원 추출하기"):
    if url:
        with st.spinner('유튜브에서 소리 훔쳐오는 중... (베를린 서버 열일 중)'):
            try:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'outtmpl': '%(title)s.%(ext)s',
                    # 차단 방지를 위한 필수 옵션들
                    'quiet': True,
                    'no_warnings': True,
                    'nocheckcertificate': True,
                    'add_header': [
                        'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                        'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                    ],
                    'referer': 'https://www.google.com/',
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    # 정보 먼저 가져오기
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info).replace('.webm', '.mp3
