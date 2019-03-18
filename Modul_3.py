##No.1

a = [[ 1 , 2 ], [ 3 , 4 ]]
b = [[ 5 , 6 ], [ 7 , 8 ]]
c = [[ 12 , 3 , " x " , " y " ], [ 12 , 33 , 4 ]]
d = [[ 3 , 4 ], [ 2 , 4 ], [ 1 , 5 ]]
e = [[ 5 , 6 , 7 ], [ 7 , 8 , 9 ]]
f = [[ 1 , 2 , 3 ], [ 4 , 5 , 6 ], [ 7 , 8 , 9 ]]

def   cekKonsis ( n ):
    x =   len (n [ 0 ])
    z =   0
    untuk saya dalam kisaran ( len (n)):
        if ( len (n [i]) == x):
           z +  =  1
    if (z ==   len (n)):
        print ( " matriks konsisten " )
    lain:
        print ( " matrik tidak konsisten " )

cekKonsis (a)
cekKonsis (b)
cekKonsis (c)

def   cekInt ( n ):
    x =   0
    y =   0
    untuk saya dalam n:
        untuk j in i:
            y +  =  1
            if ( str (j) .isdigit () == Salah):
                print ( " tidak semua isi matriks adalah angka " )
                istirahat
            lain:
                x +  =  1
    jika (x == y):
        print ( " semua isi matriks adalah angka " )
        
cekInt (a)
cekInt (b)
cekInt (c)

def   ordo ( n ):
    x, y =   0 , 0
    untuk saya dalam kisaran ( len (n)):
        x +  =  1
        y =   len (n [i])
    print ( " memiliki ordo "  +  str (x) +  " x "  +  str (y))

ordo (a)
ordo (b)
ordo (d)
ordo (e)

def   jumlah ( n , m ):
    x, y =   0 , 0
    untuk saya dalam kisaran ( len (n)):
        x +  =  1
        y =   len (n [i])
    xy = [[ 0   untuk j dalam rentang (x)] untuk i dalam kisaran (y)]
    
    z =   0
    if ( len (n) ==  len (m)):
        untuk saya dalam kisaran ( len (n)):
            if ( len (n [i]) ==   len (m [i])):
                z +  =  1
    if (z ==  len (n) dan z ==  len (m)):
        print ( " ukuran sama " )
        untuk saya dalam kisaran ( len (n)):
            untuk j dalam kisaran ( len (n [i])))):
                xy [i] [j] = n [i] [j] + m [i] [j]
        cetak (xy)
    lain:
        print ( " ukuran beda " )

jumlah (a, b)
jumlah (a, d)
   
     
def   kali ( n , m ):
    aa =   0
    x, y =   0 , 0
    untuk saya dalam kisaran ( len (n)):
        x +  =  1
        y =   len (n [i])
    v, w =   0 , 0
    untuk saya dalam kisaran ( len (m)):
        v +  =  1
        w =   len (m [i])
        
    jika (y == v):
        print ( " bisa dikalikan " )
        vwxy = [[ 0   untuk j dalam rentang (w)] untuk i dalam kisaran (x)]
        untuk saya dalam kisaran ( len (n)):
            untuk j dalam kisaran ( len (m [ 0 ])):
                untuk k dalam kisaran ( len (m)):
                    # print (n [i] [k], m [k] [j])
                    vwxy [i] [j] +  = n [i] [k] * m [k] [j]
        cetak (vwxy)
            
    lain:
        print ( " tidak memenuhi persyaratan " )

zz = [[ 1 , 2 , 3 ], [ 1 , 2 , 3 ]]
zx = [[ 1 ], [ 2 ], [ 3 ]]
kali (zz, zx)
kali (a, b)
kali (a, e)
kali (a, zx)


def   determHitung ( A , total  =  0 ):
    x =   len (A [ 0 ])
    z =   0
    untuk saya dalam kisaran ( len (A)):
        if ( len (A [i]) == x):
           z +  =  1
    if (z ==   len (A)):
        if (x ==  len (A)):
            indeks =   daftar (rentang ( len (A)))
            jika   len (A) ==   2   dan   len (A [ 0 ]) ==   2 :
                val = A [ 0 ] [ 0 ] * A [ 1 ] [ 1 ] - A [ 1 ] [ 0 ] * A [ 0 ] [ 1 ]
                mengembalikan val
            untuk fc dalam indeks:
                As = A
                As = As [ 1 :]
                tinggi =   len (As)
                untuk saya dalam kisaran (tinggi):
                    As [i] = As [i] [ 0 : fc] + As [i] [fc +  1 :]
                tanda = ( -  1 ) ** (fc %   2 )
                sub_det = determHitung (As)
                total +  = tanda * A [ 0 ] [fc] * sub_det
        lain:
            return   " tidak bisa dihitung determinan, bukan matrix bujursangkar "
    lain:
        return   " tidak bisa dihitung determinan, bukan matrix bujursangkar "
    Tolak total


