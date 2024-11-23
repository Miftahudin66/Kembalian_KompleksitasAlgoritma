class Kembalian:
    @staticmethod
    def min_koin(jumlah):
        # Daftar koin yang tersedia
        koin = [2, 3, 5, 10, 15]
        # Array untuk menyimpan jumlah minimum koin yang dibutuhkan
        dp = [float('inf')] * (jumlah + 1)
        dp[0] = 0

        # Proses untuk mencari jumlah minimum koin
        for i in range(1, jumlah + 1):
            for k in koin:
                if i - k >= 0:
                    dp[i] = min(dp[i], dp[i - k] + 1)

        return dp[jumlah] if dp[jumlah] != float('inf') else -1


if __name__ == "__main__":
    try:
        # Input dari pengguna
        jumlah = int(input("Masukkan jumlah yang ingin dikembalikan: "))
        
        result = Kembalian.min_koin(jumlah)

        if result != -1:
            print(f"Jumlah koin minimum yang dibutuhkan untuk {jumlah} adalah: {result}")
        else:
            print("Tidak mungkin untuk mendapatkan jumlah tersebut dengan koin yang tersedia.")
    except ValueError:
        print("Harap masukkan angka yang valid.")
