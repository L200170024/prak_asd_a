##NO.1
class MhsTIF(object):
    def __init__(self, nama, umur, kota, NIM):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.nim = NIM

    def __str__(self):
        x = self.nim
        return x

    def getnim(self):
        return self.nim

m0 = MhsTIF('Tika pratiwi', 13, 'Magetan','L200180048')
m1 = MhsTIF('Ika', 12, 'Sukoharjo','L200180028')
m2 = MhsTIF('Ahmad', 20, 'Surakarta', 'L200180018')
m3 = MhsTIF('Chandra', 18, 'Surakarta','L200180012')
m4 = MhsTIF('Eka', 14, 'Boyolali','L200180132')
m5 = MhsTIF('Fandi', 31, 'Salatiga','L200180042')
m6 = MhsTIF('Deni', 13, 'Klaten', 'L200180088')
m7 = MhsTIF('Galuh', 15, 'Wonogiri', 'L200180014')
m8 = MhsTIF('Janto', 23, 'Klaten', 'L200180022')
m9 = MhsTIF('Hasan', 24, 'Karanganyar', 'L200180124')
m10 = MhsTIF('Khalid', 29, 'Purwodadi', 'L200180089')
m11 = MhsTIF('Budi', 41, 'Klaten', 'L200180010')

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11]

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai.nim < A[pos - 1].nim:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

def cetakDaftar(d):
    for i in d:
        print (i)
        
insertionSort(Daftar)
cetakDaftar(Daftar)

##NO.2
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

A = [1,2,3,4,5,8,11,13,14,15]
B = [6,7,9,10,12,16,18,20,22]
C = []
C.extend(A)
C.extend(B)
print ('Nilai C' , C)

##NO.3
from time import time as detak
from random import shuffle as kocok
def swap(A,p,q):
    tmp = A[p]
    A[q]= A[q]
    A[q]= tmp
    
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range (n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
                
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil=dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i]<A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil   

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)
            
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

k = []
for i in range(1, 6001):
    k.append(i)
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw=detak();bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw));
aw=detak();selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw));
aw=detak();insertionSort(u_ins);ak=detak();print('insertion:%g detik' %(ak-aw));
