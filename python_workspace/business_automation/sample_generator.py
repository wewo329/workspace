#-*-coding:utf-8 -*-
import os
import sys
import time
import random
from shutil import rmtree

class SampleMaker:
    FIRST, MIDDLE, LAST = 0, 1, 2
    NAME_SAMPLE = (("이안남권송김지한박장"), ("은혁요진석승유"), ("우한현석찬학선"))
    CHAR_SAMPLE = "abcdefghijklnmopqrstuvwxyzABUZ1234567890"
    EMAIL_SAMPLE = ("@naver.com", "@gmail.com", "@daum.net", "@hanmail.com", "@github.io")
    DIVISION_SAMPLE = ("Develops", "Sales", "Security", "Design", "promotion")
    NUM_SAMPLE = "1234567890"

    def __init__(self):
        pass

    def make_samples(self, output_location, num_samples):
        if os.path.exists(output_location):
            rmtree(output_location)
        os.mkdir(output_location)

        for i in range(1, num_samples+1):
            self.make_inform()
            filename = output_location + "/" + str(i) + "_" + self.name
            self.write_file(filename)

    def make_inform(self):
        self.make_name()
        self.age = str(random.randint(19, 70))
        self.make_email()
        self.division = random.choice(self.DIVISION_SAMPLE)
        self.make_phonenumber()
        self.sex = random.choice(("male", "female"))

    def make_name(self):
        first = random.choice(self.NAME_SAMPLE[self.FIRST])
        middle = random.choice(self.NAME_SAMPLE[self.MIDDLE])
        last = random.choice(self.NAME_SAMPLE[self.LAST])
        self.name = first + middle + last

    def make_phonenumber(self):
        middle = "".join(random.sample(self.NUM_SAMPLE, 4))
        last = "".join(random.sample(self.NUM_SAMPLE, 4))
        self.phone = "010-" + middle + "-" + last

    def make_email(self):
        userid = "".join(random.sample(self.CHAR_SAMPLE, random.randint(6, 14)))
        site = random.choice(self.EMAIL_SAMPLE)
        self.email = userid + site

    def write_file(self, filename):
        outfile = open(filename, "w", encoding="utf8")
        outfile.write("name : " + self.name + "\nage : " + self.age + "\ne-mail : " + self.email + \
            "\ndivision : " + self.division + "\ntelephone : " + self.phone + "\nsex : " + self.sex)
        outfile.close()

if __name__ == "__main__":
    start_time = time.time()
    execute = SampleMaker()
    execute.make_samples("created_data/personal_info", 1000)
    end_time = time.time()
    print("The job took " + str(end_time-start_time) + " second")
    print(sys.stdin.encoding)