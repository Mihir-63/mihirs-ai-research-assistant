from transformers import pipeline

MODEL_NAME = "google/flan-t5-base"

summarizer = pipeline(
    "text2text-generation",
    model=MODEL_NAME,
    max_new_tokens=250
)

def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

def load_prompt():
    base_dir = os.path.dirname(__file__)  # api/
    prompt_path = os.path.join(base_dir, "summary.txt")

    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()

def summarize_chunks(chunks, max_chunks=3):
    prompt_template = load_prompt()
    summaries = []

    for chunk in chunks[:max_chunks]:
        prompt = prompt_template.replace("{text}", chunk)
        result = summarizer(prompt)[0]["generated_text"]
        summaries.append(result)

    return "\n\n".join(summaries)
