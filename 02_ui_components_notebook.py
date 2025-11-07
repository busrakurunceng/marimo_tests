"""
Marimo: UI Bileşenleri Örnekleri
=================================

Bu notebook, Marimo'nun çeşitli UI bileşenlerini gösterir.
"""

import marimo

__generated_with = "0.1.0"
app = marimo.App(width="medium")


@app.cell
def __():
    """
    ## UI Bileşenleri Koleksiyonu
    
    Marimo'da çok çeşitli UI bileşenleri mevcuttur.
    """
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    """
    ### Metin Girişleri
    """
    text_input = mo.ui.text(
        value="",
        label="Metin Girişi",
        placeholder="Bir şeyler yazın...",
        full_width=True
    )
    
    textarea = mo.ui.text_area(
        value="",
        label="Çok Satırlı Metin",
        placeholder="Birden fazla satır yazabilirsiniz...",
        full_width=True
    )
    
    return text_input, textarea


@app.cell
def __(mo):
    """
    ### Sayısal Girişler
    """
    slider = mo.ui.slider(
        start=0,
        stop=100,
        step=1,
        value=50,
        label="Slider",
        full_width=True
    )
    
    number_input = mo.ui.number(
        start=0,
        stop=1000,
        step=1,
        value=100,
        label="Sayı Girişi",
        full_width=True
    )
    
    return slider, number_input


@app.cell
def __(mo):
    """
    ### Seçim Bileşenleri
    """
    dropdown = mo.ui.dropdown(
        options=["Seçenek 1", "Seçenek 2", "Seçenek 3", "Seçenek 4"],
        value="Seçenek 1",
        label="Dropdown",
        full_width=True
    )
    
    multiselect = mo.ui.multiselect(
        options=["Python", "JavaScript", "Java", "C++", "Go", "Rust"],
        value=["Python"],
        label="Çoklu Seçim",
        full_width=True
    )
    
    radio = mo.ui.radio(
        options=["Küçük", "Orta", "Büyük"],
        value="Orta",
        label="Radio Butonlar"
    )
    
    return dropdown, multiselect, radio


@app.cell
def __(mo):
    """
    ### Boolean Bileşenleri
    """
    checkbox = mo.ui.checkbox(
        value=True,
        label="Checkbox"
    )
    
    switch = mo.ui.switch(
        value=False,
        label="Switch"
    )
    
    return checkbox, switch


@app.cell
def __(mo):
    """
    ### Butonlar
    """
    button = mo.ui.button(
        label="Tıkla!",
        kind="primary",
        full_width=False
    )
    
    return button,


@app.cell
def __(mo, text_input, textarea, slider, number_input, dropdown, multiselect, radio, checkbox, switch, button):
    """
    ### UI Bileşenleri Gösterimi
    
    Tüm UI bileşenlerini bir arada gösteriyoruz.
    """
    mo.vstack([
        mo.md("#### 📝 Metin Girişleri"),
        text_input,
        textarea,
        mo.md("#### 🔢 Sayısal Girişler"),
        slider,
        number_input,
        mo.md("#### 📋 Seçim Bileşenleri"),
        dropdown,
        multiselect,
        radio,
        mo.md("#### ☑️ Boolean Bileşenleri"),
        checkbox,
        switch,
        mo.md("#### 🔘 Butonlar"),
        button,
    ], gap=2)


@app.cell
def __(text_input, textarea, slider, number_input, dropdown, multiselect, radio, checkbox, switch, button, mo):
    """
    ### Seçilen Değerler
    
    Tüm UI bileşenlerinin değerleri otomatik olarak güncellenir.
    """
    mo.md(f"""
    **Seçilen Değerler:**
    
    - Metin: `{text_input.value}`
    - Çok Satırlı: `{textarea.value[:50]}...` (ilk 50 karakter)
    - Slider: `{slider.value}`
    - Sayı: `{number_input.value}`
    - Dropdown: `{dropdown.value}`
    - Çoklu Seçim: `{multiselect.value}`
    - Radio: `{radio.value}`
    - Checkbox: `{checkbox.value}`
    - Switch: `{switch.value}`
    - Buton Tıklama Sayısı: `{button.value}`
    
    👆 Yukarıdaki bileşenleri değiştirin ve bu değerlerin otomatik güncellendiğini görün!
    """)


if __name__ == "__main__":
    app.run()

