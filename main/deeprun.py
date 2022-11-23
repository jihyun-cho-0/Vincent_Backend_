# if __name__=="__main__":

#     # Path of the pre-trained TF model 
#     # model_path = r"C:\Users\dipesh\Desktop\Neural-Style-Transfer\model"
#     model_path = r"C:/hyeongseok_code/Carrot_Project/Neural-Style-Transfer/model"

#     # NOTE : Works only for '.jpg' and '.png' extensions,other formats may give error
#     content_image_path = r"C:/Users/rjgjf/Desktop/cat1.png"
#     # (1, 960, 640, 3) 코끼리
#     # (1, 1334, 750, 4) 고양이
#     # (1, 796, 595, 3) 지수
#     # (1, 800, 640, 3) temp
#     # (1, 600, 600, 4) 그려준 그림
    
#     style_image_path = r"C:/Users/rjgjf/Desktop/testtest.jpg"

#     img = transfer_style(content_image_path,style_image_path,model_path)
#     # Saving the generated image
#     plt.imsave('C:/Users/rjgjf/Desktop/ee3.jpg',img)
#     plt.imshow(img)
#     print(img)
#     # plt.show()

def transfer_style(content_image, style_image, model_path):
    import matplotlib.pylab as plt
    import numpy as np
    import tensorflow as tf
    import tensorflow_hub as hub

    """
    :param content_image: path of the content image
    :param style_image: path of the style image
    :param model_path: path to the downloaded pre-trained model.

    The 'model' directory already contains the downloaded pre-trained model,but 
    you can also download the pre-trained model from the below TF HUB link:
    https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2

    :return: An image as 3D numpy array.

    """

    print("Loading images...")
    # Load content and style images
    content_image = plt.imread(content_image)
    style_image = plt.imread(style_image)

    print("Resizing and Normalizing images...")
    # Convert to float32 numpy array, add batch dimension, and normalize to range [0, 1]. Example using numpy:
    content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.
    content_image = tf.convert_to_tensor(content_image[:,:,:,:3])
    # 4차원을 3차원으로 바꿔줬음
    # print(content_image.shape, '###########')
    style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.

    # Optionally resize the images. It is recommended that the style image is about
    # 256 pixels (this size was used when training the style transfer network).
    # The content image can be any size.
    style_image = tf.image.resize(style_image, (256, 256))

    print("Loading pre-trained model...")
    # The hub.load() loads any TF Hub model
    hub_module = hub.load(model_path)

    print("Generating stylized image now...wait a minute")
    # Stylize image.
    outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
    stylized_image = outputs[0]

    # reshape the stylized image
    stylized_image = np.array(stylized_image)
    stylized_image = stylized_image.reshape(
        stylized_image.shape[1], stylized_image.shape[2], stylized_image.shape[3])

    print("Stylizing completed...")
    return stylized_image

def change_image(num, image_path, style_path):
    import matplotlib.pylab as plt
    import os

    absolute_path = os.path.dirname(__file__)
    relative_path = "model"
    full_path = os.path.join(absolute_path, relative_path)
    model_path = full_path
    # 저장된 model위치 찾기
    
    absolut_media_path = os.path.abspath('media/temp')
    image_full_path = os.path.join(absolut_media_path, image_path.split('/')[-1])
    # media/temp의 경로와 파일의 경로를 합쳐줌

    if num == 1:
        # user filter를 사용할 때
        absolut_filter_path = os.path.abspath('media/user_temp_filter')
        style_full_path = os.path.join(absolut_filter_path, style_path.split('/')[-1])
        img = transfer_style(image_full_path, style_full_path, model_path)
        plt.imsave(image_full_path, img)
    else:
        # 기존 filter를 사용할 때
        absolut_filter_path = os.path.abspath('media/filter')
        style_path = str(style_path)
        # 기존 필터를 사용하면 이미지가 str 값이 아닌 imagefield 여서 str로 바꾼 후
        # 이름값을 출력해야 함
        style_full_path = os.path.join(absolut_filter_path, style_path.split('/')[-1])
        img = transfer_style(image_full_path, style_full_path, model_path)
        plt.imsave(image_full_path, img)

# change_image("C:/Users/rjgjf/Desktop/cat1.png", "C:/Users/rjgjf/Desktop/testtest.jpg")
