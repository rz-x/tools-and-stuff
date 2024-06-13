from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_model():
    model = GPT2LMHeadModel.from_pretrained('./papuGaPT2_finetuned')
    tokenizer = GPT2Tokenizer.from_pretrained('./papuGaPT2_finetuned')
    return model, tokenizer

def generate_response(model, tokenizer, prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=200, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def main():
    model, tokenizer = load_model()
    # question
    prompt = "What is love?"

    response = generate_response(model, tokenizer, prompt)
    
    print("Q:", prompt)
    print("A:", response)

if __name__ == "__main__":
    main()
