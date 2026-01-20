import gradio as gr
from detector import detect_objects
from explain import get_explanation
from PIL import Image

def process(image, level):
    image.save("temp.jpg")
    detected = detect_objects("temp.jpg")
    if detected:
        explanation = get_explanation(detected[0], level)
        return f" Detected: {', '.join(detected)}\n\n{explanation}"
    else:
        return "Hmm, I couldn’t find anything clearly in this image . Try another one or use a more zoomed-in picture!"


iface = gr.Interface(
    fn=process,
    inputs=[
        gr.Image(type="pil", label="Upload an image"),
        gr.Radio(["child", "school", "college", "expert"], label="Choose explanation level")
    ],
    outputs="text",
    title=" Friendly AI Explainer",
    description="Upload an image and let me explain it in a fun way!"
)

iface.launch()

