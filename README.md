# Super Fast and Accurate 3D Object Detection based on 3D LiDAR Point Clouds (SFA3D) 

ADD Aihub data processing version!! It is 'Not' my own project
[Original Code link](https://github.com/maudzung/SFA3D/tree/master)
[Used dataset link](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=629)

[![python-image]][python-url]
[![pytorch-image]][pytorch-url]

---

## 2. Getting Started
### 2.1. Requirement

The instructions for setting up a virtual environment is [here](https://github.com/maudzung/virtual_environment_python3).

```shell script
git clone https://github.com/maudzung/SFA3D.git SFA3D
cd SFA3D/
pip install -r requirements.txt
```

### 2.2. Data Preparation
Download the AIHub dataset from [here](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=629)

The downloaded data includes:

(Training)원천데이터 + 라벨링데이터

(Testing)원천데이터 / if you need. this code only using Training data for simple implementation.

Please make sure that you construct the source code & dataset directories structure as below.

### 2.3. How to run

#### 2.3.0 converting AIHub dataset to kitti dataset format

To convert AIHub data to KITTI data format

Warning : you should check your data root and change the directory!!
this code is not supporting for linking directory.

```shell script
cd sfa/data_process/
python data_processing.py
```

then the AIHub dataset is converted to KITTI dataset format


#### 2.3.1. Visualize the dataset 

To visualize 3D point clouds with 3D boxes, let's execute:

```shell script
cd sfa/data_process/
python kitti_dataset.py
```

#### 2.3.2. Inference

The pre-trained model was pushed to this repo.

```
python test.py --gpu_idx 0 --peak_thresh 0.2
```

#### 2.3.3. Making demonstration

```
python demo_2_sides.py --gpu_idx 0 --peak_thresh 0.2
```

The data for the demonstration will be automatically downloaded by executing the above command.


#### 2.3.4. Training

##### 2.3.4.1. Single machine, single gpu

```shell script
python train.py --gpu_idx 0
```

##### 2.3.4.2. Distributed Data Parallel Training
- **Single machine (node), multiple GPUs**

```
python train.py --multiprocessing-distributed --world-size 1 --rank 0 --batch_size 64 --num_workers 8
```

- **Two machines (two nodes), multiple GPUs**

   - _**First machine**_
    ```
    python train.py --dist-url 'tcp://IP_OF_NODE1:FREEPORT' --multiprocessing-distributed --world-size 2 --rank 0 --batch_size 64 --num_workers 8
    ```

   - _**Second machine**_
    ```
    python train.py --dist-url 'tcp://IP_OF_NODE2:FREEPORT' --multiprocessing-distributed --world-size 2 --rank 1 --batch_size 64 --num_workers 8
    ```

## Folder structure

```
${ROOT}
└── checkpoints/
    ├── fpn_resnet_18/    
        ├── fpn_resnet_18_epoch_300.pth
└── dataset/    
    └── kitti/
        ├──ImageSets/
        │   ├── test.txt
        │   ├── train.txt
        │   └── val.txt
        ├── training/
        │   ├── image_2/ (left color camera)
        │   ├── calib/
        │   ├── label_2/
        │   └── velodyne/
        └── testing/  
        │   ├── image_2/ (left color camera)
        │   ├── calib/
        │   └── velodyne/
        └── classes_names.txt
└── sfa/
    ├── config/
    │   ├── train_config.py
    │   └── kitti_config.py
    ├── data_process/
    │   ├── kitti_dataloader.py
    │   ├── kitti_dataset.py
    │   └── kitti_data_utils.py
    ├── models/
    │   ├── fpn_resnet.py
    │   ├── resnet.py
    │   └── model_utils.py
    └── utils/
    │   ├── demo_utils.py
    │   ├── evaluation_utils.py
    │   ├── logger.py
    │   ├── misc.py
    │   ├── torch_utils.py
    │   ├── train_utils.py
    │   └── visualization_utils.py
    ├── demo_2_sides.py
    ├── demo_front.py
    ├── test.py
    └── train.py
├── README.md 
└── requirements.txt
```



[python-image]: https://img.shields.io/badge/Python-3.6-ff69b4.svg
[python-url]: https://www.python.org/
[pytorch-image]: https://img.shields.io/badge/PyTorch-1.5-2BAF2B.svg
[pytorch-url]: https://pytorch.org/
