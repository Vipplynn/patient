class Procedure:
    
    def __init__(self, pro, date, prac, charge):
        self.pro = pro
        self.date = date
        self.prac = prac
        self.charge = charge
    
    def set_pro(self, pro):
        self.pro = pro

    def set_date(self, date):
        self.date = date

    def set_prac(self, prac):
        self.prac = prac

    def set_charge(self,charge):
        self.charge = charge

    def get_pro(self):
        return self.pro

    def get_date(self):
        return self.date

    def get_prac(self):
        return self.prac

    def get_charge(self):
        return self.charge