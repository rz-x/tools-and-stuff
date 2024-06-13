import argparse
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling

def load_model(model_path, tokenizer_path):
    model = GPT2LMHeadModel.from_pretrained(model_path)
    tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)
    return model, tokenizer

def load_dataset(file_path, tokenizer):
    dataset = TextDataset(tokenizer=tokenizer, file_path=file_path, block_size=128)
    return dataset

def generate_response(model, tokenizer, prompt):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def go(model_path, tokenizer_path, data_path):
    model, tokenizer = load_model(model_path, tokenizer_path)
    train_dataset = load_dataset(data_path, tokenizer)
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False)
    
    training_args = TrainingArguments(
        output_dir='./results',
        overwrite_output_dir=True,
        num_train_epochs=2,  # zmniejszenie liczby epok do 2
        per_device_train_batch_size=2,  # zmniejszenie batch size do 2
        save_steps=10_000,
        save_total_limit=2)
    
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=train_dataset)
    
    trainer.train()
    
    model.save_pretrained('./papuGaPT2_finetuned')
    tokenizer.save_pretrained('./papuGaPT2_finetuned')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fine-tune GPT-2 model on additional training data')
    parser.add_argument('--model_path', type=str, required=True, help='Path to the pre-trained GPT-2 model directory')
    parser.add_argument('--tokenizer_path', type=str, required=True, help='Path to the pre-trained GPT-2 tokenizer directory')
    parser.add_argument('--data_path', type=str, required=True, help='Path to the additional training data text file')
    
    args = parser.parse_args()
    
    go(args.model_path, args.tokenizer_path, args.data_path)
