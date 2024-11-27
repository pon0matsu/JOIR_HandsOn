import os
import cv2
import numpy as np
import argparse
from tensorflow.keras.models import load_model

def load_images(inputpath, imagesize, type_color):
    imglist = []
    filenamelist = []
    for root, dirs, files in os.walk(inputpath):
        for fn in sorted(files):
            bn, ext = os.path.splitext(fn)
            if ext not in [".bmp", ".BMP", ".jpg", ".JPG", ".jpeg", ".JPEG", ".png", ".PNG"]:
                continue

            filename = os.path.join(root, fn)

            if type_color == 'Color':
                testimage = cv2.imread(filename, cv2.IMREAD_COLOR)
                testimage = cv2.resize(testimage, imagesize, interpolation=cv2.INTER_CUBIC)
                testimage = np.asarray(testimage, dtype=np.float32)
                testimage = testimage[:, :, ::-1]

            elif type_color == 'Gray':
                testimage = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
                testimage = cv2.resize(testimage, imagesize, interpolation=cv2.INTER_CUBIC)
                testimage = np.asarray(testimage, dtype=np.float32).reshape((imagesize[1], imagesize[0], 1))

            imglist.append(testimage)
            filenamelist.append(fn)
    imgsdata = np.asarray(imglist, dtype=np.float32)

    return imgsdata, filenamelist

def main(image_dir, model_path, num_class=2):
    print("Loading model from:", model_path)
    model = load_model(model_path)

    print("Loading images from:", image_dir)
    images, images_filenames = load_images(image_dir, (576, 384), 'Color')

    images = images[:, :, 96:480, ...]
    images /= 255.0

    print('Data load finished. Number of images:', len(images))

    print('Predicting...')
    results = model.predict(images, batch_size=16, verbose=1)

    # 結果を表示
    print("\nPrediction Results:")
    print("filename, estimate_class, estimate_prob, estimate_prob_class0, estimate_prob_class1")
    for i in range(len(images)):
        estimate_class = np.argmax(results[i])
        estimate_prob = np.max(results[i])
        estimate_prob_class0 = results[i][0]
        estimate_prob_class1 = results[i][1]
        print(f"{images_filenames[i]}, {estimate_class}, {estimate_prob}, {estimate_prob_class0}, {estimate_prob_class1}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Gender Prediction Script")
    parser.add_argument('--image_dir', type=str, required=True, help="Directory containing input images")
    parser.add_argument('--model_path', type=str, required=True, help="Path to the model file")
    args = parser.parse_args()

    main(args.image_dir, args.model_path)