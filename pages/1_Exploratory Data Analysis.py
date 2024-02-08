# import requests
import streamlit as st

st.header('Exploratory Data Analysis')



st.subheader('Load data from disk')
code = '''
data_dir = '/home/meriem-mk/Downloads/food101/food-101/food-101/images'
data_dir = pathlib.Path(data_dir).with_suffix('')
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)
'''
st.code(code, language='python')

code_0 = '''
train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

  val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

class_names = train_ds.class_names
print(class_names)
'''
image_count = 101000
st.write('output:')
st.write(image_count)


st.code(code_0, language='python')
st.write('output:')
st.write('[\'apple_pie\', \'baby_back_ribs\', \'baklava\', \'beef_carpaccio\', \'beef_tartare\', \'beet_salad\', \'beignets\', \'bibimbap\', \'bread_pudding\', \'breakfast_burrito\' ...\' ]' )

st.subheader('Load data from disk')
code_01 = '''
st.code(code, language='python')
plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(class_names[labels[i]])
    plt.axis("off")
'''
st.code(code_01, language='python')
st.write('output:')
st.image('images/Pasted image 10.png')





code_2 = '''
def display_random_images(dataset_path, class_name, num_images=9):
    class_path = os.path.join(dataset_path, class_name)
    image_files = os.listdir(class_path)
    
    random_images = random.sample(image_files, min(num_images, len(image_files)))

    plt.figure(figsize=(12, 12))
    for i, image_file in enumerate(random_images):
        img_path = os.path.join(class_path, image_file)
        plt.subplot(3, 3, i + 1)
        img = mpimg.imread(img_path)
        plt.imshow(img)
        plt.title(f'{class_name} - Image {i + 1}')
        plt.axis('off')

    plt.tight_layout()
    plt.show()


display_random_images(data_dir, 'pizza', num_images=9)
'''
st.code(code_2, language='python')

st.write('output:')
st.image('images/Pasted image.png')

code_3 = '''
PIL.Image.open(str(data_dir)+'/caesar_salad/1303023.jpg')
'''
st.code(code_3, language='python')
st.write('output:')
st.image('images/Pasted image 1.png')

code_4 = '''
PIL.Image.open(str(data_dir)+'/caesar_salad/1994771.jpg')
'''
st.code(code_4, language='python')
st.write('output:')
st.image('images/Pasted image 2.png')



code_5 = '''
display_random_images(dataset_dir, 'waffles', num_images=9))
'''
st.code(code_5, language='python')
st.write('output:')
st.image('images/Pasted image 3.png')

code_6 = '''
display_random_images(dataset_dir, 'waffles', num_images=9))
'''
st.code(code_6, language='python')
st.write('output:')
st.image('images/Pasted image 5.png')


code_7 = '''
display_random_images(dataset_dir, 'waffles', num_images=9))
'''
st.code(code_7, language='python')
st.write('output:')
st.image('images/Pasted image 6.png')

code_8 = '''
display_random_images(dataset_dir, 'waffles', num_images=9))
'''
st.code(code_8, language='python')
st.write('output:')
st.image('images/Pasted image 7.png')


code_9 = '''
display_random_images(dataset_dir, 'waffles', num_images=9))
'''
st.code(code_9, language='python')
st.write('output:')
st.image('images/Pasted image 8.png')

code_10 = '''
display_random_images(dataset_dir, 'waffles', num_images=9))
'''
st.code(code_10, language='python')
st.write('output:')
st.image('images/Pasted image 9.png')


st.write("[Click here to check the complete EDA on jupyter notebook](https://github.com/meriemmekki2001/SEDS_PROJECT/blob/main/food101_EDA.ipynb)")

