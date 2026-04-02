import streamlit as st
import pandas as pd

# Sayfa Yapılandırması
st.set_page_config(page_title="Excel Master Pro | Utku", page_icon="📗", layout="wide")

# --- GELİŞMİŞ CSS (Aktif Başlık Vurgusu & Tam Merkezi Simetri) ---
st.markdown("""
    <style>
    /* Ana Arka Plan */
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* İçeriği Merkeze Sabitleme */
    .block-container {
        max-width: 900px;
        margin: 0 auto;
        padding-top: 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* Başlıklar */
    h1, h2, h3, h4 { 
        text-align: center !important; 
        color: #2EA043 !important; 
        font-family: 'Segoe UI', sans-serif;
        margin-bottom: 15px;
    }
    
    /* Üst Menü (Tabs) Tasarımı */
    .stTabs [data-baseweb="tab-list"] {
        display: flex;
        justify-content: center;
        gap: 12px;
        background-color: #161B22;
        padding: 8px;
        border-radius: 15px;
        border: 1px solid #30363D;
        margin-bottom: 30px;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #8B949E;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 10px;
        transition: all 0.3s ease;
    }

    /* SEÇİLİ BAŞLIK (Aktif Sekme) GÖRÜNÜMÜ */
    .stTabs [aria-selected="true"] {
        background-color: #2EA043 !important;
        color: white !important;
        box-shadow: 0 4px 20px rgba(46, 160, 67, 0.4);
        transform: scale(1.05);
    }

    /* Profesyonel Kart Tasarımı */
    .dark-card {
        background-color: #1C2128;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #30363D;
        border-top: 4px solid #2EA043;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 20px;
        width: 100%;
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

    /* Tablo Düzeni */
    .stTable {
        margin: 0 auto;
        width: 100% !important;
    }

    code { color: #FF7B72 !important; background-color: #0D1117 !important; border-radius: 5px; padding: 3px 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGO VE ANA BAŞLIK ---
st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=90)
st.markdown("<h1>EXCEL MASTER PROFESYONEL PORTALI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8B949E;'>Utku Tarafından Geliştirilen İleri Seviye Eğitim Platformu</p>", unsafe_allow_html=True)

# --- ANA SEKMELER ---
t1, t2, t3, t4, t5 = st.tabs([
    "🌌 Dashboard", 
    "⌨️ Kısayollar", 
    "💻 Excel Kodları", 
    "🧹 Veri Temizleme", 
    "📊 Raporlama"
])

# --- 1. DASHBOARD ---
with t1:
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Kayıtlı Veri", "150+", "Kısayol & Kod")
    c2.metric("Öğrenme Hızı", "3X", "Artış")
    c3.metric("Geliştirici", "Utku", "v7.0")
    
    st.markdown("""
    <div class="dark-card">
        <h3>🚀 Hoş Geldin Utku</h3>
        <p>Excel'de ustalaşmak için fareyi (mouse) kenara bırakmanın vakti geldi. 
        Bu platform, tamamen merkezi bir odakla en kritik bilgileri sana sunmak için tasarlandı. 
        Yeni eklenen <b>Excel Kodları</b> sekmesini incelemeyi unutma!</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. KISAYOLLAR ---
with t2:
    st.markdown("<br>", unsafe_allow_html=True)
    sub1, sub2, sub3 = st.tabs(["🔥 Temel İşlemler", "🎨 Biçimlendirme", "🧮 Giriş & Yönetim"])
    
    with sub1:
        st.subheader("Temel İşlemler & Navigasyon")
        st.table(pd.DataFrame({
            "İşlem": ["Kaydet", "Geri Al", "Yinele", "Kopyala/Yapıştır", "Tümünü Seç", "Bul/Değiştir", "Veri Sonuna Git", "A1'e Dön"],
            "Kısayol": ["Ctrl + S", "Ctrl + Z", "Ctrl + Y", "Ctrl + C / V", "Ctrl + A", "Ctrl + F / H", "Ctrl + Ok Tuşları", "Ctrl + Home"]
        }))

    with sub2:
        st.subheader("Hücre ve Veri Biçimlendirme")
        st.table(pd.DataFrame({
            "İşlem": ["Biçimlendirme Menüsü", "Kalın Yaz (Bold)", "İtalik Yaz", "Altı Çizili", "Para Birimi", "Yüzde Biçimi", "Tarih Biçimi"],
            "Kısayol": ["Ctrl + 1", "Ctrl + B", "Ctrl + I", "Ctrl + U", "Ctrl + Shift + $", "Ctrl + Shift + %", "Ctrl + Shift + #"]
        }))

    with sub3:
        st.markdown("""
        <div class="dark-card">
            <h4>Hızlı Veri Yönetimi</h4>
            • <b>Alt + = :</b> Otomatik TOPLA fonksiyonu.<br>
            • <b>Ctrl + ; / : :</b> Güncel Tarih ve Saat ekleme.<br>
            • <b>Ctrl + D / R :</b> Üsttekini/Soldakini kopyalar.<br>
            • <b>Ctrl + Shift + + / - :</b> Satır/Sütun Ekle veya Sil.<br>
            • <b>Ctrl + 9 / 0 :</b> Satır veya Sütun Gizle.
        </div>
        """, unsafe_allow_html=True)

# --- 3. EXCEL KODLARI (YENİ EKLENEN) ---
with t3:
    st.markdown("<br>", unsafe_allow_html=True)
    
    # VBA Bölümü
    st.markdown("<h3>1. VBA (Visual Basic for Applications)</h3>", unsafe_allow_html=True)
    st.markdown("<div class='dark-card'><p>VBA, Excel'in klasik Makro dilidir. Masaüstü uygulamasında rutin işleri otomatize eder.</p></div>", unsafe_allow_html=True)
    st.code("""
Sub VeriTemizle()
    Selection.ClearContents
    MsgBox "Veriler başarıyla temizlendi!", vbInformation, "Excel Master"
End Sub
    """, language="vba")
    
    # Office Scripts
    st.markdown("<br><h3>2. Office Scripts (Modern / Web)</h3>", unsafe_allow_html=True)
    st.code("""
function main(workbook: ExcelScript.Workbook) {
  let sheet = workbook.getActiveWorksheet();
  sheet.getRange("A1").setValue("Durum");
  sheet.getRange("A1").getFormat().getFill().setColor("#2EA043");
}
    """, language="typescript")

    # M Dili & Formüller
    st.markdown("<br><h3>3. Power Query & Dinamik Formüller</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dark-card">
        <b>M Kodu Örneği:</b> <code>= Table.ReplaceValue(Kaynak,"Eski","Yeni",...)</code><br><br>
        <b>FİLTRE:</b> <code>=FİLTRE(A2:B10; B2:B10="Tamamlandı")</code><br>
        <b>SIRALA:</b> <code>=SIRALA(A2:E100; 1; 1)</code>
    </div>
    """, unsafe_allow_html=True)
    st.info("💡 VBA Editörü için: Alt + F11 > Insert > Module")

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
        • Daima <b>Tablo (CTRL + T)</b> kullanın.<br>
        • Pivot tablolarınıza <b>Dilimleyiciler</b> ekleyin.<br>
        • Karmaşayı azaltın, veriyi sadeleştirin.
    </div>
    """, unsafe_allow_html=True)
