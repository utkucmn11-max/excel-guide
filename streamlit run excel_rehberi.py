import streamlit as st
import pandas as pd
from streamlit_javascript import st_javascript

# Sayfa Yapılandırması
st.set_page_config(page_title="Excel Master Pro | Utku", page_icon="📗", layout="wide")

# --- DİL ALGILAMA ---
user_lang = st_javascript("navigator.language")

if "lang" not in st.session_state:
    if user_lang and "tr" in str(user_lang).lower():
        st.session_state.lang = "Türkçe"
    else:
        st.session_state.lang = "English"

# Manuel seçim (override)
lang = st.selectbox(
    "🌍 Dil / Language",
    ["Türkçe", "English"],
    index=0 if st.session_state.lang == "Türkçe" else 1
)

st.session_state.lang = lang

# Çeviri fonksiyonu
def t(tr, en):
    return tr if st.session_state.lang == "Türkçe" else en


# --- CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .block-container {
        max-width: 900px;
        margin: 0 auto;
        padding-top: 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    h1, h2, h3, h4 { 
        text-align: center !important; 
        color: #2EA043 !important; 
    }
    .stTabs [data-baseweb="tab-list"] {
        display: flex;
        justify-content: center;
        gap: 12px;
        background-color: #161B22;
        padding: 8px;
        border-radius: 15px;
        border: 1px solid #30363D;
    }
    .stTabs [aria-selected="true"] {
        background-color: #2EA043 !important;
        color: white !important;
    }
    .dark-card {
        background-color: #1C2128;
        padding: 25px;
        border-radius: 15px;
        border-top: 4px solid #2EA043;
        margin-bottom: 20px;
        width: 100%;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)


# --- BAŞLIK ---
st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=90)

st.markdown(f"<h1>{t('EXCEL MASTER PROFESYONEL PORTALI', 'EXCEL MASTER PROFESSIONAL PORTAL')}</h1>", unsafe_allow_html=True)

st.markdown(f"<p style='text-align:center;color:#8B949E;'>"
            f"{t('Utku Tarafından Geliştirilen İleri Seviye Eğitim Platformu', 'Advanced Training Platform Developed by Utku')}"
            f"</p>", unsafe_allow_html=True)


# --- SEKMELER ---
t1, t2, t3, t4, t5 = st.tabs([
    "🌌 Dashboard",
    t("⌨️ Kısayollar", "⌨️ Shortcuts"),
    t("💻 Excel Kodları", "💻 Excel Codes"),
    t("🧹 Veri Temizleme", "🧹 Data Cleaning"),
    t("📊 Raporlama", "📊 Reporting")
])


# --- DASHBOARD ---
with t1:
    c1, c2, c3 = st.columns(3)
    c1.metric(t("Kayıtlı Veri", "Stored Data"), "150+")
    c2.metric(t("Öğrenme Hızı", "Learning Speed"), "3X")
    c3.metric(t("Geliştirici", "Developer"), "Utku")

    st.markdown(f"""
    <div class="dark-card">
        <h3>🚀 {t('Hoş Geldin', 'Welcome')}</h3>
        <p>{t(
            "Excel'de ustalaşmak için fareyi bırakma zamanı.",
            "Time to master Excel without relying on the mouse."
        )}</p>
    </div>
    """, unsafe_allow_html=True)


# --- KISAYOLLAR ---
with t2:
    st.subheader(t("Temel İşlemler", "Basic Operations"))

    st.table(pd.DataFrame({
        t("İşlem", "Action"): [
            t("Kaydet", "Save"),
            t("Geri Al", "Undo"),
            t("Yinele", "Redo")
        ],
        t("Kısayol", "Shortcut"): [
            "Ctrl + S",
            "Ctrl + Z",
            "Ctrl + Y"
        ]
    }))


# --- EXCEL KODLARI ---
with t3:
    st.subheader("VBA")

    st.code("""
Sub VeriTemizle()
    Selection.ClearContents
    MsgBox "Temizlendi!"
End Sub
""", language="vba")


# --- VERİ TEMİZLEME ---
with t4:
    st.markdown(f"""
    <div class="dark-card">
        <h4>{t("Temizleme Formülleri", "Cleaning Formulas")}</h4>
        • =TRIM(A1)<br>
        • =PROPER(A1)<br>
    </div>
    """, unsafe_allow_html=True)


# --- RAPORLAMA ---
with t5:
    st.markdown(f"""
    <div class="dark-card">
        <h4>{t("Dashboard İlkeleri", "Dashboard Principles")}</h4>
        • {t("Tablo kullan", "Use tables")}<br>
        • {t("Sade tut", "Keep it simple")}
    </div>
    """, unsafe_allow_html=True)
