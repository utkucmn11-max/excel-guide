import streamlit as st
import pandas as pd

# Sayfa Yapılandırması
st.set_page_config(page_title="Excel Master Pro | Centered", page_icon="📗", layout="wide")

# --- GELİŞMİŞ CSS (Aktif Başlık Vurgusu & Tam Simetri) ---
st.markdown("""
    <style>
    /* Ana Arka Plan */
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

    /* Başlıklar ve Metinler */
    h1, h2, h3, h4 { 
        text-align: center !important; 
        color: #2EA043 !important; 
        font-family: 'Segoe UI', sans-serif; 
    }
    
    .stMarkdown p { color: #8B949E !important; text-align: center; }

    /* Üst Menü Sekme Tasarımı */
    .stTabs [data-baseweb="tab-list"] {
        display: flex;
        justify-content: center;
        gap: 15px;
        background-color: #161B22;
        padding: 10px;
        border-radius: 15px;
        border: 1px solid #30363D;
        margin-bottom: 30px;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #8B949E;
        font-weight: bold;
        padding: 10px 25px;
        border-radius: 10px;
        transition: all 0.3s ease;
    }

    /* SEÇİLİ BAŞLIK VURGUSU */
    .stTabs [aria-selected="true"] {
        background-color: #2EA043 !important;
        color: white !important;
        box-shadow: 0 4px 15px rgba(46, 160, 67, 0.4);
        transform: scale(1.05);
    }

    /* Profesyonel Kart Tasarımları */
    .dark-card {
        background-color: #1C2128;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #30363D;
        border-top: 4px solid #2EA043;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 25px;
        width: 100%;
        text-align: center;
    }

    /* Metrikler */
    [data-testid="stMetric"] {
        background-color: #161B22;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #30363D;
        text-align: center;
    }

    /* Tabloyu Ortala */
    .stTable {
        margin: 0 auto;
        width: 100% !important;
    }

    code { color: #FF7B72 !important; background-color: #0D1117 !important; border-radius: 5px; padding: 3px 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST BÖLÜM (LOGO & BAŞLIK) ---
st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=90)
st.markdown("<h1>EXCEL MASTER PROFESYONEL PORTALI</h1>", unsafe_allow_html=True)
st.markdown("<p>İleri Seviye Veri Analizi ve Kısayol Eğitim Platformu</p>", unsafe_allow_html=True)

# --- ANA NAVİGASYON (GELİŞMİŞ SEKMELER) ---
t1, t2, t3, t4, t5 = st.tabs([
    "🌌 Dashboard", 
    "⌨️ Kısayollar", 
    "🧪 Formüller", 
    "🧹 Veri Temizleme", 
    "📊 Raporlama"
])

# --- 1. DASHBOARD ---
with t1:
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Kısayol Sayısı", "120+", "Full Paket")
    c2.metric("Verimlilik Artışı", "%95", "Maksimum")
    c3.metric("Geliştirici", "Utku", "v6.0 Pro")
    
    st.markdown("""
    <div class="dark-card">
        <h3>🚀 Neden Bu Platform?</h3>
        <p>Excel'de fare kullanmayı bıraktığınızda, sadece hızlanmazsınız; veriye olan bakış açınız değişir. 
        Bu centered (ortalanmış) arayüz, odağınızı sadece bilgiye yöneltmek için tasarlandı. 
        Her sekmede profesyonel iş hayatınızda kullanacağınız gerçek çözümler yer alıyor.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. KISAYOLLAR ---
with t2:
    st.markdown("<br>", unsafe_allow_html=True)
    sub1, sub2, sub3 = st.tabs(["🚀 Temel & Navigasyon", "🎨 Biçim", "🧮 Giriş & Yönetim"])
    
    with sub1:
        st.subheader("Navigasyon Ninja Tuşları")
        st.table(pd.DataFrame({
            "İşlem": ["Kaydet", "Geri Al", "Kopyala/Yapıştır", "Tümünü Seç", "Veri Sonuna Git", "A1'e Dön", "Satır/Sütun Seç"],
            "Kısayol": ["Ctrl + S", "Ctrl + Z", "Ctrl + C / V", "Ctrl + A", "Ctrl + Ok Tuşları", "Ctrl + Home", "Shift/Ctrl + Boşluk"]
        }))

    with sub2:
        st.subheader("Hücre ve Veri Biçimlendirme")
        st.table(pd.DataFrame({
            "İşlem": ["Biçim Menüsü", "Kalın/İtalik/Altı Çizili", "Para Birimi", "Yüzde Biçimi", "Tarih Biçimi"],
            "Kısayol": ["Ctrl + 1", "Ctrl + B / I / U", "Ctrl + Shift + $", "Ctrl + Shift + %", "Ctrl + Shift + #"]
        }))

    with sub3:
        st.markdown("""
        <div class="dark-card">
            <h4>Hızlı Veri Yönetimi</h4>
            • <b>Alt + = :</b> Otomatik TOPLA fonksiyonu ekler.<br>
            • <b>Ctrl + ; / : :</b> Güncel Tarih ve Saat ekler.<br>
            • <b>Ctrl + D / R :</b> Üsttekini/Soldakini kopyalar.<br>
            • <b>Ctrl + Shift + + / - :</b> Satır/Sütun Ekle veya Sil.<br>
            • <b>Ctrl + 9 / 0 :</b> Satır veya Sütun Gizle.
        </div>
        """, unsafe_allow_html=True)

# --- 3. FORMÜLLER ---
with t3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dark-card">
        <h3>🔍 XLOOKUP (ÇAPRAZARA)</h3>
        <p>Yeni nesil arama fonksiyonu. Sütun saymaya veda edin!</p>
        <code>=ÇAPRAZARA(aranan_değer; arama_dizisi; döndürülen_dizi)</code>
    </div>
    <div class="dark-card">
        <h3>🔒 Sabitleme ($) Mantığı</h3>
        <p>Hücreleri kilitlemek için <b>F4</b> tuşunu kullanın.</p>
        <p>$A$1 (Tam Sabit) | A$1 (Satır Sabit) | $A1 (Sütun Sabit)</p>
    </div>
    """, unsafe_allow_html=True)

# --- 4. VERİ TEMİZLEME ---
with t4:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dark-card">
        <h4>🧹 Temizleme Formülleri</h4>
        • <b>=KIRP(A1) :</b> Boşlukları yok eder.<br>
        • <b>=YAZIM.DÜZENİ(A1) :</b> Metni standartlaştırır.<br>
        • <b>=EĞERHATA(Formül; 0) :</b> Hataları temiz gösterir.
    </div>
    """, unsafe_allow_html=True)

# --- 5. RAPORLAMA ---
with t5:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dark-card">
        <h4>📊 Dashboard Tasarım İlkeleri</h4>
        <p>1. Daima <b>Tablo (CTRL + T)</b> kullanın.</p>
        <p>2. Pivot tablolarınıza <b>Dilimleyiciler</b> ekleyin.</p>
        <p>3. Karmaşayı azaltın, veriyi sadeleştirin.</p>
    </div>
    """, unsafe_allow_html=True)
