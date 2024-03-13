import cv2, os, time
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
# https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames

base = "./download/"
src = os.path.join(base, "vids")
out = os.path.join(base, "vid_frames")

if not os.path.exists(out):
    os.mkdir(out)

for im in os.listdir(src):
    vidcap = cv2.VideoCapture(os.path.join(src,im))
    # vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
    if int(major_ver)  < 3 :
        fps = vidcap.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second: {0}".format(fps))
    else :
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        print("Frames per second: {0}".format(fps))

    files = os.path.splitext(im)[0]
    count = 1
    seconds = 0
    while vidcap.isOpened():
        success,image = vidcap.read()
        if success:
            if count % 1 == 0:
                start = time.time()
                
                filename = f"{files}_{os.path.splitext(im)[0][17:].replace(' ', '-')}_frame{count}.jpg"
                cv2.imwrite(os.path.join(out,filename), image)     # save frame as JPEG file      
                print(f'Read a new frame for {filename}: {success}')
                
                seconds = time.time() - start
                count += 1
        else:
            break
    fps  = count / seconds
    print("Estimated frames per second : {0}".format(fps))
    print()
vidcap.release()
print("......Success")