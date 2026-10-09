import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
data = {"Họ và tên": 
        ["Nguyễn Lê Minh Anh", "Trần Ngọc Bích", "Lê Hoàng Nam",
        "Hoàng Minh Quân", "Lê Cát Tường", "Đặng Ngọc Anh",
        "Bùi Quốc Huy", "Hoàng Thu Hà", "Đỗ Thành Công",
        "Đặng Hoàng Uyên Vi"],
    "Điểm chuyên cần": [9, 8, 10, 7, 8, 9, 6, 10, 7, 9],
    "Điểm giữa kì": [8, 7, 9, 6, 7, 8, 5, 9, 6, 8],
    "Điểm cuối kì": [9, 8, 8, 7, 8, 9, 6, 10, 7, 9]}
df = pd.DataFrame(data)
df["Tong_ket"] = (df["Điểm chuyên cần"] * 0.2 + df["Điểm giữa kì"] * 0.3 + df["Điểm cuối kì"] * 0.5)
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"
df["Xếp loại"] = df["Tong_ket"].apply(xep_loai)
df["Tổng kết"] = df["Tong_ket"].round(2)
st.subheader("Bảng điểm 10 sinh viên")
st.dataframe(df[["Họ và tên", "Điểm chuyên cần", "Điểm giữa kì",
    "Điểm cuối kì", "Tổng kết", "Xếp loại"]], hide_index=True)
st.subheader("Thống kê lớp")
st.write("Điểm trung bình:", round(df["Tong_ket"].mean(), 2))
cao = df.loc[df["Tong_ket"].idxmax()]
thap = df.loc[df["Tong_ket"].idxmin()]
st.write("Sinh viên điểm cao nhất:", cao["Họ và tên"],
         "-", round(cao["Tong_ket"], 2))
st.write("Sinh viên điểm thấp nhất:", thap["Họ và tên"],
         "-", round(thap["Tong_ket"], 2))
st.write("Số sinh viên đạt:", int((df["Tong_ket"] >= 5).sum()))
st.subheader("Tra cứu sinh viên")
ten = st.selectbox("Chọn sinh viên", df["Họ và tên"])
sv = df[df["Họ và tên"] == ten].iloc[0]
st.write("Điểm chuyên cần:", sv["Điểm chuyên cần"])
st.write("Điểm giữa kì:", sv["Điểm giữa kì"])
st.write("Điểm cuối kì:", sv["Điểm cuối kì"])
st.write("Điểm tổng kết:", round(sv["Tong_ket"], 2))
st.write("Xếp loại:", sv["Xếp loại"])
st.subheader("Biểu đồ điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots()
ax.barh(df["Họ và tên"], df["Tong_ket"])
ax.invert_yaxis()
ax.set_xlim(0, 10)
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Họ và tên")
fig.tight_layout()
st.pyplot(fig)
st.divider()
st.caption("Người tạo: [Nguyễn Thị Thuỳ Dung] | MSSV: [024308011546]")
