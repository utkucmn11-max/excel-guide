import streamlit as st
import pandas as pd

# Sayfa Yapılandırması
st.set_page_config(page_title="Excel Master Pro | Utku", page_icon="📗", layout="wide")

# --- DİL SÖZLÜĞÜ ---
texts = {
    "Türkçe": {
        "lang_label": "Dil Seçin",
        "title": "EXCEL MASTER PROFESYONEL PORTALI",
        "subtitle": "Utku Tarafından Geliştirilen İleri Seviye Eğitim Platformu",
        "tabs": ["🌌 Dashboard", "⌨️ Kısayollar", "💻 Excel Kodları", "🧹 Veri Temizleme", "📊 Raporlama"],
        "welcome_title": "🚀 Hoş Geldin Utku",
        "welcome_text": "Excel'de ustalaşmak için fareyi kenara bırakmanın vakti geldi. Bu platform, odağınızı bilgiye yöneltmek için tasarlandı.",
        "metric_1": "Kayıtlı Veri",
        "metric_2": "Hız Artışı",
        "metric_3": "Versiyon",
        "shortcut_table_title": "Temel İşlemler & Navigasyon",
        "vba_title": "1. VBA (Makrolar)",
        "vba_desc": "Masaüstü Excel'de rutin işleri otomatize eder.",
        "clean_title": "🧹 Temizleme Formülleri",
        "report_title": "📊 Tasarım İlkeleri"
    },
    "English": {
        "lang_label": "Select Language",
        "title": "EXCEL MASTER PROFESSIONAL PORTAL",
        "subtitle": "Advanced Training Platform Developed by Utku",
        "tabs": ["🌌 Dashboard", "⌨️ Shortcuts", "💻 Excel Codes", "🧹 Data Cleaning", "📊 Reporting"],
        "welcome_title": "🚀 Welcome Utku",
        "welcome_text": "It's time to put the mouse aside to master Excel. This platform is designed to focus your attention on knowledge.",
        "metric_1": "Saved Data",
        "metric_2": "Speed Up",
        "metric_3": "Version",
        "shortcut_table_title": "Basic Operations & Navigation",
        "vba_title": "1. VBA (Macros)",
        "vba_desc": "Automates routine tasks in the desktop application.",
        "clean_title": "🧹 Cleaning Formulas",
        "report_title": "📊 Design Principles"
    }
}

# --- GELİŞMİŞ CSS (Bozmadan Korundu + Dil Seçici Özelleştirme) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* İçeriği Merkeze Sabitleme */
    .block-container {
        max-width: 950px;
        margin: 0 auto;
        padding-top: 1rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* Sol Üst Dil Seçici Alanı */
    .lang-container {
        align-self: flex-start;
        width: 150px;
        margin-bottom: -50px; /* Logoyla hizalamak için */
    }

    h1, h2, h3, h4 { text-align: center !important; color: #2EA043 !important; font-family: 'Segoe UI', sans-serif; }
    
    .stTabs [data-baseweb="tab-list"] {
        display: flex; justify-content: center; gap: 12px; background-color: #161B22;
        padding: 8px; border-radius: 15px; border: 1px solid #30363D; margin-top: 20px;
    }

    .stTabs [aria-selected="true"] {
        background-color: #2EA043 !important; color: white !important;
        box-shadow: 0 4px 20px rgba(46, 160, 67, 0.4); transform: scale(1.05);
    }

    .dark-card {
        background-color: #1C2128; padding: 25px; border-radius: 15px;
        border: 1px solid #30363D; border-top: 4px solid #2EA043;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin-bottom: 20px; width: 100%; text-align: center;
    }

    [data-testid="stMetric"] { background-color: #161B22; padding: 15px; border-radius: 12px; border: 1px solid #30363D; text-align: center; }
    code { color: #FF7B72 !important; background-color: #0D1117 !important; border-radius: 5px; padding: 3px 8px; }
    
    /* Selectbox Styling */
    div[data-baseweb="select"] > div {
        background-color: #1C2128 !important;
        border: 1px solid #30363D !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SOL ÜST DİL SEÇİCİ ---
col1, col2 = st.columns([1, 4])
with col1:
    # Sidebar yerine doğrudan sayfa içinde sol üstte
    lang_choice = st.selectbox("", ["Türkçe", "English"], label_visibility="collapsed")
    t = texts[lang_choice]

# --- ÜST BÖLÜM (LOGO & BAŞLIK) ---
st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=80)
st.markdown(f"<h1>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #8B949E;'>{t['subtitle']}</p>", unsafe_allow_html=True)

# --- ANA SEKMELER ---
t1, t2, t3, t4, t5 = st.tabs(t["tabs"])

# --- 1. DASHBOARD ---
with t1:
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric(t["metric_1"], "150+", "Full")
    c2.metric(t["metric_2"], "3X", "Turbo")
    c3.metric(t["metric_3"], "v8.5", "Global")
    
    st.markdown(f"""
    <div class="dark-card">
        <h3>{t['welcome_title']}</h3>
        <p>{t['welcome_text']}</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. KISAYOLLAR ---
with t2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(t["shortcut_table_title"])
    st.table(pd.DataFrame({
        "İşlem / Action": ["Kaydet", "Geri Al", "Kopyala/Yapıştır", "Tümünü Seç", "Filtre", "Tablo Yap", "A1'e Dön"],
        "Kısayol": ["Ctrl + S", "Ctrl + Z", "Ctrl + C / V", "Ctrl + A", "Ctrl+Shift+L", "Ctrl + T", "Ctrl + Home"]
    }))

# --- 3. EXCEL KODLARI ---
with t3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<h3>{t['vba_title']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='dark-card'><p>{t['vba_desc']}</p></div>", unsafe_allow_html=True)
    st.code("Sub HelloUtku()\n    Range('A1').Value = 'Excel Master'\nEnd Sub", language="vba")
    st.info("Alt + F11 > Insert > Module")

# --- 4. VERİ TEMİZLEME ---
with t4:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="dark-card">
        <h4>{t['clean_title']}</h4>
        • <b>=KIRP() / TRIM()</b><br>
        • <b>=YAZIM.DÜZENİ() / PROPER()</b><br>
        • <b>=EĞERHATA() / IFERROR()</b>
    </div>
    """, unsafe_allow_html=True)

# --- 5. RAPORLAMA ---
with t5:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="dark-card">
        <h4>{t['report_title']}</h4>
        • Pivot Tables & Slicers<br>
        • Dynamic Dashboards<br>
        • Clean Data Structure
    </div>
    """, unsafe_allow_html=True)
