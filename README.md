# Barcode_Analogy

For visualizing data, we have many options, like Line chart, Pie graphs, etc.
If we want to analyze data from our algorithm, we generally log the output variables into CSV files.

Now, here "Barcode_Analogy" introduces new a new way of representation of algorithm data using barcode analogy.

Generally, in Barcode, there will be machine readable information. But in this project,each strip of barcode is each processed frame output parameter.(doesnt contain any machine readable info)
you can refer the idea in detail by following this link:

Overall concept is as below.

For any algorithm we develop, we have a specific set of output parameters to analyze/compare. Here in this idea,
1. We collect those output parameters and create barcode image for each output parameter.
2. Combine these barcode images vertically.
3. Compare and analyse the concatinated image for further derivations from algorithm.

Before we start running code, download Yolov3 weights from this link: https://pjreddie.com/media/files/yolov3.weights
Place those weights file in "yolo-coco" folder. 

## Procedure to run:

1. Download the code and change the directory to place where code is downloded.

2. Execute command: 
   ###### python socialDistanceDashboard.py --videoname="Enter video name"
   
   There were other two paramters - each_strip_width,each_strip_height. Those were optional. if not passed from command line, they were taken 5 and 50 respectievely.
   
After successful execution of code, the concatinated barcode image will be saved in current directory with name **"ConcateImage.bmp"**
Output video file of algorithm also will be saved into currrent directory with name **"Output.avi"**
