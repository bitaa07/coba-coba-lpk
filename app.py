import streamlit as st
import pandas as pd

st.set_page_config(page_title="Informasi Kimia Organik", layout="centered")

st.title("🧪 Informasi Senyawa Kimia Organik Berbahaya")

# Penjelasan tentang kimia organik
st.markdown("""
Kimia organik adalah cabang ilmu kimia yang mempelajari struktur, sifat, reaksi, dan sintesis senyawa yang mengandung karbon. 
Beberapa senyawa organik digunakan dalam industri dan laboratorium, namun banyak di antaranya yang berbahaya bagi kesehatan dan lingkungan.

Aplikasi ini membantu mengenali berbagai **senyawa kimia organik berbahaya**, jenis bahayanya, serta cara penanganannya secara aman.
""")

# Data senyawa
data = {
    'Senyawa': [
        'Benzena', 'Formaldehida', 'Aseton', 'Toluena', 'Etil Asetat', 'Metanol', 'Kloroform',
        'Fenol', 'Nitrobenzena', 'Karbon tetraklorida', 'Anilin', 'Asam asetat glasial',
        'Asetonitril', 'Piridina'
    ],
    'Bahaya': [
        'Karsinogen, mudah menguap',
        'Iritasi mata dan saluran napas, toksik',
        'Mudah terbakar, iritasi',
        'Kerusakan saraf pusat',
        'Iritasi kulit dan mata, mudah terbakar',
        'Beracun jika tertelan atau terhirup',
        'Karsinogenik, depresi sistem saraf',
        'Korosif, menyebabkan luka bakar',
        'Beracun, memengaruhi sistem darah',
        'Kerusakan hati dan ginjal',
        'Beracun, iritasi kulit dan mata',
        'Korosif kuat, menyebabkan luka bakar',
        'Mudah terbakar dan racun',
        'Iritasi saluran pernapasan, racun sistemik'
    ],
    'Keparahan': [
        'Tinggi', 'Tinggi', 'Sedang', 'Tinggi', 'Sedang', 'Tinggi', 'Tinggi',
        'Tinggi', 'Tinggi', 'Tinggi', 'Sedang', 'Tinggi', 'Tinggi', 'Tinggi'
    ],
    'Penanganan': [
        'Gunakan sarung tangan dan masker, ventilasi baik',
        'Gunakan APD, hindari paparan langsung',
        'Jauhkan dari api, gunakan ventilasi',
        'Hindari inhalasi, gunakan pelindung mata',
        'Simpan dalam wadah tertutup, APD diperlukan',
        'Gunakan di ruang terbuka, APD wajib',
        'Tangani di lemari asam, hindari kontak langsung',
        'Gunakan pelindung lengkap, ventilasi maksimal',
        'Gunakan sarung tangan dan goggles',
        'Tangani dengan hati-hati di ruang berventilasi',
        'Gunakan APD lengkap, hindari kontak kulit',
        'Tangani dalam lemari asam, APD lengkap',
        'Hindari percikan, gunakan masker dan pelindung',
        'Tangani dengan ventilasi baik dan APD'
    ]
}

df = pd.DataFrame(data)

# Dropdown senyawa
pilih = st.selectbox("🔍 Pilih Senyawa Organik", [""] + df['Senyawa'].tolist())

# Tampilkan informasi senyawa
if pilih:
    row = df[df['Senyawa'] == pilih].iloc[0]
    st.markdown(f"""
    ## 🧪 {row['Senyawa']}
    - **Bahaya:** {row['Bahaya']}
    - **Tingkat Keparahan:** :red[{row['Keparahan']}]
    - **Cara Penanganan:** {row['Penanganan']}
    """)
else:
    st.info("Silakan pilih senyawa dari daftar di atas.")

# Footer
st.markdown("---")
st.caption("Dibuat oleh **Kelompok 7 - Kelas 1D** · 2025")
