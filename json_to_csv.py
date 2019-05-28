import os
import json
import csv


def fun(in_dir,out_dir,**d):

    os.chdir("C:/Users/anurag/Downloads/darkflow-master/darkflow-master") #change directory to that path where object detector YOLO v2 resides.
    if not os.path.exists(in_dir):
        print("INVALID DIRECTORY ENTERED")
    else:
        os.system("python flow --imgdir "+in_dir+"/ --model cfg/yolo.cfg --load bin/yolo.weights --json")

        filelst = os.listdir(in_dir+"/out")

        if not os.path.exists(out_dir):
            os.mkdir(out_dir)

        for j in filelst:
            infile = open(os.path.join(in_dir+"/out", j), "r")  # input the json file directory
            data = json.loads(infile.read())

            image_data = open(out_dir +"/"+ j.split(".")[0] + ".csv", 'w')  # creating corresponding .csv file

            # create the csv writer object

            csvwriter = csv.writer(image_data)

            header = ["label", "confidence", "top_left_x", "top_left_y", "bottom_right_x","bottom_right_y"]  # list containing column names
            csvwriter.writerow(header)
            for i in data:
                s = list(i.values())
                l = [s[0], s[1], s[2]["x"], s[2]["y"], s[3]["x"], s[3]["y"]]
                csvwriter.writerow(l)

            image_data.close()


if __name__=="__main__":
    in_dir_path=input("enter input directory path where images are stored")
    out_dir_path=input("enter output directory path where csv file will be stored")
    fun(in_dir_path,out_dir_path)




