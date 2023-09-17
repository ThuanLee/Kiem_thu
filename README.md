## Bài toán: Chuyển đổi tiền từ đơn vị đô `$` sang Việt Nam đồng `VND` theo tỉ giá hiện tại và xếp loại
### Luồng hoạt động của chương trình

1. Lấy tỉ giá (_rate_) hiện tại `$ - VND` bằng api
2. Người dùng nhập số tiền đô muốn chuyển đổi
3. Hệ thống trả về số tiền Việt Nam đồng sau khi quy đổi
4. Hệ thống kiểm tra mức tiền và đưa ra nhận xét:
>* Nếu bạn có **từ 1 tỉ đồng trở lên**, bạn sẽ là tỉ phú vnd
>* Nếu bạn có **từ 1 triệu đồng đến dưới 1 tỉ đồng**, bạn sẽ là triệu phú vnd
>* Nếu bạn có **ít hơn 1 triệu đồng**, bạn rất nghèo
>* Nếu bạn nhập sai định dạng (không phải số), hệ thống sẽ đưa ra thông báo lỗi

### Thiết kế các ca kiểm thử
* `Phân hoạch tương đương` Chia input thành các lớp dữ liệu đầu vào (-∞; 0) v [0; 10^6 / rate) v [10^6 / rate; 10^9 / rate) v [10^9 / rate; +∞)

<table>
    <tr>
        <th>STT</th>
        <th>Range</th>
        <th>Input</th>
        <th>Output</th>
        <th>Expected</th>
    </tr>
    <tr>
        <td>1</td>
        <td>(-∞; 0)</td>
        <td>-12</td>
        <td>Input chỉ có thể là số và không âm</td>
        <td>Input chỉ có thể là số và không âm</td>
    </tr>
    <tr>
        <td>2</td>
        <td>[0; 10^6 / rate)</td>
        <td>14</td>
        <td>Bạn rất nghèo</td>
        <td>Bạn rất nghèo</td>
    </tr>
    <tr>
        <td>3</td>
        <td>[10^6 / rate; 10^9 / rate)</td>
        <td>144.56</td>
        <td>Bạn là triệu phú VND</td>
        <td>Bạn là triệu phú VND</td>
    </tr>
    <tr>
        <td>4</td>
        <td>[10^9 / rate; +∞)</td>
        <td>420000</td>
        <td>Bạn là tỉ phú VND</td>
        <td>Bạn là tỉ phú VND</td>
    </tr>
</table>

<br>

* `Bảng quyết định` 
- Điều kiện: __Số âm__, __Số không âm__
- Hành động: __In ra lỗi__, __Đưa ra nhận xét__

<table>
    <tr>
        <th></th>
        <th></th>
        <th>R1</th>
        <th>R2</th>
    </tr>
    <tr>
        <td rowspan='2'>Điều kiện</td>
        <td>Số âm</td>
        <td>T</td>
        <td>F</td>
    </tr>
    <tr>
        <td>Số không âm</td>
        <td>F</td>
        <td>T</td>
    </tr>
    <tr>
        <td rowspan='2'>Hành động</td>
        <td>In ra lỗi</td>
        <td>x</td>
        <td></td>
    </tr>
    <tr>
        <td>Đưa ra nhận xét</td>
        <td></td>
        <td>x</td>
    </tr>
</table>
