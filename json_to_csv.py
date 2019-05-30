import os
import json
import csv
import argparse

def convert_json(in_dir,out_dir,yolo_dir):

    os.chdir(yolo_dir) #change directory to that path where object detector YOLO v2 resides.
    if not os.path.exists(in_dir):
        print("INVALID DIRECTORY ENTERED")
    else:
        os.system("python flow --imgdir "+in_dir+"/ --model cfg/yolo.cfg --load bin/yolo.weights --json")

        filelst = os.listdir(in_dir+"/out")#storing all the names of the json files in a list 

        if not os.path.exists(out_dir):
            os.mkdir(out_dir)

        for j in filelst:
            with open(os.path.join(in_dir + "/out", j), "r") as infile:  # input the json file directory
                for line in infile:
                    data = json.loads(line)
                        # creating corresponding .csv file
                    assert j.split(".")[0] !=None, "value at index 0 not present"
                    image_data = open(out_dir + "/" + j.split(".")[0] + ".csv",'w')#if file name is "demo.json" j.split(".")[0] will return "demo" as the output

                    # create the csv writer object

                    csvwriter = csv.writer(image_data)

                     header = ["label", "confidence", "top_left_x", "top_left_y", "bottom_right_x","bottom_right_y"]  # list containing column names
                     csvwriter.writerow(header)
                     for i in data:
                        s = list(i.values())
                        l = [s[0], s[1], s[2]["x"], s[2]["y"], s[3]["x"], s[3]["y"]]
                        csvwriter.writerow(l)

                     image_data.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Code to convert json to csv',
                                     usage="\n\npython json_to_csv.py"
                                           "\t --input_dir "
                                           "\t --output_dir "
                                           "\t --yolo_dir ")

    parser.add_argument('--input_dir',
                        action='store',
                        dest='input_dir',
                        required=True,
                        help='Directory where images are stored')

    parser.add_argument('--output_dir',
                        action='store',
                        dest='output_dir',
                        required=True,
                        help='Directory where output will be stored')

    parser.add_argument('--yolo_dir',
                        action='store',
                        dest='yolo_dir',
                        required=True,
                        help='Directory where object detector Yolo resides')

    args = parser.parse_args()
    convert_json(args.input_dir, args.output_dir, args.yolo_dir)
