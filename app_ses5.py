import streamlit as st
# import plotly.graph_object as go
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title = 'Belajar Streamlit'
    # ,layout='wide'
)

# Menulis teks
# st.code("Hello world!")

st.title("Analisis Perubahan Harga Gula di Indonesia")
st.markdown("Oleh : **Laily Dwi Retno Wahyuningtias**")
st.markdown("20 Februari 2024")
from PIL import Image
# from PIL import Image

image = Image.open("Capture.PNG")
st.image(
    image,
    caption="Gula"
)
# path_to_image = r'C:\Users\hp\dqlab\belajar_streamlit\Capture.PNG'
# st.image(path_to_image, caption = 'Gula', use_column_width=True)

st.write("""Harga gula menjadi perhatian utama di pasar global akhir tahun 2023. Kenaikan harga yang signifikan telah menjadi topik hangat di kalangan pelaku industri dan konsumen. Bahkan dalam [berita](https://www.cnbcindonesia.com/news/20231107154758-4-487099/siap-siap-harga-gula-terbang-ke-rp18000-ini-biang-keroknya) yang dilansir dalam lama CNBC dikatakan bahwa harga gula akan mencapai angka Rp18.000,00. Tren naik ini tidak hanya mencerminkan dinamika pasar gula yang kompleks, tetapi juga memiliki dampak yang luas pada berbagai sektor ekonomi dan kehidupan sehari-hari.""")
st.write("""Grafik kurva harga gula nasional memberikan pandangan terhadap tren pergerakan harga gula di Jawa Timur, yang merupakan penghasil gula terbesar di Indonesia. Melalui data yang diperoleh dari siskaperbapo.jatimprov.go.id, dapat ditunjukkan gambaran tentang fluktuasi harga gula nasional sebagai berikut.""")

harga_gula = r'C:\Users\hp\dqlab\belajar_streamlit\harga.csv'
harga = pd.read_csv(harga_gula)
# st.line_chart(harga.set_index('tanggal')[['harga_gula_nasional']])

plt.plot(harga['tanggal'], harga['harga_gula_nasional'])
plt.xlabel('tanggal')
plt.ylabel('Rp')
plt.xticks(rotation=90)
plt.title("Grafik Perubahan Harga Gula Nasional")
st.pyplot(plt)
st.markdown("*sumber : siskaperbapo.jatimprov.go.id*")

st.write("""Kenaikan harga gula bisa dipicu oleh berbagai faktor kompleks. Beberapa diantaranya yaitu perubahan kondisi cuaca dan kondisi ekonomi global. Perubahan kondisi cuaca ekstrem seperti kekeringan atau banjir dapat mengganggu produksi tebu. Berikut adalah grafik curah hujan (mm) yang terjadi antara bulan Oktober dan November tahun 2023 silam.""")
#Permintaan yang tinggi dari industri makanan dan minuman serta rumah tangga menyebabkan permintaan gula. Ketika permintaan melebihi pasokan, maka harga gula akan cenderung naik.

cuaca_malang = r'C:\Users\hp\dqlab\belajar_streamlit\cuaca_malang.csv'
cuaca = pd.read_csv(cuaca_malang)

st.markdown("**Grafik Curah Hujan di Kabupaten Malang**")
# st.line_chart(cuaca.set_index('tanggal')[['curah_hujan']])
fig=plt.figure()
plt.plot(cuaca['tanggal'], cuaca['curah_hujan'])
plt.xlabel('tanggal')
plt.ylabel('mm')
plt.xticks(rotation=90)
st.pyplot(fig)
# st.text("Sumbu X : Tanggal, Sumbu Y : mm")
st.markdown("*sumber : dataonline.bmkg.go.id*")

harga_cuaca = r'C:\Users\hp\dqlab\belajar_streamlit\harga_cuaca.csv'
gabungan_harga_cuaca = pd.read_csv(harga_cuaca)
# st.scatter_chart(data=gabungan_harga_cuaca, x="harga_gula_nasional", y="kelembapan_rerata")



