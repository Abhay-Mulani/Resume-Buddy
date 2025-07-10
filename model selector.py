import yaml
import google.generativeai as genai

CONFIG_PATH = r"config.yaml"

with open(CONFIG_PATH) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    api_key = data['GOOGLE_API_KEY']

genai.configure(api_key=api_key)

models = genai.list_models()

print("Available models:")
for model in models:
    print(f"- {model.name}: {model.supported_generation_methods}")
