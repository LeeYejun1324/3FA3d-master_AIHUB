import os
import shutil
import json
import numpy

root = '../datasets/084.강건한(Robust) 융합 센서 객체 인식 자율주행 데이터/01.데이터/1.Training/'
source_dir = '원천데이터/'
label_dir = '라벨링데이터/'
save_dir = 'NEW_DATASET/training/'

l_sub_dir = 'TL12_3D BB_주간_맑음_8. 자동차전용도로/1. 주간/1. 맑음/8. 자동차전용도로/'
s_sub_dir = 'TS12_3D BB_주간_맑음_8. 자동차전용도로/1. 주간/1. 맑음/8. 자동차전용도로/'

# lidar # label = [front_left, front_right, roof] / source = [total]
lidar_dir = 'lidar/'
camera_dir = 'camera/front/'
calib_dir = 'calib/front/'

## lidar label processing
count = 0

temp_root = root+label_dir+l_sub_dir

for outer in os.listdir(temp_root):
    sub_folder_fleft = os.path.join(temp_root, outer, lidar_dir+'front_left\\')
    sub_folder_fright = os.path.join(temp_root, outer, lidar_dir+'front_right\\')
    sub_folder_roof = os.path.join(temp_root, outer, lidar_dir+'roof\\')

    for inner in os.listdir(sub_folder_roof.replace('/','\\')):
        total_info_list = []
       
        with open(sub_folder_fleft+inner,'r') as fleft:
            fleft_info = json.load(fleft)
            for i in range(len(fleft_info['annotations'])):
                part_info_list = []

                fleft_info['annotations'][i]['3dbbox.category'] = fleft_info['annotations'][i]['3dbbox.category'].replace('other vehicles','other_vehicles')

                part_info_list.append(str(fleft_info['annotations'][i]['3dbbox.category']))
                part_info_list.append(str(fleft_info['annotations'][i]['3dbbox.location'][0]))
                part_info_list.append(str(fleft_info['annotations'][i]['3dbbox.location'][1]))
                part_info_list.append(str(fleft_info['annotations'][i]['3dbbox.location'][2]))
                part_info_list.append(str(fleft_info['annotations'][i]['3dbbox.dimension'][0]))
                part_info_list.append(str(fleft_info['annotations'][i]['3dbbox.dimension'][1]))
                part_info_list.append(str(fleft_info['annotations'][i]['3dbbox.dimension'][2]))
                part_info_list.append(str(fleft_info['annotations'][i]['3dbbox.rotation_y']))
                total_info_list.append(part_info_list)
            
        with open(sub_folder_fright+inner,'r') as fright:
            fright_info = json.load(fright)
            for i in range(len(fright_info['annotations'])):
                part_info_list = []

                fright_info['annotations'][i]['3dbbox.category'] = fright_info['annotations'][i]['3dbbox.category'].replace('other vehicles','other_vehicles')

                part_info_list.append(str(fright_info['annotations'][i]['3dbbox.category']))
                part_info_list.append(str(fright_info['annotations'][i]['3dbbox.location'][0]))
                part_info_list.append(str(fright_info['annotations'][i]['3dbbox.location'][1]))
                part_info_list.append(str(fright_info['annotations'][i]['3dbbox.location'][2]))
                part_info_list.append(str(fright_info['annotations'][i]['3dbbox.dimension'][0]))
                part_info_list.append(str(fright_info['annotations'][i]['3dbbox.dimension'][1]))
                part_info_list.append(str(fright_info['annotations'][i]['3dbbox.dimension'][2]))
                part_info_list.append(str(fright_info['annotations'][i]['3dbbox.rotation_y']))
                total_info_list.append(part_info_list)

        with open(sub_folder_roof+inner,'r') as roof:
            roof_info = json.load(roof)
            for i in range(len(roof_info['annotations'])):
                part_info_list = []

                roof_info['annotations'][i]['3dbbox.category'] = roof_info['annotations'][i]['3dbbox.category'].replace('other vehicles','other_vehicles')

                part_info_list.append(str(roof_info['annotations'][i]['3dbbox.category']))
                part_info_list.append(str(roof_info['annotations'][i]['3dbbox.location'][0]))
                part_info_list.append(str(roof_info['annotations'][i]['3dbbox.location'][1]))
                part_info_list.append(str(roof_info['annotations'][i]['3dbbox.location'][2]))
                part_info_list.append(str(roof_info['annotations'][i]['3dbbox.dimension'][0]))
                part_info_list.append(str(roof_info['annotations'][i]['3dbbox.dimension'][1]))
                part_info_list.append(str(roof_info['annotations'][i]['3dbbox.dimension'][2]))
                part_info_list.append(str(roof_info['annotations'][i]['3dbbox.rotation_y']))
                total_info_list.append(part_info_list)

        with open(root+save_dir+'label_2\\{:06d}.txt'.format(count),'w') as txt_file:
            for idx, i in enumerate(total_info_list):
                if idx+1 < len(total_info_list):
                    txt_file.write(' '.join(i) + "\n")
                else:
                    txt_file.write(' '.join(i))

## lidar source processing
        inner_file_name = inner[:-5]
        
        lidar_source_exist = root+source_dir+s_sub_dir+outer+'/'+lidar_dir+'total/'+inner_file_name+'.bin'
        lidar_source_exist = lidar_source_exist.replace('/','\\')

        lidar_source_move_to = root+save_dir+'velodyne/'+'{:06d}.bin'.format(count)
        lidar_source_move_to = lidar_source_move_to.replace('/','\\')
        
        shutil.copy(lidar_source_exist, lidar_source_move_to)
        

## camera source processing
        camera_source_exist = root+source_dir+s_sub_dir+outer+'/'+camera_dir+inner_file_name+'.jpg'
        camera_source_exist = camera_source_exist.replace('/','\\')

        camera_source_move_to = root+save_dir+'image_2/'+'{:06d}.jpg'.format(count)
        camera_source_move_to = camera_source_move_to.replace('/','\\')

        shutil.copy(camera_source_exist, camera_source_move_to)
        

## calib source processing
        calib_source_exist = root+source_dir+s_sub_dir+outer+'/'+calib_dir+inner_file_name+'.txt'
        calib_source_exist = calib_source_exist.replace('/','\\')

        calib_source_move_to = root+save_dir+'calib/'+'{:06d}.txt'.format(count)
        calib_source_move_to = calib_source_move_to.replace('/','\\')

        shutil.copy(calib_source_exist, calib_source_move_to)

                    
        count += 1