st.write("""Grafik di atas menunjukkan bahwa curah hujan yang terjadi pada awal bulan November menjadi salah satu faktor penyebab naiknya harga gula. Jika terjadi banjir maka mengakibatkan produksi gula terganggu, terutama jika daerah pertanian tebu atau gula terkena dampaknya. Gangguan ini dapat mengurangi pasokan gula di pasar dan meningkatkan harga.""")

st.write("""Tidak hanya kondisi cuaca ekstrim yang menjadi faktor naiknya harga gula, tetapi kondisi ekonomi global juga berpengaruh. Kenaikan harga gula di Indonesia dan kenaikan harga gula di pasar internasional juga memiliki hubungan yang sangat kompleks dan saling terkait. Walaupun Jawa Timur adalah penghasil gula terbesar di Indonesia, namun Indonesia tetap menjadi salah satu negara yang cukup bergantung pada import gula untuk memenuhi kebutuhan domestiknya. Jika harga gula di pasar internasional naik, maka dapat berdampak langsung pada harga gula di Indonesia karena biaya import menjadi lebih tinggi.""")

col1, col2 = st.columns(2)

with col1:
    #lahir_saya = st.date_input("Tanggal lahir kamu")
    # st.line_chart(harga.set_index('tanggal')[['harga_gula_nasional']])
    fig=plt.figure()
    plt.plot(harga['tanggal'], harga['harga_gula_nasional'])
    plt.xlabel('tanggal')
    plt.ylabel('Rp')
    plt.xticks(rotation=90)
    plt.title("Grafik Perubahan Harga Gula Nasional")
    st.pyplot(fig)   

with col2:
    #lahir_gebetan = st.date_input("Tanggal lahir dia")
    # st.line_chart(harga.set_index('tanggal')[['harga_gula_nasional']])
    fig=plt.figure()
    plt.plot(harga['tanggal'], harga['harga_gula_internasional'])
    plt.xlabel('tanggal')
    plt.ylabel('USD/ton')
    plt.xticks(rotation=90)
    plt.title("Grafik Perubahan Harga Gula Internasional")
    st.pyplot(fig)

st.write("""Berdasarkan grafik di atas, dapat dikatakan bahwa kenaikan harga gula di Indonesia dan kenaikan harga gula di pasar internasional saling berdampak, dan dapat mempengaruhi stabilitas harga gula di dalam negeri.""")
st.subheader("Saran dan Kesimpulan")
st.write("Berdasarkan pembahasan di atas dapat diberikan saran sebagai berikut:")
st.markdown("""
    * Pemerintah dan pelaku industri gula dapat mempertimbangkan diversifikasi sumber gula untuk mengurangi ketergantungan pada impor gula. Ini dapat dilakukan dengan mempromosikan pengembangan sumber gula alternatif atau meningkatkan efisiensi produksi gula dalam negeri.
    * Investasi dalam infrastruktur pertanian, termasuk irigasi dan sistem perlindungan tanaman, serta penerapan teknologi modern dalam produksi gula dapat membantu mengurangi dampak buruk dari kondisi cuaca ekstrem dan meningkatkan produktivitas.
    * Pemerintah dapat mengadopsi kebijakan yang bertujuan untuk menjaga stabilitas harga gula dalam negeri, termasuk mekanisme subsidi atau intervensi pasar untuk mencegah lonjakan harga yang tiba-tiba.
""")
st.write("**Kesimpulan**")
st.write("""Fluktuasi harga gula merupakan masalah kompleks yang dipengaruhi oleh berbagai faktor, termasuk kondisi cuaca, kondisi ekonomi global, dan ketergantungan pada impor. Kenaikan harga gula tidak hanya mempengaruhi pelaku industri, tetapi juga masyarakat umum dalam kehidupan sehari-hari. Oleh karena itu, diperlukan kerja sama antara pemerintah, pelaku industri, dan masyarakat untuk menghadapi tantangan ini dengan cara yang efektif, termasuk melalui diversifikasi sumber gula, penguatan infrastruktur, dan kebijakan harga yang stabil.""")

st.markdown("**Referensi**")
st.markdown("""
    1. siskaperbapo.jatimprov.go.id
    2. dataonline.bmkg.go.id
    3. databoks.katadata.co.id
    4. https://www.cnbcindonesia.com/news/20231107154758-4-487099/siap-siap-harga-gula-terbang-ke-rp18000-ini-biang-keroknya
""")

