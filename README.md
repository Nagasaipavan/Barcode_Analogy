# Barcode_Analogy

For visualizing data, we have many options, like Line chart, Pie graphs, etc.
If we want to analyze data from our algorithm, we generally log the output variables into CSV files.

Now, here "Barcode_Analogy" introduces new a new way of representation using barcode analogy.

Generally, in Barcode, there will be machine readable information. But in this project,each strip of barcode is each processed frame output parameter.

Eg: I used Social distcaning(SD) algorithm as example here.
Total number of people in frame is one of the output paramter of algorithm.
For a video with 15 frames, total number of people in each frame will be captured into list like this- [4,5,2,3,5,5,2,5,7,6,5,5,7,5,6]
So, now, this list will be normalized with max value, and scale them to 0-9 and assign colors to each strip(From Green to Yellow) based on its severity.

This way, one barcode image will be generated. We can follow similar process for differnet algorithm output parameters, vertically concatinate these barcodes and can be compared for data of any size.

The SD algorithm uses YOLOv3.Weights for YOLOv3 were availablein this link: https://pjreddie.com/media/files/yolov3.weights
Download them and place it in "yolo-coco" folder.

Open Pycharm, open socialDistanceDashboard.py file, change the videoname at filename variable., and we are ready to run.
