import numpy as np
import pandas as pd

def reader(filename):
    df = pd.read_csv(filename)
    return df

def check_overlapping(obj1, rect1, obj2, rect2):
    #case1:
    my_str = []
    if(rect1[0][0] >= rect2[0][0] and rect1[0][1] >= rect2[0][1] and rect1[1][0] >= rect2[1][0] and rect1[1][1] >= rect2[1][1]):
        my_str.append(obj1 + ' partOf ' + obj2)
   #case2:
    if(rect1[1][0] >= rect2[0][1] and rect1[0][1] < rect2[0][0]):
        my_str.append(obj1 + ' overlapWith ' + obj2)
   #case3:
    else:
        my_str.append(obj1 + ' collocateWith ' + obj2)

    return my_str

def detector(df):
    num_rows = len(df.index)
    str_value = []
    for i in range(num_rows):
        for j in range(i+1, num_rows):
            obj1 = (df.iloc[i]["label"])
            obj2 = (df.iloc[j]["label"])
            top_left1 = (int(df.iloc[i]["Top_Left_x"]), int(df.iloc[i]["Top_Left_y"]))
            bottom_right1 = (int(df.iloc[i]["Bottom_Right_x"]), int(df.iloc[i]["Bottom_Right_y"]))
            top_left2 = (int(df.iloc[j]["Top_Left_x"]), int(df.iloc[j]["Top_Left_y"]))
            bottom_right2 = (int(df.iloc[j]["Bottom_Right_x"]), int(df.iloc[j]["Bottom_Right_y"]))
            rect1 = (top_left1, bottom_right1)
            rect2 = (top_left2, bottom_right2)
            #print(top_left1, bottom_right1)
            #print(top_left2, bottom_right2)
            str_value = check_overlapping(obj1, rect1, obj2, rect2)

    return str_value



if __name__ == "__main__":
    df = reader("~/Desktop/convertcsv.csv")
    str_value_new= detector(df)
