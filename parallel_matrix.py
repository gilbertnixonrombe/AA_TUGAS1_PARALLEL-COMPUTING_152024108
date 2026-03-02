import multiprocessing

# Fungsi untuk menghitung satu baris dari hasil perkalian matriks
def compute_row(args):
    row_A, B = args
    result_row = [0] * len(B[0])
    for j in range(len(B[0])):
        for k in range(len(B)):
            result_row[j] += row_A[k] * B[k][j]
    return result_row

if __name__ == '__main__':
    # Matriks A (3x2)
    A = [[1, 2],
         [3, 4],
         [5, 6]]
         
    # Matriks B (2x3)
    B = [[7, 8, 9],
         [10, 11, 12]]

    print("Memulai komputasi matriks paralel...")

    # Membuat Pool untuk multiprocessing (menggunakan core CPU yang tersedia)
    pool = multiprocessing.Pool()
    
    # Menyiapkan argumen: setiap baris dari A dipasangkan dengan seluruh matriks B
    args = [(row, B) for row in A]
    
    # Memetakan fungsi komputasi ke dalam pool proses
    result = pool.map(compute_row, args)
    
    pool.close()
    pool.join()

    print("\nHasil Perkalian Matriks:")
    for row in result:
        print(row)
