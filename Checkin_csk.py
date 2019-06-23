import csv
import pandas as pd
import argparse

def check_csk(csk_file,inverted_index):
    error_set = list()
    with open(csk_file) as csvFile:
        csv_data = pd.read_csv(csvFile, index_col=0)
    labels=[i for i in csv_data]  #labels contains name of all the classes present in first column of csk file
    with open(inverted_index) as tsvfile:
        tsv = csv.reader(tsvfile, delimiter="\t")
        for row in tsv:   #row will return a list eg.['person,is_near,bicycle', 'test1.csv,test4.csv']
            key=row[0]
            img_id=row[1]
            triple=key.split(',')  #split will return 3 items in triple eg. triple=> ['person' , 'is_near' , 'bicycle']
            label1=triple[0]
            relation = triple[1]
            label2=triple[2]
            if label1 in labels and label2 in labels:
                value=csv_data.loc[label1][label2]   # get the cell value corresponding to both the labels in csk file
                out=value.split(',')         # using split because more than one relation can be present in a cell
                if relation not in out:
                    error_set.append(img_id)
    return error_set

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Code to check error in images',
                                     usage="\n\npython Checkin_csk.py"
                                           "\t --csk_dir "
                                           "\t --inverted_index_dir")

    parser.add_argument('--csk_dir',
                        action='store',
                        dest='csk_dir',
                        required=True,
                        help='Directory where csk file is stored')

    parser.add_argument('--inverted_index_dir',
                        action='store',
                        dest='inverted_index_dir',
                        required=True,
                        help='Directory where inverted_index is stored')

    args = parser.parse_args()
    output=check_csk(args.csk_dir,args.inverted_index_dir)
    print(f"The list of image ids containing mistakes are:{output} ")