# file_path1 = r'C:\Users\hp\dqlab\belajar_streamlit\cuaca_cabe_pasuruan_202402251216.csv'
# pasuruan = pd.read_csv(file_path1)
# file_path2 = r'C:\Users\hp\dqlab\belajar_streamlit\cuaca_harga_jatim_202402251712.csv'
# jatim = pd.read_csv(file_path2)
# file_path3 = r'C:\Users\hp\dqlab\belajar_streamlit\cuaca_harga_malang_202402251536.csv'
# malang = pd.read_csv(file_path3)
# file_path4 = r'C:\Users\hp\dqlab\belajar_streamlit\cuaca_harga_banyuwangi_202402280524.csv'
# banyuwangi = pd.read_csv(file_path4)
# file_path5 = r'C:\Users\hp\dqlab\belajar_streamlit\cuaca_harga_gresik_202402280524.csv'
# gresik = pd.read_csv(file_path5)
# file_path6 = r'C:\Users\hp\dqlab\belajar_streamlit\cuaca_harga_nganjuk_202402280524.csv'
# nganjuk = pd.read_csv(file_path6)
# file_path7 = r'C:\Users\hp\dqlab\belajar_streamlit\cuaca_harga_sidoarjo_202402280524.csv'
# sidoarjo = pd.read_csv(file_path7)
# file_path8 = r'C:\Users\hp\dqlab\belajar_streamlit\cuaca_harga_sumenep_202402280524.csv'
# sumenep = pd.read_csv(file_path8)
# file_path9 = r'C:\Users\hp\dqlab\belajar_streamlit\cuaca_harga_surabaya_202402280524.csv'
# surabaya = pd.read_csv(file_path9)
#st.dataframe(pasuruan)

# Membuat grafik harga cabe SURABAYA
# file_path10 = r'C:\Users\hp\dqlab\belajar_streamlit\harga_cabe_seluruh_202402280524.csv'
# seluruh = pd.read_csv(file_path10)
# filtered_data_seluruh = seluruh[(seluruh['Tanggal']>='2023-11-23') & (seluruh['Tanggal']<='2024-02-01')]
#st.line_chart(filtered_data.set_index('Tanggal')[['harga_pasuruan','harga_kab_malang','harga_kot_malang','harga_banyuwangi','harga_gresik','harga_nganjuk','harga_sidoarjo','harga_sumenep','harga_surabaya']])
# st.line_chart(filtered_data_seluruh.set_index('Tanggal')[['harga_surabaya']])
# filtered_data_surabaya = surabaya[(surabaya['Tanggal']>='2023-11-23') & (seluruh['Tanggal']<='2024-02-01')]
# Membuat SCATTER PLOT harga cabe dan curah hujan SURABAYA
# st.line_chart(filtered_data_surabaya.set_index('Tanggal')[['RR','Tavg','ss']])

# data = {
#     'Grafik 1': [10, 20, 30, 40, 50],
#     'Grafik 2': [15, 25, 35, 45, 55],
#     'Grafik 3': [20, 30, 40, 50, 60]
# }
# df = pd.DataFrame(data)

# st.write("Line Chart dengan Warna Berbeda")
# fig, ax = plt.subplots()
# for column in pasuruan.columns:
#     ax.plot(pasuruan[column], label=column)
# ax.legend()
# st.pyplot(fig)

# x= np.linspace(0, 10, 100)
# x = pasuruan['Tanggal']
# y1=np.sin(x)
# y1 = pasuruan['Harga_Mean']


# y2=np.cos(x)
# y2 = jatim['Harga_Mean']
# y3=np.tan(x)
# y3 = malang['Harga_Mean']
# data=pd.DataFrame({
#     'x':x,
#     'y1':y1
    # 'y2':y2,
    # 'y3':y3
# })
# membuat plot menggunakan matplotlib
# st.line_chart(data[['y1']])
# st.line_chart(data[['y1','y2','y3']])

