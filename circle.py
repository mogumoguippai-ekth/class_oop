class Circle():
    # 円の半径を初期化する
    def __init__(self, radius):
        self.radius = radius

    # 円の面積を取得する
    def area(self):
        circle_area = self.radius * self.radius * 3.1415
        # 小数点以下第2位を四捨五入する
        return round(circle_area, 2)
    
    # 円周の長さを取得する
    def perimeter(self):
        circle_perimeter = self.radius * 2 * 3.1415
        # 小数点以下第2位を四捨五入する
        return round(circle_perimeter, 2)


# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85
