"""
Marimo: SQL Entegrasyonu
========================

Bu notebook, Marimo'nun SQL entegrasyonunu gösterir.
SQL sorguları Python değişkenlerini kullanabilir.
"""

import marimo

__generated_with = "0.1.0"
app = marimo.App(width="medium")


@app.cell
def __():
    """
    ## SQL ile Veri Sorgulama
    
    Marimo'da SQL hücreleri oluşturabilir ve Python değişkenlerini kullanabilirsiniz.
    """
    import marimo as mo
    import pandas as pd
    import numpy as np
    return mo, pd, np


@app.cell
def __(pd, np):
    """
    ### Örnek Veri Oluşturma
    
    Test için bir DataFrame oluşturuyoruz.
    """
    # Örnek satış verisi
    np.random.seed(42)
    data = {
        'product': np.random.choice(['Laptop', 'Telefon', 'Tablet', 'Kulaklık'], 100),
        'region': np.random.choice(['İstanbul', 'Ankara', 'İzmir'], 100),
        'price': np.random.normal(1000, 300, 100),
        'quantity': np.random.randint(1, 50, 100),
        'date': pd.date_range('2024-01-01', periods=100, freq='D')
    }
    df = pd.DataFrame(data)
    df['revenue'] = df['price'] * df['quantity']
    
    return df,


@app.cell
def __(df, mo):
    """
    ### Veri Önizleme
    
    DataFrame'i görüntülüyoruz.
    """
    mo.md(f"""
    **Veri Özeti:**
    
    - Toplam kayıt: {len(df)}
    - Sütunlar: {', '.join(df.columns.tolist())}
    """)
    mo.ui.table(df.head(10))


@app.cell
def __(mo):
    """
    ### SQL Parametreleri
    
    UI bileşenleri ile SQL sorgu parametrelerini kontrol edebilirsiniz.
    """
    min_price = mo.ui.slider(
        start=0,
        stop=2000,
        step=50,
        value=500,
        label="Minimum Fiyat",
        full_width=True
    )
    
    selected_region = mo.ui.dropdown(
        options=["Tümü", "İstanbul", "Ankara", "İzmir"],
        value="Tümü",
        label="Bölge",
        full_width=True
    )
    
    return min_price, selected_region


@app.cell
def __(df, min_price, selected_region):
    """
    ### SQL Sorgusu
    
    Python değişkenlerini SQL sorgusunda kullanabilirsiniz.
    Marimo otomatik olarak değişkenleri SQL'e enjekte eder.
    """
    # SQL sorgusu - Marimo otomatik olarak Python değişkenlerini kullanır
    # Not: Gerçek SQL hücresi için mo.sql() kullanılır, burada örnek olarak gösteriyoruz
    
    # Filtreleme
    filtered_df = df[df['price'] >= min_price.value]
    
    if selected_region.value != "Tümü":
        filtered_df = filtered_df[filtered_df['region'] == selected_region.value]
    
    # SQL benzeri sorgu (pandas ile)
    sql_result = filtered_df.groupby(['product', 'region']).agg({
        'revenue': 'sum',
        'quantity': 'sum',
        'price': 'mean'
    }).reset_index()
    
    sql_result.columns = ['product', 'region', 'total_revenue', 'total_quantity', 'avg_price']
    sql_result = sql_result.sort_values('total_revenue', ascending=False)
    
    return filtered_df, sql_result


@app.cell
def __(sql_result, mo):
    """
    ### SQL Sonuçları
    
    SQL sorgu sonuçlarını görüntülüyoruz.
    """
    mo.md("#### 📊 SQL Sorgu Sonuçları")
    mo.ui.table(sql_result)


@app.cell
def __(filtered_df, mo):
    """
    ### Filtrelenmiş Veri
    
    Filtrelenmiş DataFrame'i görüntülüyoruz.
    """
    mo.md(f"""
    **Filtre Sonuçları:**
    
    - Filtrelenmiş kayıt sayısı: {len(filtered_df)}
    - Toplam gelir: {filtered_df['revenue'].sum():,.2f} TL
    - Ortalama fiyat: {filtered_df['price'].mean():.2f} TL
    """)


@app.cell
def __(mo):
    """
    ### SQL Hücresi Örneği (Yorum)
    
    Marimo'da gerçek SQL hücreleri oluşturmak için mo.sql() fonksiyonunu kullanabilirsiniz.
    Bu şekilde Python değişkenlerini SQL sorgusunda kullanabilirsiniz.
    """
    mo.md("""
    **Not:** Bu örnekte pandas kullanarak SQL benzeri sorgular yaptık.
    Gerçek SQL hücreleri için `mo.sql()` fonksiyonunu kullanabilirsiniz.
    
    Örnek kullanım:
    ```python
    result = mo.sql(\"\"\"
        SELECT product, SUM(revenue) as total_revenue
        FROM df
        WHERE price > {{min_price}}
        GROUP BY product
        ORDER BY total_revenue DESC
    \"\"\")
    ```
    """)


if __name__ == "__main__":
    app.run()

