from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

def generate_caption(image_path):
    # Load the BLIP processor and model
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    
    # Load the image
    raw_image = Image.open(image_path).convert("RGB")
    
    # Prepare the image and generate the caption
    inputs = processor(raw_image, return_tensors="pt")
    out = model.generate(**inputs)
    
    # Decode the output and return the caption
    caption = processor.decode(out[0], skip_special_tokens=True)
    return f"Caption: {caption}"

# Example usage
image_path = "C:\\Users\\Jashoda\\Downloads\\img.png"  # Make sure this path is correct
print(generate_caption(image_path))
