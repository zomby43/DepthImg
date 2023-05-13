✨ Depth Map Generator

This Python script uses the MiDaS model from Intel ISL to generate a depth map from a 2D image.
Requirements

    Python 3.6 or later
    The following Python packages, which are listed in requirements.txt:
        torch
        torchvision
        numpy
        opencv-python
        timm

Installation

    Clone this repository or download the ZIP file and extract it.

    Open a terminal and navigate to the directory containing the project files.

    Run the following command to install the necessary Python packages:

    bash

    pip install -r requirements.txt
    
    Note: Depending on your Python installation, you might need to use pip3 instead of pip.

Usage

    Edit the depth_map_generator.py file and replace the path in the last line of the script with the path to your input image:

    python

depth_map = predict_depth(model, r"add path to image here (e.g. C:\images\image.jpg)")

Run the script with the following command:

bash

    python depthimg.py

    Note: Depending on your Python installation, you might need to use python3 instead of python.

    The script will print a message when the depth map has been created and saved. The message will include the full path to the depth map image.

Troubleshooting

    If you get an error like ModuleNotFoundError: No module named 'torch', make sure you have installed the requirements with the command pip install -r requirements.txt.

    If you get an error like ValueError: No file found at "add path to image here (e.g. C:\images\image.jpg)", make sure the path to your image is correct and the image file exists at that location.

    If you get an error like RuntimeError: The size of tensor a (20) must match the size of tensor b (19) at non-singleton dimension 2, make sure the width and height of your image are both divisible by 32.

License

This project is licensed under the terms of the MIT license.
