{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import tensorflow as tf\
from tensorflow.keras import layers, models\
\
class CaptchaModel:\
    def __init__(self, num_chars, seq_length):\
        self.num_chars = num_chars\
        self.seq_length = seq_length\
        \
    def build_model(self):\
        input_img = layers.Input(shape=(50, 200, 3))\
        \
        x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(input_img)\
        x = layers.MaxPooling2D((2, 2))(x)\
        \
        x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)\
        x = layers.MaxPooling2D((2, 2))(x)\
        \
        x = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)\
        x = layers.BatchNormalization()(x)\
        x = layers.MaxPooling2D((2, 2))(x)\
        \
        x = layers.Flatten()(x)\
        x = layers.Dense(256, activation='relu')(x)\
        x = layers.Dropout(0.3)(x)\
        x = layers.Dense(128, activation='relu')(x)\
        x = layers.Dropout(0.3)(x)\
        \
        outputs = []\
        for _ in range(self.seq_length):\
            output = layers.Dense(self.num_chars, activation='softmax')(x)\
            outputs.append(output)\
        \
        model = models.Model(inputs=input_img, outputs=outputs)\
        \
        model.compile(\
            optimizer='adam',\
            loss='categorical_crossentropy',\
            metrics=['accuracy']\
        )\
        \
        return model}
