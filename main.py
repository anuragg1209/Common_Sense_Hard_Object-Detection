import subprocess

def invoke_scripts(search):
    arg = f"python Download_Images.py --query {search}"
    print("working")
    subprocess.call(arg, shell=True)
    arg1 = "python json_to_csv.py"
    subprocess.call(arg1, shell=True)
    arg2 = "python CollocationDetector.py"
    subprocess.call(arg2, shell=True)

