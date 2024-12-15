import pandas as pd
import random
import numpy as np

majors = ["EE-E18", "QHT94", "IT-E7", "EM3", "BF2", "CH2","BF1","BF2","BF-E12","BF-E19","CH1","CH2","CH3","CH-E11","ED2","EE1","EE2","EE-E18","EE-E8","EE-EP","EM1","EM3","EM4","EM5","EM-E13","EM-E14","EM-VUW","ET1","ET2","TROY-BA","TROY-IT","TX1"]
schools = ["ĐẠI HỌC BÁCH KHOA HÀ NỘI", "TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN - ĐH QG HÀ NỘI","HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG","TRƯỜNG ĐẠI HỌC CÔNG NGHIỆP HÀ NỘI","TRƯỜNG ĐẠI HỌC CMC","TRƯỜNG ĐẠI HỌC KINH TẾ KỸ THUẬT CÔNG NGHIỆP","TRƯỜNG ĐẠI HỌC CÔNG NGHIỆP HÀ NỘI"]
# 1. Tạo danh sách ID sinh viên (id_sv) duy nhất
num_students = 20000
id_sv_list = [f"{random.randint(10000000000, 99999999999)}" for _ in range(num_students)]

# 2. Tạo bảng `sinh_vien`
sinh_vien = pd.DataFrame({
    'id_sv': id_sv_list,
    'ten_sv': [f"Họ Tên {i}" for i in range(num_students)],
    'ngay_sinh': pd.to_datetime(np.random.choice(pd.date_range('2002-01-01', '2006-12-31'), num_students)),
    'gioi_tinh': np.random.choice(['Nam', 'Nữ'], num_students),
    'uu_tien': np.random.choice(['Không', 'Đối tượng 1', 'Đối tượng 2'], num_students),
    'khu_vuc': np.random.choice(['KV1', 'KV2', 'KV3'], num_students),
    'diem_khuyen_khich': np.random.uniform(0, 2, num_students).round(2),
    'ma_tinh': [id_sv[:3] for id_sv in id_sv_list],
    'loai_thi_sinh': np.random.choice(['Thí sinh không phải tự do', 'Thí sinh tự do'], num_students)
})

# 3. Tạo bảng `cc_sinh_vien`
cc_sinh_vien = pd.DataFrame({
    'id_sv': id_sv_list,
    'id_cc': [f"CC{i}" for i in range(num_students)],
    'ngoai_ngu': np.random.choice(['Tiếng Anh', 'Tiếng Nhật', 'Tiếng Pháp'], num_students),
    'code_ngoai_ngu': np.random.choice(['N1', 'N2', 'N3'], num_students),
    'loai_cc': np.random.choice(['IELTS', 'TOEFL', 'JLPT'], num_students),
    'diem_cc': np.random.uniform(4.0, 9.0, num_students).round(1),
    'diem_quy_doi_THPT': np.random.uniform(8.0, 10.0, num_students).round(1)
})

# Tạo bảng `nguyen_vong` với số lượng nguyện vọng lớn hơn số sinh viên
nguyen_vong_list = []
for id_sv in id_sv_list:
    # Mỗi sinh viên có từ 1 đến 5 nguyện vọng
    num_nv = random.randint(1, 5)
    for nv in range(1, num_nv + 1):
        nguyen_vong_list.append({
            'id_sv': id_sv,
            'id_nv': f"{id_sv}_NV{nv}",  # Định danh nguyện vọng dựa trên id_sv
            'tt_nv': nv,  # Thứ tự nguyện vọng
            'ma_truong': np.random.choice(['BKA', 'QHT','BVH','DCN','CMC','DKK','DCN','QHI']),
            'ten_truong': np.random.choice(schools),
            'ma_nganh': np.random.choice(majors),
            'ten_nganh': np.random.choice(['Kỹ thuật Điện', 'Công nghệ Thông tin', 'Kỹ thuật Hóa học', 'Kỹ thuật Sinh học']),
            'phuong_thuc_1': np.random.choice([1, 0]),
            'phuong_thuc_2': np.random.choice([1, 0]),
            'phuong_thuc_3': np.random.choice([1, 0]),
            'phuong_thuc_4': np.random.choice([1, 0])
        })

nguyen_vong = pd.DataFrame(nguyen_vong_list)

# 5. Xuất dữ liệu ra file CSV
sinh_vien.to_csv('sinh_vien.csv', index=False, encoding='utf-8-sig')
cc_sinh_vien.to_csv('cc_sinh_vien.csv', index=False, encoding='utf-8-sig')
nguyen_vong.to_csv('nguyen_vong.csv', index=False, encoding='utf-8-sig')

# 6. Tạo bảng `ket_qua_xet_tuyen`
ket_qua_xet_tuyen = pd.DataFrame({
    'id_sv': id_sv_list,
    'tong_diem_xet_tuyen': np.random.uniform(20.0, 30.0, num_students).round(2),
    'nganh_tt': np.random.choice(['CH2', 'EM3', 'ET1', 'IT-E7', 'BF2'], num_students)
})

# Xuất dữ liệu ra file CSV
ket_qua_xet_tuyen.to_csv('ket_qua_xet_tuyen.csv', index=False, encoding='utf-8-sig')
print("Dữ liệu đã được sinh ngẫu nhiên và đảm bảo tính match giữa các bảng!")