# plt.figure(figsize=(10,6))
# Plot grafik pertama dengan warna biru
# plt.plot(x,y1,label='Grafik 1', color='blue')
# # Plot grafik kedua dengan warna merah
# plt.plot(x,y2,label='Grafik 2', color='red')
# # Plot grafik ketiga dengan warna hijau
# plt.plot(x,y3, label='Grafik 3', color='green')
# menambahkan judul dan label sumbu
# plt.title('Line Chart dengan Grafik yang berbeda')
# plt.xlabel('X-axis Label')
# plt.ylabel('Y-axis Label')
# menampilkan legenda 
# plt.legend()
# plt.xticks(rotation=90)

# menampilkan plot menggunakan streamlit
# st.pyplot(plt)


# nilai_minimal, nilai_maksimal= 2023-11-01, 2023-02-01
# nilai_minimal, nilai_maksimal= 2023-12-15, 2023-12-15

# parameter_alpha = st.slider(
#     "Pilih rentang waktu",
#     min_value=0.0,
#     max_value=1.0,
#     step=0.1,
#     value=0.5
# )

# st.line_chart(pasuruan.set_index('Tanggal'))
# st.line_chart(pasuruan.set_index('Tanggal')['Harga_Mean'], use_container_width=True)
# st.line_chart(pasuruan.set_index('Tanggal')[['RR','ss','Tavg']])

# st.line_chart(data=pasuruan, x="Tanggal", y="Harga_Mean")
# st.line_chart(data=pasuruan, x="Tanggal", y="RR")
# st.header("Header")
# st.subheader("Subheader")
# st.text("Oleh : Laily Dwi Retno Wahyuningtias")
# st.code("import streamlit as st")
# st.code("""
#     import numpy as np
#     import pandas as pd
# """)
# st.latex("y = 2x^2 + 3x + 5")
# # Hands on activity: adjust text as class context

# # markdown text
# st.markdown("# Title")
# st.markdown("_italic_")
# st.markdown("__bold__")
# st.markdown("""
#     1. Number 1
#     2. Number 2
#     3. Number 3
# """)

# # # Quizz
# # # 1. How to write bullet points?
# st.markdown("""
#     * Bullet 1
#     * Bullet 2
#     * Bullet 3
# """)
# # # 2. How to write text with hyperlink?
# st.markdown("""
#     [google](https://google.com)
# """)

# # WIDGET <- Input elements
# st.header("Widget")

# ini_tombol = st.button("Tekan tombol ini")
# ini_tombol

# saya_setuju = st.checkbox("Centang jika setuju")
# saya_setuju
# if saya_setuju:
#     st.write("Anda setuju untuk belajar lebih giat")
# else:
#     st.write("Ayo belajar")

# # radio button, memilih salah satu opsi dari sekian opsi
# buah_favorit = st.radio(
#     "Pilihan buah favorit kamu",
#     ['Apel','Anggur','Jeruk','Mangga']
# )
# buah_favorit
# st.write(f"Buah kesukaanku adalah {buah_favorit}")

# # selectbox menampilkan menu dropdown untuk dipilih
# makanan = st.selectbox(
#     "Pilih makanan yang akan diorder",
#     ['Paket 1','Paket Goceng','Kids meal']
# )
# st.write(f"Anda akan mengorder {makanan}")

# # multiselect memungkinkan kita memilih multiple choices
# belanjaan = st.multiselect(
#     "Pilih item belanjaan kalian",
#     ['Terigu','Minyak goreng','Biskuit','Minuman']
# )
# belanjaan
# if len(belanjaan) > 0:
#     st.write(f"Pilihan pertama Anda adalah {belanjaan[0]}")

# # slider memungkinkan kita untuk memilih numerik input dengan range yang ditentukan
# parameter_alpha = st.slider(
#     "Insert alpha value",
#     min_value=0.0,
#     max_value=1.0,
#     step=0.1,
#     value=0.5
# )
# st.write(f"Parameter yang dipilih adalah {parameter_alpha}")

# Jika input berupa kategorikal, kita dapat menggunakan select_slider
# ukuran_baju = st.select_slider(
#     "Ukuran baju",
#     ['SS','S','M','L','XL','XXL']
# )
# st.write(f"Ukuran baju yang dipilih adalah {ukuran_baju}")

# # number_input untuk input number
# kode_pos = st.number_input(
#     "Masukkan kode pos",
#     min_value=0,
#     max_value=999999,
#     step=10
# )
# kode_pos

