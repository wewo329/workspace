import os
import sys
import time
import pyexcel.cookbook as pc
import sample_generator as sg
from shutil import rmtree
from kor_encode import KorEncode as ke

class SampleMerger:
    def __init__(self):
        pass

    def merge_xlsx_directly(self, output_location, input_location):
        pass

    def merge_xlsx_throw_csv(self, output_location, input_location):
        self.merge_for_csv(output_location, input_location)
        csv_filename = output_location + "merge_for_csv.csv"
        time.sleep(1)
        ke.euc_to_utf8(csv_filename)
        utf8_filename = csv_filename.replace(".csv", "-utf8.csv")
        xlsx_filename = csv_filename.replace(".csv", ".xlsx")
        self.csv_to_xlsx(xlsx_filename, utf8_filename)
        os.remove(csv_filename)
        os.remove(utf8_filename)

        return "merge_xlsx_throw_csv: ok"

    def csv_to_xlsx(self, output_file, input_file):
        pc.merge_all_to_a_book([input_file], output_file)

    def merge_into_file(self, output_location, input_location, type_of_file):
        files = os.listdir(input_location)

        if len(files) == 0:
            print("There are no files in the '" + input_location + "' directory.")
            return

        if os.path.exists(output_location):
            rmtree(output_location)
        os.mkdir(output_location)

        merged_file = open(output_location + "/merge_into_file." + type_of_file, "w", encoding="utf8")

        for file in files:
            content = open(input_location + "/" +
                           file, "r", encoding="utf8")
            merged_file.write(content.read() + "\n\n")
            content.close()

        merged_file.close()

    def csv_format(self, files, input_location):
        headers = []
        is_first_header = True
        csv_content = ""
        for filename in files:
            file = open(input_location + filename, "r", encoding="utf8")
            lines = file.readlines()
            # 한 라인을 : 기준으로 나눠서 왼쪽은 헤더로 오른쪽은 컨텐츠 리스트로 만듬
            contents = []
            for line in lines:
                contents.append(line.split(":")[-1].strip())
                # 헤더는 한번만 원소별로 ,로 나눠서 문자열로 바꾼 뒤 파일에 입력
                if len(contents) > len(headers):
                    headers.append(line.split(":")[0].strip())

            if is_first_header:
                head = ", ".join(headers)
                csv_content += head
                is_first_header = False
            # 파일별로 콘텐츠는 계속 초기화 되어가며 ,로 나눠서 문자열로 바꾼 뒤 파일에 입력
            new_line = ", ".join(contents)
            csv_content += "\n" + new_line      

            file.close()
        return csv_content

    def merge_for_csv(self, output_location, input_location):
        # 파일들을 리스트로 받아옴
        files = os.listdir(input_location)

        if len(files) == 0:
            print("There are no files in the '" + input_location + "' directory.")
            return

        if os.path.exists(output_location):
            rmtree(output_location)
        os.mkdir(output_location)

        # 머지될 csv파일을 만듬
        merged_csv = open(output_location + "merge_for_csv.csv", "w", encoding="euc-kr")
        # 파일 내용을 라인별로 나눠서 리스트로 받아옴         
        merged_csv.write(self.csv_format(files, input_location))
        merged_csv.close()


if __name__ == "__main__":
    start_time = time.time()
    personal_info = "created_data/personal_info/"
    merged_files = "created_data/merged_files/"
    SM = SampleMerger()
    SM.merge_xlsx_throw_csv(merged_files, personal_info)
    # SM.merge_for_csv(merged_files, personal_info)
    end_time = time.time()
    print("The job took " + str(end_time-start_time) + " second")
