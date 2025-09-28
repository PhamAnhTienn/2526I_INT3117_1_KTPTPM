def test(nhiet_do: float, do_am: float):
    if not (0.0 <= nhiet_do <= 50.0) or not (0.0 <= do_am <= 100.0):
        return "Đầu vào không hợp lệ"

    nhiet_do_dat_chuan = 15.0 <= nhiet_do <= 25.0
    do_am_dat_chuan = 40.0 <= do_am <= 60.0

    if nhiet_do_dat_chuan and do_am_dat_chuan:
        return "Đạt chất lượng"
    elif nhiet_do_dat_chuan or do_am_dat_chuan:
        return "Cần kiểm tra lại"
    else:
        return "Loại bỏ"
    
if __name__ == "__main__":
    print("Kiem thu bien single boundary")
    print(test(25.0, 0.0)) 
    print(test(25.0, 0.1)) 
    print(test(25.0, 50.0)) 
    print(test(25.0, 99.9))  
    print(test(25.0, 100.0))
    print(test(0.0, 50.0))  
    print(test(0.1, 50.0))
    print(test(49.9, 50.0)) 
    print(test(50.0, 50.0))  
    
    print("Kiem thu bang quyet dinh")
    print(test(30.0, 70.0))  
    print(test(0.0, 0.0))   
    print(test(50.0, 100.0))