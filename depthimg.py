import torch
import cv2
import torchvision.transforms as transforms
import os

def load_model():
    model = torch.hub.load("intel-isl/MiDaS", "MiDaS")
    model.eval()
    return model


def predict_depth(model, img_path):
    # Check if the image path is valid
    if not os.path.isfile(img_path):
        raise ValueError(f"No file found at {img_path}")

    img = cv2.imread(img_path)
    if img is None:
        raise ValueError(f"The file at {img_path} could not be read as an image")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # resize to be multiple of 32
    height, width, _ = img.shape
    new_height = (height // 32) * 32
    new_width = (width // 32) * 32
    img = cv2.resize(img, (new_width, new_height))

    transform = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    input_img = transform(img).unsqueeze(0)

    with torch.no_grad():
        prediction = model(input_img)

    prediction = prediction.squeeze().numpy()

    # normalize the prediction to 0-255 and convert to uint8
    prediction = cv2.normalize(prediction, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # save the depth map with same base name as input image but different extension
    base_name = os.path.basename(img_path)
    name_without_extension = os.path.splitext(base_name)[0]
    output_path = os.path.join(os.getcwd(), f"{name_without_extension}_depth_map.png")
    cv2.imwrite(output_path, prediction)

    print(f"✨ Depth map image has been saved at {os.path.abspath(output_path)}")

    return prediction


# Add your image path here:

model = load_model()
depth_map = predict_depth(model, r"C:\Users\psych\Desktop\glitch\back.png")
