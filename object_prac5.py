class My_Data():

    def __init__(self, My_Name, My_Nature, My_Blood_Type, My_Age, My_Brith):
        self.My_Name = My_Name
        self.My_Nature = My_Nature
        self.My_Blood_Type = My_Blood_Type
        self.My_Age = My_Age
        self.My_Brith = My_Brith

    def My_Data_Display(self):
        print("名前: %s 性別: %s " %(self.My_Name, self.My_Nature))
        print("血液型: %s 年齢: %s " %(self.My_Blood_Type, self.My_Age))
        print("生年月日: %s " %(self.My_Brith))



