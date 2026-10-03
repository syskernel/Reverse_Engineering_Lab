import sys
import pandas as pd

def main():
    df = pd.read_excel('problems.xlsx')
    for num in df["Problem"]:
        if num == int(sys.argv[2]):
            row = df[df["Problem"] == num]
            print(row)

if __name__ == '__main__':
    main()