import sys

class KorEncode:
    def __init__(self):
        pass

    def euc_to_utf8(filename: str):
        in_file = open(filename, "r", encoding="euc-kr")

        out_file = open(filename.replace(".csv", "-utf8.csv"), "w", encoding="utf8")

        content = in_file.read()
        out_file.write(content)

        in_file.close()
        out_file.close()

if __name__ == "__main__":
    filename = sys.argv[1]
    print(filename)
    KorEncode.euc_to_utf8(filename)