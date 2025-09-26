import math  # mathモジュールを呼び出す

class Rectangle:
    # 高さと幅を初期化する
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # 長方形の面積を取得する
    def area(self):
        rectangle_area = self.height * self.width
        # 小数点第2位で四捨五入する
        return f"{rectangle_area:.2f}"

    # 長方形の対角線を取得する
    def diagonal(self):
        # mathモジュールのsqrt()関数を用いる
        rectangle_diagonal = math.sqrt(self.height**2 + self.width**2)
        # 小数点第2位で四捨五入する
        return f"{rectangle_diagonal:.2f}"


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
