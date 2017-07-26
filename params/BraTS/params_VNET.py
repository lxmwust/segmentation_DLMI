import params as p
from src.config import DB

# IMPORTANT! The criteria used to choose the parameters is that there are 3 samples of +/- per subject
# in every subepoch. There are 600 segments / subepoch.
# 1*5*20*100 = 10000 ( N_EXAMPLES_PER_CLASS * N_CLASSES * N_SUBEPOCHS * N_SUBJECTS_TRAIN = N_SEGMENTS_TRAIN )
def get_params():
    params = {
        p.DATABASE: DB.iSEG,
        p.INPUT_DIM: [224,224,160],

        p.N_CLASSES: 5,
        p.N_EPOCHS: 150,
        p.N_SUBEPOCHS: 1,
        p.BATCH_SIZE: 1,
        p.CLASS_WEIGHTS: 'inverse_weights',

        p.SAMPLING_SCHEME: 'whole',
        p.SAMPLING_WEIGHTS: [0.5, 0.5],
        p.N_SEGMENTS_TRAIN: 120,
        p.N_SUBJECTS_TRAIN: None,

        p.N_SEGMENTS_VALIDATION: 10,
        p.N_SUBJECTS_VALIDATION: None,

        p.TRAIN_SIZE: 0.6,
        p.DEV_SIZE: 0.4,

        p.DATA_AUGMENTATION_FLAG: False,
        p.NUM_MODALITIES: 4,

        p.BN_LAST: False,
        p.SHORTCUT_INPUT: False,

        p.OUTPUT_PATH: '/work/acasamitjana/segmentation/BraTS/VNet',
        p.MODEL_NAME: 'v_net',
        p.LR: 0.0005
    }

    return params
