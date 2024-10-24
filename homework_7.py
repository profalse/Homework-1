class House_human():
    """описание людского дома"""
    def __init__(self, style, number, capacity):
        """свойства дома"""
        self.style = style
        self.number = number
        self.capacity = capacity
        self.coast = 100
        self.level = 0

    def build(self):
        """строит дом"""
        # print("Дом " + self.style + " под номером " + str(self.number) + " вместимостью " + str(self.capacity) + " построен.")
        # print(f"Дом {self.style} под номером {str(self.number)} вместимостью {str(self.capacity)} построен.")
    
    def level_of_houses(self, level):
        """уровень дома"""
        if self.level + level == 1:
            self.level += 1
            print('хижина')
        elif self.level + level == 2:
            self.level += 2
            print('ферма')
        elif self.level + level == 3:
            self.level += 3
            print('таверна')
        elif self.level + level == 4:
            self.level += 4
            print('замок')

House1 = House_human("ферма", 1, 15)
House2 = House_human("хижина", 5, 10)

# print(House2.style)
# print(House2.number)
# print(House2.capacity)

# House1.build()

House1.level_of_houses(2)
print(House1.level)


class House_horde(House_human):
    """дом орды"""
    def __init__(self, style, number, damage):
        super().__init__(self, style, number)
        self.damage = damage

House_horde1 = House_horde("землянка", 1, 15)
print(House_horde1.damage)