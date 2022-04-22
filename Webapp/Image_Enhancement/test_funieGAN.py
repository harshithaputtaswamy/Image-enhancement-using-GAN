"""
# > Script for testing FUnIE-GAN 
# > Notes and Usage:
#    - set data_dir and model paths
#    - python test_funieGAN.py
"""
import os
import time
import ntpath
import numpy as np
from PIL import Image
from os.path import join, exists
from keras.models import model_from_json
from django.conf import settings

## local libs
from Image_Enhancement.utils.data_utils import getPaths, read_and_resize, preprocess, deprocess

def test_model(filename):

    output_dir = os.path.join(settings.MEDIA_ROOT, "output/")
    if not exists(output_dir): os.makedirs(output_dir)

    ## test funie-gan
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    img_file = os.path.join(settings.MEDIA_ROOT, 'input/'+filename)
    print(img_file)
    img_path = os.path.join(settings.MEDIA_ROOT, img_file)
    model_h5 = join(ROOT_DIR, 'saved_model/model_15320_.h5')
    model_json = join(ROOT_DIR, 'saved_model/model_15320_.json')

    # sanity
    assert (exists(model_h5) and exists(model_json))

    # load model
    with open(model_json, "r") as json_file:
        loaded_model_json = json_file.read()
    funie_gan_generator = model_from_json(loaded_model_json)

    # load weights into new model
    funie_gan_generator.load_weights(model_h5)
    print("\nLoaded data and model")

    # testing loop
    times = []; s = time.time()
    inp_img = read_and_resize(img_path, (256, 256))
    im = preprocess(inp_img)
    im = np.expand_dims(im, axis=0) # (1,256,256,3)

    # generate enhanced image
    s = time.time()
    gen = funie_gan_generator.predict(im)
    gen_img = deprocess(gen)[0]
    tot = time.time()-s
    times.append(tot)
    out_img = gen_img
    Image.fromarray(out_img).save(join(output_dir, filename))

    Ttime, Mtime = np.sum(times[1:]), np.mean(times[1:]) 
    print ("Time taken: {0} sec at {1} fps".format(Ttime, 1./Mtime))
    print("\nSaved generated images in in {0}\n".format(output_dir))

