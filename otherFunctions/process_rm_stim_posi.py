import pandas as pd


def x_coor_to_lst(input_x_coor: float) -> list:
    return list([input_x_coor, 0])


def process_col(input_df: pd.DataFrame, col_name: str, func_name):
    if col_name in input_df.columns:
        input_df[col_name] = input_df[col_name].map(func_name)
    else:
        raise Exception(f"Warning: missing {col_name}")

def transform_size(size):
    return [size, size]

if __name__ == '__main__':
    save_to_excel = True
    filename = "files/conditions.xlsx"
    df = pd.read_excel(filename)
    to_process = ["pos1", "pos2", "pos3", "pos4", "pos5", "pos6"]
    size = ["size"]
    # to_process = ["pos1", "pos2"]
    for pos in to_process:
        process_col(input_df = df, col_name = pos, func_name = x_coor_to_lst)
    
    process_col(df, col_name = "size", func_name = transform_size)

    if save_to_excel:
        df.to_excel("processed_condition.xlsx")
    
        


