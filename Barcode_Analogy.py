import numpy as np
import cv2

def Barcode_heatmap_totalviolations(start_frame,end_frame,Total_violations_result,individual_barcode_width,barcode_height,barcode_savepath):
    color_lut = [(123,190,99),(125,200,133),(127,210,168),(129,220,203),(131,230,237),
                 (130,221,255),(124,192,253),(119,163,252),(113,134,250),(107,105,248)] #LUT for colors assignment for final barcode

    Total_violations_sublist = Total_violations_result[start_frame:end_frame]    # Take sublist from from start to end frame you need to analyze

    max_val = max(Total_violations_sublist)
    print("Total people at risk sublist :")
    print(Total_violations_sublist)
    print("Total people at risk Max_val: " + str(max_val))                          # print max value in sublist aquired.

    barcode_data = []
    for index in range(len(Total_violations_sublist)):
        value = Total_violations_sublist[index]
        num = int((value / max_val) * 100)            # Values normalization within sublist taken.
        quotient = int(num / 10)                      # Scaling the values to 1 - 10 for colors assignment.
        if quotient == 10:
            quotient = 9
        color = color_lut[quotient]
        barcode_data.append(color)                    # Assign the color based on severity of the number.

    # grab the individual bar width and allocate memory for the barcode visualization
    barcode = np.zeros((barcode_height, len(barcode_data) * individual_barcode_width, 3), dtype="uint8")

    # loop over the averages and create a single 'bar' for
    # each frame average in the list
    for (i, avg) in enumerate(barcode_data):
        cv2.rectangle(barcode, (i * individual_barcode_width, 0),
                      (((i + 1) * individual_barcode_width)-1, barcode_height-1), avg, -1)

    return barcode                                   # return the barcode image for further processing

def Barcode_heatmap_totalpeople(start_frame,end_frame,totalpeople,individual_barcode_width,barcode_height,barcode_savepath):
    color_lut = [(123,190,99),(125,200,133),(127,210,168),(129,220,203),(131,230,237),
                 (130,221,255),(124,192,253),(119,163,252),(113,134,250),(107,105,248)]

    Total_violations_sublist = totalpeople[start_frame:end_frame]
    print("\n")
    print("Total People sublist :")
    print(Total_violations_sublist)
    max_val = max(Total_violations_sublist)
    print("Total people Max_val: " + str(max_val))


    barcode_data = []

    for index in range(len(Total_violations_sublist)):
        value = Total_violations_sublist[index]
        num = int((value / max_val) * 100)
        quotient = int(num / 10)
        if quotient == 10:
            quotient = 9
        color = color_lut[quotient]
        barcode_data.append(color)

    # grab the individual bar width and allocate memory for the barcode visualization
    barcode = np.zeros((barcode_height, len(barcode_data) * individual_barcode_width, 3), dtype="uint8")

    # loop over the averages and create a single 'bar' for
    # each frame average in the list
    for (i, avg) in enumerate(barcode_data):
        cv2.rectangle(barcode, (i * individual_barcode_width, 0),
                      (((i + 1) * individual_barcode_width)-1, barcode_height-1), avg, -1)

    #cv2.imwrite(barcode_savepath,barcode)
    return barcode


def Barcode_heatmap_averageIntensity(start_frame,end_frame,avg_intensity,
                                     individual_barcode_width,barcode_height,
                                     barcode_savepath):
    Avg_intesnity_sublist = avg_intensity[start_frame:end_frame]

    barcode_data = []
    for index in range(len(Avg_intesnity_sublist)):
        value = Avg_intesnity_sublist[index]
        barcode_data.append(value)

    # grab the individual bar width and allocate memory for the barcode visualization
    barcode = np.zeros((barcode_height, len(barcode_data) * individual_barcode_width, 3),
                       dtype="uint8")

    # loop over the averages and create a single 'bar' for
    # each frame average in the list
    for (i, avg) in enumerate(barcode_data):
        cv2.rectangle(barcode, (i * individual_barcode_width, 0),
                      (((i + 1) * individual_barcode_width)-1, barcode_height-1), avg, -1)

    return barcode

def Barcode_heatmap_RAMpercent(start_frame,end_frame,RAMData_list,
                               individual_barcode_width,barcode_height,
                               barcode_savepath):
    color_lut = [(123, 190, 99), (125, 200, 133), (127, 210, 168), (129, 220, 203), (131, 230, 237),
                 (130, 221, 255), (124, 192, 253), (119, 163, 252), (113, 134, 250), (107, 105, 248)]

    RAM_Data_sublist = RAMData_list[start_frame:end_frame]

    barcode_data = []
    for index in range(len(RAM_Data_sublist)):
        value = RAM_Data_sublist[index]
        num = int(value)
        quotient = int(num / 10)
        if quotient == 10:
            quotient = 9

        color = color_lut[quotient]
        barcode_data.append(color)

    # grab the individual bar width and allocate memory for the barcode visualization
    barcode = np.zeros((barcode_height, len(barcode_data) * individual_barcode_width, 3), dtype="uint8")

    # loop over the averages and create a single 'bar' for
    # each frame average in the list
    for (i, avg) in enumerate(barcode_data):
        cv2.rectangle(barcode, (i * individual_barcode_width, 0),
                      (((i + 1) * individual_barcode_width)-1, barcode_height-1), avg, -1)

    #cv2.imwrite(barcode_savepath,barcode)
    return barcode


def Barcode_heatmap_CPUUtilization(start_frame,end_frame,Data_list,individual_barcode_width,barcode_height,barcode_savepath):
    color_lut = [(123, 190, 99), (125, 200, 133), (127, 210, 168), (129, 220, 203), (131, 230, 237),
                 (130, 221, 255), (124, 192, 253), (119, 163, 252), (113, 134, 250), (107, 105, 248)]

    Data_sublist = Data_list[start_frame:end_frame]
    #Data_sublist = [16.7, 0.0, 25.0, 22.2, 0.0, 0.0, 12.5, 0.0, 0.0, 0.0, 27.0, 10.0, 20.0, 15.0, 22.0]
    print("\n")
    print("Total CPU Utilization Sublist :")
    print(Data_sublist)
    max_val = max(Data_sublist)
    print("CPU Utilization Max_val: " + str(max_val))

    barcode_data = []

    for index in range(len(Data_sublist)):
        value = Data_sublist[index]
        num = int(value)
        quotient = int(num / 10)
        if quotient == 10:
            quotient = 9

        color = color_lut[quotient]
        barcode_data.append(color)

    # grab the individual bar width and allocate memory for the barcode visualization
    barcode = np.zeros((barcode_height, len(barcode_data) * individual_barcode_width, 3), dtype="uint8")

    # loop over the averages and create a single 'bar' for
    # each frame average in the list
    for (i, avg) in enumerate(barcode_data):
        cv2.rectangle(barcode, (i * individual_barcode_width, 0),
                      (((i + 1) * individual_barcode_width)-1, barcode_height-1), avg, -1)

    #cv2.imwrite(barcode_savepath,barcode)
    return barcode

def concateimages(image1,image2,image3,image4,image5,savepath):
    result1 = cv2.vconcat([image1, image2])
    result2 = cv2.vconcat([result1, image3])
    result3 = cv2.vconcat([result2, image4])
    result = cv2.vconcat([result3, image5])
    cv2.imwrite(savepath,result)