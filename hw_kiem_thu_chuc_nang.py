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

def main():
    print("Kiem thu bien single boundary")
    assert test(25.0, 0.0) == "Cần kiểm tra lại"
    assert test(25.0, 0.1) == "Cần kiểm tra lại"
    assert test(25.0, 50.0) == "Đạt chất lượng"
    assert test(25.0, 99.9) == "Cần kiểm tra lại"
    assert test(25.0, 100.0) == "Cần kiểm tra lại"
    assert test(0.0, 50.0) == "Cần kiểm tra lại"
    assert test(0.1, 50.0) == "Cần kiểm tra lại"
    assert test(49.9, 50.0) == "Cần kiểm tra lại"
    assert test(50.0, 50.0) == "Cần kiểm tra lại"

    print("Kiem thu bang quyet dinh")
    assert test(-1, -1) == "Đầu vào không hợp lệ"
    assert test(-1, 30) == "Đầu vào không hợp lệ"
    assert test(-1, 50) == "Đầu vào không hợp lệ"
    assert test(-1, 70) == "Đầu vào không hợp lệ"
    assert test(-1, 110) == "Đầu vào không hợp lệ"
    assert test(10, -1) == "Đầu vào không hợp lệ"
    assert test(10, 30) == "Loại bỏ"
    assert test(10, 50) == "Cần kiểm tra lại"
    assert test(10, 70) == "Loại bỏ"
    assert test(10, 110) == "Đầu vào không hợp lệ"
    assert test(25, -1) == "Đầu vào không hợp lệ"
    assert test(25, 30) == "Cần kiểm tra lại"
    assert test(25, 50) == "Đạt chất lượng"
    assert test(25, 70) == "Cần kiểm tra lại"
    assert test(25, 110) == "Đầu vào không hợp lệ"
    assert test(40, -1) == "Đầu vào không hợp lệ"
    assert test(40, 30) == "Loại bỏ"
    assert test(40, 50) == "Cần kiểm tra lại"
    assert test(40, 70) == "Loại bỏ"
    assert test(40, 110) == "Đầu vào không hợp lệ"
    assert test(60, -1) == "Đầu vào không hợp lệ"
    assert test(60, 30) == "Đầu vào không hợp lệ"
    assert test(60, 50) == "Đầu vào không hợp lệ"
    assert test(60, 70) == "Đầu vào không hợp lệ"
    assert test(60, 110) == "Đầu vào không hợp lệ"


if __name__ == "__main__":
    main()

