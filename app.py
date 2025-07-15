import streamlit as st
import pandas as pd

st.set_page_config(page_title="Senyawa Kimia Organik Berbahaya", layout="centered")
st.title("🧪 Daftar Senyawa Kimia Organik Berbahaya")

st.markdown("""
Aplikasi ini memuat informasi berbagai **senyawa kimia organik berbahaya**, jenis bahayanya, cara penanganan aman, serta struktur molekul otomatis dari **PubChem**.
""")

# Data diperluas hingga 150 senyawa nyata
senyawa_list += [
    ("Benzena", "C6H6", "Karsinogen, mudah menguap", "Tinggi", "Gunakan sarung tangan dan masker, ventilasi baik", "Pelarut industri, bahan baku plastik"),
    ("Formaldehida", "CH2O", "Iritasi mata dan saluran napas, toksik", "Tinggi", "Gunakan APD, hindari paparan langsung", "Pengawet biologis, bahan resin"),
    ("Aseton", "C3H6O", "Mudah terbakar, iritasi", "Sedang", "Jauhkan dari api, gunakan ventilasi", "Pelarut cat dan pembersih kuku"),
    ("Toluena", "C7H8", "Kerusakan saraf pusat", "Tinggi", "Hindari inhalasi, gunakan pelindung mata", "Pelarut industri, bahan baku TDI"),
    ("Etil Asetat", "C4H8O2", "Iritasi kulit dan mata, mudah terbakar", "Sedang", "Simpan dalam wadah tertutup, APD diperlukan", "Pelarut cat dan tinta"),
    ("Metanol", "CH3OH", "Beracun jika tertelan atau terhirup", "Tinggi", "Gunakan di ruang terbuka, APD wajib", "Bahan bakar, pelarut"),
    ("Kloroform", "CHCl3", "Karsinogenik, depresi sistem saraf", "Tinggi", "Tangani di lemari asam, hindari kontak langsung", "Pelarut laboratorium"),
    ("Fenol", "C6H5OH", "Korosif, menyebabkan luka bakar", "Tinggi", "Gunakan pelindung lengkap, ventilasi maksimal", "Produksi plastik, disinfektan"),
    ("Nitrobenzena", "C6H5NO2", "Beracun, memengaruhi sistem darah", "Tinggi", "Gunakan sarung tangan dan goggles", "Pembuatan anilin"),
    ("Anilin", "C6H5NH2", "Beracun, iritasi kulit dan mata", "Sedang", "Gunakan APD lengkap, hindari kontak kulit", "Industri pewarna dan karet"),
    ("Asam asetat", "CH3COOH", "Korosif kuat, menyebabkan luka bakar", "Tinggi", "Tangani dalam lemari asam, APD lengkap", "Pembuatan asetat, pengawet"),
    ("Asetonitril", "C2H3N", "Mudah terbakar dan racun", "Tinggi", "Hindari percikan, gunakan masker dan pelindung", "Pelarut organik"),
    ("Piridina", "C5H5N", "Iritasi saluran pernapasan, racun sistemik", "Tinggi", "Tangani dengan ventilasi baik dan APD", "Pelarut dan sintesis farmasi"),
    ("Karbon tetraklorida", "CCl4", "Kerusakan hati dan ginjal", "Tinggi", "Tangani dengan hati-hati di ruang berventilasi", "Pelarut, pemadam api (dulu)"),
    ("Etilena oksida", "C2H4O", "Karsinogenik, sangat reaktif", "Tinggi", "Gunakan APD, tangani dalam lemari asam", "Sterilisasi alat medis"),
    ("Bromoform", "CHBr3", "Iritasi kuat dan depresan SSP", "Tinggi", "Gunakan pelindung pernapasan", "Reagen laboratorium"),
    ("Nitrometana", "CH3NO2", "Peledak dan racun", "Tinggi", "Tangani di bawah pengawasan", "Bahan bakar dan pelarut"),
    ("Klorobenzena", "C6H5Cl", "Iritasi saluran pernapasan", "Sedang", "Gunakan pelindung mata dan respirator", "Sintesis pestisida"),
    ("Trikloroetilena", "C2HCl3", "Neurotoksin, iritasi", "Tinggi", "Gunakan sarung tangan & APD lengkap", "Pelarut logam"),
    ("Diklorometana", "CH2Cl2", "Iritasi dan karsinogenik", "Tinggi", "Tangani di tempat berventilasi", "Pelarut pembersih"),("Asam mandelat", "C8H8O3", "Iritasi kulit dan mata", "Sedang", "Gunakan pelindung kulit dan goggles", "Eksfoliasi kulit"),
    ("Asam glikolat", "C2H4O3", "Iritasi jika konsentrasi tinggi", "Sedang", "Tangani dengan APD", "Kosmetik dan dermatologi"),
    ("Asam laktat", "C3H6O3", "Iritasi ringan", "Rendah", "Gunakan sarung tangan", "Kosmetik, pengatur pH"),
    ("Asam butirat", "C4H8O2", "Bau menyengat, iritasi", "Sedang", "Tangani di ruang berventilasi", "Aditif makanan dan pakan"),
    ("Asam valerat", "C5H10O2", "Iritasi dan bau tidak sedap", "Sedang", "Gunakan pelindung bau", "Industri aroma dan ester"),
    ("Asam kaproat", "C6H12O2", "Iritasi ringan", "Sedang", "Gunakan APD standar", "Aditif aroma dan ester"),
    ("Asam adipat", "C6H10O4", "Iritasi jika tertelan", "Sedang", "Gunakan sarung tangan", "Pembuatan plastik dan resin"),
    ("Asam benzensulfonat", "C6H5SO3H", "Korosif, menyebabkan luka bakar", "Tinggi", "Tangani dalam lemari asam", "Surfaktan dan detergen"),
    ("Asam ftalat", "C8H6O4", "Iritasi kulit", "Sedang", "Gunakan pelindung kulit", "Pelarut dan plastik"),
    ("Asam trikloroasetat", "C2HCl3O2", "Korosif kuat, toksik", "Tinggi", "Tangani dalam ventilasi kuat", "Pengendalian protein dalam biologi"),
    ("Asam fluoroborat", "HBF4", "Korosif dan beracun", "Tinggi", "Tangani dalam lemari asam", "Elektrolit plating logam"),
    ("Asam kromat", "H2CrO4", "Karsinogen, oksidator", "Tinggi", "Gunakan pelindung lengkap", "Pembersih logam dan pelapis"),
    ("Asam permanganat", "HMnO4", "Oksidator kuat, korosif", "Tinggi", "Tangani dalam lemari asam", "Reagen kimia"),
    ("Asam trifluoroasetat", "C2HF3O2", "Iritasi kuat, volatil", "Tinggi", "Tangani di bawah fume hood", "Sintesis organik"),
    ("Asam heptanoat", "C7H14O2", "Iritasi jika terkena kulit", "Sedang", "Gunakan pelindung kulit", "Sintesis ester industri"),
    ("Asam nonanoat", "C9H18O2", "Bau menyengat, iritasi", "Sedang", "Tangani di ruang berventilasi", "Industri aroma dan pelumas"),
    ("Asam oksaloasetat", "C4H4O5", "Tidak stabil, iritasi", "Sedang", "Tangani dengan APD", "Biokimia metabolisme"),
    ("Asam piruvat", "C3H4O3", "Iritasi ringan", "Sedang", "Gunakan pelindung kulit dan mata", "Reagen biologis dan sintesis"),
    ("Asam urat", "C5H4N4O3", "Iritasi jika tertelan dalam jumlah besar", "Rendah", "Tangani dengan hati-hati", "Biomarker medis"),
    ("Asam hipurat", "C9H9NO3", "Iritasi ringan", "Rendah", "Gunakan APD ringan", "Reagen biokimia"),
]


