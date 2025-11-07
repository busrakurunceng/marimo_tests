"""
Marimo: İnteraktif Dashboard Örneği
===================================

Bu notebook, tüm özellikleri bir araya getiren kapsamlı bir dashboard örneğidir.
"""

import marimo

__generated_with = "0.1.0"
app = marimo.App(width="medium")


@app.cell
def __():
    """
    ## İnteraktif Dashboard
    
    Bu dashboard, Marimo'nun tüm özelliklerini bir araya getirir:
    - Reaktif hücreler
    - UI bileşenleri
    - Veri görselleştirme
    - SQL sorguları
    - Layout bileşenleri
    """
    import marimo as mo
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    from datetime import datetime, timedelta
    
    return mo, pd, np, px, go, datetime, timedelta


@app.cell
def __(pd, np, datetime, timedelta):
    """
    ### Veri Oluşturma
    
    Dashboard için örnek veri oluşturuyoruz.
    """
    np.random.seed(42)
    
    # Tarih aralığı (son 90 gün)
    data_start_date = datetime.now() - timedelta(days=90)
    dates = [data_start_date + timedelta(days=x) for x in range(90)]
    
    # Ürün kategorileri
    products = ['Laptop', 'Telefon', 'Tablet', 'Kulaklık', 'Kamera']
    regions = ['İstanbul', 'Ankara', 'İzmir', 'Bursa']
    
    # Veri oluştur
    data = []
    for date in dates:
        for product in products:
            for region in regions:
                if np.random.random() > 0.3:  # %70 olasılıkla satış
                    data.append({
                        'date': date,
                        'product': product,
                        'region': region,
                        'quantity': np.random.randint(1, 20),
                        'price': np.random.normal(1000, 200),
                        'revenue': 0  # Sonra hesaplanacak
                    })
    
    df = pd.DataFrame(data)
    df['revenue'] = df['quantity'] * df['price']
    df['revenue'] = df['revenue'].round(2)
    
    return df,


@app.cell
def __(df, mo):
    """
    ### Dashboard Başlığı
    
    Dashboard başlığı ve açıklama.
    """
    mo.md("""
    # 📊 Satış Dashboard'u
    
    Bu dashboard, Marimo'nun tüm özelliklerini gösteren kapsamlı bir örnektir.
    
    **Özellikler:**
    - ⚡ Reaktif hücre sistemi
    - 🎛️ İnteraktif filtreler
    - 📈 Dinamik grafikler
    - 📊 SQL sorguları
    - 🎨 Modern layout
    """)


@app.cell
def __(mo, df, pd):
    """
    ### Filtreler
    
    Dashboard filtreleri.
    """
    # Tarih aralığı için basit bir yaklaşım (date_range yerine)
    # Tarihleri date formatına çevir
    min_date = df['date'].min().date() if hasattr(df['date'].min(), 'date') else df['date'].min()
    max_date = df['date'].max().date() if hasattr(df['date'].max(), 'date') else df['date'].max()
    
    # Basit tarih seçimi için dropdown veya slider kullan
    # Bu örnekte tarih filtresini kaldırıp sadece diğer filtreleri kullanıyoruz
    # Alternatif olarak, tarih filtresini opsiyonel yapabiliriz
    
    product_filter = mo.ui.multiselect(
        options=sorted(df['product'].unique().tolist()),
        value=sorted(df['product'].unique().tolist()),
        label="Ürünler",
        full_width=True
    )
    
    region_filter = mo.ui.dropdown(
        options=["Tümü"] + sorted(df['region'].unique().tolist()),
        value="Tümü",
        label="Bölge",
        full_width=True
    )
    
    min_revenue = mo.ui.slider(
        start=0,
        stop=int(df['revenue'].max()),
        step=100,
        value=0,
        label="Minimum Gelir",
        full_width=True
    )
    
    return product_filter, region_filter, min_revenue


