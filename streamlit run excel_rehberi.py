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
        max-width: 1000px;
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

    /* SEÇİLİ BAŞLIK VURGUSU */
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
        text-align: left; /* Kod içerikleri soldan başlar */
    }

    /* Metrik Kutuları */
    [data-testid="stMetric"] {
        background-color: #161B22;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #30363D;
        text-align: center;
    }

    code { color: #FF7B72 !important; background-color: #0D1117 !important; border-radius: 5px; padding: 3px 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST BÖLÜM ---
st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=80)
st.markdown("<h1>EXCEL MASTER PROFESYONEL PORTALI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8B949E;'>Otomasyon, Kodlama ve İleri Düzey Excel Rehberi</p>", unsafe_allow_html=True)

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
    c1.metric("Otomasyon", "VBA & Script", "Aktif")
    c2.metric("Verimlilik", "%100", "Maksimum")
    c3.metric("Geliştirici", "Utku", "v6.5")
    
    st.markdown("""
    <div class="dark-card" style="text-align: center;">
        <h3>🚀 Profesyonel Gelişim</h3>
        <p>Excel'de sadece formüllerle değil, kodlarla da hükmedin. Bu platformda klasik kısayolların yanı sıra 
        VBA ve Office Scripts gibi otomasyon dillerini de bulacaksınız.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. KISAYOLLAR ---
with t2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("⌨️ Ninja Kısayol Kütüphanesi")
    ks_df = pd.DataFrame({
        "İşlem": ["Kaydet", "Geri Al", "Kopyala/Yapıştır", "Tümünü Seç", "Filtre Aç/Kapat", "Tablo Yap", "A1'e Git", "Veri Sonuna Git"],
        "Kısayol": ["Ctrl + S", "Ctrl + Z", "Ctrl + C / V", "Ctrl + A", "Ctrl+Shift+L", "Ctrl + T", "Ctrl + Home", "Ctrl + Ok Tuşları"]
    })
    st.table(ks_df)

# --- 3. EXCEL KODLARI (YENİ BÖLÜM) ---
with t3:
    st.markdown("<br>", unsafe_allow_html=True)
    
    # VBA BÖLÜMÜ
    st.markdown("<h3>1. VBA (Visual Basic for Applications)</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dark-card">
        <p>VBA, Excel'in klasik Makro dilidir. Masaüstü uygulamasında rutin işleri tek tuşla yapmak için kullanılır.</p>
        <b>Temel Bir VBA Makrosu:</b>
    </div>
    """, unsafe_allow_html=True)
    st.code("""
Sub VeriTemizle()
    ' Seçili alandaki verileri siler
    Selection.ClearContents
    
    ' Kullanıcıya bilgi verir
    MsgBox "Veriler başarıyla temizlendi!", vbInformation, "Excel Master"
End Sub
    """, language="vba")

    st.markdown("<b>Hücreye Veri Yazdıran Kod:</b>", unsafe_allow_html=True)
    st.code("""
Sub MerhabaDünya()
    Range("A1").Value = "Merhaba Utku!"
    Range("A1").Font.Bold = True
    Range("A1").Font.Color = vbGreen
End Sub
    """, language="vba")

    st.info("💡 VBA Editörüne girmek için: **Alt + F11** > **Insert** > **Module** yolunu izleyin.")

    # OFFICE SCRIPTS
    st.markdown("<br><h3>2. Office Scripts (Web & Bulut)</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dark-card">
        <p>Excel Web ve 365'te kullanılan, TypeScript tabanlı modern yapıdır.</p>
        <b>Otomatik Tablo Scripti:</b>
    </div>
    """, unsafe_allow_html=True)
    st.code("""
function main(workbook: ExcelScript.Workbook) {
  let sheet = workbook.getActiveWorksheet();
  sheet.getRange("A1").setValue("Durum");
  sheet.getRange("A1").getFormat().getFill().setColor("#2EA043");
}
    """, language="typescript")

    # POWER QUERY & FORMÜLLER
    st.markdown("<br><h3>3. Power Query (M Dili) & Dinamik Formüller</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dark-card">
        <b>M Kodu Örneği:</b><br>
        <code>= Table.ReplaceValue(Kaynak,"Eski","Yeni",Replacer.ReplaceText,{"Sütun1"})</code>
        <br><br>
        <b>Dinamik Formüller:</b><br>
        • <b>FİLTRE:</b> <code>=FİLTRE(A2:B10; B2:B10="Tamamlandı")</code><br>
        • <b>SIRALA:</b> <code>=SIRALA(A2:E100; 1; 1)</code>
    </div>
    """, unsafe_allow_html=True)

# --- 4. VERİ TEMİZLEME ---
with t4:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dark-card" style="text-align: center;">
        <h4>🧹 Veri Temizleme Standartları</h4>
        • <b>=KIRP(A1) :</b> Boşlukları temizler.<br>
        • <b>=YAZIM.DÜZENİ(A1) :</b> Baş harfleri büyütür.<br>
        • <b>=EĞERHATA(Formül; 0) :</b> Temiz rapor görünümü sağlar.
    </div>
    """, unsafe_allow_html=True)

# --- 5. RAPORLAMA ---
with t5:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dark-card" style="text-align: center;">
        <h4>📊 Dashboard Tasarım İlkeleri</h4>
        • Her zaman <b>Tablo (CTRL + T)</b> formatını kullanın.<br>
        • Pivot tablolarınıza <b>Dilimleyiciler (Slicers)</b> ekleyin.<br>
        • Karmaşık grafiklerden kaçının, sadeliğe odaklanın.
    </div>
    """, unsafe_allow_html=True)
