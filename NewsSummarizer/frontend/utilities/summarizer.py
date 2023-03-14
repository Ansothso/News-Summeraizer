import os
import openai
import spacy
from spacy.lang.en import English

API_KEY = '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'

nlp = spacy.load("en_core_web_sm")


<<<<<<< HEAD
openai.api_key = API_KEY
=======
openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.api_key = API_KEY

>>>>>>> 97be65f5c6200fc81d3c9423320116f7643ad869

def text_to_chunks(text):
  chunks = [[]]
  chunk_total_words = 0

  sentences = nlp(text)

  for sentence in sentences.sents:
    chunk_total_words += len(sentence.text.split(" "))

    if chunk_total_words > 1500:
      chunks.append([])
      chunk_total_words = len(sentence.text.split(" "))

    chunks[len(chunks)-1].append(sentence.text)
  
  return chunks

def summarize(text):
    prompt = f"Summarize this in one sentence:\n\n{text}"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=1
    )
    return response['choices'][0]['text']

def get_summary(text):
    chunks = text_to_chunks(text)

    chunk_summaries = []

    for chunk in chunks:
        chunk_summary = summarize(" ".join(chunk))
        chunk_summaries.append(chunk_summary)

    return " ".join(chunk_summaries)