z = [[ 3 , 1 ], [ 2 , 5 ]]
x = [[ 1 , 2 , 1 ], [ 3 , 3 , 1 ], [ 2 , 1 , 2 ]]
v = [[ 1 , -  2 , 0 , 0 ], [ 3 , 2 , -  3 , 1 ], [ 4 , 0 , 5 , 1 ], [ 2 , 3 , -  1 , 4 ]]
r = [[ 10 , 23 , 45 , 12 , 13 ], [ 1 , 2 , 3 , 4 , 5 ], [ 1 , 2 , 3 , 4 , 6 ], [ 4 , 2 , 3 , 4 , 8 ] , [ 1 , 4 , 5 , 6 , 10 ]]
print (determHitung (z))
print (determHitung (x))
print (determHitung (v))
print (determHitung (r))
print (determHitung (d))
print (determHitung (e))

##No.2
def   buatNol ( n , m  = Tidak Ada):
    jika (m == Tidak Ada):
        m = n
    print ( " membuat matriks 0 dengan ordo "  +  str (n) +  " x "  +  str (m))
    cetak ([[ 0   untuk j dalam kisaran (m)] untuk i dalam kisaran (n)])

buatNol ( 2 , 4 )
buatNol ( 3 )

def   buatIden ( n ):
    print ( " membuat matriks identitas dengan ordo "  +  str (n) +  " x "  +  str (n))
    cetak ([[ 1   jika j == saya yang lain   0   untuk j dalam rentang (n)] untuk saya dalam kisaran (n)])

buatIden ( 4 )
buatIden ( 2 )

##No.3
kelas Node:
    def   __init__ ( mandiri , data ):
        self .data = data
        self .next =   Tidak ada
kelas LinkedList:
    def   __init__ ( mandiri ):
        self .head =   Tidak ada
    def   pushAw ( self , new_data ):
        new_node = Node (new_data)
        new_node.next =   self .head
        self .head = new_node
    def   pushAk ( mandiri , data ):
        if ( self .head ==   Tidak Ada):
            self .head = Node (data)
        lain:
            saat ini =   self .head
            while (current.next! = Tidak Ada):
                current = current.next
            current.next = Node (data)
        kembali diri. kepala
     sisipan def (diri, data, pos):
        simpul = Node (data)
        jika tidak diri .head:
            self .head = node
        elif pos ==  0 :
            node.next =   self .head
            self .head = node
        lain:
            prev =   Tidak Ada
            saat ini =   self .head
            current_pos =   0
            while (current_pos < pos) dan current.next:
                prev = saat ini
                current = current.next
                current_pos +  =  1
            prev.next = Simpul
            node.next = saat ini
        kembali diri. kepala
    def   deleteNode ( mandiri , posisi ):
        if   self .head ==   Tidak Ada:
            kembali 
        temp =   self .head
        jika posisi ==   0 :
            self .head = temp.next
            temp =   Tidak ada
            kembali 
        untuk saya dalam jangkauan (posisi -  1 ):
            temp = temp.next
            jika temp tidak ada:
                istirahat
        jika temp tidak ada:
            kembali 
        jika temp.next adalah   Tidak Ada :
            kembali 
        next   = temp.next.next
        temp.next =   Tidak Ada
        temp.next =   berikutnya
     pencarian def (mandiri, x):
        saat ini =   self .head
        saat ini! =   Tidak Ada:
            jika current.data == x:
                kembali   " Benar "
            current = current.next
        kembali   " Salah "
     tampilan def (mandiri):
        saat ini =   self .head
        sementara saat ini tidak ada:
            print (current.data, end   =   '   ' )
            current = current.next   
    
llist = LinkedList ()
llist.pushAw ( 21 )
llist.pushAw ( 22 )
llist.pushAw ( 12 )
llist.pushAw ( 14 )
llist.pushAw ( 2 )
llist.pushAw ( 19 )
llist.pushAk ( 9 )
llist.deleteNode ( 0 )
llist.insert ( 1 , 6 )
print (llist.search ( 21 ))
print (llist.search ( 29 ))
llist.display ()

##No.4
kelas Node:
    def   __init__ ( mandiri , data ):
        self .data = data
        self .prev =   Tidak ada
kelas DoublyLinkedList:
    def   __init__ ( mandiri ):
        self .head =   Tidak ada
    def   awal ( self , new_data ):
        print ( " tambah pada awal " , new_data)
        new_node = Node (new_data)
        new_node.next =   self .head
        jika diri .head adalah tidak ada:
            self .head.prev = new_node
        self .head = new_node
    def   akhir ( self , new_data ):
        print ( " tambah pada akhir " , new_data)
        new_node = Node (new_data)
        new_node.next =   Tidak Ada
        jika   self .head tidak ada:
            new_node.prev =   Tidak Ada
            self .head = new_node
            kembali 
        last =   self .head
        sementara (last.next tidak ada):
            last = last.next
        last.next = new_node
        new_node.prev = terakhir
        kembali
    def   printList ( self , node ):
        print ( " \ n Dari Depan: " )
        sementara (simpul adalah tidak ada):
            print ( "   % d  "   % (node.data))
            last = node
            node = node.next
        print ( " \ n Dari Belakang: " )
        sementara (terakhir adalah tidak ada):
            cetak ( "   % d  "   % (last.data))
            last = last.prev
llist = DoublyLinkedList ()
llist.awal ( 7 )  
llist.awal ( 1 )
llist.akhir ( 6 )
llist.akhir ( 4 )
llist.printList (llist.head)
