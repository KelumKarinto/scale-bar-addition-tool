# Scale Bar Addition Tool

This tool allows you to add a scale bar to microscope images in the `.tif` format (1920x1440). It is designed to work with the OLYMPUS IX71 microscope but can be adjusted to work with other models.

## Usage

To run the script, you must provide the path to the image and the type of scope. Available types include `4X_1X`, `4X_1.6X`, `10X_1X`, `10X_1.6X`, `40X_1X`, `40X_1.6X`. Check the calibrations of scopes for OLYMPUS IX71.

Command example:
```
python add_scale_bar.py image_path.tif 10X_1.6X
```

## Constants

The constants at the beginning of the script (`scale_pixel_4X_1X_100_um`, `scale_pixel_10X_1X_100_um`, `scale_pixel_40X_1X_100_um`) are specific to the OLYMPUS IX71 microscope. You must adjust these values if you are working with a different microscope. Make sure to calibrate and find the correct values for the specific magnification levels.

## Requirements

The script requires the following Python libraries:
- PIL
- OpenCV
- NumPy

You can install these using pip:
```
pip install pillow opencv-python numpy
```

## Customization

You can also adjust the scale bar's position, thickness, and font size in the code if needed.
