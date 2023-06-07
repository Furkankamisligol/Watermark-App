import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk, ImageFont


def add_watermark(image_path, watermark_text, output_path, text_color=(0, 0, 0)):
    # Open the image using PIL
    image = Image.open(image_path)

    # Create a transparent overlay for the watermark
    watermark = Image.new('RGBA', image.size, (0, 0, 0, 0))

    width, height = image.size

    # Create a drawing object
    draw = ImageDraw.Draw(watermark)

    # Set the watermark text and font
    text = watermark_text
    # font_size = max(1, int(image.size[0] / 20))
    font_path = r'.\Mega Brush.otf'
    font = ImageFont.truetype(font_path, 30)
    # text_font = ImageFont.truetype(font_path, font_size)

    # Calculate the position to place the watermark (bottom right corner)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = width - text_width - 10
    y = height - text_height - 10

    # Draw the watermark text on the overlay
    draw.text((x, y), text, font=font, fill=text_color)

    # Combine the original image with the watermark overlay
    watermarked_image = Image.alpha_composite(image.convert('RGBA'), watermark)

    # Save the watermarked image to the output path
    watermarked_image.save(output_path)


def upload_image():
    # Open a file dialog for image selection
    image_path = filedialog.askopenfilename(filetypes=[('Image files', '*.jpg;*.jpeg;*.png;*.gif')])

    if image_path:
        # Get the watermark text from the entry field
        watermark_text = watermark_entry.get()

        # Generate the output path
        output_path = r'.\Watermark_\watermarked_photos/' + image_path.split('/')[-1]

        # Add watermark to the image
        add_watermark(image_path, watermark_text, output_path)

        # Display the watermarked image in a new window
        watermarked_window = tk.Toplevel(root)
        watermarked_image = Image.open(output_path)
        watermarked_photo = ImageTk.PhotoImage(watermarked_image)
        label = tk.Label(watermarked_window, image=watermarked_photo)
        label.pack()
        watermarked_window.mainloop()


# Create the main application window
root = tk.Tk()
root.minsize(width=400, height=200)
root.config(padx=20, pady=20)
# Create a label and entry field for the watermark text
watermark_label = tk.Label(root, text='Watermark Text:')
watermark_label.pack()
watermark_entry = tk.Entry(root)
watermark_entry.pack()

# Create a button to upload the image
upload_button = tk.Button(root, text='Upload Image', command=upload_image)
upload_button.pack()

# Start the application main loop
root.mainloop()
