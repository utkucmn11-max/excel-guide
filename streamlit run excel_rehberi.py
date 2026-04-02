import streamlit as st
import pandas as pd

# Sayfa Genişliği ve Tarayıcı Sekmesi Ayarları
st.set_page_config(
    page_title="Excel Master Rehberi",
    page_icon="📗",
    layout="wide"
)

# --- GELİŞMİŞ CSS (Yeşil & Beyaz Kurumsal Tema) ---
st.markdown("""
    <style>
    /* Ana Arka Plan */
    .stApp {
        background-color: #fcfcfa;
    }
    
    /* Yan Menü (Sidebar) Stil */
    [data-testid="stSidebar"] {
        background-color: #fffffa !important;
        border-right: 2px solid #217346;
    }
    
    /* Kart Tasarımları */
    .info-card {
        background-color: #fffffa;
        padding: 25px;
        border-radius: 12px;
        border-top: 5px solid #217346;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        color: #333;
    }
    
    /* Başlık Renkleri */
    h1, h2, h3 {
        color: #217346 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Buton ve Linklerin Üzerine Gelince Değişen Renkler */
    .stRadio > div {
        gap: 10px;
    }
    
    /* Metrik Alanları */
    div[data-testid="stMetricValue"] {
        color: #217346 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (NAVİGASYON) ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=120)
    st.markdown("## **Excel Eğitim Portalı**")
    st.write("Profesyonel Gelişim Platformu")
    st.markdown("---")
    
    choice = st.radio(
        "Kategoriler",
        ["🏠 Dashboard", "⌨️ Kısayol Ansiklopedisi", "🧪 Formüller & Mantık", "📉 Veri Analizi", "⚙️ Ayarlar & Püf Noktaları"]
    )
    
    st.markdown("---")
    st.success("**Geliştirici:** Utku\n\n*Hızlı, Pratik, Profesyonel*")

# --- SAYFA İÇERİKLERİ ---

# 1. DASHBOARD (ANA SAYFA)
if choice == "🏠 Dashboard":
    st.markdown("<h1>📊 Excel Master Dashboard</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Öğrenilebilir Fonksiyon", value="480+", delta="Haftalık Güncel")
    with col2:
        st.metric(label="Kısayol Kombinasyonu", value="120", delta="Hız %40 Artar")
    with col3:
        st.metric(label="Zorluk Seviyesi", value="Başlangıç-İleri", delta="Hepsi İçin")

    st.markdown("""
    <div class="info-card">
        <h3>🚀 Neden Bu Rehber?</h3>
        <p>İş hayatında en çok kullanılan araç olan Excel'i, karmaşadan uzak, sadece en önemli ve işe yarar kısımlarıyla öğrenmeniz için bu dijital rehberi hazırladık. 
        Sol menüden istediğiniz uzmanlık alanını seçerek hemen başlayabilirsiniz.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🔔 Günün İpucu")
    st.warning("**Hızlı Doldurma (Flash Fill):** Bir sütundaki veriyi (örneğin ad-soyad ayırma) bir kez manuel yapıp **CTRL + E** tuşuna basarsanız, Excel tüm listeyi sizin için otomatik tamamlar.")

# 2. KISAYOLLAR
elif choice == "⌨️ Kısayol Ansiklopedisi":
    st.markdown("<h1>⌨️ Profesyonel Kısayollar</h1>", unsafe_allow_html=True)
    
    tabs = st.tabs(["🚀 En Hızlılar", "🔧 Düzenleme", "🖱️ Gezinme"])
    
    with tabs[0]:
        st.markdown("""
        <div class="info-card">
            <b>ALT + =</b> : Otomatik Toplam (Hücreleri saniyeler içinde toplar)<br><br>
            <b>F4</b> : Son yapılan işlemi tekrarlar veya hücreyi sabitler ($)<br><br>
            <b>CTRL + SHIFT + L</b> : Filtreleri anında açar veya kapatır.
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[1]:
        st.table(pd.DataFrame({
            "Kısayol": ["CTRL + T", "CTRL + ;", "ALT + Enter", "CTRL + D"],
            "Açıklama": ["Tablo Oluştur", "Güncel Tarihi Ekle", "Hücre İçi Alt Satır", "Üstteki Hücreyi Aşağı Kopyala"]
        }))

# 3. FORMÜLLER
elif choice == "🧪 Formüller & Mantık":
    st.markdown("<h1>🧪 Formüller ve Fonksiyonlar</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <h3>📌 DÜŞEYARA (VLOOKUP)</h3>
        <p>En çok kullanılan formüldür. Bir değeri arayıp karşılığını getirir.</p>
        <code>=DÜŞEYARA(aranan_değer; tablo_dizisi; sütun_indis_sayısı; [aralık_bak])</code>
    </div>
    <div class="info-card">
        <h3>📌 ÇAPRAZARA (XLOOKUP)</h3>
        <p>Düşeyara'nın hatasız ve daha gelişmiş versiyonudur (Excel 365).</p>
        <code>=ÇAPRAZARA(aranan_değer; arama_dizisi; döndürülen_dizi)</code>
    </div>
    """, unsafe_allow_html=True)

# 4. VERİ ANALİZİ
elif choice == "📉 Veri Analizi":
    st.markdown("<h1>📉 Veri Analizi ve Görselleştirme</h1>", unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Pivot Tablolar")
        st.write("Verileri saniyeler içinde özetlemek, raporlamak ve karşılaştırmak için Ekle > PivotTable yolunu kullanın.")
    with col_b:
        st.subheader("Dilimleyiciler (Slicers)")
        st.write("Pivot tablolarınızı ve grafiklerinizi tek tıkla filtrelemek için interaktif butonlar ekleyin.")

# 5. AYARLAR
elif choice == "⚙️ Ayarlar & Püf Noktaları":
    st.markdown("<h1>⚙️ Excel'i Özelleştirin</h1>", unsafe_allow_html=True)
    with st.expander("Geliştirici Sekmesini Aktif Etme"):
        st.write("Dosya > Seçenekler > Şeridi Özelleştir kısmından 'Geliştirici' kutusunu işaretleyin. Makrolar dünyasına giriş yapın!")
