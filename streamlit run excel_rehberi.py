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
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVİGASYON ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=100)
    st.markdown("### **Excel Master v4.5**")
    choice = st.radio("Eğitim Modülleri", 
        ["🌌 Dashboard", "⌨️ Ninja Kısayolları", "🧪 İleri Formül Analizi", "🧹 Veri Temizleme", "📊 Raporlama Sanatı"])
    st.markdown("---")
    st.markdown("👤 **Geliştirici:** Utku")

# --- 1. DASHBOARD ---
if choice == "🌌 Dashboard":
    st.markdown("<h1>📊 Excel Master Dashboard</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("Kayıtlı Kısayol", "50+", "Yeni Eklendi")
    col2.metric("İş Akış Hızı", "%85", "Maksimum")
    col3.metric("Veri Güvenliği", "Yüksek", "Stabil")
    
    st.markdown("""
    <div class="dark-card">
        <h3>🚀 Profesyonel Başlangıç</h3>
        <p>Excel'de fareyi ne kadar az kullanırsanız, o kadar profesyonelleşirsiniz. Bu rehber size klavye hakimiyeti ve veri yönetimi becerisi kazandırmak için tasarlandı.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. KISAYOLLAR (GÜNCELLENMİŞ VE GENİŞLETİLMİŞ) ---
elif choice == "⌨️ Ninja Kısayolları":
    st.markdown("<h1>⌨️ Profesyonel Kısayol Kütüphanesi</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["🔥 Temel & Navigasyon", "🎨 Biçimlendirme", "🧮 Formül & Giriş", "📁 Satır & Sayfa"])

    with tab1:
        st.subheader("Genel İşlemler & Hızlı Hareket")
        temel_data = {
            "İşlem": ["Kaydet", "Geri Al", "Yinele", "Kopyala", "Yapıştır", "Tümünü Seç", "Bul / Değiştir"],
            "Türkçe / İngilizce": ["Ctrl + S", "Ctrl + Z", "Ctrl + Y", "Ctrl + C", "Ctrl + V", "Ctrl + A", "Ctrl + F / H"]
        }
        st.table(pd.DataFrame(temel_data))
        
        st.markdown("""
        <div class="dark-card">
            <b>Navigasyon (Fare Yok!):</b><br>
            • <b>Ctrl + Ok Tuşları:</b> Verinin en sonuna ışınlanır.<br>
            • <b>Ctrl + Shift + Ok:</b> Gidilen yere kadar tüm veriyi seçer.<br>
            • <b>Ctrl + Home:</b> A1 hücresine geri döner.<br>
            • <b>Shift + Boşluk / Ctrl + Boşluk:</b> Tüm satırı veya sütunu seçer.
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.subheader("Veri Görünümünü Düzenleme")
        bicim_data = {
            "Biçim Türü": ["Kalın / İtalik / Altı Çizili", "Hücreleri Biçimlendir Menüsü", "Para Birimi ($/₺)", "Yüzde Biçimi (%)", "Tarih Biçimi"],
            "Kısayol": ["Ctrl + B / I / U", "Ctrl + 1", "Ctrl + Shift + $", "Ctrl + Shift + %", "Ctrl + Shift + #"]
        }
        st.table(pd.DataFrame(bicim_data))

    with tab3:
        st.subheader("Hızlı Veri Girişi")
        st.markdown("""
        <div class="dark-card">
            • <b>Alt + = :</b> Otomatik TOPLA fonksiyonu ekler.<br>
            • <b>Ctrl + ; :</b> Güncel Tarihi ekler.<br>
            • <b>Ctrl + Shift + : :</b> Güncel Saati ekler.<br>
            • <b>F2 :</b> Hücrenin içine girer.<br>
            • <b>Ctrl + D / R :</b> Üsttekini aşağı / Soldakini sağa kopyalar.
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.subheader("Yapısal Yönetim")
        yapi_data = {
            "İşlem": ["Yeni Satır/Sütun Ekle", "Satır/Sütun Sil", "Satırı / Sütunu Gizle", "Yeni Sayfa (Tab) Aç", "Sayfalar Arası Geçiş"],
            "Kısayol": ["Ctrl + Shift + +", "Ctrl + -", "Ctrl + 9 / 0", "Shift + F11", "Ctrl + PgUp / PgDn"]
        }
        st.table(pd.DataFrame(yapi_data))

# --- DİĞER BÖLÜMLER (MEVCUT YAPIYI KORUYORUZ) ---
elif choice == "🧪 İleri Formül Analizi":
    st.header("🧪 Formül Mühendisliği")
    with st.expander("🔍 XLOOKUP (ÇAPRAZARA)"):
        st.code("=ÇAPRAZARA(aranan_değer; arama_dizisi; döndürülen_dizi)")
    with st.expander(" Sabitleme ($) Mantığı"):
        st.write("F4 tuşu ile hücreyi kilitleyebilirsiniz: $A$1")

elif choice == "🧹 Veri Temizleme":
    st.header("🧹 Veri Hijyeni")
    st.info("KIRP, YAZIM.DÜZENİ ve TEMİZLE fonksiyonları ile kirli veriden kurtulun.")

elif choice == "📊 Raporlama Sanatı":
    st.header("📊 Etkileyici Dashboardlar")
    st.write("Dilimleyiciler (Slicers) ve Dinamik Grafikler ile raporlarınızı canlandırın.")