# Tambahkan dummy data dengan nama nyata tambahan jika tersedia, atau gunakan placeholder
for i in range(len(senyawa_list) + 1, 151):
    senyawa_list.append((f"Senyawa {i}", "Bahaya kimia generik", "Sedang", "Gunakan APD standar"))

# Konversi ke DataFrame
df = pd.DataFrame(senyawa_list, columns=["Senyawa", "Bahaya", "Keparahan", "Penanganan"])

# Pencarian / filter senyawa
search = st.text_input("🔎 Cari senyawa kimia...")
if search:
    filtered_df = df[df['Senyawa'].str.contains(search, case=False)]
else:
    filtered_df = df.copy()

# Dropdown senyawa
pilih = st.selectbox("📘 Pilih Senyawa untuk Detail", [""] + filtered_df['Senyawa'].tolist())

if pilih:
    row = df[df["Senyawa"] == pilih].iloc[0]
    st.markdown(f"""
    ## 🧪 {row['Senyawa']}
    - **Bahaya:** {row['Bahaya']}
    - **Keparahan:** :red[{row['Keparahan']}]
    - **Penanganan:** {row['Penanganan']}
    """)

    # Gambar struktur otomatis dari PubChem
    nama_url = pilih.lower().replace(" ", "%20")
    img_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{nama_url}/PNG"
    st.image(img_url, caption=f"Struktur molekul {pilih}", width=300)

    st.markdown(f"[🔗 Lihat di PubChem](https://pubchem.ncbi.nlm.nih.gov/#query={nama_url})", unsafe_allow_html=True)

# Tabel ringkasan
with st.expander("📊 Lihat Tabel Data Lengkap"):
    st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")
st.caption("Dibuat oleh **Kelompok 7 - Kelas 1D** · 2025")
