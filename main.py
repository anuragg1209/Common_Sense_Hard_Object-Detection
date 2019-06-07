from subprocess import Popen, PIPE

import argparse

def invoke_scripts(args):

    p0 = Popen(['python', 'Download_Images.py', '--download', f'{args.image_search_term}', '--output_dir', f'{args.image_output_dir}'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out0, err0 = p0.communicate()
    print(f"working0 with err {err0} and\n output {out0}")

    p1 = Popen(['python', 'json_to_csv.py', '--input_dir', f'{args.image_output_dir}', '--output_dir', f'{args.yolo_output_dir}', '--yolo_dir', f'{args.yolo_dir}'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out1, err1 = p1.communicate()
    print(f"working1 with err {err1} and\n output {out1}")

    p2 = Popen(['python', 'CollocationDetector.py', '--input_dir', f'{args.yolo_output_dir}', '--output_dir', f'{args.collocations_output_dir}'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out2, err2 = p2.communicate()
    print(f"working1 with err {err2} and\n output {out2}")


if __name__ == '__main__':
    # image_search_term
    # image_output_dir
    # yolo_output_dir
    # yolo_dir
    # collocations_output_dir

    parser = argparse.ArgumentParser(description='End to end script',
                                     usage="\n\npython main.py"
                                           "\t --image_output_dir "
                                           "\t --yolo_output_dir "
                                           "\t --yolo_dir "
                                           "\t --image_search_term"
                                           "\t --collocations_output_dir")

    parser.add_argument('--image_search_term',
                        action='store',
                        dest='image_search_term',
                        required=True,
                        help='Collect images using this search term e.g., kids on boat')

    parser.add_argument('--image_output_dir',
                        action='store',
                        dest='image_output_dir',
                        default='/Images/',
                        required=False,
                        help='Image output directory location')
    parser.add_argument('--yolo_output_dir',
                        action='store',
                        dest='yolo_output_dir',
                        default='/csv_files/',
                        required=False,
                        help='csv files output directory location')
    parser.add_argument('--yolo_dir',
                        action='store',
                        dest='yolo_dir',
                        default='C:/Users/sony/Downloads/darkflow-master/darkflow-master/',
                        required=False,
                        help='Yolo v2 directory location')
    parser.add_argument('--collocations_output_dir',
                        action='store',
                        dest='collocations_output_dir',
                        default='/tsv_files/',
                        required=False,
                        help='Collocations_map output directory location')
    args = parser.parse_args()
    invoke_scripts(args=args)

