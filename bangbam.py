from importlib.util import set_loader


class BangBam:
    def __init__(self, kich_thuoc = 10):
        self.danh_sach = [None for _ in range(kich_thuoc)]
    #def
    
    def __str__(self):
        kq = '['
        stt1 = 0
        for x in self.danh_sach:
            stt1 += 1
            if stt1 != 1:
                kq = kq + ', '
            #if
            if x is None:
                kq = kq + '[None]'
            else:
                kq = kq + '['
                stt2 = 0
                for e in x:
                    stt2 += 1
                    if stt2 != 1:
                        kq = kq + ', '
                    #if
                    kq = kq + str(e[0])+ ': ' + str(e[1])
                #for
                kq = kq + ']'
            #if
        kq = kq + ']'
        return kq
    #def
    
    def bam(self, khoa):
        kich_thuoc = len(self.danh_sach)
        return hash(khoa) % kich_thuoc
    #def
    
    def them(self, khoa, gia_tri):
        chi_muc = self.bam(khoa)
        if self.danh_sach[chi_muc] is None:
            #them moi
            self.danh_sach[chi_muc] = list()
            self.danh_sach[chi_muc].append([khoa, gia_tri])
        else:
            #cap nhat
            cap_nhat = False
            for x in self.danh_sach[chi_muc]:
                if x[0] == khoa:
                    x[1] = gia_tri
                    cap_nhat = True
                    break       
                #if
            #for
            if cap_nhat == False:
                self.danh_sach[chi_muc].append([khoa, gia_tri])
            #if  
        #if
    #def
    
    def lay(self, khoa):
        chi_muc = self.bam(khoa)
        if self.danh_sach[chi_muc] is None:
            return None
        else:
            for x in self.danh_sach[chi_muc]:
                if x[0] == khoa:
                    return x[1]
                #if
            #for
        #if        
    #def
    
    def __setitem__(self, khoa,gia_tri):
        self.them(khoa, gia_tri)
    #def
    
    def __getitem__(self, khoa):
        return self.lay(khoa)
    #def
    
#class
def main():
    bang_bam = BangBam(5)
    import random
    for _ in range(18):
        khoa = random.randint(0,10)
        gia_tri = random.randint(0, 100)
        print(f'* Them khoa = {khoa}, gia tri = {gia_tri}')
        #bang_bam.them(khoa, gia_tri)
        bang_bam[khoa] = gia_tri
        print(bang_bam)
        print()
    #for
    
    khoa = int(input('Nhap vao mot khoa: '))
    #gia_tri = bang_bam.lay(khoa)
    gia_tri = bang_bam[khoa]
    print(f'*Khoa {khoa} co gia tri la {gia_tri}')
#def

if __name__ == '__main__':
    main()
#if