@app.cell
def __(mo, product_filter, region_filter, min_revenue):
    """
    ### Filtre Kontrol Paneli
    
    UI bileşenlerini gösteriyoruz.
    """
    mo.vstack([
        mo.md("#### 🎛️ Filtreler"),
        product_filter,
        region_filter,
        min_revenue,
    ], gap=2)


@app.cell
def __(df, product_filter, region_filter, min_revenue):
    """
    ### Veri Filtreleme
    
    Filtrelere göre veriyi filtreliyoruz.
    """
    filtered_df = df.copy()
    
    # Ürün filtresi
    if product_filter.value:
        filtered_df = filtered_df[filtered_df['product'].isin(product_filter.value)]
    
    # Bölge filtresi
    if region_filter.value != "Tümü":
        filtered_df = filtered_df[filtered_df['region'] == region_filter.value]
    
    # Gelir filtresi
    filtered_df = filtered_df[filtered_df['revenue'] >= min_revenue.value]
    
    return filtered_df,


@app.cell
def __(filtered_df, mo):
    """
    ### Özet İstatistikler
    
    Dashboard için özet istatistikler.
    """
    total_revenue = filtered_df['revenue'].sum()
    total_quantity = filtered_df['quantity'].sum()
    avg_price = filtered_df['price'].mean()
    total_transactions = len(filtered_df)
    
    mo.hstack([
        mo.stat(
            label="Toplam Gelir",
            value=f"${total_revenue:,.2f}",
            caption=f"{total_transactions} işlem"
        ),
        mo.stat(
            label="Toplam Miktar",
            value=f"{total_quantity:,}",
            caption="Adet"
        ),
        mo.stat(
            label="Ortalama Fiyat",
            value=f"${avg_price:,.2f}",
            caption="Birim başına"
        ),
    ], justify="space-around", gap=2)


@app.cell
def __(filtered_df, px, mo):
    """
    ### Grafikler
    
    Filtrelenmiş veri için grafikler.
    """
    # Ürün bazında gelir
    product_revenue = filtered_df.groupby('product')['revenue'].sum().reset_index()
    product_revenue = product_revenue.sort_values('revenue', ascending=True)
    
    fig1 = px.bar(
        product_revenue,
        x='revenue',
        y='product',
        orientation='h',
        title='Ürün Bazında Toplam Gelir',
        color='revenue',
        color_continuous_scale='Viridis'
    )
    fig1.update_layout(height=300)
    
    # Bölge bazında gelir
    region_revenue = filtered_df.groupby('region')['revenue'].sum().reset_index()
    
    fig2 = px.pie(
        region_revenue,
        values='revenue',
        names='region',
        title='Bölge Bazında Gelir Dağılımı'
    )
    fig2.update_layout(height=300)
    
    # Zaman serisi
    daily_revenue = filtered_df.groupby('date')['revenue'].sum().reset_index()
    
    fig3 = px.line(
        daily_revenue,
        x='date',
        y='revenue',
        title='Günlük Gelir Trendi',
        markers=True
    )
    fig3.update_layout(height=300)
    
    mo.vstack([
        mo.hstack([
            mo.ui.plotly(fig1),
            mo.ui.plotly(fig2)
        ], justify="start", gap=2),
        mo.ui.plotly(fig3)
    ], gap=3)


@app.cell
def __(filtered_df, mo):
    """
    ### Detaylı Tablo
    
    Filtrelenmiş veriyi tablo olarak görüntülüyoruz.
    """
    mo.md("#### 📊 Detaylı Veri Tablosu")
    mo.ui.table(filtered_df.head(100))


@app.cell
def __(filtered_df, mo):
    """
    ### Özet Rapor
    
    Filtrelenmiş veri için özet rapor.
    """
    summary = filtered_df.groupby(['product', 'region']).agg({
        'revenue': 'sum',
        'quantity': 'sum'
    }).reset_index()
    summary = summary.sort_values('revenue', ascending=False)
    
    mo.md("#### 📈 Ürün ve Bölge Bazında Özet")
    mo.ui.table(summary.head(20))


if __name__ == "__main__":
    app.run()

