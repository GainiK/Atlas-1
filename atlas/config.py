# Copyright 2020 Magic Leap, Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#  Originating Author: Zak Murez (zak.murez.com)

import argparse
from fvcore.common.config import CfgNode as _CfgNode



def convert_to_dict(cfg_node, key_list=[]):
    """ Convert a config node to dictionary """
    _VALID_TYPES = {tuple, list, str, int, float, bool}
    if not isinstance(cfg_node, _CfgNode):
        if type(cfg_node) not in _VALID_TYPES:
            print("Key {} with value {} is not a valid type; valid types: {}".format(
                ".".join(key_list), type(cfg_node), _VALID_TYPES), )
        return cfg_node
    else:
        cfg_dict = dict(cfg_node)
        for k, v in cfg_dict.items():
            cfg_dict[k] = convert_to_dict(v, key_list + [k])
        return cfg_dict 

class CfgNode(_CfgNode):
    """Remove once  https://github.com/rbgirshick/yacs/issues/19 is merged"""
    def convert_to_dict(self):
        return convert_to_dict(self)

CN = CfgNode


_C = CN()
_C.LOG_DIR = "logs_atlas_cleargrasp"
_C.VOXEL_SIZE = 0.003125
_C.VOXEL_DIM_TRAIN = [128, 128, 64]
_C.VOXEL_DIM_VAL = [128, 128, 64]
_C.VOXEL_DIM_TEST = [128, 128, 64]

_C.DATASETS_TRAIN = ['/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0000/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0001/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0002/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0003/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0004/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0005/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0006/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0007/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0008/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0009/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0010/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0011/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0012/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0013/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0014/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0015/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0016/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0017/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0018/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0019/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0020/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0021/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0022/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0023/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0024/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0025/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0026/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0027/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0028/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0029/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0030/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0031/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0032/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0033/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0034/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0035/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0036/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0037/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0038/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0039/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0040/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0041/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0042/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0043/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0044/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0045/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0046/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0047/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0048/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0049/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0050/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0051/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0052/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0053/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0054/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0055/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0056/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0057/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0058/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0059/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0060/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0061/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0062/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0063/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0064/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0065/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0066/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0067/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0068/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0069/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0070/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0071/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0072/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0073/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0074/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0075/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0076/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0077/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0078/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0079/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0080/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0081/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0082/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0083/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0084/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0085/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0086/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0087/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0088/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0089/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0090/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0091/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0092/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0093/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0094/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0095/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0096/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0097/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0098/info.json',
                     '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans/scene0099/info.json']

_C.DATASETS_VAL = ['/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans_test/scene0100/info.json',
                   '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans_test/scene0101/info.json',
                   '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans_test/scene0102/info.json',
                   '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans_test/scene0103/info.json',
                   '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans_test/scene0104/info.json',
                   '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans_test/scene0105/info.json',
                   '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans_test/scene0106/info.json',
                   '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans_test/scene0107/info.json',
                   '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans_test/scene0108/info.json',
                   '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans_test/scene0109/info.json',
                   '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans_test/scene0110/info.json',
                   '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans_test/scene0111/info.json',
                   '/home/gaini/scannet_cleargrasp/prepared_data/scannet/scans_test/scene0112/info.json']


_C.DATA = CN()
_C.DATA.BATCH_SIZE_TRAIN = 1 # batch size per gpu
_C.DATA.NUM_FRAMES_TRAIN = 8
_C.DATA.NUM_FRAMES_VAL = 8
_C.DATA.FRAME_SELECTION = 'random'
_C.DATA.RANDOM_ROTATION_3D = True
_C.DATA.RANDOM_TRANSLATION_3D = True
_C.DATA.PAD_XY_3D = 1.
_C.DATA.PAD_Z_3D = .25

_C.TRAINER = CN()
_C.TRAINER.NAME = "atlas"
_C.TRAINER.VERSION = "default"
_C.TRAINER.NUM_GPUS = 1
_C.TRAINER.PRECISION = 16 # 16bit of 32bit
_C.TRAINER.BATCH_BACKBONE2D_TIME = True
_C.TRAINER.FINETUNE3D = False
_C.TRAINER.CHECKPOINT_PERIOD = 20

_C.OPTIMIZER = CN()
_C.OPTIMIZER.TYPE = "Adam"
_C.OPTIMIZER.ADAM = CN()
_C.OPTIMIZER.ADAM.LR = 5e-4
_C.OPTIMIZER.BACKBONE2D_LR_FACTOR = 1.
_C.SCHEDULER = CN()
_C.SCHEDULER.TYPE = "StepLR"
_C.SCHEDULER.STEP_LR = CN()
_C.SCHEDULER.STEP_LR.STEP_SIZE = 300 #200
_C.SCHEDULER.STEP_LR.GAMMA = .1


