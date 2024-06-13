import argparse
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Hugging Face GPT2 model downloader

def download_model(model_name, save_directory):
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    model.save_pretrained(f'{save_directory}_model')
    tokenizer.save_pretrained(f'{save_directory}_tokenizer')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download GPT2 model from Hugging Face")
    parser.add_argument('-n', '--model_name', type=str, required=True, help="Model name to download: account/modelname")
    parser.add_argument('-d', '--directory', type=str, required=True, help="Save to directory")

    args = parser.parse_args()

    download_model(args.model_name, args.save_directory)
