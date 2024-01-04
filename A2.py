#StustDrinkShop

class Drinks:
    def __init__(self):
        self.price = 0 #初始化 價格
    def SetPrice(self, price):#設定價格
        self.price = price

class ColdDrinks(Drinks):#繼承Drinks

    def __init__(self,name,price,ice,sugar):#初始化 名稱、價格、冰量、甜度
        self.name = name
        self.price = price #繼承Drinks
        self.ice = ice
        self.sugar = sugar

    def SetName(self, name):
        self.name = name
    def SetSugar(self, sugar):
        self.sugar = sugar

    def ShowVal(self):#來顯示所有數值來測試
        print("Name:" + str(self.name) + " price:" + str(self.price) + " ice:" +  str(self.ice) + " sugar:" + str(self.sugar))


class HotDrinks(Drinks):#繼承Drinks

    def __init__(self,name,price,sugar):#初始化 名稱、價格、甜度
        self.name = name
        self.price = price
        self.sugar = sugar

    def SetName(self, name):
        self.name = name
    def SetSugar(self, sugar):
        self.sugar = sugar

    def ShowVal(self):#來顯示所有數值來測試
        print("Name:" + str(self.name) + " price:" + str(self.price) + " sugar:" + str(self.sugar))       


g_ColdDrinks = ColdDrinks("tea",45,3,5)
g_ColdDrinks.ShowVal()#顯示所有數值
g_ColdDrinks.SetPrice(50)#設定價錢
g_ColdDrinks.ShowVal()

g_HotDrinks = HotDrinks("coco",60,5)
g_HotDrinks.ShowVal()#顯示所有數值
g_HotDrinks.SetPrice(75)#設定價錢
g_HotDrinks.SetName("hotcoco")#設定名稱
g_HotDrinks.ShowVal()#顯示所有數值

g_ColdDrinks_1 = ColdDrinks("milk tea",50,3,3)
g_ColdDrinks_1.ShowVal()#顯示所有數值
g_ColdDrinks_1.SetSugar(5)#設定甜度
g_ColdDrinks_1.ShowVal()#顯示所有數值

print("\n\n\n")

class Emplayer:
    def __init__(self, Name, Seniority, WorkTime):#初始化 名稱、年資、工作時數
        self.Name = Name
        self.Seniority = Seniority
        self.WorkTime = WorkTime

    def FindName(self):#查找姓名 會輸出改員工的姓名、年資、工作時數
        print("Name:" + str(self.Name) + " " + "Seniority:" + str(self.Seniority) + " " + "WorkTime" + str(self.WorkTime))

    def CalacMonthSalary(self):#計算月薪
        MonthSalary = (self.Seniority * self.WorkTime) * 30 #公式 (年資 x 時數) x 30天
        print("MonthSalary:" + str(MonthSalary))
    def SetWorkTime(self,WorkTime):#設定工作時數
        self.WorkTime = WorkTime
    def SetSeniority(self,Seniority):#設定年資
        self.Seniority = Seniority

Emplayer_1 = Emplayer("Leo",158,7)
Emplayer_1.FindName()#尋找姓名 順便顯示所有數值測試
Emplayer_1.CalacMonthSalary()#計算月薪
Emplayer_1.SetSeniority(178)#設定年資
Emplayer_1.SetWorkTime(8)#設定工作時數
Emplayer_1.CalacMonthSalary()#計算月薪

Emplayer_2 = Emplayer("Sun",170,7)
Emplayer_2.FindName()#尋找姓名 順便顯示所有數值測試
Emplayer_2.CalacMonthSalary()#計算月薪

Emplayer_3 = Emplayer("Junny",180,6)
Emplayer_3.FindName()#尋找姓名 順便顯示所有數值測試
Emplayer_3.CalacMonthSalary()#計算月薪
Emplayer_3.SetSeniority(185)#設定年資
Emplayer_3.CalacMonthSalary()#計算月薪