import base64
from io import BytesIO

from potassium import Potassium, Request, Response

from diffusers import StableDiffusionPipeline
import torch

app = Potassium("my_app")

# @app.init runs at startup, and loads models into the app's context
@app.init
def init():
    model = StableDiffusionPipeline.from_pretrained("ECRodriguez/ecrodriguez-workshop", torch_dtype=torch.float16)
    model.to("cuda")
   
    context = {
        "model": model
    }

    return context

# @app.handler runs for every call
@app.handler("/")
def handler(context: dict, request: Request) -> Response:
    prompt = request.json.get("prompt")
    model = context.get("model")

    with torch.autocast("cuda"):
        image = model(
            prompt,
            num_inference_steps=70,
            guidance_scale=6,
        ).images[0]

    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return Response(
        json = {"image_base64": image_base64}, 
        status=200
    )

if __name__ == "__main__":
    app.serve()