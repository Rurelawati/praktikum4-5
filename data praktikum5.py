# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:48:46 2020

@author: ASUS
"""

print("======================================================================")
print("=========================> Program Input Data <=======================")
print("======================================================================")
data = {}
while True:
    print("")
    m = input("===>> (L)ihat,  (T)ambah,  (U)bah,  (H)apus,  (C)ari,  (K)eluar <<=== : ")
    print("========================================================================")
    print("| NO |     Nama      |     Nim     |  Tugas  |  UTS  |  UAS  |  Akhir  |")
    print("========================================================================")
    print(">>>>>>>>>>>>>>>>>>>>>>>> TIDAK ADA DATA <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    if m.lower() == 'k' :
        break
    
    elif m.lower() == 'l' :
        print("DAFTAR NILAI")
        print("=====================================================================")
        print("| NO |     NAMA    |    NIM     |  TUGAS  |  UTS  |  UAS  |  AKHIR  |")
        print("=====================================================================")
        i = 0
        for x in data.items():
            i += 1
            print(" 1 |  {0:9}  |  {1:9}  |  {2:9}  |  {3:9}  |  {4:9}  |  {5:9}  |" .format(
                x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4]))
            
        else:
            print("Tidak ada Data")
        
    elif m.lower() == 't' :
        print("Tambah Data")
        nama = input("Nama                        : ")
        nim = input("Nim                          : ")
        tugas = float(input("Masukan Nilai Tugas  : "))
        uts = float(input("Masukan Nilai UTS      : "))
        uas = float(input("Masukan Nilai UAS      : "))
        akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
        data[nama] = nim, tugas, uts, uas, akhir
        
    elif m.lower() == 'u' :
        print("Ubah Data Mahasiswa")
        nama = input("Nama  : ")
        if nama in data.keys():
            nim = input("Nim  :")
            tugas = float(input("Masukan Nilai tugas : " ))
            uts = float(input("Masukan Nilai uts  : "))
            uas = float(input("Masukan Nilai uas  : "))
            akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
            data[nama] = nim, tugas, uts, uas, akhir
        
        else:
            print("Tidak ada Data")
    
    elif m.lower() == 'h' :
        print("Hapus Data Mahasiswa")
        nama = input("Nama   : ")
        if nama in data.keys():
            print("Datanya", nama, "adalah {0}".format(data[nama]))
        else:
            print("Tidak ada Data")
    
    else:
        print("Plih menu yang tersedia")
        
            
            
            
    
        
        
    
    
    
     
