#StustDrinkShop

class Drinks:
    def __init__(self):
        self.price = 0
    def SetPrice(self, price):
        self.price = price

class ColdDrinks(Drinks):#繼承Drinks

    def __init__(self,name,price,ice,sugar):#初始化 名稱、價格、冰量、甜度
        self.name = name
        self.price = price
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
g_ColdDrinks.ShowVal()
g_ColdDrinks.SetPrice(50)
g_ColdDrinks.ShowVal()

g_HotDrinks = HotDrinks("coco",60,5)
g_HotDrinks.ShowVal()
g_HotDrinks.SetPrice(75)
g_HotDrinks.SetName("hotcoco")
g_HotDrinks.ShowVal()

g_ColdDrinks_1 = ColdDrinks("milk tea",50,3,3)
g_ColdDrinks_1.ShowVal()
g_ColdDrinks_1.SetSugar(5)
g_ColdDrinks_1.ShowVal()

print("\n\n\n")

class Emplayer:
    def __init__(self, Name, Seniority, WorkTime):#初始化 名稱、年資、工作時數
        self.Name = Name
        self.Seniority = Seniority
        self.WorkTime = WorkTime

    def FindName(self):#查找姓名 會輸出改員工的姓名、年資、工作時數
        print("Name:" + str(self.Name) + " " + "Seniority:" + str(self.Seniority) + " " + "WorkTime" + str(self.WorkTime))

    def CalacMonthSalary(self):#計算月薪
        MonthSalary = (self.Seniority * self.WorkTime) * 30
        print("MonthSalary:" + str(MonthSalary))
    def SetWorkTime(self,WorkTime):#設定工作時數
        self.WorkTime = WorkTime
    def SetSeniority(self,Seniority):#設定年資
        self.Seniority = Seniority

Emplayer_1 = Emplayer("Leo",158,7)
Emplayer_1.FindName()
Emplayer_1.CalacMonthSalary()
Emplayer_1.SetSeniority(178)
Emplayer_1.SetWorkTime(8)
Emplayer_1.CalacMonthSalary()

Emplayer_2 = Emplayer("Sun",170,7)
Emplayer_2.FindName()
Emplayer_2.CalacMonthSalary()

Emplayer_3 = Emplayer("Junny",180,6)
Emplayer_3.FindName()
Emplayer_3.CalacMonthSalary()
Emplayer_3.SetSeniority(185)
Emplayer_3.CalacMonthSalary()