# import random

import sys
import os
import random
import pymysql

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from sample_generator import SampleMaker

YEARS = list(range(70,100))
MONTHES = list(range(1, 13))
M30 = [4, 6, 9, 11]
DAYS = list(range(1, 32))
DAYS30 = list(range(1, 31))
DAYS28 = list(range(1, 29))
ADDRS = ['서울', '대전', '부산', '의정부', '양주', '전주', '광주', '강원', '제주', '인천']

class Studnet1000_make():

    def make_birth(self):
        y = random.choice(YEARS)
        m = random.choice(MONTHES)
        if m == 2:
            d = random.choice(DAYS28)
        elif m in M30:
            d = random.choice(DAYS30)
        else:
            d = random.choice(DAYS)
            
        birth  = "{}{:02d}{:02d}".format(y, m, d)
        return birth

    def make_data(self):
        sm = SampleMaker
        data = []
        for _ in range(0, 1000):
            sm.make_name(sm) 
            addr = random.choice(ADDRS)
            birth = self.make_birth(self)
            sm.make_phonenumber(sm)
            sm.make_email(sm)
            gender = random.choice((0, 1))
            result = (sm.name, addr, birth, sm.phone, sm.email, gender)
            data.append(result)

        return data

if __name__ == "__main__":
    exec = Studnet1000_make
    data = [random.choice((0, 1)) for _ in range(0, 1000)]
    print(data)

    conn = pymysql.connect(
        host='172.30.1.30', 
        user='dooo', 
        password='dooo!', 
        port=3306, 
        db='dooodb', 
        charset='utf8')

    with conn:
        cur = conn.cursor()
        sql = "update Student set gender = %d"
        cur.executemany(sql, data)
        print("AffecedRowCount", cur.rowcount)
        conn.commit()