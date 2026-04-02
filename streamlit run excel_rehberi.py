import streamlit as st
import pandas as pd

# Sayfa Yapılandırması
st.set_page_config(page_title="Excel Master Pro | Utku", page_icon="📗", layout="wide")

# --- DİL SÖZLÜĞÜ ---
texts = {
    "Türkçe": {
        "title": "EXCEL MASTER PROFESYONEL PORTALI",
        "subtitle": "İleri Seviye Veri Analizi ve Kısayol Eğitim Platformu",
        "tabs": ["🌌 Dashboard", "⌨️ Kısayollar", "🧪 Formüller", "🧹 Veri Temizleme", "📊 Raporlama"],
        "m1_label": "Kısayol Sayısı", "m1_val": "120+", "m1_delta": "Full Paket",
        "m2_label": "Verimlilik Artışı", "m2_val": "%95", "m2_delta": "Maksimum",
        "m3_label": "Geliştirici", "m3_val": "Utku", "m3_delta": "v6.0 Pro",
        "card_h3": "🚀 Neden Bu Platform?",
        "card_p": "Excel'de fare kullanmayı bıraktığınızda, sadece hızlanmazsınız; veriye olan bakış açınız değişir. Bu centered (ortalanmış) arayüz, odağınızı sadece bilgiye yöneltmek için tasarlandı.",
        "shortcut_sub": ["🚀 Temel & Navigasyon", "🎨 Biçim", "🧮 Giriş & Yönetim"],
        "table_h": "Navigasyon Ninja Tuşları",
        "table_h2": "Hücre ve Veri Biçimlendirme",
        "table_cols": ["İşlem", "Kısayol"],
        "formula_h": "🔍 XLOOKUP (ÇAPRAZARA)",
        "formula_p": "Yeni nesil arama fonksiyonu. Sütun saymaya veda edin!",
        "fix_h": "🔒 Sabitleme ($) Mantığı",
        "fix_p": "Hücreleri kilitlemek için <b>F4</b> tuşunu kullanın.",
        "clean_h": "🧹 Temizleme Formülleri",
        "report_h": "📊 Dashboard Tasarım İlkeleri"
    },
    "English": {
        "title": "EXCEL MASTER PROFESSIONAL PORTAL",
        "subtitle": "Advanced Data Analysis and Shortcut Training Platform",
        "tabs": ["🌌 Dashboard", "⌨️ Shortcuts", "🧪 Formulas", "🧹 Data Cleaning", "📊 Reporting"],
        "m1_label": "Shortcut Count", "m1_val": "120+", "m1_delta": "Full Pack",
        "m2_label": "Efficiency Increase", "m2_val": "%95", "m2_delta": "Maximum",
        "m3_label": "Developer", "m3_val": "Utku", "m3_delta": "v6.0 Pro",
        "card_h3": "🚀 Why This Platform?",
        "card_p": "When you stop using the mouse in Excel, you don't just speed up; your perspective on data changes. This centered interface is designed to focus your attention only on knowledge.",
        "shortcut_sub": ["🚀 Basics & Nav", "🎨 Format", "🧮 Input & Mgmt"],
        "table_h": "Navigation Ninja Keys",
        "table_h2": "Cell and Data Formatting",
        "table_cols": ["Action", "Shortcut"],
        "formula_h": "🔍 XLOOKUP",
        "formula_p": "Next generation search function. Say goodbye to column counting!",
        "fix_h": "🔒 Absolute Reference ($)",
        "fix_p": "Use the <b>F4</b> key to lock cells.",
        "clean_h": "🧹 Cleaning Formulas",
        "report_h": "📊 Dashboard Design Principles"
    }
}

# --- GELİŞMİŞ CSS (Sağ Alt Köşe Düzenlemesi Dahil) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* İçeriği Merkeze Hapsetme */
    .block-container {
        max-width: 1000px;
        margin: 0 auto;
        padding-top: 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    h1, h2, h3, h4 { text-align: center !important; color: #2EA043 !important; font-family: 'Segoe UI', sans-serif; }
    .stMarkdown p { color: #8B949E !important; text-align: center; }

    .stTabs [data-baseweb="tab-list"] {
        display: flex; justify-content: center; gap: 15px; background-color: #161B22;
        padding: 10px; border-radius: 15px; border: 1px solid #30363D; margin-bottom: 30px;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #2EA043 !important; color: white !important;
        box-shadow: 0 4px 15px rgba(46, 160, 67, 0.4); transform: scale(1.05);
    }

    .dark-card {
        background-color: #1C2128; padding: 30px; border-radius: 15px;
        border: 1px solid #30363D; border-top: 4px solid #2EA043;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin-bottom: 25px; width: 100%; text-align: center;
    }

    [data-testid="stMetric"] { background-color: #161B22; padding: 20px; border-radius: 15px; border: 1px solid #30363D; text-align: center; }
    code { color: #FF7B72 !important; background-color: #0D1117 !important; border-radius: 5px; padding: 3px 8px; }

    /* SAĞ ALT KÖŞE DİL SEÇİCİ STİLİ */
    [data-testid="stVerticalBlock"] > div:last-child {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 999;
        background-color: #1C2128;
        padding: 5px;
        border-radius: 10px;
        border: 1px solid #2EA043;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST BÖLÜM ---
st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=90)

# --- DİL SEÇİMİ (Sağ Alt Köşe İçin Değişken Tanımı) ---
# Not: Streamlit'te en sona eklenen eleman CSS ile sağ alta sabitlendi
lang = st.selectbox("🌐", ["Türkçe", "English"], index=0)
t = texts[lang]

st.markdown(f"<h1>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p>{t['subtitle']}</p>", unsafe_allow_html=True)

# --- ANA NAVİGASYON ---
t1, t2, t3, t4, t5 = st.tabs(t["tabs"])

with t1:
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric(t["m1_label"], t["m1_val"], t["m1_delta"])
    c2.metric(t["m2_label"], t["m2_val"], t["m2_delta"])
    c3.metric(t["m3_label"], t["m3_val"], t["m3_delta"])
    
    st.markdown(f"""
    <div class="dark-card">
        <h3>{t['card_h3']}</h3>
        <p>{t['card_p']}</p>
    </div>
    """, unsafe_allow_html=True)

with t2:
    st.markdown("<br>", unsafe_allow_html=True)
    sub1, sub2, sub3 = st.tabs(t["shortcut_sub"])
    with sub1:
        st.subheader(t["table_h"])
        st.table(pd.DataFrame({
            t["table_cols"][0]: ["Kaydet", "Geri Al", "Kopyala/Yapıştır", "Tümünü Seç", "Veri Sonuna Git", "A1'e Dön"],
            t["table_cols"][1]: ["Ctrl + S", "Ctrl + Z", "Ctrl + C / V", "Ctrl + A", "Ctrl + Ok", "Ctrl + Home"]
        }))
    # ... diğer alt sekmeler metinleri t[] içinden alarak devam eder ...

with t3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<div class='dark-card'><h3>{t['formula_h']}</h3><p>{t['formula_p']}</p></div>", unsafe_allow_html=True)

with t4:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<div class='dark-card'><h4>{t['clean_h']}</h4></div>", unsafe_allow_html=True)

with t5:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<div class='dark-card'><h4>{t['report_h']}</h4></div>", unsafe_allow_html=True)
