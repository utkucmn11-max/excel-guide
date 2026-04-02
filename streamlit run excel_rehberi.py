import streamlit as st
import pandas as pd

# Sayfa Yapılandırması
st.set_page_config(page_title="Excel Pro Rehberi | Active Design", page_icon="📗", layout="wide")

# --- GELİŞMİŞ CSS (Seçili Başlık Vurgusu ve Ortalama) ---
st.markdown("""
    <style>
    /* Ana Arka Plan */
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* Blok Konteyner Ayarı */
    .block-container {
        padding-top: 2rem;
        max-width: 1000px; /* İçeriği toplu tutmak için */
        margin: 0 auto;
    }

    /* Başlıklar */
    h1, h2, h3 { 
        text-align: center !important; 
        color: #2EA043 !important; 
        font-family: 'Segoe UI', sans-serif;
        margin-bottom: 20px;
    }
    
    /* Sekme (Tabs) Tasarımı */
    .stTabs [data-baseweb="tab-list"] {
        display: flex;
        justify-content: center;
        gap: 10px;
        background-color: #161B22;
        padding: 8px;
        border-radius: 12px;
        border: 1px solid #30363D;
        margin-bottom: 30px;
    }
    
    /* Seçili Olmayan Sekmeler */
    .stTabs [data-baseweb="tab"] {
        color: #8B949E;
        font-weight: 600;
        border-radius: 8px;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }

    /* SEÇİLİ BAŞLIK (Aktif Sekme) Vurgusu */
    .stTabs [aria-selected="true"] {
        background-color: #2EA043 !important; /* Parlak Yeşil */
        color: #FFFFFF !important;
        box-shadow: 0 0 15px rgba(46, 160, 67, 0.4);
        transform: scale(1.05); /* Hafif büyüme efekti */
    }

    /* Kartlar (Ortalanmış) */
    .dark-card {
        background-color: #1C2128;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #30363D;
        border-top: 4px solid #2EA043;
        margin-bottom: 25px;
        text-align: center;
    }
    
    /* Metrik Kutuları */
    [data-testid="stMetric"] {
        background-color: #161B22;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #30363D;
        text-align: center;
    }

    code { color: #FF7B72 !important; background-color: #0D1117 !important; border-radius: 4px; padding: 2px 6px; }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST BÖLÜM ---
st.markdown("<div style='text-align: center;'><img src='https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg' width='80'></div>", unsafe_allow_html=True)
st.markdown("<h1>EXCEL MASTER PORTALI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8B949E;'>Seçtiğiniz sekmeye göre profesyonel içerikler yüklenir.</p>", unsafe_allow_html=True)

# --- ANA NAVİGASYON ---
t1, t2, t3, t4, t5 = st.tabs([
    "🌌 Ana Panel", 
    "⌨️ Ninja Tuşları", 
    "🧪 Formül Dünyası", 
    "🧹 Temizlik Rehberi", 
    "📊 Rapor Tasarımı"
])

# --- İÇERİKLER (Her şey with bloğu içinde ve ortalı) ---

with t1:
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Kayıtlar", "120+", "Kısayol")
    c2.metric("Hız", "3X", "Artış")
    c3.metric("Tema", "Dark", "Vurgulu")
    
    st.markdown("""
    <div class="dark-card">
        <h3>🚀 Profesyonel Odak Modu</h3>
        <p>Şu an <b>Ana Panel</b> sekmesindesiniz. Yukarıdaki yeşil vurgulu başlıklar arasında geçiş yaparak 
        öğrenmek istediğiniz uzmanlık alanına odaklanabilirsiniz. Tasarım, dikkatinizin dağılmaması için 
        tamamen merkezi simetride tutulmuştur.</p>
    </div>
    """, unsafe_allow_html=True)

with t2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("⌨️ En Kritik Klavye Kombinasyonları")
    # Tabloyu merkeze almak için kolon kullanıyoruz
    st.table(pd.DataFrame({
        "İşlem": ["Kaydet", "Geri Al", "Kopyala", "Yapıştır", "Filtrele", "Tablo Yap", "A1'e Git"],
        "Kısayol": ["Ctrl + S", "Ctrl + Z", "Ctrl + C", "Ctrl + V", "Ctrl+Shift+L", "Ctrl + T", "Ctrl + Home"]
    }))

with t3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dark-card">
        <h3>🔍 ÇAPRAZARA (XLOOKUP)</h3>
        <code>=ÇAPRAZARA(aranan_değer; arama_dizisi; döndürülen_dizi)</code>
        <p style='margin-top:15px;'>Hücreleri Sabitlemek için: <b>F4 Tuşu</b> ($A$1)</p>
    </div>
    """, unsafe_allow_html=True)

with t4:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dark-card">
        <h3>🧹 Veri Temizleme Standartları</h3>
        • <b>=KIRP() :</b> Gereksiz boşluklar.<br>
        • <b>=YAZIM.DÜZENİ() :</b> Büyük/Küçük harf standardı.<br>
        • <b>=EĞERHATA() :</b> Temiz rapor görünümü.
    </div>
    """, unsafe_allow_html=True)

with t5:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dark-card">
        <h3>📊 Etkileyici Dashboard Kuralları</h3>
        <p>1. Fareyi değil, <b>Dilimleyicileri</b> kullandırın.</p>
        <p>2. Pivot Tablo verilerini <b>Dinamik Grafiklere</b> bağlayın.</p>
        <p>3. Renkleri sade tutun (Beyaz, Siyah ve Excel Yeşili).</p>
    </div>
    """, unsafe_allow_html=True)
