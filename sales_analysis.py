import marimo

__generated_with = "0.17.7"
app = marimo.App()


@app.cell
def intro():
    import marimo as mo
    mo.md("""
    # 🧩 Marimo Deneyi: Etkileşimli Satış Analiziii
    Bu notebook, Marimo’nun **reaktif hücre sistemi**, **UI bileşenleri**, **SQL entegrasyonuuu**, 
    **veri görselleştirme** ve **yeniden üretilebilirlik** özelliklerini test eder.
    """)
    return (mo,)


@app.cell
def features():
    def _():
        import marimo as mo
        return mo.md("""
        ## 🔋 batteries-included  
        Jupyter, Streamlit, Jupytext, ipywidgets, Papermill ve daha fazlasının yerini alabilecek **tümleşik bir yapı** sunar.  

        ---

        ## ⚡ reactive  
        Bir hücreyi çalıştırdığında, ona bağlı tüm hücreler **otomatik olarak yeniden çalıştırılır** veya **eski (stale)** olarak işaretlenir.  

        ---

        ## 🖐️ interactive  
        **Slaytlar, tablolar, grafikler** ve benzeri bileşenleri doğrudan Python değişkenlerine bağlayabilirsin.  
        Callback fonksiyonlarına gerek yoktur.  

        ---

        ## 🐍 git-friendly  
        Tüm not defterleri **.py uzantılı dosyalar** olarak saklanır, böylece sürüm kontrol sistemleriyle uyumludur.  

        ---

        ## 🛢️ designed for data  
        DataFrame'ler, veritabanları, veri ambarları ve gölleri (lakehouse) üzerinde **SQL sorguları** çalıştırabilir, veri filtreleme ve arama işlemleri yapabilirsin.  

        ---

        ## 🤖 AI-native  
        Veri odaklı çalışmalar için **yapay zekâ destekli hücre oluşturma** özelliği içerir.  

        ---

        ## 🔬 reproducible  
        Gizli durum (hidden state) yoktur.  
        **Deterministik çalışma** ve **yerleşik paket yönetimi** ile tekrarlanabilir sonuçlar üretir.  

        ---

        ## 🏃 executable  
        Not defterleri **Python scripti olarak çalıştırılabilir** ve **CLI parametreleriyle** özelleştirilebilir.  

        ---

        ## 🛜 shareable  
        Çalışmanı **etkileşimli bir web uygulaması** veya **sunum slaytı** olarak paylaşabilir, hatta tarayıcıda **WASM** ile çalıştırabilirsin.  

        ---

        ## 🧩 reusable  
        Bir not defterinde tanımladığın fonksiyon veya sınıfları başka bir not defterinde **import** edebilirsin.  

        ---

        ## 🧪 testable  
        Not defterini doğrudan **pytest** ile test edebilirsin.  

        ---

        ## ⌨️ modern editor  
        GitHub Copilot, AI asistanları, **vim tuşları**, değişken gezgini (variable explorer) gibi modern editör özelliklerini destekler.  
        """)


    _()
    return


@app.cell
def load_data(mo):
    import pandas as pd
    data = pd.read_csv("sales_data.csv")
    mo.md("### 📊 Örnek Satış Verisi")
    mo.ui.dataframe(data.head())
    return (data,)


@app.cell
def ui_elements(data, mo):
    region_selector = mo.ui.dropdown(
        label="Bölge seçin:",
        options=["Tümü"] + list(data["region"].unique()),
        value="Tümü"
    )
    min_revenue_slider = mo.ui.slider(0, 4500, 100, label="Minimum gelir filtresi:")
    mo.md("### 🔧 Filtre Seçimleri")
    region_selector
    min_revenue_slider
    return min_revenue_slider, region_selector


@app.cell
def filter_data(data, min_revenue_slider, mo, region_selector):
    filtered_df = data.copy()
    if region_selector.value != "Tümü":
        filtered_df = filtered_df[filtered_df["region"] == region_selector.value]
    filtered_df = filtered_df[filtered_df["revenue"] >= min_revenue_slider.value]
    mo.md("### 🔍 Filtrelenmiş Veri")
    mo.ui.dataframe(filtered_df)
    return


@app.cell
def sql_query(min_revenue_slider, mo):
    import duckdb
    query = f"""
    SELECT region, product, revenue
    FROM filtered_df
    WHERE revenue >= {min_revenue_slider.value}
    """
    sql_result = duckdb.sql(query).to_df()
    mo.md("### 🧠 SQL Sorgu Sonucu")
    mo.ui.dataframe(sql_result)
    return (sql_result,)


@app.cell
def visualize(mo, region_selector, sql_result):
    import plotly.express as px
    fig = px.bar(sql_result, x="product", y="revenue", color="region",
                 title=f"Satış Gelirleri ({region_selector.value})")
    mo.md("### 📈 Dinamik Grafik (Plotly)")
    mo.ui.plotly(fig)
    return


@app.cell
def reactive_example(mo):
    a = 5
    b = a * 2
    mo.md(f"#### 🧮 Reaktif Örnek: a = {a}, b = a*2 = {b}")
    return


@app.cell
def reproducibility(mo):
    mo.md("""
    ### 🔁 Yeniden Üretilebilirlik
    Marimo, hücreleri **bağımlılık sırasına göre otomatik yeniden çalıştırır**.
    Bu yüzden hücreleri karışık sırada çalıştırsan bile sonuçlar tutarlıdır.
    """)
    return


@app.cell
def conclusion(mo):
    mo.md("""
    ## ✅ Sonuç
    Bu notebook:
    - Reaktif hücre sistemiyle **otomatik güncellenen bağımlılıklar** gösterdi
    - **UI bileşenleri**yle kullanıcı etkileşimi sağladı
    - **SQL entegrasyonu** ve **Plotly görselleştirme** içerdi
    - **Yeniden üretilebilir** sonuçlar üretti

    ▶️ `marimo run sales_analysis_marimo.py` komutuyla çalıştırabilirsin.
    """)
    return


if __name__ == "__main__":
    app.run()
