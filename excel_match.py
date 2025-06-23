import pandas as pd
import argparse


def match_excel(file1, file2, key, output="match_output.xlsx"):
    """Eşleşen verileri belirtilen sütun üzerinde birleştirir ve Excel'e kaydeder."""
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)
    merged = df1.merge(df2, on=key, how="inner")
    merged.to_excel(output, index=False)
    print(f"✅ {output} başarıyla oluşturuldu. {len(merged)} satır eşleşti.")


def main():
    parser = argparse.ArgumentParser(description="İki Excel dosyasındaki verileri belirtilen anahtar sütun üzerinden eşleştirir.")
    parser.add_argument("file1", help="Birinci Excel dosyası")
    parser.add_argument("file2", help="İkinci Excel dosyası")
    parser.add_argument("key", help="Eşleştirilecek sütun adı")
    parser.add_argument("-o", "--output", default="match_output.xlsx", help="Çıktı dosya adı")
    args = parser.parse_args()
    match_excel(args.file1, args.file2, args.key, args.output)


if __name__ == "__main__":
    main()
