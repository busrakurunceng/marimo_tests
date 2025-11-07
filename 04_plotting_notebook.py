"""
Marimo: Veri Görselleştirme
===========================

Bu notebook, Marimo'da veri görselleştirme örneklerini gösterir.
"""

import marimo

__generated_with = "0.1.0"
app = marimo.App(width="medium")


@app.cell
def __():
    """
    ## Veri Görselleştirme
    
    Marimo'da Plotly, Matplotlib ve diğer görselleştirme kütüphanelerini kullanabilirsiniz.
    """
    import marimo as mo
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    return mo, pd, np, px, go


@app.cell
def __(pd, np):
    """
    ### Örnek Veri Oluşturma
    
    Görselleştirme için örnek veri oluşturuyoruz.
    """
    np.random.seed(42)
    
    # Zaman serisi verisi
    dates = pd.date_range('2024-01-01', periods=100, freq='D')
    sales = np.cumsum(np.random.normal(100, 20, 100))
    
    # Kategorik veri
    categories = ['A', 'B', 'C', 'D', 'E']
    values = np.random.randint(10, 100, 5)
    
    # Dağılım verisi
    x_data = np.random.normal(100, 15, 1000)
    y_data = np.random.normal(100, 15, 1000)
    
    return dates, sales, categories, values, x_data, y_data


@app.cell
def __(mo):
    """
    ### Grafik Parametreleri
    
    UI bileşenleri ile grafik parametrelerini kontrol edebilirsiniz.
    """
    chart_type = mo.ui.dropdown(
        options=["Çizgi Grafiği", "Bar Grafiği", "Dağılım Grafiği", "Pasta Grafiği"],
        value="Çizgi Grafiği",
        label="Grafik Tipi",
        full_width=True
    )
    
    color_scheme = mo.ui.dropdown(
        options=["Viridis", "Plasma", "Inferno", "Magma", "Cividis"],
        value="Viridis",
        label="Renk Şeması",
        full_width=True
    )
    
    return chart_type, color_scheme


@app.cell
def __(dates, sales, categories, values, x_data, y_data, chart_type, color_scheme, px, pd):
    """
    ### Dinamik Grafik Oluşturma
    
    UI bileşenlerine göre grafik tipi değişir.
    """
    color_map = {
        "Viridis": px.colors.sequential.Viridis,
        "Plasma": px.colors.sequential.Plasma,
        "Inferno": px.colors.sequential.Inferno,
        "Magma": px.colors.sequential.Magma,
        "Cividis": px.colors.sequential.Cividis,
    }
    
    if chart_type.value == "Çizgi Grafiği":
        chart_df = pd.DataFrame({'Tarih': dates, 'Satış': sales})
        chart_fig = px.line(
            chart_df,
            x='Tarih',
            y='Satış',
            title='Zaman Serisi - Satış Trendi',
            color_discrete_sequence=color_map[color_scheme.value]
        )
    elif chart_type.value == "Bar Grafiği":
        chart_df = pd.DataFrame({'Kategori': categories, 'Değer': values})
        chart_fig = px.bar(
            chart_df,
            x='Kategori',
            y='Değer',
            title='Bar Grafiği - Kategoriler',
            color='Değer',
            color_continuous_scale=color_scheme.value.lower()
        )
    elif chart_type.value == "Dağılım Grafiği":
        chart_df = pd.DataFrame({'X': x_data, 'Y': y_data})
        chart_fig = px.scatter(
            chart_df,
            x='X',
            y='Y',
            title='Dağılım Grafiği',
            color_discrete_sequence=color_map[color_scheme.value]
        )
    else:  # Pasta Grafiği
        chart_df = pd.DataFrame({'Kategori': categories, 'Değer': values})
        chart_fig = px.pie(
            chart_df,
            values='Değer',
            names='Kategori',
            title='Pasta Grafiği - Kategoriler',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
    
    chart_fig.update_layout(height=500)
    return chart_fig,


@app.cell
def __(chart_fig, mo):
    """
    ### Grafik Görüntüleme
    
    Plotly grafiklerini görüntülüyoruz.
    """
    mo.ui.plotly(chart_fig)


@app.cell
def __(dates, sales, px, mo, pd):
    """
    ### Çoklu Grafik
    
    Birden fazla grafik gösterebilirsiniz.
    """
    multi_df = pd.DataFrame({'Tarih': dates, 'Satış': sales})
    
    # İki grafik yan yana
    multi_fig1 = px.line(multi_df, x='Tarih', y='Satış', title='Satış Trendi')
    multi_fig1.update_layout(height=300)
    
    multi_fig2 = px.bar(multi_df.tail(20), x='Tarih', y='Satış', title='Son 20 Gün')
    multi_fig2.update_layout(height=300)
    
    mo.hstack([
        mo.ui.plotly(multi_fig1),
        mo.ui.plotly(multi_fig2)
    ], justify="start", gap=2)


@app.cell
def __(mo, np):
    """
    ### Matplotlib Örneği
    
    Matplotlib grafiklerini de kullanabilirsiniz.
    Not: Matplotlib yüklü değilse bu bölüm atlanır.
    """
    try:
        import matplotlib.pyplot as plt
        
        mpl_fig, ax = plt.subplots(figsize=(10, 6))
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y)
        ax.set_title('Matplotlib Grafiği - Sinüs Fonksiyonu')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        plt.tight_layout()
        
        mo.mpl(mpl_fig)
    except ImportError:
        mo.md("""
        **Matplotlib yüklü değil.**
        
        Matplotlib'i yüklemek için:
        ```bash
        pip install matplotlib
        ```
        """)


if __name__ == "__main__":
    app.run()

