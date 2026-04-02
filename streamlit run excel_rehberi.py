import streamlit as st
import pandas as pd

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Excel Master Rehberi",
    page_icon="📗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS (Profesyonel Görünüm İçin) ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .excel-card {
        background-color: #ffffff;
        padding: 20px;
        border-left: 5px solid #217346;
        border-radius: 5px;
        margin-bottom: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.03);
    }
    </style>
    """, unsafe_allow_index=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg/1200px-Microsoft_Office_Excel_%282019%E2%80%93present%29.svg.png", width=100)
    st.title("Excel Rehberi")
    st.info("Bu rehber, temelden ileri seviyeye tüm Excel bilgilerini içerir.")
    menu = st.radio(
        "Kategoriler",
        ["🏠 Ana Sayfa", "⌨️ Kısayol Kütüphanesi", "🧪 Formüller & Fonksiyonlar", "📊 Veri Analizi & Pivot", "⚠️ Hata Kılavuzu"]
    )
    st.markdown("---")
    st.write("👤 Geliştirici: **Utku**")

# --- İÇERİK BÖLÜMLERİ ---

if menu == "🏠 Ana Sayfa":
    st.title("Excel'de Ustalaşmaya Hazır Mısın?")
    st.markdown("""
    <div class="excel-card">
        <h3>Neden Excel Öğrenmelisiniz?</h3>
        <p>Excel, dünya genelinde iş dünyasının dilidir. Veriyi yönetmek, analiz etmek ve görselleştirmek için en güçlü araçtır.</p>
    </div>
    """, unsafe_allow_index=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Toplam Fonksiyon", "450+", "+12 Yeni")
    col2.metric("Kullanıcı Kitlesi", "1.2 Milyar", "Dünya Geneli")
    col3.metric("Öğrenme Süresi", "4 Hafta", "Düzenli Çalışma")

elif menu == "⌨️ Kısayol Kütüphanesi":
    st.header("Hız Kazandıracak Kısayollar")
    
    tab1, tab2, tab3 = st.tabs(["Genel", "Hücre Yönetimi", "Veri Seçimi"])
    
    with tab1:
        shortcuts = {
            "Kısayol": ["F4", "ALT + =", "CTRL + ;", "CTRL + Shift + 1", "CTRL + T"],
            "Fonksiyon": ["Son işlemi tekrarla / Sabitleme", "Otomatik Toplam", "Güncel Tarihi Ekle", "Sayı Biçimi (Virgüllü)", "Tablo Oluştur"]
        }
        st.table(pd.DataFrame(shortcuts))
    
    with tab2:
        st.write("**Hücre Düzenleme:** F2 tuşu ile hücre içine girebilirsiniz.")
        st.write("**Yorum Ekleme:** Shift + F2")

elif menu == "🧪 Formüller & Fonksiyonlar":
    st.header("Fonksiyonlar Sözlüğü")
    
    search = st.text_input("🔍 Fonksiyon Ara (Örn: DÜŞEYARA, EĞER...)")
    
    with st.expander("📍 Arama ve Başvuru Fonksiyonları"):
        st.markdown("""
        * **DÜŞEYARA (VLOOKUP):** Bir tablodaki veriyi başka bir yerde arar.
        * **İNDİS & KAÇINCI:** Düşeyara'nın daha profesyonel ve hızlı alternatifidir.
        * **XLOOKUP (ÇAPRAZARA):** Yeni nesil en güçlü arama fonksiyonu.
        """)
        
    with st.expander("📝 Metin Fonksiyonları"):
        st.code("=BİRLEŞTİR(A1; B1)  ->  İki hücreyi birleştirir.")
        st.code("=SOLDAN(A1; 3)  ->  Soldan ilk 3 karakteri alır.")

elif menu == "📊 Veri Analizi & Pivot":
    st.header("Veriyi Bilgiye Dönüştürün")
    st.markdown("""
    ### Pivot Tablo (Özet Tablo) Nedir?
    Binlerce satırlık veriyi saniyeler içinde özetlemenizi sağlayan en güçlü Excel özelliğidir.
    
    **Nasıl Yapılır?**
    1. Verinizi seçin.
    2. `Ekle > PivotTable` yolunu izleyin.
    3. Alanları sürükle-bırak yöntemiyle Satır ve Değerlere yerleştirin.
    """)
    st.image("https://img-c.udemycdn.com/redactor/raw/2019-01-30_15-18-05-9610f63b0646c075783307a048701986.png", caption="Pivot Tablo Mantığı")

elif menu == "⚠️ Hata Kılavuzu":
    st.header("Excel Hataları ve Çözümleri")
    errors = {
        "Hata Kodu": ["#SAYI/0!", "#AD?", "#DEĞER!", "#BAŞV!"],
        "Anlamı": ["Sıfıra bölme hatası", "Formül adı yanlış yazılmış", "Yanlış veri tipi (Metinle sayı toplama gibi)", "Geçersiz hücre başvurusu (Silinmiş hücre)"],
        "Çözüm": ["Bölenin 0 olmadığını kontrol et", "Yazımı kontrol et", "Hücre biçimini düzelt", "Formülün referansını güncelle"]
    }
    st.table(pd.DataFrame(errors))
