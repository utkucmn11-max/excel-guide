import streamlit as st
import pandas as pd

# Sayfa Yapılandırması - Tam Genişlik ve Orta Odak
st.set_page_config(page_title="Excel Pro Rehberi | Utku", page_icon="📗", layout="wide")

# --- KUSURSUZ CSS (Karanlık Mod & Orta Hizalama) ---
st.markdown("""
    <style>
    /* Ana Arka Plan */
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* İçeriği Merkeze Hapsetme */
    .block-container {
        max-width: 950px;
        margin: 0 auto;
        padding-top: 2rem;
    }

    /* Başlıklar */
    h1, h2, h3 { 
        text-align: center !important; 
        color: #2EA043 !important; 
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Üst Menü (Sekmeler) Tasarımı */
    .stTabs [data-baseweb="tab-list"] {
        display: flex;
        justify-content: center;
        gap: 15px;
        background-color: #161B22;
        padding: 10px;
        border-radius: 15px;
        border: 1px solid #30363D;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #8B949E;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 25px;
    }

    /* Seçili (Aktif) Başlık Vurgusu */
    .stTabs [aria-selected="true"] {
        background-color: #2EA043 !important;
        color: white !important;
        box-shadow: 0 4px 15px rgba(46, 160, 67, 0.3);
    }

    /* Profesyonel Kartlar */
    .pro-card {
        background-color: #1C2128;
        padding: 25px;
        border-radius: 12px;
        border-left: 5px solid #2EA043;
        border-right: 1px solid #30363D;
        border-bottom: 1px solid #30363D;
        margin-bottom: 20px;
        text-align: center;
    }

    /* Metrikler */
    [data-testid="stMetric"] {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 12px;
        text-align: center;
        padding: 15px;
    }

    code { color: #FF7B72 !important; background-color: #0D1117 !important; padding: 4px; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST LOGO VE BAŞLIK ---
col_logo, col_empty = st.columns([1, 10]) # Logo için hizalama
with col_logo:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=70)

st.markdown("<h1>EXCEL MASTER PORTALI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8B949E;'>Profesyonel Veri Yönetimi ve Kısayol Akademisi</p>", unsafe_allow_html=True)

# --- ANA SEKMELER ---
t1, t2, t3, t4, t5 = st.tabs([
    "🌌 Dashboard", 
    "⌨️ Ninja Tuşları", 
    "🧪 Formül Analizi", 
    "🧹 Veri Hijyeni", 
    "📊 Raporlama"
])

# --- 1. DASHBOARD ---
with t1:
    st.markdown("<br>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    m1.metric("Kayıtlı Veri", "150+", "Kısayol & İpucu")
    m2.metric("Verimlilik", "%95", "Optimize")
    m3.metric("Geliştirici", "Utku", "v6.0 Pro")
    
    st.markdown("""
    <div class="pro-card">
        <h3>🚀 Uzmanlığa İlk Adım</h3>
        <p>Excel'de ustalık, klavye hakimiyeti ile başlar. Bu portalda her şey merkeze odaklı ve 
        dikkat dağıtıcı unsurlardan temizlenmiştir. Üstteki sekmeleri kullanarak eğitimlere başlayabilirsin.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. KISAYOLLAR ---
with t2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("⌨️ En Çok Kullanılan Ninja Kısayolları")
    
    ks_data = {
        "İşlem": ["Kaydet", "Geri Al", "Yinele", "Kopyala", "Yapıştır", "Kes", "Tümünü Seç", "Bul / Değiştir"],
        "Kısayol (TR/EN)": ["Ctrl + S", "Ctrl + Z", "Ctrl + Y", "Ctrl + C", "Ctrl + V", "Ctrl + X", "Ctrl + A", "Ctrl + F / H"]
    }
    st.table(pd.DataFrame(ks_data))
    
    st.markdown("""
    <div class="pro-card">
        <b>💡 Kritik İpucu:</b> Hücreyi kilitlemek (Sabitlemek) için <b>F4</b> tuşunu kullanmayı unutma!
    </div>
    """, unsafe_allow_html=True)

# --- 3. FORMÜLLER ---
with t3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="pro-card">
        <h3>🔍 XLOOKUP (ÇAPRAZARA)</h3>
        <p>Eski nesil Düşeyara'nın (VLOOKUP) tahtını yıkan en güçlü fonksiyon.</p>
        <code>=ÇAPRAZARA(aranan_değer; arama_dizisi; döndürülen_dizi)</code>
    </div>
    <div class="pro-card">
        <h3>🔒 Hücre Sabitleme ($) Mantığı</h3>
        • <b>$A$1 :</b> Tam Kilit <br>
        • <b>A$1 :</b> Satır Kilit <br>
        • <b>$A1 :</b> Sütun Kilit
    </div>
    """, unsafe_allow_html=True)

# --- 4. VERİ TEMİZLEME ---
with t4:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="pro-card">
        <h3>🧹 Veri Temizleme Araçları</h3>
        • <b>=KIRP(A1) :</b> Gereksiz boşlukları temizler.<br>
        • <b>=YAZIM.DÜZENİ(A1) :</b> Baş harfleri büyütür.<br>
        • <b>=EĞERHATA(Formül; 0) :</b> Hatalı sonuçları gizler.
    </div>
    """, unsafe_allow_html=True)

# --- 5. RAPORLAMA ---
with t5:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="pro-card">
        <h3>📊 Profesyonel Dashboard Kuralları</h3>
        1. Daima <b>CTRL + T</b> ile tablo formatını kullan.<br>
        2. Raporlarına interaktif <b>Dilimleyiciler (Slicers)</b> ekle.<br>
        3. Karmaşık grafikler yerine sade ve anlaşılır görseller seç.
    </div>
    """, unsafe_allow_html=True)
