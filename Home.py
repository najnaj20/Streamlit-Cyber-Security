import streamlit as st
from email.mime import image
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import json
from streamlit_lottie import st_lottie
import requests
import urllib
from datetime import datetime
import csv
import time
import pandas as pd
from lib2to3.pgen2.pgen import DFAState
from idna import valid_contextj
from msilib.schema import Class
from pyrsistent import v




st.set_page_config(
    page_title="Final Project AKIBA Team ",
    page_icon="👋",
)

with st.sidebar:
    choose = option_menu("Cyber Security", ["Home", "URL Checker", "About"],
                         icons=['house', 'search', 'person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#15202b"},
        "icon": {"color": "#ffffff", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#7b53fa"},
        "nav-link-selected": {"background-color": "#7856ff"},
        
    }
    
    )
    

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_hacker = load_lottiefile(r"C:\Users\DELL Latitude 7400\Desktop\streamlit wit\lottiefiles\happy-hacker.json") 


if choose == "Home":

    st.title("Apa itu Phising dan Langkah Mengatasinya :lock:")
    with st.container():
        left_column, right_column = st.columns([0.7, 0.3])
        with left_column:
            st.subheader ("Apa itu phising ?")
            st.write("Phising adalah upaya untuk mendapatkan informasi data seseorang dengan teknik pengelabuan. Data yang menjadi sasaran phising adalah data pribadi (nama, usia, alamat), data akun (username dan password), dan data finansial (informasi kartu kredit, rekening).")
            st.write("Terkadang sebagai korban, kamu tidak akan menyadari kalau kamu sudah menjadi korban phising. Ini bisa terjadi karena pelaku menempatkan dirinya sebagai institusi atau seseorang yang berwenang dan terpercaya. Lalu, pelaku akan membuat berbagai jenis phising seperti email atau website yang serupa dengan aslinya sehingga korban tidak akan sadar sudah dikelabui.")
    
        with right_column:
            st_lottie(
            lottie_hacker,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            height=None,
            width=None,
            key=None,
            )
   


    with st.container():
        st.subheader("Bagaimana aksi phising dijalankan ?")
        st.write("Cara kerja phising adalah memanipulasi informasi dan memanfaatkan kelalaian korban.")
        st.subheader("1. Pelaku Memilih Calon Korban")
        st.write("Tahap awal kegiatan web phising akan dimulai dengan menentukan siapa calon korbannya. Pada umumnya, korban yang disukai adalah pengguna platform pembayaran online seperti PayPal, Ovo, dan lainnya.")
        st.subheader("2. Pelaku Menentukan Tujuan Phising")
        st.write("""
        Setelah mendapatkan calon korban yang potensial, pelaku akan mulai memikirkan apa yang akan dicapai dari kegiatan web phising yang dilakukan.

        Apakah akan menarget username dan password pengguna untuk menguasai akun. Apa malah mendapatkan semua informasi korban melalui sebuah prosedur yang disiapkan.

        Pada contoh aksi phising PayPal, pelaku menginginkan semua informasi dari pengguna platform tersebut. Seperti ditunjukkan welivescurity.com, pengguna akan menerima email untuk mengkonfirmasi data diri melalui sebuah link website palsu yang disediakan.
        """)
        st.subheader("3. Pelaku Membuat Website Phising")
        st.write("Untuk melancarkan aksinya, pelaku akan mulai menyiapkan website palsu untuk melakukan aksi phising. Mulai dari mendesain website palsu, memilih nama domain yang mirip dengan domain asli hingga menyiapkan konten dengan tulisan yang meyakinkan.")
        st.subheader("4. Calon Korban Mengakses Website Phising")
        st.write("Dengan tampilan website dan informasi yang meyakinkan, tak sedikit calon korban yang akhirnya mengakses website phising milik pelaku. Langkah ini biasanya didahului dengan mengajak calon korban melalui email phising atau link yang disebarkan via SMS atau akun media sosial.")
        st.subheader("5. Calon Korban Mengikuti Instruksi Pelaku")
        st.write("""
        Inilah kunci dari terjadinya aksi phising. JIka calon korban melakukan instruksi yang diberikan pelaku, maka pelaku akan berhasil mencapai tujuannya
        Sebagai contoh, pada halaman website yang disediakan, calon korban diminta melakukan update informasi pribadi hingga data pembayaran pada akun yang digunakan. Pada saat selesai mengisi data dan melakukan submit, saat itulah semua informasi korban berhasil dimiliki.""")
        st.subheader("6. Data Korban akan Dimanfaatkan")
        st.write("""
        Jika aksi web phising berhasil, pelaku akan memanfaatkan data yang telah diterima. Apa saja yang bisa dilakukan?

        - Menjual informasi yang didapatkan ke pihak ketiga yang membutuhkan data calon konsumen. Misalnya, untuk tujuan telemarketing atau kegiatan marketing online lainnya.
        - Menjual informasi data tersebut untuk kepentingan politik atau iklan penjualan produk.
        - Menjalankan aksi penipuan. Misalnya, dengan menyatakan seseorang memenangkan undian tertentu yang pada akhirnya meminta orang tersebut mengirimkan sejumlah uang.
        - Menggunakan data yang dimiliki untuk mencoba membobol akun yang dimiliki atau akun lain.
        - Melakukan pinjaman online mengatasnamakan korban dengan menggunakan data diri lengkap korban. Tentu saja, korban lah yang akan ditagih pelunasan atas pinjaman tersebut.
        
        """)
        st.subheader("Jenis-Jenis Phising")
        st.write("""
        Ada beberapa jenis phising yang sering digunakan pelaku untuk mengambil data-data korban dengan cara yang ilegal. Berikut ini adalah jenis-jenisnya dari phising:

        - Email phising
        Jenis yang pertama adalah email phising. Sesuai dengan namanya, phising ini menggunakan email atau surat elektronik sebagai media untuk menipu korbannya. Email ini dibuat semirip mungkin dengan email asli dari sebuah instansi atau lembaga dan dikirimkan secara masif.

        - Spear phising
        Spear phising ini mirip dengan email phising, tetapi ada perbedaan dalam cara mengirimkan emailnya. Email phising dikirimkan secara masif dan acak, sedangkan spear phising akan menarget korban tertentu. Phising jenis ini dilakukan setelah pelaku memiliki informasi dari korban.

        - Web phising
        Berbeda dengan sebelumnya, kali ini menggunakan media website untuk mengelabui korbannya. Pelaku akan membuat website yang terlihat mirip baik dari tampilan maupun nama domain dengan website resminya. Web phising juga dikenal dengan istilah domain spoofing.

        - Whaling
        Jenis phising yang terakhir ini mirip seperti spear phising, yaitu menargetkan satu orang yang memiliki kewenangan tinggi dalam suatu organisasi atau institusi secara spesifik. Dengan whaling, pelaku mendapatkan banyak keuntungan dari akses yang didapatkan.
        
        """)
        st.subheader("Cara Menghindari Phising")
        st.write("""
        Agar tak menjadi korban phising, kamu harus mengetahui cara untuk menghindarinya. Nah, di sini kami sudah mencari dan menyediakan cara untuk menghindari phising. Berikut ini adalah caranya:

        - Menjaga keamanan email.
        - Teliti dalam menerima email, seperti nama pengirim email, isi email, dan file atau link yang tercantum di dalam email.
        - Mengaktifkan two-factor authentication untuk meningkatkan keamanan akun.
        - Teliti dalam membuka website, seperti memeriksa URL dari website dan jangan membuka link sembarangan.
        - Selalu waspada jika kamu dimintai data-data pribadi.
        
        """)
 
if choose == "URL Checker":
    st.title("Apakah website ini aman?")

    class UrlData:
        def __init__(self, json_data):
            self.success = json_data['success']
            self.message = json_data['message']
            if self.success == True:
                self.unsafe = json_data['unsafe']
                self.risk_score = json_data['risk_score']
                self.domain = json_data['domain']
                self.domain_rank = json_data['domain_rank']
                self.domain_age = json_data['domain_age']
                self.domain_age_years = self.domain_age['human']
                self.domain_age_iso = self.domain_age['iso']
                self.domain_age_date = self.domain_age_iso[0:10]
                self.server = json_data['server']
                self.ip_address = json_data['ip_address']
                self.category = json_data['category']
                self.spamming = json_data['spamming']
                self.malware = json_data['malware']
                self.phishing = json_data['phishing']
                self.suspicious = json_data['suspicious']
                self.adult = json_data['adult']
        
        def write_data(write):
            st.write('Risk Score : ', write.risk_score, '%')  
            st.write('Domain :', write.domain)
            st.write('Domain Rank : ', write.domain_rank)
            st.write('Domain Age : ', write.domain_age_years, ", ", write.domain_age_date )
            st.write('IP Address : ', write.ip_address)
            st.write('Category : ', write.category)
            st.write('Spamming : ', write.spamming)
            st.write('Malware : ', write.malware)
            st.write('Phishing : ', write.phishing)
            st.write('Suspicious : ', write.suspicious)
            st.write('Adult : ', write.adult)

        def csv_rows(list):
            # data rows of csv file 
            rows = [['Data', 'Description', 'Result'], 
                    ['Unsafe', 'Can this URL be untrusted?', list.unsafe],
                    ['Domain', 'Domain name of the final URL after all redirections', list.domain],
                    ['Domain Rank', 'Estimated popularity rank of website globally. Value is "0" if the domain is unranked or has low traffic.', list.domain_rank],
                    ['IP Address', 'The IP address corresponding to the server of the domain name.', list.ip_address],
                    ['Category', 'Website classification and category related to the content and industry of the site. Over 70 categories are available including "Video Streaming", "Trackers", "Gaming", "Privacy", "Advertising", "Hacking", "Malicious", "Phishing", etc. The value will be "N/A" if unknown', list.category],
                    ['Risk Score', 'Overall threat score from 0 (clean) to 100 (high risk).', list.risk_score],
                    ['Spamming','Is this domain recently sending SPAM?', list.spamming],
                    ['Malware', 'Indicates if this domain has recently hosted malware, viruses, or C2 activity.', list.malware],
                    ['Phishing', 'Indicates if this site has been recently associated with known phishing techniques.', list.phishing],
                    ['Suspicious', 'Indicates reputation issues and potentially malicious activity', list.suspicious],
                    ['Adult', '	Is this URL or domain hosting dating or adult content?', list.adult],
                    ]
            return rows
        
        def csv_maker(csvv):
            # name of csv file 
            filename = "checking_records.csv"

            # writing to csv file 
            with open(filename, 'w') as csvfile: 
                # creating a csv writer object 
                csvwriter = csv.writer(csvfile)           
                # writing the data rows   
                csvwriter.writerows(csvv.csv_rows())


            st.subheader('Phishing URL Detection')


    # input URL
    url = st.text_input('', placeholder='Enter URL', help='Enter the full URL you want to check')
    encoded_url = urllib.parse.quote(url, safe='')
    api_url_json = 'https://ipqualityscore.com/api/json/url'
    API_KEY = '5bPlipx9etjbQRobKUTol1RjfQZP9s9J'

    st.caption(f'''Supported by [IPQualityScore](https://www.ipqualityscore.com/).
    Compare with other URL checkers: [Google](https://transparencyreport.google.com/safe-browsing/search?url={encoded_url}), [Virus Total](https://www.virustotal.com/gui/home/url)''')




    # is URL empty?
    url_empty = url=='' 
    if url_empty == True:
        st.empty()
    else:   
        # data being loaded
        with st.spinner('Checking URL... '):
            # send get request to ipqualityscore server
            request_data = requests.get(api_url_json + '/'+ API_KEY + '/' + encoded_url)
            json_data = request_data.json() # data requests in json format
                
            # show table directly from json
            #data_str = data.text
            #df = pd.read_json(data_str)
            #df = df.astype(str)
                #st.dataframe(df)

            data = UrlData(json_data)
            success = data.success
                    
            time.sleep(0.7)

        if success == True :
            try:   
                phishing = data.phishing
                risk_score = data.risk_score
                    
                if phishing == True:
                    st.error('PHISHING THREAT DETECTED!!! ')
                    with st.expander("Information about URL", expanded=True):
                        # write URL information
                        data.write_data()

                elif risk_score < 30 and phishing == False:
                    st.success('Website is safe')
                    with st.expander("Information about URL", expanded=True):
                        # write URL information
                        data.write_data()
                                
                elif  risk_score >= 30 and phishing == False:
                        st.warning('''BE CAREFUL!!! There's something fishy about this URL.                            It may not contain any phishing threat, but check out any possible risk below.
                            ''')
                with st.expander("Information about URL", expanded=True):
                        # write URL information
                        data.write_data()

                    # print json file
                    #st.write(json_data)
                    
                                    # reading csv
                data.csv_maker() #  write data to csv file
                with st.expander("Information about URL in Table Form", expanded=False):
                    df = pd.read_csv('checking_records.csv', index_col='Data') # read csv data
                    df

            except:    
                    #st.write(json_data)
                    st.write('Invalid URL or domain. Please check the URL and try again.')
                        
        else:
                st.write(data.message)
                st.empty()


if choose == "About":

    # ---- Use Local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    with st.container():
        st.title(":mailbox: Connect with me")

        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/portofnajwa@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            github = Image.open(r'C:\Users\DELL Latitude 7400\Desktop\streamlit wit\images\github.png')
            st.image(github)
            st.caption('https://github.com/najnaj20')
