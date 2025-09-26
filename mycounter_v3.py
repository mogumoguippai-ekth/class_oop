class MyCounterV3:

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
        
    # カウンタをstepの数だけ減らす
    def count_down(self):
        self.value -= self.step
        return


counter1 = MyCounterV3(value=1, step=2)
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 3

counter1.count_up()
print(counter1.value)  # 5

counter1.count_down()
print(counter1.value)  # 3

counter2 = MyCounterV3(value=3, step=4)
print(counter2.value)  # 3

counter2.count_down()
print(counter2.value)  # -1

counter2.count_down()
print(counter2.value)  # -5
