import streamlit as st



st.set_page_config(
    page_title="SEDS Project",
    page_icon=":sparkles:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)



st.title('Food Image Classification :spaghetti: :fries: :pizza: :custard:')
st.header(' Chosen framework: :orange[TensorFlow]')
st.header(' Chosen dataset: :orange[food101] ')
st.subheader('Let\'s explore Computer Vision together :female-technologist:',  divider='rainbow')

st.subheader(' I- Image Classification')
image_classification = """ Image classification is a computer vision task where a machine learning model is trained to assign predefined labels 
or categories to input images. The goal is to teach the model to recognize and categorize objects or patterns within the images accurately. """
st.markdown(image_classification, unsafe_allow_html=True)

st.subheader(' II- What is Computer Vision ?') 
computer_vision= """
Computer vision is a branch of artificial intelligence that enables machines to interpret and understand visual information from the world, involving tasks like image recognition and object detection. It aims to replicate human vision in machines for various applications."""
st.markdown(computer_vision, unsafe_allow_html=True)

st.subheader(' III- Why Tensorflow ?')
tf= """TensorFlow is often chosen in AI due to its versatility, robustness, and extensive community support. It offers a flexible framework for building and deploying machine learning models, has a user-friendly high-level API, and is widely used in both research and industry, making it a popular choice for AI projects."""
st.markdown(tf, unsafe_allow_html=True)

st.subheader(' IV- What is Deep Learning ?')
deep_learning= """Deep learning is a subset of machine learning that involves neural networks with multiple layers (deep neural networks). These networks, inspired by the structure of the human brain, can automatically learn and represent complex patterns and features from data. Deep learning has been particularly successful in tasks such as image and speech recognition, natural language processing, and playing games, contributing to advancements in artificial intelligence."""
st.markdown(deep_learning, unsafe_allow_html=True)

st.subheader(' V- What is CNN ?') 
cnn= """CNN stands for Convolutional Neural Network. It's a type of deep neural network designed for processing and analyzing visual data, such as images. CNNs are particularly effective in tasks like image recognition and object detection, as they automatically learn hierarchical representations of features from the input data through convolutional layers."""
st.markdown(cnn, unsafe_allow_html=True)

st.subheader(' VI- CNN Architecture')
cnn_architecture= """
"""
st.markdown(cnn_architecture, unsafe_allow_html=True)
st.image('images/cnn.png',width=600)

st.subheader(' VII- How to deal with Overfitting ?') 
text = '''  <h5> Dropout</h5>
    <p> Dropout randomly deactivates (drops out) a proportion of neurons in a neural network, helping prevent overfitting by making the network more robust and less dependent on specific neurons. This encourages the network to learn more general and robust features. </p>

    <h5> Data Augmentation </h5>
    <p> In computer vision (CV), data augmentation involves applying various transformations, such as rotation, flipping, and scaling, to images in a training dataset. This technique helps improve the robustness and performance of computer vision models by providing a more diverse set of training examples. </p>

    <h5> Transfer Learning </h5>
   
 <p> Transfer learning in computer vision involves using a pre-trained neural network on a large dataset for a specific task and adapting it to a new, related task with a smaller dataset. This helps leverage the knowledge gained from the original task, improving the performance of the model on the new task.</p>
'''
st.markdown(text, unsafe_allow_html=True)
st.subheader(' VIII- food101 dataset')
food101= """ The Food101 dataset is a collection of 101,000 labeled images representing 101 different food categories. It is commonly used in computer vision research for training and evaluating models that aim to recognize and classify various types of food.
"""
st.markdown(food101, unsafe_allow_html=True)






