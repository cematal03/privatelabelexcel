import pandas as pd

# Basit bir tablo oluştur
data = {
    "Ürün": ["Ürün A", "Ürün B", "Ürün C"],
    "Fiyat": [100, 150, 200],
    "Stok": [50, 75, 100]
}
df = pd.DataFrame(data)

# Excel olarak kaydet
df.to_excel("test_output.xlsx", index=False)

print("✅ test_output.xlsx başarıyla oluşturuldu.")
