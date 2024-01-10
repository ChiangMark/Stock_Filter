import datetime
from FinMind.data import DataLoader

class StockAnalyzer:
    def __init__(self):
        self.stock_list = ['3380', "1524", '2330']
        self.current_date = datetime.date.today()
        self.target_five_date = self.current_date - datetime.timedelta(days=5)
        self.target_ten_date = self.current_date - datetime.timedelta(days=10)
        self.target_twenty_date = self.current_date - datetime.timedelta(days=20)
        print(self.target_twenty_date)
        self.target_end_date = self.current_date
        self.dl = DataLoader()
        self.perfect_stock = []
        self.opportunistic_stock = []
        self.bad_stock = []

    def get_target(self):
        for stock_name in self.stock_list:
            five_price = self.dl.taiwan_stock_daily(stock_id=stock_name, start_date=self.target_five_date, end_date=self.target_end_date)
            ten_price = self.dl.taiwan_stock_daily(stock_id=stock_name, start_date=self.target_ten_date, end_date=self.target_end_date)
            twenty_price = self.dl.taiwan_stock_daily(stock_id=stock_name, start_date=self.target_twenty_date, end_date=self.target_end_date)
            today_price = self.dl.taiwan_stock_daily(stock_id=stock_name, start_date=self.current_date)

            # 计算五日、十日、二十日平均收盘价
            five_average = five_price["close"].mean()
            #print(five_average)
            ten_average = ten_price["close"].mean()
            #print(ten_average)
            twenty_average = twenty_price["close"].mean()
            #print(twenty_average)

            today_closing_price = today_price["close"].iloc[0]

            if today_closing_price > five_average and today_closing_price > ten_average and today_closing_price > twenty_average:
                self.perfect_stock.append(stock_name)
            elif today_closing_price > five_average and today_closing_price < ten_average and today_closing_price < twenty_average:
                self.opportunistic_stock.append(stock_name)
            else:
                self.bad_stock.append(stock_name)

        # print("站上所有均線:", self.perfect_stock)
        # print("抄底:", self.opportunistic_stock)
        # print("再觀察:", self.bad_stock)

if __name__ == "__main__":
    st = StockAnalyzer()
    st.get_target()