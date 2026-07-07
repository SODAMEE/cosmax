"""성분노트 — Streamlit Cloud 앱
원본 HTML(성분조합추천.html)을 그대로 임베드하여 디자인과
JavaScript 인터랙션(피부 타입 선택, 성분 드롭다운 등)을 유지합니다.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="성분노트 — 사기 전에 먼저 확인하는 화장품 성분",
    page_icon="🧪",
    layout="wide",
)

# Streamlit 기본 여백/헤더/푸터 제거 → HTML이 전체 화면을 차지하도록
st.markdown(
    """
    <style>
      #MainMenu, header, footer { visibility: hidden; }
      .block-container {
          padding: 0 !important;
          max-width: 100% !important;
      }
      iframe { display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_FILE = Path(__file__).parent / "성분조합추천.html"

if not HTML_FILE.exists():
    st.error(
        "`성분조합추천.html` 파일을 찾을 수 없어요. "
        "app.py와 같은 폴더(저장소 루트)에 HTML 파일을 함께 올려주세요."
    )
    st.stop()

html_source = HTML_FILE.read_text(encoding="utf-8")

# scrolling=True + 충분한 높이로 페이지 전체 렌더링
components.html(html_source, height=6800, scrolling=True)
