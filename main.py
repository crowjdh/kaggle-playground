import pandas as pd


def main():
    data = pd.read_csv('data.csv')
    print(data.head(10))
    data.isna().any()


if __name__ == '__main__':
    main()
