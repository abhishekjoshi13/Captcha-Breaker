{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import tensorflow as tf\
import os\
import numpy as np\
from dataset import CaptchaDataset\
from model import CaptchaModel\
\
class CaptchaTrainer:\
    def __init__(self, data_dir, model_save_path='captcha_model.h5'):\
        self.data_dir = data_dir\
        self.model_save_path = model_save_path\
        self.dataset = CaptchaDataset(data_dir)\
        \
    def prepare_data(self):\
        self.dataset.load_dataset()\
        if len(self.dataset.images) == 0:\
            raise ValueError("No training data found. Please generate CAPTCHA images first.")\
        train_data, val_data = self.dataset.split_data()\
        return train_data, val_data\
    \
    def train(self, epochs=30, batch_size=16):\
        train_data, val_data = self.prepare_data()\
        \
        char_count = len(self.dataset.characters)\
        seq_len = self.dataset.sequence_length\
        \
        captcha_model = CaptchaModel(char_count, seq_len)\
        model = captcha_model.build_model()\
        \
        print("Starting training...")\
        print(f"Training samples: \{len(self.dataset.images)\}")\
        print(f"Character set: \{self.dataset.characters\}")\
        \
        early_stop = tf.keras.callbacks.EarlyStopping(\
            monitor='val_loss',\
            patience=8,\
            restore_best_weights=True\
        )\
        \
        reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(\
            monitor='val_loss',\
            factor=0.2,\
            patience=5,\
            min_lr=0.0001\
        )\
        \
        history = model.fit(\
            train_data,\
            epochs=epochs,\
            batch_size=batch_size,\
            validation_data=val_data,\
            callbacks=[early_stop, reduce_lr],\
            verbose=1\
        )\
        \
        model.save(self.model_save_path)\
        print(f"Model saved as \{self.model_save_path\}")\
        \
        return history, model\
\
def main():\
    try:\
        trainer = CaptchaTrainer('captcha_images')\
        history, model = trainer.train(epochs=20)\
        print("Training completed successfully!")\
    except Exception as e:\
        print(f"Training failed: \{e\}")\
\
if __name__ == "__main__":\
    main()}
