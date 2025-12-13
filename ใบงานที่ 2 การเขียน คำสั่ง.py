<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>ใบสมัคร</title>
    <style>
        body {
            font-family: Tahoma;
            padding: 20px;
        }
        form {
            max-width: 500px;
            margin: auto;
        }
        label {
            display: block;
            margin-top: 10px;
        }
        input, select, textarea, button {
            width: 100%;
            padding: 6px;
            margin-top: 5px;
        }
    </style>
</head>
<body>

<h2>ใบสมัครสมาชิก</h2>

<form>

    <!-- 1 ชื่อ-สกุล -->
    <label>ชื่อ - สกุล</label>
    <input type="text" required>

    <!-- 2 อายุ -->
    <label>อายุ</label>
    <input type="number" min="1">

    <!-- 3 ที่อยู่เลขที่ -->
    <label>ที่อยู่เลขที่</label>
    <input type="text">

    <!-- 4 ตำบล/แขวง -->
    <label>ตำบล / แขวง</label>
    <input type="text">

    <!-- 5 อำเภอ / เขต -->
    <label>อำเภอ / เขต</label>
    <input type="text">

    <!-- 6 จังหวัด -->
    <label>จังหวัด</label>
    <input type="text">

    <!-- 7 รหัสไปรษณีย์ -->
    <label>รหัสไปรษณีย์</label>
    <input type="text" maxlength="5">

    <!-- 8 เบอร์โทร -->
    <label>เบอร์โทรศัพท์</label>
    <input type="tel">

    <!-- 9 Email -->
    <label>Email</label>
    <input type="email">

    <!-- 10 ตั้งรหัสเข้าใช้งาน -->
    <label>ตั้งรหัสเข้าใช้งาน</label>
    <input type="password">

    <!-- 11 Username -->
    <label>Username</label>
    <input type="text">

    <!-- 12 Password -->
    <label>Password</label>
    <input type="password">

    <!-- 13 แนบรูปภาพ -->
    <label>แนบรูปภาพ</label>
    <input type="file" accept="image/*">

    <!-- 14 ปุ่ม Save -->
    <br><br>
    <button type="submit">Save</button>

    <!-- 15 เงื่อนไขการสมัคร -->
    <label>
        <input type="checkbox" required>
        ยินยอมเงื่อนไขการสมัคร
    </label>

</form>

</body>
</html>
