# Dicoding Project



## 🚀 Cara Menjalankan
Pastikan telah menginstal Python di sistem Anda. Kemudian, ikuti langkah-langkah berikut:


### **1. Lakukan Clone Repository atau memindahkan ke direktori tugas kita**
Clone repository dengan cara : 
```bash
git clone <repository_url>
```
Memindahkan file yang ada ke direktori yang kita inginkan : 
```bash
cd submission/dashboard
```

### **2. Aktifkan Virtual Environment (Opsional)**
Jika proyek menggunakan virtual environment, aktifkan dengan:
```bash
source venv/bin/activate  # Pada Linux/macOS
venv\Scripts\activate     # Pada Windows
```

### **3. Install Dependensi**
Instal semua dependensi yang tersedia dengan cara :
```bash
pip install -r requirements.txt
```

### **4. Jalankan Dashboard**
Jalankan skrip utama dengan perintah berikut:
```bash
streamlit run dashboard/dashboard.py
```


---



### 5. Buatlah Struktur folder "Submission" menjadi seperti berikut 
```
submission
│── dashboard
│   │── dashboard.py
│   │── all_data.csv
│── data
│   │   │── day.csv
│   │   │── hour.csv
│── requirements.txt
│── README.md
│── url.txt