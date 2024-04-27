from PIL import Image


def split_image(image_path, output_folder):
    """
    This function takes an image and splits it into four vertical slices.
    Each slice is saved as a separate PNG file in the specified output folder.
    This is useful for processing images into segments for analysis or machine learning.

    Parameters:
    image_path (str): The path to the input image file.
    output_folder (str): The directory where the sliced images will be saved.
    """
    # Load the image
    img = Image.open(image_path)

    # Calculate the new height for the slices
    img_width, img_height = img.size
    slice_height = img_height // 4

    # Split the image into four parts
    for i in range(4):
        # Define the bounding box for the slice
        top = i * slice_height
        bottom = (i + 1) * slice_height if (i < 3) else img_height  # Ensure the last slice includes the remainder

        # Crop the image and save it
        img_slice = img.crop((0, top, img_width, bottom))
        img_slice.save(f"{output_folder}/sliced_image_{i + 1}.png")


# Usage examples
split_image("/home/nox/123/sliced_image_1.png", "/home/nox/123/1")
split_image("/home/nox/123/sliced_image_2.png", "/home/nox/123/2")
split_image("/home/nox/123/sliced_image_3.png", "/home/nox/123/3")
split_image("/home/nox/123/sliced_image_4.png", "/home/nox/123/4")
