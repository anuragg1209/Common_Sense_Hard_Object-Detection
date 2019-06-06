# Common_Sense_Hard_Object-Detection

Step1=> Run Download_Image.py which takes a query and dir path as input and stores the images in the provided dir path.
Step2=> Run json_to_csv.py which takes 3 inputs(input_dir path,output_dir path, yolo_dir).This script will perform object detection
        using Yolo v2 and converts the output json files to csv files. csv files will be stored in output_dir.
Step3=>Run CollocationsDetector.py which will form collocations_map and invertedindex and stores both of them in a separate tsv files.
Step4=>(optional)main.py will invoke above 3 scripts in sequence.This step is to be performed if above 3 steps not done.
Step5=>Run flask1.py, contains the flask app which displays the collocations_map on UI. flask1.py requires 3 html files(hello.html,
        index.html,analysis.html). Index.html uses style.css file. 
        
