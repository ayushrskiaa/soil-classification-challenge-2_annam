"""
Author: Annam.ai IIT Ropar
Team Name: KrishiSetu
Team Members: Dnyandeep Chute,Ayush Kumar, Suyash Mishra, Krish Kalgude, Yash Verma


"""

# Here you add all the preprocessing related details for the task completed from Kaggle.

import os
from PIL import Image
import torch
from torch.utils.data import Dataset

label_map = {
    'Alluvial soil': 0,
    'Black Soil': 1,
    'Clay soil': 2,
    'Red soil': 3
}

inv_label_map = {v: k for k, v in label_map.items()}


class SoilDataset(Dataset):
    def __init__(self, df, image_dir, transform=None, is_test=False):
        self.df = df
        self.image_dir = image_dir
        self.transform = transform
        self.is_test = is_test

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        image_id = self.df.iloc[idx]['image_id']
        image_path = os.path.join(self.image_dir, image_id)

        image = Image.open(image_path).convert('RGB')
        if self.transform:
            image = self.transform(image)

        if self.is_test:
            return image, image_id
        else:
            label = label_map[self.df.iloc[idx]['soil_type']]
            return image, label
