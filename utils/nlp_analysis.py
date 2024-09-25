from transformers import pipeline, BertTokenizer

# Load pre-trained BERT NER model and tokenizer
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def extract_skills_with_bert(text):
    """
    Extracts potential skills or relevant entities from the given text using BERT and decodes subwords properly.
    
    Args:
        text (str): The job description or resume text.
    
    Returns:
        skills (list): A list of extracted entities relevant to skills or qualifications.
    """
    ner_results = ner_pipeline(text)
    
    # Extract and decode relevant entities
    skills = []
    for result in ner_results:
        if result['entity'].startswith('I-') or result['entity'].startswith('B-'):
            tokenized_word = result['word']
            # Decode subwords if necessary
            if "##" in tokenized_word:
                decoded_word = tokenizer.decode(tokenizer.convert_tokens_to_ids(tokenized_word))
                skills.append(decoded_word.strip())
            else:
                skills.append(tokenized_word)
    
    return list(set(skills))  # Return unique skills
