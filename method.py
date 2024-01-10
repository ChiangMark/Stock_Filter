import datetime
from datetime import time, timedelta, date
import FinMind
from FinMind.data import DataLoader

dl = DataLoader()

class stock():
    def __init__(self):
        self.stock_list = ['3380', "1524", '2330']
        #self.start_time = time (0,0,0)
        # self.current_time = datetime.datetime.now()
        #self.end_time = time(9,0,0)
        self.current_date = datetime.date.today()
        self.target_five_date = datetime.date.today()
        self.target_ten_date = datetime.date.today()
        self.target_twenty_date = datetime.date.today()
        self.target_end_date = datetime.date.today()
        self.formatted_current_date = self.current_date.strftime("%Y-%m-%d")
        self.target_five_day = 4
        self.target_ten_day = 9
        self.target_twenty_day = 19
        self.target_end_date_num = 1
        self.perfect_stock = []
        self.opportunistic_stock = []
        self.bad_stock = []
        
    # def count_current_date(self):
    #     if self.current_date.weekday in [5, 6]:
    #         print("今天是六")
    #         self.current_date -=datetime.timedelta(days=1)
    #     elif self.current_date.weekday in [6, 7]:
    #         print("今天是日")
    #         self.current_date -=datetime.timedelta(days=2)
    #     else:
    #         print("今天是平日")
    
    def get_five_day_ago_date(self):
        while self.target_five_day > 0:
            self.target_five_date -= datetime.timedelta(days=1)
            # 如果是周六（weekday()返回5）或周日（weekday()返回6），则再向前推一天
            if self.target_five_date.weekday() in [5, 6]:
                continue
            self.target_five_day -= 1
            
    def get_ten_day_ago_date(self):
        while self.target_ten_day > 0:
            self.target_ten_date -= datetime.timedelta(days=1)
            # 如果是周六（weekday()返回5）或周日（weekday()返回6），则再向前推一天
            if self.target_ten_date.weekday() in [5, 6]:
                continue
            self.target_ten_day -= 1
            
    def get_twenty_day_ago_date(self):
        while self.target_twenty_day > 0:
            self.target_twenty_date -= datetime.timedelta(days=1)
            # 如果是周六（weekday()返回5）或周日（weekday()返回6），则再向前推一天
            if self.target_twenty_date.weekday() in [5, 6]:
                continue
            self.target_twenty_day -= 1
    
    def get_tomorrow_date(self):
        while self.target_end_date_num > 0:
            self.target_end_date += datetime.timedelta(days=1)
            # 如果是周六（weekday()返回5）或周日（weekday()返回6），则再向前推一天
            if self.target_end_date.weekday() in [5, 6]:
                continue
            self.target_end_date_num -= 1
        
    def get_target(self):
        for stock_name in self.stock_list:
            #fine close value
            five_price = dl.taiwan_stock_daily(stock_id=stock_name, start_date=self.target_five_date, end_date=self.target_end_date)
            five_closing_price = five_price.head()["close"]
            ten_price = dl.taiwan_stock_daily(stock_id=stock_name, start_date=self.target_ten_date, end_date=self.target_end_date)
            ten_closing_price = ten_price.head()["close"]
            twenty_price = dl.taiwan_stock_daily(stock_id=stock_name, start_date=self.target_twenty_date, end_date=self.target_end_date)
            twenty_closing_price = twenty_price.head()["close"]
            
            
            today_price = dl.taiwan_stock_daily(stock_id=stock_name, start_date=self.current_date)
            today_closing_price = today_price.head()["close"]
            
            # find average value
            five_average = five_closing_price.mean()
            ten_average = ten_closing_price.mean()   
            twenty_average = twenty_closing_price.mean() 
            
            #find target stock
            if today_closing_price[0] > five_average and today_closing_price[0] > ten_average and today_closing_price[0] > twenty_average:
                self.perfect_stock.append(stock_name)               
            elif today_closing_price[0] > five_average and today_closing_price[0] < ten_average and today_closing_price[0] < twenty_average:
                self.opportunistic_stock.append(stock_name)
            else:
                self.bad_stock.append(stock_name)
        print("站上所有均線:", self.perfect_stock)
        print("抄底:", self.opportunistic_stock)
        print("再觀察:", self.bad_stock)
            
if __name__ == "__main__":
    st = stock()
    # st.count_current_date()
    st.get_five_day_ago_date()
    st.get_ten_day_ago_date()
    st.get_twenty_day_ago_date()
    st.get_tomorrow_date()
    st.get_target()