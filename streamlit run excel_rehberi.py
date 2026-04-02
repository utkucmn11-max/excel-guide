import streamlit as st
import pandas as pd

# Sayfa Genişliği ve Başlığı
st.set_page_config(page_title="Excel Pro Rehberi", page_icon="📈", layout="wide")

# --- CUSTOM CSS (Tasarımı Profesyonelleştiren Bölüm) ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stSidebar { background-color: #ffffff !important; border-right: 1px solid #e0e0e0; }
    .excel-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 8px solid #217346;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .header-text { color: #217346; font-family: 'Segoe UI', sans-serif; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Menü) ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=60)
    st.markdown("<h2 class='header-text'>Excel Akademi</h2>", unsafe_allow_html=True)
    menu = st.radio("Eğitim İçeriği", 
                    ["💎 Ana Panel", "⌨️ Kısayol Sözlüğü", "🧪 Formül Kütüphanesi", "📊 Veri Görselleştirme", "🛠️ Gelişmiş Ayarlar"])
    st.markdown("---")
    st.caption("Versiyon 2.0 | Utku Tarafından Geliştirildi")

# --- İÇERİK ---
if menu == "💎 Ana Panel":
    st.markdown("<h1 class='header-text'>Hoş Geldin, Excel'de Uzmanlaşmaya Başla</h1>", unsafe_allow_html=True)
    
    # Üst Bilgi Kartları
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="excel-card"><h3>450+</h3><p>Fonksiyon Desteği</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="excel-card"><h3>100+</h3><p>Pratik Kısayol</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="excel-card"><h3>Sınırsız</h3><p>Veri Analiz Gücü</p></div>', unsafe_allow_html=True)

    st.subheader("📌 Nereden Başlamalıyım?")
    st.write("""
    Excel öğrenmek bir maratondur. Önce temel hücre yapısını, ardından **Tablo Oluşturma (CTRL+T)** mantığını ve en sonunda **Pivot Tabloları** öğrenerek profesyonel hayata adım atabilirsin.
    """)

elif menu == "⌨️ Kısayol Sözlüğü":
    st.header("Hızınızı 2 Katına Çıkaracak Tuşlar")
    
    tab1, tab2 = st.tabs(["Genel Kullanım", "Veri İşleme"])
    with tab1:
        ks = {
            "Kısayol": ["F4", "ALT + =", "CTRL + Shift + L", "CTRL + T", "CTRL + PageDown"],
            "Ne İşe Yarar?": ["Hücreyi Sabitle / Son İşlemi Tekrarla", "Otomatik Toplam Al", "Hızlı Filtre Ekle", "Veriyi Tabloya Dönüştür", "Sayfalar Arası Geçiş"]
        }
        st.table(pd.DataFrame(ks))
    with tab2:
        st.info("İpucu: Hücre içinde alt satıra geçmek için **ALT + ENTER** kombinasyonunu kullanın.")

elif menu == "🧪 Formül Kütüphanesi":
    st.header("Fonksiyonların Gücünü Keşfedin")
    
    kat = st.selectbox("Kategori Seç", ["Arama & Başvuru", "Mantıksal", "Metin"])
    
    if kat == "Arama & Başvuru":
        st.markdown("""
        <div class="excel-card">
            <h4>XLOOKUP (ÇAPRAZARA)</h4>
            <p>Düşeyara'nın (VLOOKUP) yerini alan, hem sağa hem sola bakabilen en modern formüldür.</p>
            <code>=ÇAPRAZARA(aranan_değer; arama_dizisi; döndürülen_dizi)</code>
        </div>
        """, unsafe_allow_html=True)
    
    elif kat == "Mantıksal":
        st.code("=EĞER(koşul; doğruysa_ne_yazsın; yanlışsa_ne_yazsın)")

elif menu == "📊 Veri Görselleştirme":
    st.header("Veriyi Hikayeleştirin")
    st.write("Excel'de etkileyici grafikler oluşturmak için önce verinizi temizlemelisiniz.")
    st.image("https://images.squarespace-cdn.com/content/v1/553697e1e4b096538b3684a0/1502462310183-Y5L3T753G5D8N5M6W0V8/Excel+Charts.png", caption="Örnek Profesyonel Grafik Yapısı")

elif menu == "🛠️ Gelişmiş Ayarlar":
    st.header("Excel Ayarları ve Özellikler")
    with st.expander("Geliştirici Sekmesini Açmak"):
        st.write("Dosya > Seçenekler > Şeridi Özelleştir > Geliştirici (Onay kutusunu işaretleyin). Bu sayede Makro ve VBA kullanabilirsiniz.")
    with st.expander("Hızlı Erişimi Özelleştir"):
        st.write("En üstteki hızlı erişim çubuğuna 'Geri Al', 'Kaydet' yanına 'Değer Olarak Yapıştır'ı eklemek çok zaman kazandırır.")
