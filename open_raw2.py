import cv2
import numpy as np
import os
# import imageio
# import rawpy

# def extract2(input_raw_file, output_jpg_file):
#     with rawpy.imread(input_raw_file) as raw:
#         # Process the RAW image data
#         rgb = raw.postprocess()
#         # Save the processed image as a JPEG file using imageio
#         imageio.imsave(output_jpg_file, rgb)

# # Define the path to the raw file
# image_path = "./Amplitude_frame.raw"
# # Create the output folder if it doesn't exist
# output_folder = "./"
def extract(image_path, output_folder):
    # Define the dimensions and data format of the .raw file
    width = 640
    height = 480
    bit_depth = 32  # Typically, 16-bit depth for depth data

    # Read the single .raw file
    with open(image_path, 'rb') as f:
        data = np.fromfile(f, np.uint16)  # Use np.uint8 for 8-bit depth

    # Reshape the data to match the dimensions
    data = data.reshape((height, width))
    # Optionally, normalize the data to 8-bit for display (adjust as needed)
    min_val = np.min(data)
    max_val = np.max(data)
    data = ((data - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    # Save the frame as a .jpg image
    # frame_filepath = os.path.join(output_folder, os.path.splitext(os.path.basename(image_path))[0]+'.jpg')
    frame_filepath = output_folder
    cv2.imwrite(frame_filepath, data)
    
    return frame_filepath


raw_folder = 'raw_imgs/'

raw_imgs_error = []

raw_list = os.listdir(raw_folder)
for rw in raw_list:
    for imgs in os.listdir(os.path.join(raw_folder, rw)):
        if os.path.splitext(imgs)[-1] == '.raw':
            input_raw_file = os.path.join(raw_folder, rw, imgs)
            # Open the RAW file
            try:
                file_prefix = '_'.join(rw.split('_')[3:])
                output_jpg_file = f'{file_prefix}_{os.path.splitext(imgs)[0]}.jpg'
                output_jpg_file = os.path.join('imgs', 'amp_'+file_prefix, output_jpg_file)
                
                if not os.path.exists('imgs/'):
                    os.mkdir('imgs/')
                if not os.path.exists('imgs/'+'amp_'+file_prefix):
                    os.mkdir('imgs/'+'amp_'+file_prefix)

                output_jpg_file = extract(input_raw_file, output_jpg_file)
                
                if os.path.exists(output_jpg_file):
                    print('file extracted:', output_jpg_file)
                else:
                    print('file not saved:', input_raw_file)
                    raw_imgs_error.append(input_raw_file)
            except Exception as e:
                print('extracted error :', e)
                print('--> ', input_raw_file)
                raw_imgs_error.append(input_raw_file)

with open('raw_error_list.txt', 'w') as filehandle:
    for listitem in raw_imgs_error:
        filehandle.write(f'{listitem}\n')