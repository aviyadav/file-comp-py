import polars as pl
from datacompy import PolarsCompare

def run_datacompy(df1, df2):
    compare = PolarsCompare(
        df1,
        df2,
        join_columns='acct_id',
        abs_tol=0.0001,
        rel_tol=0,
        df1_name='original',
        df2_name='new'
    )

    print(compare.report())

    print(compare.df1_unq_rows)
    print(compare.df2_unq_rows)

    print(compare.intersect_columns())

    print(compare.df1_unq_columns())

    print(compare.df2_unq_columns())

if __name__ == "__main__":
    df1 = pl.read_csv('data/file1.csv')
    df2 = pl.read_csv('data/file2.csv')

    run_datacompy(df1, df2)
