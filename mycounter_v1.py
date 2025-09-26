class MyCounterV1:

    # カウンタ初期値を初期化する
    def __init__(self, value):
        self.value = value

    # カウンタ初期入力値を返す
    def get_value(self):
        return self.value
    
    # カウンタを1つ増やす
    def count_up(self):
        self.value += 1
        return


counter1 = MyCounterV1(value=0)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2

counter2 = MyCounterV1(value=7)
print(counter2.value)  # 7

counter2.count_up()
print(counter2.value)  # 8

counter2.count_up()
print(counter2.value)  # 9
