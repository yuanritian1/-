# 一条具有明确的目的的语句，可以使用字符串格式化语法来实现，格式化的语法如下：
# print("Hello, %d" % (1*1))
# print(f"Hello, {1*1}")
# print("Hello,%s" % type(1))
name = "传智播客"
stock_price = 71.63
stock_code = "003232"
stock_price_daily_growth_factor = 1.25
growth_days = 7
print(f"公司：{name},股票代码：{stock_code},当前股价：{19.99}")
print(f"每日增长系数：{stock_price_daily_growth_factor},经过{growth_days}天后,当前股价：%.2f" % (
    stock_price))
