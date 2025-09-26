import math

class Square:


    def __init__(self, side):
        self.side = side
    
        # 正方形の面積を取得する
    def area(self):
        rectangle_area = self.side * self.side
        # 小数点以下が0なら整数で、そうでないなら小数点第2位で四捨五入する
        # mothモジュールのmodf()関数で判定する
        if math.modf(rectangle_area)[0] == 0:
            # 整数部を返す
            return int(rectangle_area)
        else:
            # 小数点第2位で四捨五入する
            return round(rectangle_area, 2)

    # 長方形の対角線を取得する
    def diagonal(self):
        # mathモジュールのsqrt()関数を用いる
        rectangle_diagonal = self.side * math.sqrt(2)
        # 小数点以下が0なら整数で、そうでないなら小数点第2位で四捨五入する
        # mothモジュールのmodf()関数で判定する
        if math.modf(rectangle_diagonal)[0] == 0:
            # 整数部を返す
            return int(rectangle_diagonal)
        else:
            # 小数点第2位で四捨五入する
            return round(rectangle_diagonal, 2)


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
