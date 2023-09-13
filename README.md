# Scale Bar Addition Tool

This tool allows you to add a scale bar to microscope images in the `.tif` format (1920x1440). It is designed to work with the OLYMPUS IX71 microscope but can be adjusted to work with other models.

![10X_1 6X_scaled](https://github.com/KORINZ/scale-bar-addition-tool/assets/111611023/43ef5d9a-9e1d-4ace-82bb-b52bb435b9b9)

## Usage

To run the script, you must provide the path to the image and the type of scope. Available types include `4X_1X`, `4X_1.6X`, `10X_1X`, `10X_1.6X`, `40X_1X`, `40X_1.6X`. Check the calibrations of scopes for OLYMPUS IX71.

Command example:

   ```shell
   python add_scale_bar.py image_path.tif 10X_1.6X
   ```

However, if the target image filename contains the scope type (e.g., 10X_1.6X), it will automatically detect it, and no scope type argument is required.

## Constants

The constants at the beginning of the script (`scale_pixel_4X_1X_100_um`, `scale_pixel_10X_1X_100_um`, `scale_pixel_40X_1X_100_um`) are specific to the OLYMPUS IX71 microscope. You must adjust these values if you are working with a different microscope. Calibrate and find the correct values for the specific magnification levels.

## Installation

1. **Clone the repository**:

   ```shell
   git clone https://github.com/KORINZ/scale-bar-addition-tool.git
   ```

2. **Navigate to the directory**:

   ```shell
   cd scale-bar-addition-tool
   ```

3. **Install the requirements**:

   ```shell
   pip install -r requirements.txt
   ```

## Requirements

The script requires the following Python libraries, which can be installed using the `requirements.txt` file:

- PIL (Pillow)
- OpenCV (opencv-python)
- NumPy

## Customization

You can adjust the scale bar's position, thickness, font size, image size, and image format in the code if needed. Consult the code comments for further guidance on these adjustments.
