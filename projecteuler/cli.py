import sys
import pandas as pd

def main():
    df = pd.read_excel('problems.xlsx')
    try:
        num = int(sys.argv[2])
    except ValueError:
        print("Argument must be an integer!")
        exit()
    if num not in df["Problem"].values:
        print(num)
        print("Problem number exists between 1- 1011!")
        exit()
    for cell in df["Problem"]:
        if cell == num:
            row = df[df["Problem"] == num].iloc[0].to_dict()
            print(row)

if __name__ == '__main__':
    main()