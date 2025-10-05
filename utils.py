{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import random\
import string\
from PIL import Image, ImageDraw, ImageFont\
import os\
\
class CaptchaGenerator:\
    def __init__(self, width=200, height=50):\
        self.width = width\
        self.height = height\
        self.characters = string.ascii_uppercase + string.digits\
        self.sequence_length = 5\
        \
    def generate_random_text(self):\
        return ''.join(random.choices(self.characters, k=self.sequence_length))\
    \
    def add_noise(self, image):\
        draw = ImageDraw.Draw(image)\
        for _ in range(50):\
            x = random.randint(0, self.width)\
            y = random.randint(0, self.height)\
            draw.point((x, y), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))\
        return image\
    \
    def add_lines(self, image):\
        draw = ImageDraw.Draw(image)\
        for _ in range(2):\
            start_x = random.randint(0, self.width)\
            start_y = random.randint(0, self.height)\
            end_x = random.randint(0, self.width)\
            end_y = random.randint(0, self.height)\
            draw.line([(start_x, start_y), (end_x, end_y)], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=1)\
        return image\
    \
    def generate_captcha(self, save_dir='captcha_images', count=100):\
        if not os.path.exists(save_dir):\
            os.makedirs(save_dir)\
            \
        try:\
            font = ImageFont.truetype("Arial.ttf", 32)\
        except:\
            try:\
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)\
            except:\
                try:\
                    font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 32)\
                except:\
                    font = ImageFont.load_default()\
                    print("Using default font - CAPTCHAs may look different")\
        \
        print(f"Generating \{count\} CAPTCHA images...")\
        \
        for i in range(count):\
            text = self.generate_random_text()\
            image = Image.new('RGB', (self.width, self.height), color=(255, 255, 255))\
            draw = ImageDraw.Draw(image)\
            \
            x_pos = 10\
            for char in text:\
                draw.text((x_pos, 5), char, font=font, fill=(0, 0, 0))\
                x_pos += 35\
            \
            image = self.add_noise(image)\
            image = self.add_lines(image)\
            \
            filename = f"\{text\}.png"\
            filepath = os.path.join(save_dir, filename)\
            image.save(filepath)\
            \
        print(f"Generated \{count\} CAPTCHA images in \{save_dir\}")\
\
def create_sample_data():\
    generator = CaptchaGenerator()\
    generator.generate_captcha('captcha_images', 150)\
\
if __name__ == "__main__":\
    create_sample_data()}
