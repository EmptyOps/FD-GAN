from __future__ import print_function, absolute_import
import os.path as osp

from ..utils.data import Dataset
from ..utils.osutils import mkdir_if_missing
from ..utils.serialization import write_json


class Market1501(Dataset):

    def __init__(self, root, split_id=0, num_val=100, truncate=-1):
        super(Market1501, self).__init__(root, split_id=split_id, truncate=truncate)

        if not self._check_integrity():
            raise RuntimeError("Dataset not found or corrupted. " +
                               "Please follow README.md to prepare Market1501 dataset.")

        self.load(num_val)
