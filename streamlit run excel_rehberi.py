import streamlit as st
import pandas as pd

# Sayfa Ayarları
st.set_page_config(page_title="Excel Rehberi", page_icon="📊", layout="wide")

# Kenar Çubuğu (Sidebar) Navigasyon
st.sidebar.title("📑 İçerik Menüsü")
page = st.sidebar.radio("Gitmek istediğiniz bölüm:", 
    ["Ana Sayfa", "Kısayol Tuşları", "Temel Fonksiyonlar", "Veri Ayarları", "İleri Seviye İpuçları"])

# --- ANA SAYFA ---
if page == "Ana Sayfa":
    st.title("🚀 Excel Rehberi'ne Hoş Geldiniz")
    st.markdown("""
    Bu platform, Excel dünyasında ustalaşmanız için tasarlandı. 
    Aşağıdaki kategorilerden birini seçerek öğrenmeye başlayabilirsiniz.
    
    * **Kısayollar:** İş akışınızı hızlandırın.
    * **Fonksiyonlar:** Formüllerle verilerinizi konuşturun.
    * **Ayarlar:** Excel'i kendinize göre özelleştirin.
    """)
    st.info("İpucu: Sağ taraftaki menüyü kullanarak bölümler arasında geçiş yapabilirsiniz.")

# --- KISAYOL TUŞLARI ---
elif page == "Kısayol Tuşları":
    st.header("⌨️ En Çok Kullanılan Kısayollar")
    
    data = {
        "Kısayol": ["CTRL + C", "CTRL + V", "CTRL + Z", "CTRL + Shift + L", "F2", "ALT + ="],
        "Açıklama": ["Kopyala", "Yapıştır", "Geri Al", "Filtre Ekle/Kaldır", "Hücreyi Düzenle", "Otomatik Toplam"]
    }
    df = pd.DataFrame(data)
    st.table(df)

# --- TEMEL FONKSİYONLAR ---
elif page == "Temel Fonksiyonlar":
    st.header("🧮 Temel Fonksiyonlar")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Matematiksel")
        st.code("=TOPLA(A1:A10)", language="excel")
        st.write("Belirlenen aralıktaki tüm sayıları toplar.")
        
        st.code("=ORTALAMA(B1:B10)", language="excel")
        st.write("Sayıların aritmetik ortalamasını alır.")

    with col2:
        st.subheader("Mantıksal")
        st.code('=EĞER(C1>50; "Geçti"; "Kaldı")', language="excel")
        st.write("Belirli bir koşula göre sonuç döndürür.")

# --- VERİ AYARLARI ---
elif page == "Veri Ayarları":
    st.header("⚙️ Önemli Ayarlar ve Özellikler")
    
    with st.expander("Veri Doğrulama (Data Validation)"):
        st.write("Hücrelere girilecek verileri kısıtlamak için kullanılır (Örn: Sadece sayı veya liste).")
        
    with st.expander("Koşullu Biçimlendirme"):
        st.write("Hücreleri içindeki değere göre otomatik olarak renklendirmenizi sağlar.")

# Alt Bilgi
st.sidebar.markdown("---")
st.sidebar.write("📊 Utku tarafından geliştirildi.")