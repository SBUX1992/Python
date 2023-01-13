"""
날짜 : 2023-01-11
이름 : 강중현
내용 : 파이썬 상속 실습하기
"""

from sub2.StockAccount import StockAccount

kb = StockAccount('국민은행', '101-12-1110', '홍길동', 5000, '삼성전자', 10, 60000)
kb.deposit(1000000)
kb.sell(5, 70000)
kb.show()



