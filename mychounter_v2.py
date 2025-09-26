class MyCounterV2:

    # カウンタ初期値を初期化する
    def __init__(self, value, step):
        self.value = value
        self.step = step

    
    # カウンタ初期入力値を返す
    def value(self):
        return self.value

    # カウンタをstepの数だけ増やす
    def count_up(self):
        self.value += self.step
        return


counter1 = MyCounterV2(value=0, step=1)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2

counter2 = MyCounterV2(value=0, step=3)
print(counter2.value)  # 0

counter2.count_up()
print(counter2.value)  # 3

counter2.count_up()
print(counter2.value)  # 6
