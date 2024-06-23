#CÂU 2A Thay đổi số tiền VÀ 4C Phát hiện thay đổi số tiền
    def themBlock_BinhThuong(self,gd):
        self.layChuoiKhoi() # Gọi phương thức layChuoiKhoi để cập nhật hoặc xử lý chuỗi khối.
        khoi_HT = KhoiGD() # Tạo một đối tượng mới của lớp KhoiGD.
        ck = self.ds_khoi # Lấy danh sách khối từ thuộc tính ds_khoi của đối tượng hiện tại.
        k0 = ck.chuoi_khoi[ck.tong_so_khoi-1].bam_HT # Lấy hash của khối cuối cùng trong chuỗi khối.
        khoi_HT.taoKhoi(gd,k0) # Sử dụng phương thức taoKhoi để tạo một khối mới với dữ liệu 'gd' và hash 'k0'.
        # self.ds_khoi.themKhoi(khoi_HT) # Dòng này đã bị comment, nếu không nó sẽ thêm khối mới vào danh sách khối.
        return khoi_HT # Trả về đối tượng khối mới đã được tạo.

--> Phương thức này có thể được sử dụng trong việc thêm một khối giao dịch (transaction block) vào một chuỗi khối (blockchain) trong một hệ thống tiền điện tử hoặc một ứng dụng tương tự. gd có thể là thông tin giao dịch, và khoi_HT là khối mới được tạo ra từ thông tin này. Dòng code bị comment (đánh dấu bằng #) không được thực thi, có thể vì lý do nào đó người lập trình không muốn thêm khối vào chuỗi tại thời điểm này. Nếu bạn muốn thêm khối vào chuỗi, bạn cần bỏ comment dòng đó.


Đoạn code Python này định nghĩa một phương thức themBlock_TanCong2A trong một lớp, có vẻ như là để thêm một khối vào một chuỗi khối (blockchain) với một số thao tác đặc biệt. Dưới đây là giải thích từng bước:
    def themBlock_TanCong2A(self, gd):
        self.layChuoiKhoi()  # Cập nhật hoặc xử lý chuỗi khối.
        khoi_HT = KhoiGD()  # Tạo một đối tượng mới của lớp KhoiGD.
        ck = self.ds_khoi  # Lấy danh sách khối từ thuộc tính ds_khoi của đối tượng hiện tại.
        gd.so_tien = gd.so_tien*5  # Nhân số tiền trong giao dịch 'gd' lên 5 lần.
        k0 = ck.chuoi_khoi[ck.tong_so_khoi-1].bam_HT  # Lấy hash của khối cuối cùng trong chuỗi khối.
        khoi_HT.taoKhoi(gd, k0)  # Tạo một khối mới với dữ liệu 'gd' đã được sửa đổi và hash 'k0'.
        # self.ds_khoi.themKhoi(khoi_HT)  # Dòng này đã bị comment, nếu không nó sẽ thêm khối mới vào danh sách khối.
        return khoi_HT  # Trả về đối tượng khối mới đã được tạo.

Phần quan trọng của phương thức này là dòng gd.so_tien = gd.so_tien*5, nơi mà số tiền trong giao dịch được nhân lên 5 lần. Điều này có thể tạo ra một hành động không chính đáng trong chuỗi khối, có thể là một cuộc tấn công hoặc gian lận, vì vậy phương thức được đặt tên là TanCong2A (có thể được hiểu là "Tấn công 2A"). Dòng code bị comment (đánh dấu bằng #) không được thực thi, có thể vì lý do nào đó người lập trình không muốn thêm khối vào chuỗi tại thời điểm này hoặc để tránh hành vi không mong muốn. Nếu bạn muốn thêm khối vào chuỗi, bạn cần bỏ comment dòng đó và đảm bảo rằng hành động này là hợp lệ và an toàn.


Phương thức themBlock_TanCong2A có vẻ như là để thêm một khối giao dịch bất thường vào chuỗi khối, với việc tăng số tiền giao dịch lên 5 lần. Điều này có thể là một hành động gian lận hoặc tấn công trong hệ thống blockchain.
    def themBlock_TanCong2A(self, gd):
        self.layChuoiKhoi()  # Cập nhật hoặc xử lý chuỗi khối.
        khoi_HT = KhoiGD()  # Tạo một đối tượng mới của lớp KhoiGD.
        ck = self.ds_khoi  # Lấy danh sách khối từ thuộc tính ds_khoi của đối tượng hiện tại.
        gd.so_tien = gd.so_tien*5  # Nhân số tiền trong giao dịch 'gd' lên 5 lần.
        k0 = ck.chuoi_khoi[ck.tong_so_khoi-1].bam_HT  # Lấy hash của khối cuối cùng trong chuỗi khối.
        khoi_HT.taoKhoi(gd, k0)  # Tạo một khối mới với dữ liệu 'gd' đã được sửa đổi và hash 'k0'.
        # self.ds_khoi.themKhoi(khoi_HT)  # Dòng này đã bị comment, nếu không nó sẽ thêm khối mới vào danh sách khối.
        return khoi_HT  # Trả về đối tượng khối mới đã được tạo.


Phương thức luuGiaoDichBanDau dùng để lưu trữ thông tin của một giao dịch ban đầu vào một đối tượng mới, có thể để kiểm tra hoặc tham chiếu sau này.
    def luuGiaoDichBanDau(self, gd):
        gd1 = KhoiGD()  # Tạo một đối tượng mới của lớp KhoiGD.
        # Sao chép thông tin giao dịch ban đầu vào đối tượng mới.
        gd1.so_tien = gd.so_tien
        gd1.thoi_gian_phat_sinh = gd.thoi_gian_phat_sinh
        gd1.tai_khoan_nguon = gd.tai_khoan_nguon
        gd1.tai_khoan_dich = gd.tai_khoan_dich
        return gd1  # Trả về đối tượng giao dịch mới.


Phương thức kiemTraTanCong4C kiểm tra xem có sự khác biệt về số tiền giữa giao dịch ban đầu và giao dịch trong khối hiện tại hay không, điều này có thể chỉ ra một hành động tấn công hoặc gian lận.
    def kiemTraTanCong4C(self, gd1, khoi_ht):
        if gd1.so_tien == khoi_ht.tt_GD.so_tien:
            return 0  # Không có tấn công nếu số tiền giữa hai giao dịch bằng nhau.
        else:
            return 1  # Có tấn công nếu số tiền giữa hai giao dịch không bằng nhau.
        # so_tien = 0  # Dòng này đã bị comment và không được sử dụng.


Phương thức themBlock này có chức năng thêm một khối vào chuỗi khối, nhưng nó cũng mô phỏng việc tấn công và phát hiện thâm nhập. Nếu số ngẫu nhiên từ 8 trở lên, một tấn công sẽ được mô phỏng thông qua phương thức themBlock_TanCong2A. Sau đó, hệ thống sẽ kiểm tra xem có tấn công hay không thông qua phương thức kiemTraTanCong4C. Nếu không có tấn công, khối sẽ được thêm vào chuỗi khối an toàn. Nếu có tấn công, hệ thống sẽ ghi nhận và vẫn thêm khối vào chuỗi khối, có thể để mục đích ghi nhận và phân tích sau này. Dòng code bị comment (đánh dấu bằng #) không được thực thi và có thể được bỏ qua hoặc xem xét lại tùy theo ngữ cảnh sử dụng.
    def themBlock(self,gd):
        # self.layChuoiKhoi()
        # khoi_HT = KhoiGD()
        # ck = self.ds_khoi
        # k0 = ck.chuoi_khoi[ck.tong_so_khoi-1].bam_HT
        # khoi_HT.taoKhoi(gd,k0)
        khoi_HT = KhoiGD()  # Tạo một đối tượng mới của lớp KhoiGD.
        gd1 = self.luuGiaoDichBanDau(gd)  # Lưu thông tin giao dịch ban đầu.
        
        # MO PHONG TAN CONG
        so_ngau_nhien = randint(1, 10) # Tạo một số ngẫu nhiên từ 1 đến 10.
        print("So ngau nhien: ", so_ngau_nhien) # In số ngẫu nhiên ra màn hình.
        if so_ngau_nhien >= 8:
            khoi_HT = self.themBlock_TanCong2A(gd) # Nếu số ngẫu nhiên từ 8 trở lên,
        else:
            khoi_HT = self.themBlock_BinhThuong(gd) # Nếu không, thêm khối bình thường.
        # MO PHONG TAN CONG
        #
        # PHAT HIEN THAM NHAP (Tường lửa)
        kt = self.kiemTraTanCong4C(gd1, khoi_HT)  # Kiểm tra xem có tấn công hay không.
        if kt == 0:
            print("An toan")  # Nếu an toàn, in thông báo và reset số lần bị tấn công.
            print("Tổng số lần bị tấn công là:", self.so_lan_BTC)
            self.so_lan_BTC = 0
            self.ds_khoi.themKhoi(khoi_HT)  # Thêm khối vào chuỗi khối.
        else:
            print("Bi tan cong")  # Nếu bị tấn công, in thông báo và tăng số lần bị tấn công.
            self.so_lan_BTC = self.so_lan_BTC + 1
            # self.themBlock(gd1)  # Dòng này đã bị comment và không được sử dụng.
        # PHAT HIEN THAM NHAP (Tường lửa)
            self.ds_khoi.themKhoi(khoi_HT)  # Thêm khối vào chuỗi khối

    #CÂU 2A Thay đổi số tiền VÀ 4C Phát hiện thay đổi số tiền
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################

    #CÂU 2B Thay đổi tài khoản nguồn VÀ 4A Phát hiện thay đổi TK_nguồn
    def themBlock_BinhThuong(self, gd):
        self.layChuoiKhoi()  # Cập nhật chuỗi khối hiện tại.
        khoi_HT = KhoiGD()  # Tạo một đối tượng khối giao dịch mới.
        ck = self.ds_khoi  # Lấy danh sách khối hiện tại.
        k0 = ck.chuoi_khoi[ck.tong_so_khoi-1].bam_HT  # Lấy hash của khối cuối cùng trong chuỗi.
        khoi_HT.taoKhoi(gd, k0)  # Tạo khối mới với thông tin giao dịch 'gd' và hash 'k0'.
        # self.ds_khoi.themKhoi(khoi_HT)  # Dòng này đã bị comment, không thêm khối vào chuỗi.
        return khoi_HT  # Trả về khối mới tạo.

    def themBlock_TanCong2B(self, gd):
        self.layChuoiKhoi()  # Cập nhật chuỗi khối hiện tại.
        khoi_HT = KhoiGD()  # Tạo một đối tượng khối giao dịch mới.
        ck = self.ds_khoi  # Lấy danh sách khối hiện tại.
        gd.tai_khoan_nguon = "Mr.Súi_Hacker"  # Thay đổi tài khoản nguồn thành hacker.
        k0 = ck.chuoi_khoi[ck.tong_so_khoi-1].bam_HT  # Lấy hash của khối cuối cùng trong chuỗi.
        khoi_HT.taoKhoi(gd, k0)  # Tạo khối mới với thông tin giao dịch đã bị thay đổi và hash 'k0'.
        # self.ds_khoi.themKhoi(khoi_HT)  # Dòng này đã bị comment, không thêm khối vào chuỗi.
        return khoi_HT  # Trả về khối mới tạo.

    def luuGiaoDichBanDau(self, gd):
        gd1 = KhoiGD()  # Tạo một đối tượng khối giao dịch mới.
        
        # 4 dòng code bên dưới dùng để sao chép thông tin giao dịch ban đầu vào đối tượng mới.
        gd1.so_tien = gd.so_tien
        gd1.thoi_gian_phat_sinh = gd.thoi_gian_phat_sinh
        gd1.tai_khoan_nguon = gd.tai_khoan_nguon
        gd1.tai_khoan_dich = gd.tai_khoan_dich
        
        return gd1  # Trả về đối tượng giao dịch mới.

    def kiemTraTanCong4A(self, gd1, khoi_ht):
        if gd1.tai_khoan_nguon == khoi_ht.tt_GD.tai_khoan_nguon:
            return 0  # Nếu tài khoản nguồn không thay đổi, không có tấn công.
        else:
            return 1  # Nếu tài khoản nguồn thay đổi, có tấn công.
        # so_tien = 0  # Dòng này đã bị comment và không được sử dụng.

        def themBlock(self, gd):
            khoi_HT = KhoiGD()  # Tạo một đối tượng khối giao dịch mới.
            gd1 = self.luuGiaoDichBanDau(gd)  # Lưu thông tin giao dịch ban đầu.
            # Mô phỏng tấn công:
            so_ngau_nhien = randint(1, 10)  # Tạo một số ngẫu nhiên từ 1 đến 10.
            print("So ngau nhien: ", so_ngau_nhien)  # In số ngẫu nhiên ra màn hình.
        if so_ngau_nhien >= 8:
            khoi_HT = self.themBlock_TanCong2B(gd)  # Nếu số ngẫu nhiên từ 8 trở lên, thực hiện tấn công.
        else:
            khoi_HT = self.themBlock_BinhThuong(gd)  # Nếu không, thêm khối bình thường.
        
        # Phát hiện thâm nhập (Tường lửa):
        kt = self.kiemTraTanCong4A(gd1, khoi_HT)  # Kiểm tra xem có tấn công hay không.
        if kt == 0:
            print("An toan")  # Nếu an toàn, thông báo và thêm khối vào chuỗi.
            self.ds_khoi.themKhoi(khoi_HT)            
        else:
            print("Bi tan cong")  # Nếu bị tấn công, thông báo nhưng vẫn thêm khối vào chuỗi.
            # self.themBlock(gd1)  # Dòng này đã bị comment và không được sử dụng.
            self.ds_khoi.themKhoi(khoi_HT) 

        Đoạn code này mô phỏng việc thêm khối vào một chuỗi khối và kiểm tra các tấn công có thể xảy ra. Các phương thức themBlock_BinhThuong và themBlock_TanCong2B được sử dụng để thêm khối bình thường và khối bị tấn công tương ứng. Phương thức luuGiaoDichBanDau được sử dụng để lưu thông tin giao dịch ban đầu, và kiemTraTanCong4A để kiểm tra sự thay đổi của tài khoản nguồn, nhằm phát hiện tấn công. Cuối cùng, phương thức themBlock quyết định liệu có thêm khối bình thường hay khối bị tấn công dựa trên một số ngẫu nhiên và sau đó kiểm tra xem có tấn công hay không. Nếu không có tấn công, khối sẽ được thêm vào chuỗi khối; nếu có tấn công, hệ thống sẽ thông báo nhưng vẫn thêm khối vào chuỗi khối. Dòng code bị comment (đánh dấu bằng #) không được thực thi và có thể được bỏ qua hoặc xem xét lại tùy theo ngữ cảnh sử dụng.
    #CÂU 2B Thay đổi tài khoản nguồn VÀ 4A Phát hiện thay đổi TK_nguồn

#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################



#CÂU 4D Cd.	Làm 1 gói tường lửa sao cho - 80% phát hiện được thay đổi TK_nguồn - 90% phát hiện được thay đổi TK_đích - 100% phát hiện được thay đổi số tiền
    
Phương thức themBlock_BinhThuong này dùng để thêm một khối giao dịch bình thường vào chuỗi khối. Nó cập nhật chuỗi khối hiện tại, tạo một khối mới và chuẩn bị thông tin cần thiết để thêm khối đó vào chuỗi.
    def themBlock_BinhThuong(self, gd):
        self.layChuoiKhoi()  # Gọi phương thức layChuoiKhoi để cập nhật chuỗi khối hiện tại.
        khoi_HT = KhoiGD()  # Tạo một đối tượng mới của lớp KhoiGD, có thể đại diện cho một khối giao dịch.
        ck = self.ds_khoi  # Lấy danh sách khối từ thuộc tính ds_khoi của đối tượng hiện tại.
        k0 = ck.chuoi_khoi[ck.tong_so_khoi-1].bam_HT  # Lấy hash của khối cuối cùng trong chuỗi khối.
        khoi_HT.taoKhoi(gd, k0)  # Sử dụng phương thức taoKhoi để tạo một khối mới với thông tin giao dịch 'gd' và hash 'k0'.
        # self.ds_khoi.themKhoi(khoi_HT)  # Dòng này đã bị comment, nếu không nó sẽ thêm khối mới vào danh sách khối.
        return khoi_HT  # Trả về đối tượng khối mới đã được tạo.


Phương thức themBlock_TanCong2A mô phỏng việc thêm một khối bị tấn công vào chuỗi khối, nơi số tiền trong giao dịch được tăng lên đáng kể.
    def themBlock_TanCong2A(self, gd):
        self.layChuoiKhoi()  # Tương tự như trên, cập nhật chuỗi khối hiện tại.
        khoi_HT = KhoiGD()  # Tạo một đối tượng khối giao dịch mới.
        ck = self.ds_khoi  # Lấy danh sách khối hiện tại.
        gd.so_tien = gd.so_tien*5  # Nhân số tiền trong giao dịch 'gd' lên 5 lần, mô phỏng một tấn công.
        k0 = ck.chuoi_khoi[ck.tong_so_khoi-1].bam_HT  # Lấy hash của khối cuối cùng trong chuỗi khối.
        khoi_HT.taoKhoi(gd, k0)  # Tạo một khối mới với thông tin giao dịch đã bị thay đổi và hash 'k0'.
        # self.ds_khoi.themKhoi(khoi_HT)  # Dòng này đã bị comment, không thêm khối vào chuỗi.
        return khoi_HT  # Trả về khối mới tạo.




Phương thức luuGiaoDichBanDau dùng để lưu trữ thông tin của một giao dịch ban đầu vào một đối tượng mới, có thể để kiểm tra hoặc tham chiếu sau này.
    def luuGiaoDichBanDau(self, gd):
        gd1 = KhoiGD()  # Tạo một đối tượng khối giao dịch mới.
        # 4 dòng code bên dưới là để sao chép thông tin giao dịch ban đầu vào đối tượng mới.
        gd1.so_tien = gd.so_tien
        gd1.thoi_gian_phat_sinh = gd.thoi_gian_phat_sinh
        gd1.tai_khoan_nguon = gd.tai_khoan_nguon
        gd1.tai_khoan_dich = gd.tai_khoan_dich
        
        return gd1  # Trả về đối tượng giao dịch mới.

Phương thức kiemTraTanCong4C kiểm tra xem có sự khác biệt về số tiền giữa giao dịch ban đầu và giao dịch trong khối hiện tại hay không, điều này có thể chỉ ra một hành động tấn công hoặc gian lận.
    def kiemTraTanCong4C(self, gd1, khoi_ht):
        if gd1.so_tien == khoi_ht.tt_GD.so_tien:
            return 0  # Nếu số tiền giữa hai giao dịch bằng nhau, không có tấn công.
        else:
            return 1  # Nếu số tiền giữa hai giao dịch không bằng nhau, có tấn công.
            

Phương thức kiemTraTanCong4B tương tự như trên, nhưng kiểm tra tài khoản đích của giao dịch.
    def kiemTraTanCong4B(self, gd1, khoi_ht):
        if gd1.tai_khoan_dich == khoi_ht.tt_GD.tai_khoan_dich:
            return 0  # Nếu tài khoản đích không thay đổi, không có tấn công.
        else:
            return 1  # Nếu tài khoản đích thay đổi, có tấn công.



Phương thức kiemTraTanCong4A kiểm tra sự thay đổi của tài khoản nguồn, nhằm phát hiện tấn công.
    def kiemTraTanCong4A(self, gd1, khoi_ht):
        if gd1.tai_khoan_nguon == khoi_ht.tt_GD.tai_khoan_nguon:
            return 0  # Nếu tài khoản nguồn không thay đổi, không có tấn công.
        else:
            return 1  # Nếu tài khoản nguồn thay đổi, có tấn công.


Phương thức kiemTraTanCong4D quyết định kiểm tra loại tấn công nào dựa trên một số ngẫu nhiên và in ra thông báo phù hợp nếu phát hiện thay đổi trong giao dịch.

    def kiemTraTanCong4D(self, gd1, khoi_ht):
        so_ngau_nhien = randint(1, 10)  # Tạo một số ngẫu nhiên từ 1 đến 10.
        print("So ngau nhien 4D: ", so_ngau_nhien)  # In số ngẫu nhiên ra màn hình.
        kt1 = 0 # khởi tạo biến kiểm tra 1 (kt1) = 0
        kt2 = 0 # khởi tạo biến kiểm tra 2 (kt2) = 0
        kt3 = 0 # khởi tạo biến kiểm tra 3 (kt3) = 0
        # Dựa vào số ngẫu nhiên để quyết định kiểm tra loại tấn công nào.
        # In ra thông báo phù hợp nếu phát hiện thay đổi trong giao dịch.
        
        # dựa vào số ngẫu nhiên, giá trị của kt1, kt2, kt3 sẽ thay đổi
        if so_ngau_nhien >=3:
            # dựa vào số ngẫu nhiên, nếu số ngẫu nhiên >=3 thì giá trị của kt1, kt2, kt3 sẽ thay đổi sau khi chạy qua 3 dòng code bên dưới.
            kt1 = self.kiemTraTanCong4A(gd1, khoi_ht)
            kt2 = self.kiemTraTanCong4B(gd1, khoi_ht)
            kt3 = self.kiemTraTanCong4C(gd1, khoi_ht)
        elif so_ngau_nhien >=2:
            # dựa vào số ngẫu nhiên, nếu số ngẫu nhiên >=2 thì giá trị của kt2, kt3 sẽ thay đổi sau khi chạy qua 2 dòng code bên dưới.
            kt2 = self.kiemTraTanCong4B(gd1, khoi_ht)
            kt3 = self.kiemTraTanCong4C(gd1, khoi_ht)
        else:
            # dựa vào số ngẫu nhiên, nếu số ngẫu nhiên KHÔNG >=3 cũng KHÔNG >=2 thì giá trị của kt3 sẽ thay đổi sau khi chạy qua dòng code bên dưới.
            kt3 = self.kiemTraTanCong4C(gd1, khoi_ht)
        
        #sau khi có được giá trị của kt2, kt2, kt3 từ việc thực thi những logic code ở trên
        
        
        if kt1 == 1:
            # nếu kt1 = 1 thì sẽ in ra dòng chữ "Phát hiện thay đổi TK nguồn" và return để kết thúc hàm này
            print("Phát hiện thay đổi TK nguồn")
            return

        if kt2 == 1:
            # nếu kt2 = 1 thì sẽ in ra dòng chữ "Phát hiện thay đổi TK đích" và return để kết thúc hàm này
            print("Phát hiện thay đổi TK đich")
            return

        if kt3 == 1:
            # nếu kt3 = 1 thì sẽ in ra dòng chữ "Phát hiện thay đổi số tiền" và return để kết thúc hàm này
            print("Phat hien thay doi so tien")
            return
        


    def themBlock(self, gd):
        # self.layChuoiKhoi()
        # khoi_HT = KhoiGD()
        # ck = self.ds_khoi
        # k0 = ck.chuoi_khoi[ck.tong_so_khoi-1].bam_HT
        # khoi_HT.taoKhoi(gd,k0)
        
        khoi_HT = KhoiGD()# Tạo một khối giao dịch mới
        gd1 = self.luuGiaoDichBanDau(gd)# Lưu trữ giao dịch ban đầu

        # MO PHONG TAN CONG
        so_ngau_nhien = randint(1, 10) #tìm số ngẫu nhiên từ 1 tới 10
        print("So ngau nhien: ", so_ngau_nhien) # in ra số ngẫu nhiên đó
        
        if so_ngau_nhien >= 3:
            # Nếu số ngẫu nhiên từ 3 trở lên, thực hiện thêm khối theo cách tấn công 2A
            khoi_HT = self.themBlock_TanCong2A(gd)
        else:
            # Nếu số ngẫu nhiên nhỏ hơn 3, thêm khối bình thường
            khoi_HT = self.themBlock_BinhThuong(gd)
        # MO PHONG TAN CONG
        
        # PHAT HIEN THAM NHAP (Tường lửa)
        self.kiemTraTanCong4D(gd1, khoi_HT)# Kiểm tra xem có tấn công hay không bằng cách sử dụng hàm kiemTraTanCong4D
        # self.themBlock(gd1)
        # PHAT HIEN THAM NHAP (Tường lửa)
        self.ds_khoi.themKhoi(khoi_HT)# Thêm khối vào danh sách khối sau khi đã kiểm tra
    
   #CÂU 4D Cd.	Làm 1 gói tường lửa sao cho - 80% phát hiện được thay đổi TK_nguồn - 90% phát hiện được thay đổi TK_đích - 100% phát hiện được thay đổi số tiền
