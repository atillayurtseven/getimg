import requests, base64
from enum import Enum

class Pipeline(Enum):
    text_to_image = "text-to-image"
    image_to_image = "image-to-image"
    inpaint = "inpaint"
    ip_adapter = "ip-adapter"
    controlnet = "controlnet"
    instruct = "instruct"
    upscale = "upscale"
    face_fix = "face-fix"

    def __str__(self):
        return self.value

class Models(Enum):
    flux_schnell = "v1/flux-schnell"
    essential_v2 = "v1/essential-v2"
    stable_diffusion_xl = "v1/stable-diffusion-xl"
    stable_diffusion = "v1/stable-diffusion-xl"
    latent_consistency = "v1/latent-consistency"
    enhancements = "v1/enhancements"

    def __str__(self):
        return self.value

class BaseIMG:
    def __init__(self, api_key):
        self.api_key = api_key

    def to_img(self, text: str) -> bytes:
        """
        Encodes a string to Base64.
        """
        return base64.b64encode(text.encode())

    def to_str(self, text: bytes) -> str:
        """
        Decodes a Base64 string to its original format.
        """
        return base64.b64decode(text).decode()

    def to_file(self, text, file_name):
        """
        Saves a Base64-encoded image to a file.
        """
        image_data = base64.b64decode(text)
        with open(file_name, "wb") as file:
            file.write(image_data)

    def from_file(self, file_name) -> str:
        """
        Reads an image file and returns its Base64 representation.
        """
        with open(file_name, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")  # Bytes türünde döndürür

    def jpg_to_base64(image_path) -> bytes:
        """
        Converts a JPG image to Base64 encoding.
        """
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read())  # Bytes

    def send_request(self, payload, model, pipeline, method="POST") -> dict:
        """
        Sends an HTTP request to the GetIMG API with the specified model and pipeline.
        """
        uri = f"https://api.getimg.ai/{model}/{pipeline}"
        header = {
            "accept": "application/json",
            "authorization": f"Bearer {self.api_key}",
            "content-type": "application/json"
        }
        if method == "POST":
            response = requests.post(uri, json=payload, headers=header)
        elif method == "GET":
            response = requests.get(uri, data=payload, headers=header)
        data = {}
        if response.status_code == 200:
            data = response.json()
        else:
            print(response.status_code)
            print(response.content)
        return data

    def list_all_models(self) -> dict:
        """
        Fetches all available models from the API.
        """
        return self.send_request({}, 'v1/models', method="GET")

    def get_model(self, id) -> dict:
        """
        Retrieves details of a specific model by ID.
        """
        return self.send_request({}, f'v1/models/{id}', method="GET")

    def get_account_balance(self) -> dict:
        """
        Gets the account balance associated with the API key.
        """
        return self.send_request({}, f'v1/account/balance', method="GET")

    def _generate_image(self, payload, model: Models, pipeline: Pipeline, save_to_file=None) -> dict:
        """
        Generates an image using the specified model and pipeline.
        """
        img = self.send_request(payload, model, pipeline)
        if save_to_file is not None and "image" in img:
            self.to_file(img['image'], save_to_file)
        return img

class FluxSchnell(BaseIMG):
    def text_to_image(self, payload, save_to_file=None):
        """
        https://docs.getimg.ai/reference/postfluxschnelltexttoimage
        """
        return self._generate_image(payload, Models.flux_schnell, Pipeline.text_to_image, save_to_file=save_to_file)

class EssentialV2(BaseIMG):
    def text_to_image(self, payload, save_to_file=None):
        """
        https://docs.getimg.ai/reference/postessentialv2texttoimage
        """
        return self._generate_image(payload, Models.essential_v2, Pipeline.text_to_image, save_to_file=save_to_file)

class StableDiffusionXL(BaseIMG):
    def text_to_image(self, payload, save_to_file=None):
        """
        https://docs.getimg.ai/reference/poststablediffusionxltexttoimage
        """
        return self._generate_image(payload, Models.stable_diffusion_xl, Pipeline.text_to_image, save_to_file=save_to_file)

    def image_to_image(self, payload, save_to_file=None):
        """
        https://docs.getimg.ai/reference/poststablediffusionxlimagetoimage
        """
        return self._generate_image(payload, Models.stable_diffusion_xl, Pipeline.image_to_image, save_to_file=save_to_file)

    def inpaint(self, payload, save_to_file=None):
        """
        https://docs.getimg.ai/reference/poststablediffusionxlinpaint
        """
        return self._generate_image(payload, Models.stable_diffusion_xl, Pipeline.inpaint, save_to_file=save_to_file)

    def ip_adapter(self, payload, save_to_file=None):
        """
        https://docs.getimg.ai/reference/poststablediffusionxlipadapter
        """
        return self._generate_image(payload, Models.stable_diffusion_xl, Pipeline.ip_adapter, save_to_file=save_to_file)

class StableDiffusion(BaseIMG):
    def text_to_image(self, payload, save_to_file=None):
        """
        https://docs.getimg.ai/reference/poststablediffusiontexttoimage
        """
        return self._generate_image(payload, Models.stable_diffusion, Pipeline.text_to_image, save_to_file)

    def image_to_image(self, payload, save_to_file=None):
        """
        https://docs.getimg.ai/reference/poststablediffusiontexttoimage
        """
        return self._generate_image(payload, Models.stable_diffusion, Pipeline.image_to_image, save_to_file)

    def controlnet(self, payload, save_to_file=None):
        """
        https://docs.getimg.ai/reference/poststablediffusioncontrolnet
        """
        return self._generate_image(payload, Models.stable_diffusion, Pipeline.controlnet, save_to_file)

    def inpaint(self, payload, save_to_file=None):
        """
        https://docs.getimg.ai/reference/poststablediffusioninpaint
        """
        return self._generate_image(payload, Models.stable_diffusion, Pipeline.inpaint, save_to_file)

    def instruct(self, payload, save_to_file=None):
        """
        https://docs.getimg.ai/reference/poststablediffusioninstruct
        """
        return self._generate_image(payload, Models.stable_diffusion, Pipeline.instruct, save_to_file)

class LatentConsistency(BaseIMG):
    def text_to_image(self, payload, save_to_file=None):
        """
        https://docs.getimg.ai/reference/postlatentconsistencytexttoimage
        """
        return self._generate_image(payload, Models.latent_consistency, Pipeline.text_to_image, save_to_file)

    def image_to_image(self, payload, save_to_file=None):
        """
        https://docs.getimg.ai/reference/postlatentconsistencyimagetoimage
        """
        return self._generate_image(payload, Models.latent_consistency, Pipeline.image_to_image, save_to_file)

class Enhancements(BaseIMG):
    def upscale(self, payload, save_to_file=None):
        """
        https://docs.getimg.ai/reference/postenhancementsupscale
        """
        return self._generate_image(payload, Models.enhancements, Pipeline.upscale, save_to_file)

    def face_fix(self, payload, save_to_file=None):
        """
        https://docs.getimg.ai/reference/postenhancementsfacefix
        """
        return self._generate_image(payload, Models.enhancements, Pipeline.face_fix, save_to_file)

class GetIMG:
    def __init__(self, api_key):
        self.api_key = api_key
        self.flux_schnell = FluxSchnell(api_key)
        self.essential_v2 = EssentialV2(api_key)
        self.stable_diffusion_xl = StableDiffusionXL(api_key)
        self.stable_diffusion = StableDiffusion(api_key)
        self.latent_consistency = LatentConsistency(api_key)
        self.enhancements = Enhancements(api_key)