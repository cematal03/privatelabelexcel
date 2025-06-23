# privatelabelexcel

Bu proje basit Excel işlemlerini göstermek için örnek Python betikleri içerir.

## Mevcut Betikler

- `test_excel.py`: Örnek bir tablo oluşturup `test_output.xlsx` dosyasına kaydeder.
- `excel_match.py`: İki Excel dosyasındaki verileri ortak bir sütuna göre eşleştirip `match_output.xlsx` dosyasına kaydeder.

## Kullanım

```bash
python test_excel.py
```

```bash
python excel_match.py dosya1.xlsx dosya2.xlsx AnahtarSutun -o sonuc.xlsx
```

Her iki komut da başarıyla tamamlandığında ilgili Excel dosyalarını oluşturur.
