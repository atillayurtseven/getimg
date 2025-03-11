# GetIMG API Python Wrapper

This repository provides a Python wrapper for interacting with the GetIMG API, allowing users to generate images using various AI models and pipelines. The wrapper includes support for text-to-image, image-to-image, inpainting, controlnet, and more.

## Features

- **Multiple Models Supported**: Includes Stable Diffusion XL, Flux Schnell, Essential V2, Latent Consistency, and more.
- **Multiple Pipelines**: Supports text-to-image, image-to-image, inpainting, controlnet, IP adapter, face fix, and upscaling.
- **Base64 Encoding/Decoding**: Easily convert images to/from Base64 for API requests.
- **Flexible API Handling**: Allows sending requests to GetIMG with various models and pipelines.
- **Account Management**: Fetch account balance and model details.

## Installation

To use this library, first clone the repository:

```sh
git clone https://github.com/atillayurtseven/getimg.git
cd getimg
```

Then install the required dependencies:

```sh
pip install requests
```

## Getting an API Key

To use the GetIMG API, you need an API key. You can obtain one by registering at [GetIMG.ai](https://getimg.ai/).

## Usage

### Initializing the API Wrapper

```python
from getimg import GetIMG

api_key = "your_api_key_here"
getimg = GetIMG(api_key)
```

### Text-to-Image Example

```python
payload = {
    "prompt": "A cute rabbit riding a motorbike"
}
img = getimg.flux_schnell.text_to_image(payload, save_to_file="./out.jpeg")
```
![Output](out.jpeg)

### Image-to-Image Example

```python
payload = {
    "image": getimg.stable_diffusion.from_file("input.jpg"),
    "prompt": "Make it look like a watercolor painting"
}

image_response = getimg.stable_diffusion.image_to_image(payload, save_to_file="output.jpg")
print(image_response)
```

### Inpainting Example

```python
payload = {
    "image": getimg.stable_diffusion.from_file("input.jpg"),
    "mask": getimg.stable_diffusion.from_file("mask.png"),
    "prompt": "Restore missing details"
}

image_response = getimg.stable_diffusion.inpaint(payload, save_to_file="output.jpg")
print(image_response)
```

### Fetch Account Balance

```python
balance = getimg.stable_diffusion.get_account_balance()
print(balance)
```

## Supported Models

| Model | API Path |
|--------|-----------|
| Flux Schnell | `v1/flux-schnell` |
| Essential V2 | `v1/essential-v2` |
| Stable Diffusion XL | `v1/stable-diffusion-xl` |
| Stable Diffusion | `v1/stable-diffusion-xl` |
| Latent Consistency | `v1/latent-consistency` |
| Enhancements | `v1/enhancements` |

## Supported Pipelines

| Pipeline | Description |
|----------|-------------|
| text-to-image | Generates images from text prompts |
| image-to-image | Converts an input image based on a prompt |
| inpaint | Edits specific parts of an image using a mask |
| ip-adapter | Uses reference images for stylistic adaptation |
| controlnet | Applies structure-based modifications to images |
| upscale | Increases the resolution of an image |
| face-fix | Enhances facial details in images |

## API Endpoints

The wrapper interacts with the following API endpoints:

- **`POST /v1/{model}/{pipeline}`** - Generate images using a specified model and pipeline.
- **`GET /v1/models`** - List all available models.
- **`GET /v1/models/{id}`** - Retrieve details of a specific model.
- **`GET /v1/account/balance`** - Fetch the account balance.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Contributing

Contributions are welcome! Please open an issue or pull request if you have improvements or suggestions.

## Contact

For any questions or feedback, feel free to reach out via GitHub issues.

