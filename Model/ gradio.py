import gradio as gr
from PIL import Image, ImageDraw, ImageFont

def predict_food(img):
    # Dự đoán
    test_results = model.predict(source=img, save=False, show=False)
    result = test_results[0]

  #Get top5
    predictions = []
    for idx in result.probs.top5:
        name = result.names[idx]
        score = result.probs.data[idx].item()
        predictions.append(f"{name}: {score:.2%}")

    #draw top1 
    top1_idx = result.probs.top1
    top1_name = result.names[top1_idx]
    top1_score = result.probs.data[top1_idx].item()

    image_pil = Image.open(img).convert("RGB")
    draw = ImageDraw.Draw(image_pil)
    text = f"{top1_name} ({top1_score:.2%})"
    draw.text((10, 10), text, fill="red")

    return image_pil, "\n".join(predictions)

iface = gr.Interface(
    fn=predict_food,
    inputs=gr.Image(type="filepath"),
    outputs=[gr.Image(type="pil"), gr.Textbox()],
    title=" YOLOv8 - Vietnamese food recognition",
    description="Upload food images"
)

iface.launch(share=True)
