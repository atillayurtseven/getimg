from getimg import GetIMG

api_key = "YOUR_API_KEY"
g = GetIMG(api_key=api_key)
payload = {
    "prompt": "A cute rabbit riding a motorbike"
}
g.flux_schnell.text_to_image(payload, save_to_file="./out.jpeg")