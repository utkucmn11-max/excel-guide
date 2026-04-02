import streamlit as st
import pandas as pd

# Sayfa Yapılandırması
st.set_page_config(page_title="Excel Pro Rehberi | Dark Mode", page_icon="📗", layout="wide")

# --- DARK MODE & PROFESSIONAL GREEN CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    [data-testid="stSidebar"] { background-color: #161B22 !important; border-right: 1px solid #30363D; }
    h1, h2, h3, h4 { color: #2EA043 !important; font-family: 'Segoe UI', sans-serif; }
    .dark-card {
        background-color: #1C2128;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #2EA043;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        margin-bottom: 20px;
        border: 1px solid #30363D;
    }
    .stMetric { background-color: #1C2128; padding: 15px; border-radius: 10px; border: 1px solid #30363D; }
    code { color: #FF7B72 !important; background-color: #0D1117 !important; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #1C2128;
        border-radius: 5px 5px 0px 0px;
        padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVİGASYON ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=100)
    st.markdown("### **Excel Master v4.6**")
    choice = st.radio("Eğitim Modülleri", 
        ["🌌 Dashboard", "⌨️ Ninja Kısayolları", "🧪 İleri Formül Analizi", "🧹 Veri Temizleme", "📊 Raporlama Sanatı"])
    st.markdown("---")
    st.markdown("👤 **Geliştirici:** Utku")

# --- 1. DASHBOARD ---
if choice == "🌌 Dashboard":
    st.markdown("<h1>📊 Excel Master Dashboard</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("Kayıtlı Bilgi", "150+", "Zengin İçerik")
    col2.metric("İş Akış Hızı", "%90", "Maksimum")
    col3.metric("Tema", "Dark Mode", "Aktif")
    
    st.markdown("""
    <div class="dark-card">
        <h3>🚀 Profesyonel Başlangıç</h3>
        <p>Hoş geldin Utku. Bu rehber, bir Excel kullanıcısını "Ninja" seviyesine taşımak için optimize edildi. 
        Fareye veda etmeye ve formüllerle veri yönetmeye hazır ol.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. KISAYOLLAR ---
elif choice == "⌨️ Ninja Kısayolları":
    st.markdown("<h1>⌨️ Profesyonel Kısayol Kütüphanesi</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["🔥 Temel & Navigasyon", "🎨 Biçimlendirme", "🧮 Formül & Giriş", "📁 Satır & Sayfa"])

    with tab1:
        st.subheader("Genel İşlemler & Hızlı Hareket")
        temel_data = {
            "İşlem": ["Kaydet", "Geri Al", "Yinele", "Kopyala", "Yapıştır", "Kes", "Tümünü Seç", "Bul / Değiştir"],
            "Kısayol (TR/EN Ortak)": ["Ctrl + S", "Ctrl + Z", "Ctrl + Y", "Ctrl + C", "Ctrl + V", "Ctrl + X", "Ctrl + A", "Ctrl + F / H"]
        }
        st.table(pd.DataFrame(temel_data))
        
        st.markdown("""
        <div class="dark-card">
            <b>Hızlı Navigasyon (Fare Yok!):</b><br>
            • <b>Ctrl + Ok Tuşları:</b> Verinin en sonuna (Sınırına) ışınlanır.<br>
            • <b>Ctrl + Shift + Ok:</b> Gidilen yere kadar tüm hücreleri seçer.<br>
            • <b>Ctrl + Home:</b> Tablonun başına (A1) anında döner.<br>
            • <b>Shift + Boşluk:</b> Mevcut satırı komple seçer.<br>
            • <b>Ctrl + Boşluk:</b> Mevcut sütunu komple seçer.
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.subheader("Hücre ve Veri Biçimlendirme")
        bicim_data = {
            "Biçim Türü": ["Kalın Yaz (Bold)", "İtalik Yaz", "Altı Çizili", "Biçimlendirme Menüsü", "Para Birimi ($/₺)", "Yüzde Biçimi (%)", "Tarih Biçimi"],
            "Kısayol": ["Ctrl + B", "Ctrl + I", "Ctrl + U", "Ctrl + 1", "Ctrl + Shift + $", "Ctrl + Shift + %", "Ctrl + Shift + #"]
        }
        st.table(pd.DataFrame(bicim_data))

    with tab3:
        st.subheader("Formül ve Veri Girişi")
        st.markdown("""
        <div class="dark-card">
            • <b>Alt + = :</b> Otomatik TOPLA fonksiyonu ekler (Hayat kurtarır).<br>
            • <b>Ctrl + ; (Noktalı Virgül) :</b> Güncel Tarihi ekler.<br>
            • <b>Ctrl + Shift + : (İki Nokta) :</b> Güncel Saati ekler.<br>
            • <b>F2 :</b> Hücrenin içine girer (Düzenleme modu).<br>
            • <b>Ctrl + D (Down) :</b> Üstteki hücreyi aşağıya kopyalar.<br>
            • <b>Ctrl + R (Right) :</b> Soldaki hücreyi sağa kopyalar.
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.subheader("Satır, Sütun ve Sayfa Yönetimi")
        yapi_data = {
            "İşlem": ["Yeni Satır/Sütun Ekle", "Satır/Sütun Sil", "Satırı Gizle", "Sütunu Gizle", "Yeni Sayfa Aç", "Sayfalar Arası Geçiş"],
            "Kısayol": ["Ctrl + Shift + +", "Ctrl + -", "Ctrl + 9", "Ctrl + 0", "Shift + F11", "Ctrl + PgUp / PgDn"]
        }
        st.table(pd.DataFrame(yapi_data))

# --- 3. İLERİ FORMÜL ANALİZİ ---
elif choice == "🧪 İleri Formül Analizi":
    st.markdown("<h1>🧪 İleri Seviye Formül Mühendisliği</h1>", unsafe_allow_html=True)
    
    col_f1, col_f2 = st.columns(2)
    
    with col_f1:
        st.markdown("""
        <div class="dark-card">
            <h4>🔍 XLOOKUP (ÇAPRAZARA)</h4>
            <p>Excel'in en yeni ve güçlü arama fonksiyonudur. Soldan sağa arama zorunluluğunu kaldırır.</p>
            <code>=ÇAPRAZARA(aranan_değer; arama_dizisi; döndürülen_dizi)</code>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("📌 İNDİS & KAÇINCI"):
            st.write("Düşeyara'dan daha hızlı çalışır ve tablo yapısı değişse de bozulmaz.")
            st.code("=İNDİS(Dizi; KAÇINCI(Değer; Aranan_Dizi; 0))")

    with col_f2:
        st.markdown("""
        <div class="dark-card">
            <h4>🔒 Sabitleme ($) Mantığı</h4>
            <p>F4 tuşuna basarak hücreleri kilitlersiniz. Formülü kaydırdığınızda değerler bozulmaz.</p>
            • <b>$A$1 :</b> Tam Sabit<br>
            • <b>A$1 :</b> Satır Sabit<br>
            • <b>$A1 :</b> Sütun Sabit
        </div>
        """, unsafe_allow_html=True)

# --- 4. VERİ TEMİZLEME ---
elif choice == "🧹 Veri Temizleme":
    st.markdown("<h1>🧹 Veri Hijyeni ve Temizleme</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="dark-card">
        <h3>Profesyonel Veri Temizleme Fonksiyonları</h3>
        • <b>=KIRP(A1) :</b> Hücre içindeki tüm gereksiz boşlukları temizler.<br>
        • <b>=YAZIM.DÜZENİ(A1) :</b> Metinlerin baş harflerini büyütür, gerisini küçültür.<br>
        • <b>=TEMİZLE(A1) :</b> Yazdırılamayan karakterleri veriden atar.<br>
        • <b>=EĞERHATA(Formül; 0) :</b> Eğer formül hata verirse (#N/A gibi), yerine 0 veya istediğiniz metni yazar.
    </div>
    """, unsafe_allow_html=True)

# --- 5. RAPORLAMA SANATI ---
elif choice == "📊 Raporlama Sanatı":
    st.markdown("<h1>📊 Raporlama ve Dashboard Sanatı</h1>", unsafe_allow_html=True)
    st.write("Veriyi sadece listelemeyin, bir hikaye anlatın.")
    
    st.markdown("""
    <div class="dark-card">
        <h4>Dashboard İpuçları</h4>
        1. <b>Dilimleyiciler (Slicers):</b> Pivot tabloları interaktif butonlara dönüştürün.<br>
        2. <b>Dinamik Grafikler:</b> Veri eklendikçe kendini güncelleyen tablolar için CTRL+T kullanın.<br>
        3. <b>Koşullu Biçimlendirme:</b> Hedefin altında kalan hücreleri otomatik kırmızı yaparak dikkat çekin.
    </div>
    """, unsafe_allow_html=True)
