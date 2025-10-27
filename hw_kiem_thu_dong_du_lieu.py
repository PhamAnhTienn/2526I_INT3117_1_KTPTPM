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
    test_cases = [
        (10, 30, "Loại bỏ"), 
        (25, 50, "Đạt chất lượng"), 
        (40, 50, "Cần kiểm tra lại"),
        (-1, -1, "Đầu vào không hợp lệ")
    ]

    passed = 0
    print("--- Bắt đầu kiểm thử ---")

    for i, (nhiet_do, do_am, expected) in enumerate(test_cases):
        actual = test(nhiet_do, do_am)
        if actual == expected:
            status = "Passed"
            passed += 1
        else:
            status = "Failed"

        print(f"Ca #{i+1}: Đầu vào ({nhiet_do}, {do_am})")
        print(f"   -> Kết quả mong đợi: '{expected}'")
        print(f"   -> Kết quả thực tế:  '{actual}'")
        print(f"   -> Trạng thái: {status}\n")

    print("--- Kết thúc kiểm thử ---")
    print(f"Tổng kết: {passed}/{len(test_cases)} ca kiểm thử đã đạt.")


if __name__ == "__main__":
    main()
