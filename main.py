import yfinance
import datetime


class stock:
    def __init__(self):
        self.stock_list = ['3380.TW', "1524.TW"]
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
            self.five_price = yfinance.download(self.stock_list, start=self.target_five_date, end=self.target_end_date, progress=False)
            self.five_closing_price = self.five_price["Adj Close"][stock_name]
            #print("近五日收盤價: ", self.five_closing_price)
            self.five_total = len(self.five_closing_price)
            
            self.ten_price = yfinance.download(self.stock_list, start=self.target_ten_date, end=self.target_end_date, progress=False)
            self.ten_closing_price = self.ten_price["Adj Close"][stock_name]
            #print("近十日收盤價: ", self.ten_closing_price)
            self.ten_total = len(self.ten_closing_price)
            
            self.twenty_price = yfinance.download(self.stock_list, start=self.target_twenty_date, end=self.target_end_date, progress=False)
            self.twenty_closing_price = self.twenty_price["Adj Close"][stock_name]
            #print("近二十日收盤價: ", self.twenty_closing_price)
            self.twenty_total = len(self.twenty_closing_price)
            
            self.today_price = yfinance.download(self.stock_list, period="1d", progress=False)
            self.today_closing_price = self.today_price["Adj Close"][stock_name]
            #print("今日收盤價: ", self.today_closing_price)
            
            
            self.sum = 0
            for j5 in self.five_closing_price:
                self.sum += j5
                self.five_average = self.sum / self.five_total
            #print("五日平均收盤價: ", self.five_average)
            self.sum = 0    
            for j10 in self.ten_closing_price:
                self.sum += j10
                self.ten_average = self.sum / self.ten_total
            #print("十日平均收盤價: ", self.ten_average)    
            self.sum = 0
            for j20 in self.twenty_closing_price:
                self.sum += j20
                self.twenty_average = self.sum / self.twenty_total
            #print("二十日平均收盤價: ", self.twenty_average)  
            
            if self.today_closing_price[0] > self.five_average and self.today_closing_price[0] > self.ten_average and self.today_closing_price[0] > self.twenty_average:
                print("Higher than average:", stock_name)
            else:
                pass

if __name__ == "__main__":
    st = stock()
    st.get_five_day_ago_date()
    st.get_ten_day_ago_date()
    st.get_twenty_day_ago_date()
    st.get_tomorrow_date()
    st.get_target()