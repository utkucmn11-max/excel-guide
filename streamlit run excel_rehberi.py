import streamlit as st
import pandas as pd

# Sayfa Yapılandırması
st.set_page_config(page_title="Excel Pro Rehberi | Dark Mode", page_icon="📗", layout="wide")

# --- DARK MODE & PROFESSIONAL GREEN CSS ---
st.markdown("""
    <style>
    /* Ana Arka Plan ve Metin Renkleri */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    
    /* Yan Menü (Sidebar) Karanlık Tasarım */
    [data-testid="stSidebar"] {
        background-color: #161B22 !important;
        border-right: 1px solid #30363D;
    }
    
    /* Başlıklar ve Alt Başlıklar */
    h1, h2, h3, h4 {
        color: #2EA043 !important; /* Excel Yeşili (Dark Mode Uyumlu) */
        font-family: 'Segoe UI', sans-serif;
    }

    /* Profesyonel Kart Tasarımları (Dark Card) */
    .dark-card {
        background-color: #1C2128;
        padding: 25px;
        border-radius: 12px;
        border-left: 5px solid #2EA043;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        margin-bottom: 25px;
        border: 1px solid #30363D;
    }

    /* Tablo ve Metrik Düzenlemeleri */
    .stMetric {
        background-color: #1C2128;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363D;
    }
    
    /* Kod Blokları Renk Uyumu */
    code {
        color: #FF7B72 !important;
        background-color: #0D1117 !important;
    }

    /* Sidebar Yazı Rengi */
    .css-17l2qt2 {
        color: #FFFFFF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVİGASYON ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=100)
    st.markdown("### **Excel Master v4.0**")
    st.write("Profesyonel Karanlık Arayüz")
    st.markdown("---")
    
    choice = st.radio(
        "Eğitim Modülleri",
        ["🌌 Dashboard", "⌨️ Ninja Kısayolları", "🧪 İleri Formül Analizi", "🧹 Veri Temizleme", "📊 Raporlama Sanatı"]
    )
    
    st.markdown("---")
    st.markdown("👤 **Geliştirici:** Utku")
    st.caption("Karanlık Mod Aktif ✅")

# --- 1. DASHBOARD ---
if choice == "🌌 Dashboard":
    st.markdown("<h1>📊 Excel Master Dashboard</h1>", unsafe_allow_html=True)
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Kayıtlı Fonksiyon", "480+", "Güncel")
    with m2:
        st.metric("İş Akış Hızı", "%65", "Verimlilik")
    with m3:
        st.metric("Hata Oranı", "%0.2", "Optimizasyon")

    st.markdown("""
    <div class="dark-card">
        <h3>🚀 Profesyonel Strateji</h3>
        <p>Excel'de ustalık, sadece formül bilmek değil; veriyi nasıl yöneteceğini bilmektir. 
        Bu rehberde, ham veriyi alıp profesyonel bir rapora dönüştürmenin tüm adımlarını bulacaksınız.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("💡 Altın Kural")
    st.info("**Sabitleme ($):** Formüllerde F4 tuşu hayat kurtarır. Hücreyi kilitlemeden asla karmaşık hesaplamalara girmeyin.")

# --- 2. KISAYOLLAR ---
elif choice == "⌨️ Ninja Kısayolları":
    st.header("⌨️ Zaman Kazandıran Profesyonel Tuşlar")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="dark-card">
            <h4>Seçim ve Veri Kontrolü</h4>
            <b>CTRL + SHIFT + L</b> : Filtreleri açar/kapatır.<br>
            <b>CTRL + T</b> : Veriyi anında tabloya dönüştürür.<br>
            <b>CTRL + SHIFT + 1</b> : Sayıyı binlik ayırıcı yapar.
        </div>
        """, unsafe_allow_html=True)
    
    with col_b:
        st.markdown("""
        <div class="dark-card">
            <h4>Hücre İçi Sihirbazlar</h4>
            <b>ALT + =</b> : Saniyeler içinde otomatik toplam alır.<br>
            <b>ALT + Enter</b> : Aynı hücrede alt satıra geçer.<br>
            <b>CTRL + D</b> : Üstteki hücreyi anında aşağı kopyalar.
        </div>
        """, unsafe_allow_html=True)

# --- 3. İLERİ FORMÜL ANALİZİ ---
elif choice == "🧪 İleri Formül Analizi":
    st.header("🧪 Formül Mühendisliği")
    
    with st.expander("🔍 XLOOKUP (ÇAPRAZARA) - Yeni Nesil"):
        st.write("Düşeyara'nın tüm eksiklerini kapatan, Excel'in en güçlü arama fonksiyonu.")
        st.code("=ÇAPRAZARA(aranan_değer; arama_dizisi; döndürülen_dizi; [bulunamıyorsa]; [eşleştirme_modu])")

    with st.expander("⚖️ İNDİS & KAÇINCI (Index-Match)"):
        st.write("Büyük veri setlerinde Düşeyara'dan daha hızlı ve esnek çalışır.")
        st.code("=İNDİS(Sonuç_Sütunu; KAÇINCI(Kriter; Arama_Sütunu; 0))")

# --- 4. VERİ TEMİZLEME ---
elif choice == "🧹 Veri Temizleme":
    st.header("🧹 Veri Düzenleme Teknikleri")
    
    st.markdown("""
    <div class="dark-card">
        <h4>ETL Süreci (Extract, Transform, Load)</h4>
        1. <b>KIRP (TRIM):</b> Gereksiz tüm boşlukları temizler.<br>
        2. <b>TEMİZLE (CLEAN):</b> Basılamayan karakterleri yok eder.<br>
        3. <b>YAZIM.DÜZENİ (PROPER):</b> İsimlerin baş harflerini düzeltir.
    </div>
    """, unsafe_allow_html=True)

# --- 5. RAPORLAMA SANATI ---
elif choice == "📊 Raporlama Sanatı":
    st.header("📊 Dashboard ve Raporlama")
    
    st.markdown("""
    <div class="dark-card">
        <h3>Profesyonel Bir Raporun 3 Ayağı</h3>
        <ul>
            <li><b>Dinamiklik:</b> Pivot tablolar ve Dilimleyiciler (Slicers) kullanın.</li>
            <li><b>Görsellik:</b> Grafiklerde karmaşadan kaçının, "Data-to-Ink" oranına dikkat edin.</li>
            <li><b>Doğruluk:</b> 'Hata Denetimi' ve 'Veri Doğrulama' ile kullanıcı hatalarını engelleyin.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