# # Text input
# nama = st.text_input("Masukkan nama kalian")
# nama

# # Text area
# komentar = st.text_area("Masukkan komentar kamu")
# komentar

# # Input tanggal
# import datetime

# tanggal_lahir = st.date_input(
#     "Tanggal lahir"
# )
# tanggal_lahir

# # Input waktu, step dalam detik 
# jam_mulai = st.time_input("masukkan jam mulai", step=600)
# jam_mulai

# # Input warna
# warna = st.color_picker("masukkan warna")
# warna
# # Use HTML and inline CSS to set the color of the text
# styled_text = f'<span style="color:{warna};">Ini adalah text dengan warna yang dipilih.</span>'
# # Display the text using st.write
# st.write(styled_text, unsafe_allow_html=True)

# # Menampilkan media

# # Image
# from PIL import Image

# image = Image.open("sunrise.jpeg")
# st.image(
#     image,
#     caption="A beautiful sunrise"
# )

# # Home exercise
# # Tampilkan audio
# # Tampilkan video

# # container and layouting

# # Kolom

# col1, col2 = st.columns(2)

# with col1:
#     #lahir_saya = st.date_input("Tanggal lahir kamu")
#     st.line_chart(harga.set_index('tanggal')[['harga_gula_nasional']])

# with col2:
#     #lahir_gebetan = st.date_input("Tanggal lahir dia")
#     st.line_chart(harga.set_index('tanggal')[['harga_gula_nasional']])


# # kolom dengan lebar custom
# kol1, kol2 = st.columns([3,6])

# with kol1:
#     lahir_aku = st.date_input("Tanggal lahir aku")

# with kol2:
#     lahir_kamu = st.date_input("Tanggal lahir dirinya")

# sidebar
# with st.sidebar:
#     st.title("Titanic survival model explorer")
#     your_name = st.text_input("Enter your name")

#     with st.expander("Lorem ipsum"):
#         st.write("dolor sit amet")

# Tabbing
# tab1, tab2, tab3 = st.tabs(['Tab1', 'Tab2', 'Tab3'])

# with tab1:
#     st.write("Tab 1: Lorem ipsum dolor sit amet")

# with tab2:
#     st.write("Tab 2: Lorem ipsum dolor sit amet")

# with tab3:
#     st.write("Tab 3: Lorem ipsum dolor sit amet")

# Container
# custom_container = st.container(border=True)
# with custom_container:
#     st.write("ini teks di dalam container")

# st.write("SEDANGKAN teks ini di luar container")

# # Basic plotting
#import pandas as pd

# file_path = r'C:\Users\hp\dqlab\belajar_streamlit\cuaca_cabe_pasuruan_202402251216.csv'
# pasuruan = pd.read_csv(file_path)
# st.dataframe(pasuruan)

# # # Tambahkan widget untuk mengunggah file CSV
# uploaded_file = st.sidebar.file_uploader('C:\Users\hp\dqlab\belajar_streamlit\cuaca_cabe_pasuruan_202402251216.csv', type=['csv'])
# # # Jika file CSV diunggah, baca data menjadi DataFrame
# if uploaded_file is not None:
#     pasuruan = pd.read_csv(uploaded_file)
#     st.write(pasuruan)

# Bar chart
# df = pd.DataFrame({
#     "name": ["A","B","C"],
#     "value": [1,2,3]
# })

# st.bar_chart(data=pasuruan, x="Tanggal", y="Harga_Mean")

# # Line plot
# df = pd.DataFrame({
#     "date": pd.date_range(start='2024-01-01', end='2024-01-10', freq='D'),
#     "value": [1,2,3,4,3,2,1,2,3,4]
# })

# st.line_chart(data=df, x="date", y="value")

# scatter plot
# import numpy as np
# np.random.seed(42)
# random_numbers = np.random.uniform(0, 10, 200)

# df = pd.DataFrame({
#     "value1": random_numbers[:100],
#     "value2": random_numbers[100:]
# })

# st.scatter_chart(data=df, x="value1", y="value2")

# Home exercise: berikan centered title pada setiap plot di atas

# Selesai, tekan control+C pada terminal untuk mengakhiri app
# Lalu exit untuk turn off virtual environment
