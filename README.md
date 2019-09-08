# Common_Sense_Hard_Object-Detection

Step1 ==> Run flask_app.py on local host which takes a query as input from the user and after that it calls "main.py"script.

Now a home page UI is displayed on the browser showing all the 3 output files generated(collocations_map,inverted_index,error_set).

main.py script invokes "Image_download.py" ,"json_to_csv.py" , "CollocationsDetector.py" and "Checkin_csk.py" respectively.
Make sure that all the directory paths are provided correctly in the "main.py" and other scripts.
