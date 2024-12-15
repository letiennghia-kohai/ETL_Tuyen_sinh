import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import sessionmaker

# Đọc dữ liệu từ các file CSV
sinh_vien = pd.read_csv('sinh_vien.csv', encoding='utf-8-sig')
nguyen_vong = pd.read_csv('nguyen_vong.csv', encoding='utf-8-sig')
ket_qua_xet_tuyen = pd.read_csv('ket_qua_xet_tuyen.csv', encoding='utf-8-sig')
cc_sinh_vien = pd.read_csv('cc_sinh_vien.csv', encoding='utf-8-sig')

# Chuyển đổi ngày sinh thành định dạng ngày tháng
sinh_vien['ngay_sinh'] = pd.to_datetime(sinh_vien['ngay_sinh'], errors='coerce')  # Đảm bảo định dạng ngày tháng

# Kiểm tra và loại bỏ các dòng thiếu giá trị (nếu có)
nguyen_vong = nguyen_vong.dropna(subset=['id_sv', 'ma_nganh'])
cc_sinh_vien = cc_sinh_vien.dropna(subset=['id_sv', 'loai_cc'])

# Tạo một số cột mới nếu cần thiết (ví dụ: tách tỉnh từ CCCD)
# sinh_vien['ma_tinh'] = sinh_vien['cccd'].str[:3]  # Giả sử mã tỉnh là 3 ký tự đầu của CCCD

# Chuẩn hóa giá trị cho các cột
sinh_vien['gioi_tinh'] = sinh_vien['gioi_tinh'].apply(lambda x: 'Nam' if x in ['Nam', 'male'] else 'Nữ')
sinh_vien['khu_vuc'] = sinh_vien['khu_vuc'].apply(lambda x: 'KV1' if 'KV1' in x else ('KV2' if 'KV2' in x else 'KV3'))

# Thay thế giá trị null hoặc missing
sinh_vien['diem_khuyen_khich'] = sinh_vien['diem_khuyen_khich'].fillna(0)
sinh_vien['gioi_tinh'] = sinh_vien['gioi_tinh'].fillna('Không xác định')
sinh_vien['khu_vuc'] = sinh_vien['khu_vuc'].fillna('Không xác định')

# Loại bỏ bản ghi trùng lặp
sinh_vien = sinh_vien.drop_duplicates(subset=['id_sv'])
nguyen_vong = nguyen_vong.drop_duplicates(subset=['id_sv', 'id_nv'])

# Thay đổi thông tin kết nối phù hợp với cơ sở dữ liệu của bạn
username = 'root'  # Thay bằng username của bạn
password = 'nghiakohai3'  # Thay bằng password của bạn
host = 'localhost'
port = '3306'  # Hoặc port của PostgreSQL là '5432'
database = 'university_data'

# Kết nối tới MySQL (hoặc PostgreSQL)
# Đảm bảo đã cài đặt pymysql hoặc mysqlclient
# pip install pymysql sqlalchemy
# Tạo engine
engine = create_engine(f'mysql+mysqldb://{username}:{password}@{host}:{port}/{database}', echo=True)

# Tạo session
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Sử dụng session để ghi dữ liệu
    sinh_vien.to_sql('sinh_vien', con=session.bind, if_exists='replace', index=False)
    nguyen_vong.to_sql('nguyen_vong', con=session.bind, if_exists='replace', index=False)
    ket_qua_xet_tuyen.to_sql('ket_qua_xet_tuyen', con=session.bind, if_exists='replace', index=False)
    cc_sinh_vien.to_sql('cc_sinh_vien', con=session.bind, if_exists='replace', index=False)
    
    # Commit thay đổi
    session.commit()
    print("Đã ghi dữ liệu thành công!")

except Exception as e:
    # Rollback nếu có lỗi
    session.rollback()
    print(f"Lỗi khi ghi dữ liệu: {e}")

finally:
    # Đóng session
    session.close()