# 💡 Marimo Satış Analizleri

🌟 Marimo ile oluşturulmuş bu demo proje, veri analisti bakış açısından **reaktif not defteri deneyimini** keşfetmek için hazırlandı. Marimo hücreleri kullanılarak veri yükleme, etkileşimli filtreleme, SQL sorgulama ve Plotly grafiklerini tek bir uygulama içinde birleştirir.  
📚 Ek olarak, Marimo'nun temel özelliklerini tanıtan altı farklı eğitim not defteri ve sahte satış verisi üretmek için yardımcı bir Python script'i içerir.

## 📦 İçindekiler

- 📊 `sales_analysis.py`: Etkileşimli satış panosu (Marimo uygulaması)
- 🛠️ `generate_sales_data.py`: Demo veri setini yeniden üretmek için yardımcı script
- 🎯 `01_...` → `06_...`: Marimo'nun reaktiflik, UI bileşenleri, SQL, grafik, dataframe ve dashboard yeteneklerini adım adım gösteren eğitim not defterleri
- 📦 `requirements.txt`: Projenin bağımlılıkları
- 📈 `sales_data.csv`: Dashboardsa bağlanan örnek veri seti (script ile yeniden üretilebilir)

## 🧰 Gereksinimler

- 🐍 Python 3.10+
- 🧭 Git (yerel kurulum için)
- 🛡️ Sanal ortam önerilir (ör. `python -m venv .venv`)

## ⚙️ Kurulum

```bash
git clone https://github.com/busrakurunceng/marimo_tests.git
cd marimo_tests
python -m venv .venv
.venv\Scripts\activate      # PowerShell
pip install -r requirements.txt
```

> **Not:** Bağımlılıklar arasında `marimo`, `pandas`, `numpy`, `duckdb`, `plotly`, `matplotlib`, `ipywidgets` ve `jupyter` bulunur.

## 🧪 Veri Setini Yeniden Üretme

Projede örnek olarak kullanılan `sales_data.csv` dosyası zaten depo içinde yer alır. Güncel verilerle sıfırdan oluşturmak istersen:

```bash
python generate_sales_data.py
```

Script 1000 satırlık sahte satış verisi üretir ve çıktısını konsola özetler.

## 🚀 Marimo Uygulamasını Çalıştırma

```bash
marimo run sales_analysis.py
```

Komut tarayıcıda interaktif bir dashboard açar:

- 🗺️ Bölge filtreleri ve gelir eşiği slider'ı
- 📋 Filtre sonrası tablo görünümü
- 🧠 DuckDB ile dinamik SQL sorgusu
- 📊 Plotly ile ürün bazlı gelir grafiği
- 🧩 Marimo'nun reaktiflik, yeniden üretilebilirlik ve paylaşılabilirlik özelliklerini anlatan bilgi kartları

## 🎓 Eğitim Not Defterleri

Aşağıdaki dosyalar Marimo'nun farklı özelliklerini deneyimlemek için hazırlanmış öğrenme senaryolarıdır:

1. 🧠 `01_reactive_basics_notebook.py` – Reaktif hücre mantığı ve veri akışı  
2. 🎚️ `02_ui_components_notebook.py` – Dropdown, slider gibi UI bileşenleri  
3. 🗄️ `03_sql_notebook.py` – DuckDB üzerinden SQL entegrasyonu  
4. 📈 `04_plotting_notebook.py` – Plotly ile görselleştirme  
5. 🧮 `05_dataframe_notebook.py` – DataFrame keşfi ve filtreleme  
6. 🧭 `06_interactive_dashboard_notebook.py` – Bir araya getirilmiş dashboard örneği

Her birini Marimo ile görüntülemek için:

```bash
marimo run 01_reactive_basics_notebook.py   # Uygulama olarak çalıştırır, yalnızca izlersin
# veya
marimo edit 02_ui_components_notebook.py   # Editör arayüzünü açar, hücreleri değiştirip kaydedebilirsin
```

## 🛠️ Geliştirme İpuçları

- 🌱 Değişiklik yapmadan önce yeni bir branch aç: `git checkout -b feature/isim`
- ✍️ Küçük ve anlamlı commit mesajları kullan
- 📁 Eğer yeni notebook eklersen, `.gitignore` dosyasındaki kurallara uyduğundan emin ol

## 📄 Lisans

Bu depo eğitim amaçlıdır; lisans bilgisi belirtilmemiştir. Projeyi kullanırken şirket/kurum politikalarına uygun davrandığından emin ol.

## 🤝 Marimo ile Jupyter Notebook Karşılaştırması

- ⚡ **Reaktif çalışma modeli:** Marimo'da bir hücreyi çalıştırdığında ona bağlı hücreler otomatik yeniden çalışır veya stale olarak işaretlenir; Jupyter'da sıralı çalıştırma zorunludur ve gizli durum oluşabilir. [Marimo highlights](https://docs.marimo.io/?utm_source=chatgpt.com#highlights)
- 🧬 **Git uyumluluğu:** Her notebook saf `.py` dosyasıdır, difflere bakmak ve sürüm kontrolünde çalışmak kolaydır; Jupyter JSON yapısı gereği karmaşık diff üretir. [Marimo highlights](https://docs.marimo.io/?utm_source=chatgpt.com#highlights)
- 🧩 **Yapılandırılmış UI bileşenleri:** Slider, dropdown, tablo gibi bileşenler Python değişkenlerine doğrudan bağlanır, callback yazmaya gerek kalmaz; Jupyter'da benzer deneyim için ek kütüphaneler gerekir. [Marimo highlights](https://docs.marimo.io/?utm_source=chatgpt.com#highlights)
- 🛢️ **Dahili SQL ve veri araçları:** DataFrame'ler üzerinde yerleşik filtreleme, SQL sorguları ve hızlı tablo görünümü sunar; Jupyter'da bu deneyim parçalıdır. [Marimo highlights](https://docs.marimo.io/?utm_source=chatgpt.com#highlights)
- 🔁 **Tekrarlanabilirlik ve performans:** Marimo deterministik yürütme sırası ve paket yönetimiyle tutarlı sonuçlar üretir; Jupyter'da aynı deneyimi sağlayacak standart bir mekanizma yoktur. [Marimo highlights](https://docs.marimo.io/?utm_source=chatgpt.com#highlights)

