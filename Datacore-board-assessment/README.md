# thuctap_3T
task 1: 

Khởi tạo Trình Duyệt: Mã sẽ khởi tạo trình duyệt Chrome trong chế độ headless (không hiển thị giao diện người dùng).

em sử dụng selenium và webdriver để crawl data từ trang web https://cafef.vn/du-lieu/{exchange}/{ticker}-ban-lanh-dao-so-huu.chn
sau khi làm truy cập được trang web cần để crawl data, webdriver sẽ chờ 30s để trang web tải xog và cung cấp mã html của trang, sau khi truy nhập được vào mã html biến wait sẽ tìm đến đúng thẻ có nội dung vd (directorandonwer_name-top) để lưu tên vd Trương Gia Bình, và sau đó được in ra tất cả các hoạt động này sẽ được thực hiện ngay sau 30s trang web tải được mã html, nếu như sau 30s webdriver chưua thể truy nhập vào mã html sẽ xuất hiện lỗi timeout và em đã cho vòng lặp này chạy tối đa 5 lần để có thể lấy được thông tin cho từng mã.

Lặp qua các mã chứng khoán: Mã sẽ lặp qua các mã chứng khoán của các công ty trên 3 sàn chứng khoán:

- HOSE: Hệ thống các công ty lớn.

- HNX: Các công ty trên sàn Hà Nội.

- UPCOM: Các công ty chưa niêm yết trên sàn chính thức.

Lưu dữ liệu: Sau khi thu thập, dữ liệu sẽ được lưu vào file Parquet và có thể đọc lại bằng Pandas.

Task 2: 

Tương tự giống với task 1 về output nhưng trong bài này em phải tìm cách lấy được CSRF token của trang web vì vietstock có tính bảo mật khá cao, sau khi đã lấy được CSRF token bằng cách tìm 'value' của token nằm trong thẻ form action ban-lanh-dao.htm thì có thể dễ dàng truy cập được vào dữ liệu ban trong với cách tương tự như ở task 1 là tìm đến thẻ chứa tên, vai trò và chưcs vụ của người đứng đầu, với selenium là một cung cụ rất mạnh, nó giúp chúng ta tự động lấy được CSRL token, cũng như duy trì session management nên em không cần viết code để duy trì session hay cookies mà selenium tự động làm được hết điều đó 

Sau khi lấy được CSRL token thì các bước sau được làm tương tự như task 1

Task 3:
với nhiệm vụ này thì em chưa kịp hoàn thành trong thời gian quy định, em sẽ cố gắng hoàn thiện sau ạ, em mới chỉ đồng nhất dữ liệu, hợp nhất 2 dataframe và chọn ra row "golden"