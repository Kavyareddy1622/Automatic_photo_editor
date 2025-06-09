from PIL import Image, ImageEnhance, ImageFilter

def auto_edit(input_path, output_path, resize=(800, 800)):
    img = Image.open(input_path)

    # Resize first
    img = img.resize(resize)

    # Enhance brightness
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.5)

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)

    # Apply sharpen filter
    img = img.filter(ImageFilter.SHARPEN)

    # Convert to grayscale
    img = img.convert('L')

    # Save the edited image
    img.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    input_file = "download.jpg"     
    output_file = "edited_image.jpg"
    auto_edit(input_file, output_file)

    