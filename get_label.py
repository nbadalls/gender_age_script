# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/minivision/.spyder2/.temp.py
Use to create label from landmark file
"""
import sys
import os

def getGenderSign(id_part):

	if id_part.find('.jpg') >=0:
		id_part = id_part.split('.jpg')[0]
	gender_sign = int(id_part[-2])
	
	if gender_sign %2 ==0:
		label = 0
	else:
		label = 1
	return label


#for pingtai data process
def Get_landmarks():
    landmark_path = sys.argv[1]
    file = open(landmark_path,"r")
    file_out = open("{}_label.txt".format(landmark_path.split('.txt')[0]), "w")
    
    lines = file.readlines();
    for line in lines:
        img_path = line.split(".jpg")[0] #/media/minivision/Elements/Image_data/gender_age_data/Second_batch/src_image/Glasses/blackFrame/0/032122198111082046.jpg
        img_name = os.path.basename(img_path)
	path_part = img_path.split('/')
        gender_label = path_part[-2] #0
        age = 2016-int(img_name[6:10])
        
        #judge age period  
        start_age = 16
        age_label = -1
        for i in xrange(5):
            if age >=start_age + i*10 and age <= start_age*(i+1)*10-1:
                    age_label = i
        if age_label ==-1:
                continue
        
        #judge label period
            
        #line_label = "{}.jpg {} {}\n".format(img_path,age_label, gender_label)
	line_label = "{}.jpg {} {} {}\n".format(img_path,age_label, age, gender_label)
        file_out.write(line_label)
   
#for hotel data process    
def GetlabelFromLandmark():
    landmark_path = sys.argv[1]
    file = open(landmark_path,"r")
    file_out = open("{}_label.txt".format(landmark_path.split('.txt')[0]), "w")
    
    lines = file.readlines();
    for line in lines:
        img_path = line.split(".jpg")[0] #/media/minivision/Elements/Image_data/gender_age_data/Second_batch/src_image/Glasses/blackFrame/0/032122198111082046.jpg
        img_name = os.path.basename(img_path)
		path_part = img_path.split('/')
       
		id_part = img_name.split('_')[-1]
        age = 2017-int(id_part[6:10])
		gender_label = getGenderSign(id_part) #0
        
        #judge age period  
        start_age = 16
        age_label = -1
        for i in xrange(5):
            if age >=start_age + i*10 and age <= start_age*(i+1)*10-1:
                    age_label = i
        if age_label ==-1:
                continue
        
        #judge label period
            
        #line_label = "{}.jpg {} {}\n".format(img_path,age_label, gender_label)
		line_label = "{}.jpg {} {} {}\n".format(img_path,age_label, age, gender_label)
        file_out.write(line_label)



        
if __name__ == '__main__':
    if len(sys.argv) <1:
	print ''' Usage: 
Input landmarkFilePath
'''
    else:
    	#GetlabelFromLandmark()
	Get_landmarks()
            
                
        
