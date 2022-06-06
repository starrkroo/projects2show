#!/usr/bin/env python3

from PIL import Image
from huepy import *

def resize_image(input_image_path, output_image_path, size):
  original_image = Image.open(input_image_path)
  width, height = original_image.size

  print(orange('From:'))
  print('x = {}\ny = {}\n'.format(width, height))

  resized_image = original_image.resize(size)
  width, height = resized_image.size
  
  print(green("To: "))
  print('x = {}\ny = {}'.format(width, height))
  resized_image.show()
  resized_image.save(output_image_path)

if __name__ == '__main__':
  resize_image('example.jpg', 'example.jpg', (1280, 720))
