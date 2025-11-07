"""
Sahte satış verisi oluşturucu
Bu script, test için gerçekçi satış verisi üretir.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Rastgelelik için seed
np.random.seed(42)

# Bölgeler ve ürünler
regions = ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya']
products = ['Laptop', 'Telefon', 'Tablet', 'Kulaklık', 'Kamera', 'Monitör', 'Klavye', 'Mouse']

# Tarih aralığı (son 6 ay)
start_date = datetime.now() - timedelta(days=180)
dates = [start_date + timedelta(days=x) for x in range(180)]

# Veri oluştur
data = []
for _ in range(1000):
    region = np.random.choice(regions)
    product = np.random.choice(products)
    date = np.random.choice(dates)
    
    # Bölge ve ürüne göre farklı gelir dağılımları
    base_revenue = {
        'İstanbul': 50000,
        'Ankara': 35000,
        'İzmir': 40000,
        'Bursa': 30000,
        'Antalya': 32000
    }[region]
    
    product_multiplier = {
        'Laptop': 1.5,
        'Telefon': 1.2,
        'Tablet': 0.8,
        'Kulaklık': 0.3,
        'Kamera': 1.0,
        'Monitör': 0.6,
        'Klavye': 0.2,
        'Mouse': 0.15
    }[product]
    
    revenue = np.random.normal(base_revenue * product_multiplier, base_revenue * 0.3)
    revenue = max(1000, revenue)  # Minimum gelir
    
    quantity = np.random.randint(1, 50)
    
    data.append({
        'date': date.strftime('%Y-%m-%d'),
        'region': region,
        'product': product,
        'quantity': quantity,
        'revenue': round(revenue, 2),
        'unit_price': round(revenue / quantity, 2)
    })

# DataFrame oluştur
df = pd.DataFrame(data)

# CSV'ye kaydet
df.to_csv('sales_data.csv', index=False, encoding='utf-8-sig')
print(f"✅ {len(df)} satırlık satış verisi 'sales_data.csv' dosyasına kaydedildi.")
print(f"📊 Veri özeti:")
print(df.describe())
print(f"\n📈 Bölge bazında toplam gelir:")
print(df.groupby('region')['revenue'].sum().sort_values(ascending=False))

