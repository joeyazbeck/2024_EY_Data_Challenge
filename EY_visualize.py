#Script to load and visualize the RGB layers of the image.
#Input is the image file path only.


import rasterio
import matplotlib.pyplot as plt


def load_and_visualize(image_path):
    
    with rasterio.open(image_path) as src:
        red=src.read(1)
        blue=src.read(2)
        green=src.read(3)
    
    fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(20,5))
    ax1.imshow(red,cmap='Reds')
    ax1.set_title('Red Band')
    ax2.imshow(green,cmap='Greens')
    ax2.set_title('Green Band')
    ax3.imshow(blue,cmap='Blues')
    ax3.set_title('Blue Band')
    plt.show()



if __name__ == "__main__":
    
    image_path='C:\\Users\\user\\Desktop\\2024 EY Open Science Data Challenge\\Post_Event_San_Juan.tif'
    load_and_visualize(image_path)
    
    
    
    
    