_C.MODEL = CN()
#TODO: images are currently loaded RGB, but the pretrained models expect BGR
_C.MODEL.PIXEL_MEAN = [103.53, 116.28, 123.675]
_C.MODEL.PIXEL_STD = [1., 1., 1.]

# for d2 backbone
_C.MODEL.BACKBONE = CN()
_C.MODEL.BACKBONE.NAME = "build_resnet_fpn_backbone"
_C.MODEL.BACKBONE.FREEZE_AT = 2
_C.MODEL.BACKBONE.WEIGHTS = "/home/gaini/Atlas/weights/R-50.pth" # pretrained weights
_C.MODEL.RESNETS = CN()
_C.MODEL.RESNETS.DEPTH = 50
_C.MODEL.RESNETS.OUT_FEATURES = ["res2", "res3", "res4", "res5"]
_C.MODEL.RESNETS.NUM_GROUPS = 1
_C.MODEL.RESNETS.NORM = "nnSyncBN"
_C.MODEL.RESNETS.WIDTH_PER_GROUP = 64
_C.MODEL.RESNETS.STRIDE_IN_1X1 = True
_C.MODEL.RESNETS.RES5_DILATION = 1
_C.MODEL.RESNETS.RES2_OUT_CHANNELS = 256
_C.MODEL.RESNETS.STEM_OUT_CHANNELS = 64
_C.MODEL.RESNETS.DEFORM_ON_PER_STAGE = [False, False, False, False]
_C.MODEL.RESNETS.DEFORM_MODULATED = False
_C.MODEL.RESNETS.DEFORM_NUM_GROUPS = 1
_C.MODEL.FPN = CN()
_C.MODEL.FPN.IN_FEATURES = ["res2", "res3", "res4", "res5"]
_C.MODEL.FPN.OUT_CHANNELS = 256
_C.MODEL.FPN.NORM = "nnSyncBN"
_C.MODEL.FPN.FUSE_TYPE = "sum"

_C.MODEL.BACKBONE3D = CN()
_C.MODEL.BACKBONE3D.CHANNELS = [32, 64, 128, 256]
_C.MODEL.BACKBONE3D.LAYERS_DOWN = [1, 2, 3, 4]
_C.MODEL.BACKBONE3D.LAYERS = [3, 2, 1]
_C.MODEL.BACKBONE3D.NORM = "nnSyncBN"
_C.MODEL.BACKBONE3D.DROP = 0.
_C.MODEL.BACKBONE3D.CONDITIONAL_SKIP = False

_C.MODEL.HEADS2D = CN()
_C.MODEL.HEADS2D.HEADS = [""]
_C.MODEL.HEADS2D.SEMSEG = CN()
_C.MODEL.HEADS2D.SEMSEG.NUM_CLASSES = 41
_C.MODEL.HEADS2D.SEMSEG.LOSS_WEIGHT = 1.

_C.MODEL.HEADS3D = CN()
_C.MODEL.HEADS3D.HEADS = ["tsdf"]
_C.MODEL.HEADS3D.MULTI_SCALE = True
_C.MODEL.HEADS3D.TSDF = CN()
_C.MODEL.HEADS3D.TSDF.LOSS_WEIGHT = 1.
_C.MODEL.HEADS3D.TSDF.LABEL_SMOOTHING = 1.05
_C.MODEL.HEADS3D.TSDF.LOSS_SPLIT = 'pred'
_C.MODEL.HEADS3D.TSDF.LOSS_LOG_TRANSFORM = True
_C.MODEL.HEADS3D.TSDF.LOSS_LOG_TRANSFORM_SHIFT = 1.0
_C.MODEL.HEADS3D.TSDF.SPARSE_THRESHOLD = [.99, .99, .99]
_C.MODEL.HEADS3D.SEMSEG = CN()
_C.MODEL.HEADS3D.SEMSEG.NUM_CLASSES = 41
_C.MODEL.HEADS3D.SEMSEG.LOSS_WEIGHT = .05
_C.MODEL.HEADS3D.COLOR = CN()
_C.MODEL.HEADS3D.COLOR.LOSS_WEIGHT = 1.

def get_parser():
    parser = argparse.ArgumentParser(description="Atlas Training")
    parser.add_argument("--config-file", default="", metavar="FILE", 
        help="path to config file")
    parser.add_argument(
        "opts",
        help="Modify config options using the command-line",
        default=None,
        nargs=argparse.REMAINDER,
    )
    return parser

def get_cfg(args):
    cfg = _C.clone()
    if args.config_file:
        cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    cfg.freeze()
    return cfg

