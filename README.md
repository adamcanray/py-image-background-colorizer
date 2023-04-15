# Image Background Colorizer

This is a simple Python script that allows you to change the background color of an image to any color of your choice. The script takes an image file as input and outputs a new image file with the background color changed.

> I'm using this because my laptop doesn't currently have photoshop and I have trust issues trying online tools on the internet. so i decided to make this simple shi'🤪.

## Usage

To use the script, follow these simple steps:

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Put the image file you want to change the background color of in the same directory as the script.
3. Open the script in your preferred Python editor and modify the newVal parameter in the `cv2.floodFill()` function to the RGB value of the color you want the background to be. For example, if you want the background to be red, set `newVal=(0, 0, 255)`.
4. Run the script by typing python colorizer.py in the terminal.
5. The output image file with the new background color will be saved in the same directory as the original image file.

That's it! Enjoy colorizing your images!
