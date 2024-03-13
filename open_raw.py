import rawpy
import imageio
import os

# Replace 'input_image.raw' with the path to your .raw file
# input_raw_file = './DEPTH_AMPLITUDE_140836247_3643_H_Flip/DEPTH_99.raw'
raw_folder = 'raw_imgs/'

raw_imgs_error = []

raw_list = os.listdir(raw_folder)
for rw in raw_list:
    for imgs in os.listdir(os.path.join(raw_folder, rw)):
        if os.path.splitext(imgs)[-1] == '.raw':
            input_raw_file = os.path.join(raw_folder, rw, imgs)
            # Open the RAW file
            try:
                with rawpy.imread(input_raw_file) as raw:
                    # Process the RAW image data
                    rgb = raw.postprocess()

                    # Replace 'output_image.jpg' with the desired name for the output .jpg file
                    file_prefix = '_'.join(rw.split('_')[3:])
                    output_jpg_file = f'{file_prefix}_{os.path.splitext(imgs)[0]}.jpg'
                    output_jpg_file = os.path.join('imgs', 'amp_'+file_prefix, output_jpg_file)
                    if not os.path.exists('imgs/'):
                        os.mkdir('imgs/')
                    if not os.path.exists('imgs/'+'amp_'+file_prefix):
                        os.mkdir('imgs/'+'amp_'+file_prefix)

                    # Save the processed image as a JPEG file using imageio
                    imageio.imsave(output_jpg_file, rgb)
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
