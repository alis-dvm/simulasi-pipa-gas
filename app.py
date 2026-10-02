"""Simulasi Perpipaan Gas — pembungkus Streamlit.

Jalankan:  streamlit run app.py
Aplikasi simulasinya sendiri ada di simulasi_perpipaan_gas.html (HTML + JS mandiri);
file ini hanya menyajikannya di dalam halaman Streamlit.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

HTML_FILE = Path(__file__).parent / "simulasi_perpipaan_gas.html"

st.set_page_config(page_title="Simulasi Perpipaan Gas", page_icon="🛢️", layout="wide",
                   initial_sidebar_state="collapsed")

# Buang padding bawaan Streamlit supaya simulator memenuhi halaman.
st.markdown(
    """<style>
    .block-container{padding:0.4rem 0.6rem 0 0.6rem;max-width:100%;}
    header[data-testid="stHeader"]{height:0;min-height:0;background:transparent;}
    footer{visibility:hidden;}
    iframe{border:0;border-radius:10px;}
    </style>""",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Tampilan")
    height = st.slider("Tinggi area simulasi (px)", 600, 1600, 900, 50)
    st.caption("Tema warna dipilih dari menu TEMA di kanan atas simulator.")
    st.download_button("⬇️ Unduh versi HTML mandiri", HTML_FILE.read_bytes(),
                       file_name="Simulasi_Perpipaan_Gas_v2.html", mime="text/html")

if not HTML_FILE.exists():
    st.error(f"File {HTML_FILE.name} tidak ditemukan di folder yang sama dengan app.py.")
    st.stop()

components.html(HTML_FILE.read_text(encoding="utf-8"), height=height, scrolling=False)
