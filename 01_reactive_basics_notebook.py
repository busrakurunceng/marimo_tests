"""
Marimo: Reaktif Programlama Temelleri
=====================================

Bu notebook, Marimo'nun reaktif hücre sistemini gösterir.
Bir hücredeki değişiklik, bağımlı hücreleri otomatik olarak günceller.
"""

import marimo

__generated_with = "0.1.0"
app = marimo.App(width="medium")


@app.cell
def __():
    """
    ## Reaktif Hücre Sistemi
    
    Marimo'da bir değişken değiştiğinde, ona bağımlı tüm hücreler
    otomatik olarak yeniden çalıştırılır.
    """
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    """
    ### Slider ile Değer Seçimi
    
    Slider'ı hareket ettirdiğinizde, aşağıdaki hücreler otomatik güncellenir.
    """
    number = mo.ui.slider(
        start=1,
        stop=100,
        value=50,
        label="Sayı Seçin",
        full_width=True
    )
    number


@app.cell
def __(number):
    """
    ### Bağımlı Hesaplama
    
    Bu hücre, yukarıdaki slider değerine bağımlıdır.
    Slider değiştiğinde bu hücre OTOMATIK olarak çalışır.
    """
    squared = number.value ** 2
    doubled = number.value * 2
    return squared, doubled


@app.cell
def __(number, squared, doubled, mo):
    """
    ### Sonuç Gösterimi
    
    Tüm değerler otomatik olarak güncellenir.
    """
    mo.md(f"""
    **Reaktif Hesaplama Sonuçları:**
    
    - Seçilen sayı: **{number.value}**
    - Karesi: **{squared}**
    - İki katı: **{doubled}**
    - Toplam: **{number.value + squared + doubled}**
    
    👆 Yukarıdaki slider'ı değiştirin ve bu değerlerin otomatik güncellendiğini görün!
    """)


@app.cell
def __(mo):
    """
    ### Çoklu UI Bileşenleri
    
    Birden fazla UI bileşeni kullanabilirsiniz.
    """
    name = mo.ui.text(
        value="Marimo",
        label="İsim",
        placeholder="İsminizi girin",
        full_width=True
    )
    
    age = mo.ui.slider(
        start=0,
        stop=120,
        value=25,
        label="Yaş",
        full_width=True
    )
    
    active = mo.ui.checkbox(
        value=True,
        label="Aktif"
    )
    
    return name, age, active


@app.cell
def __(name, age, active, mo):
    """
    ### Dinamik İçerik
    
    UI bileşenlerindeki değerler değiştiğinde bu içerik otomatik güncellenir.
    """
    status = "aktif" if active.value else "pasif"
    
    mo.md(f"""
    **Kullanıcı Bilgileri:**
    
    - İsim: **{name.value}**
    - Yaş: **{age.value}**
    - Durum: **{status}**
    
    {name.value}, {age.value} yaşında ve {status} durumda.
    """)


@app.cell
def __(name, age, active):
    """
    ### Programatik Hesaplama
    
    UI değerleri Python kodunda kullanılabilir.
    """
    user_info = {
        "name": name.value,
        "age": age.value,
        "active": active.value,
        "next_year_age": age.value + 1
    }
    return user_info,


@app.cell
def __(user_info, mo):
    """
    ### Dictionary Gösterimi
    
    Python objelerini görselleştirebilirsiniz.
    """
    mo.md(f"""
    **Kullanıcı Bilgileri (Dictionary):**
    
    ```python
    {user_info}
    ```
    """)


if __name__ == "__main__":
    app.run()

