"""
Marimo: DataFrame İşlemleri
===========================

Bu notebook, Marimo'da DataFrame işlemlerini gösterir.
"""

import marimo

__generated_with = "0.1.0"
app = marimo.App(width="medium")


@app.cell
def __():
    """
    ## DataFrame İşlemleri
    
    Marimo'da DataFrame'leri görüntülemek, filtrelemek ve düzenlemek kolaydır.
    """
    import marimo as mo
    import pandas as pd
    import numpy as np
    return mo, pd, np


@app.cell
def __(pd, np):
    """
    ### Örnek DataFrame Oluşturma
    
    Test için büyük bir DataFrame oluşturuyoruz.
    """
    np.random.seed(42)
    
    data = {
        'id': range(1, 1001),
        'name': [f'Kullanıcı {i}' for i in range(1, 1001)],
        'age': np.random.randint(18, 80, 1000),
        'city': np.random.choice(['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya'], 1000),
        'salary': np.random.normal(50000, 15000, 1000),
        'department': np.random.choice(['IT', 'Sales', 'Marketing', 'HR', 'Finance'], 1000),
        'join_date': pd.date_range('2020-01-01', periods=1000, freq='D')
    }
    
    df = pd.DataFrame(data)
    df['salary'] = df['salary'].round(2)
    
    return df,


@app.cell
def __(df, mo):
    """
    ### DataFrame Görüntüleme
    
    DataFrame'i interaktif bir tablo olarak görüntüleyebilirsiniz.
    """
    mo.md(f"""
    **DataFrame Özeti:**
    
    - Toplam satır: {len(df)}
    - Sütunlar: {', '.join(df.columns.tolist())}
    """)
    
    mo.ui.table(df.head(20))


@app.cell
def __(mo, df):
    """
    ### Filtreleme UI Bileşenleri
    
    DataFrame'i filtrelemek için UI bileşenleri kullanabilirsiniz.
    """
    min_age = mo.ui.slider(
        start=18,
        stop=80,
        step=1,
        value=25,
        label="Minimum Yaş",
        full_width=True
    )
    
    max_salary = mo.ui.slider(
        start=0,
        stop=100000,
        step=1000,
        value=100000,
        label="Maksimum Maaş",
        full_width=True
    )
    
    selected_city = mo.ui.dropdown(
        options=["Tümü"] + sorted(df['city'].unique().tolist()),
        value="Tümü",
        label="Şehir",
        full_width=True
    )
    
    selected_department = mo.ui.multiselect(
        options=sorted(df['department'].unique().tolist()),
        value=sorted(df['department'].unique().tolist()),
        label="Departman",
        full_width=True
    )
    
    search_text = mo.ui.text(
        value="",
        label="İsimde Ara",
        placeholder="Kullanıcı adında ara...",
        full_width=True
    )
    
    return min_age, max_salary, selected_city, selected_department, search_text


@app.cell
def __(df, min_age, max_salary, selected_city, selected_department, search_text):
    """
    ### Filtrelenmiş DataFrame
    
    UI bileşenlerine göre DataFrame'i filtreliyoruz.
    """
    filtered_df = df.copy()
    
    # Yaş filtresi
    filtered_df = filtered_df[filtered_df['age'] >= min_age.value]
    
    # Maaş filtresi
    filtered_df = filtered_df[filtered_df['salary'] <= max_salary.value]
    
    # Şehir filtresi
    if selected_city.value != "Tümü":
        filtered_df = filtered_df[filtered_df['city'] == selected_city.value]
    
    # Departman filtresi
    if selected_department.value:
        filtered_df = filtered_df[filtered_df['department'].isin(selected_department.value)]
    
    # İsim arama
    if search_text.value:
        filtered_df = filtered_df[
            filtered_df['name'].str.contains(search_text.value, case=False, na=False)
        ]
    
    return filtered_df,


@app.cell
def __(filtered_df, mo):
    """
    ### Filtrelenmiş Sonuçlar
    
    Filtrelenmiş DataFrame'i görüntülüyoruz.
    """
    mo.md(f"""
    **Filtre Sonuçları:**
    
    - Filtrelenmiş kayıt sayısı: {len(filtered_df)}
    - Ortalama yaş: {filtered_df['age'].mean():.1f}
    - Ortalama maaş: {filtered_df['salary'].mean():,.2f} TL
    """)
    
    mo.ui.table(filtered_df.head(50))


@app.cell
def __(filtered_df, mo):
    """
    ### Özet İstatistikler
    
    Filtrelenmiş veri için özet istatistikler.
    """
    summary = filtered_df.groupby('department').agg({
        'salary': ['mean', 'min', 'max', 'count'],
        'age': 'mean'
    }).round(2)
    
    summary.columns = ['Ortalama Maaş', 'Min Maaş', 'Max Maaş', 'Kişi Sayısı', 'Ortalama Yaş']
    
    mo.md("#### Departman Bazında Özet İstatistikler")
    mo.ui.table(summary)


@app.cell
def __(filtered_df, mo):
    """
    ### Şehir Bazında Dağılım
    
    Şehirlere göre kullanıcı dağılımı.
    """
    city_dist = filtered_df['city'].value_counts().reset_index()
    city_dist.columns = ['Şehir', 'Kullanıcı Sayısı']
    
    mo.md("#### Şehir Bazında Kullanıcı Dağılımı")
    mo.ui.table(city_dist)


if __name__ == "__main__":
    app.run()

