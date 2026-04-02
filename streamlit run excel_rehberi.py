import streamlit as st
import pandas as pd
import locale

# Sayfa ayarı
st.set_page_config(page_title="Excel Master Pro | Utku", page_icon="📗", layout="wide")

# --- DİL ALGILAMA (KURULUMSUZ) ---
if "lang" not in st.session_state:
    try:
        system_lang = locale.getdefaultlocale()[0]
        if system_lang and "tr" in system_lang.lower():
            st.session_state.lang = "Türkçe"
        else:
            st.session_state.lang = "English"
    except:
        st.session_state.lang = "English"

# Manuel seçim
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
    margin: auto;
    text-align: center;
}
.dark-card {
    background-color: #1C2128;
    padding: 20px;
    border-radius: 15px;
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)


# --- BAŞLIK ---
st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=90)

st.markdown(f"# {t('EXCEL MASTER PROFESYONEL PORTALI', 'EXCEL MASTER PROFESSIONAL PORTAL')}")
st.markdown(t(
    "Utku tarafından geliştirildi",
    "Developed by Utku"
))


# --- SEKMELER ---
t1, t2, t3 = st.tabs([
    "🌌 Dashboard",
    t("⌨️ Kısayollar", "⌨️ Shortcuts"),
    t("💻 Kodlar", "💻 Codes")
])


# --- DASHBOARD ---
with t1:
    col1, col2 = st.columns(2)
    col1.metric(t("Veri", "Data"), "150+")
    col2.metric(t("Hız", "Speed"), "3X")

    st.markdown(f"""
    <div class="dark-card">
        <h3>{t("Hoş geldin!", "Welcome!")}</h3>
        <p>{t("Excel öğrenme platformuna giriş yaptın.", "You entered the Excel learning platform.")}</p>
    </div>
    """, unsafe_allow_html=True)


# --- KISAYOLLAR ---
with t2:
    st.subheader(t("Temel Kısayollar", "Basic Shortcuts"))

    st.table(pd.DataFrame({
        t("İşlem", "Action"): [
            t("Kaydet", "Save"),
            t("Kopyala", "Copy"),
            t("Yapıştır", "Paste")
        ],
        t("Kısayol", "Shortcut"): [
            "Ctrl + S",
            "Ctrl + C",
            "Ctrl + V"
        ]
    }))


# --- KODLAR ---
with t3:
    st.subheader("VBA")

    st.code("""
Sub Temizle()
    Selection.ClearContents
End Sub
""", language="vba")
