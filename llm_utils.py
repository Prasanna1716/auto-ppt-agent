from huggingface_hub import InferenceClient

HF_TOKEN = "your_token_here"
client = InferenceClient(token=HF_TOKEN)

MODEL = "Qwen/Qwen2.5-7B-Instruct"


def generate_slide_plan(topic):

    return [
        f"Introduction to {topic}",
        f"Why {topic} Matters",
        f"Key Concepts",
        f"Tools & Workflow",
        f"Real-World Applications",
        f"Conclusion / Thank You"
    ]


def generate_slide_content(title):

    prompt = f"""
    Create content for a PowerPoint slide titled: {title}

    Requirements:
    - 4 short bullet points (one line each)
    - Add 1 short humorous or smart quote at the end
    - Student-friendly tone
    - Minimal text
    - Slight humor allowed

    Format:
    Bullet 1
    Bullet 2
    Bullet 3
    Bullet 4
    Quote: ...
    """

    try:
        response = client.chat_completion(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )

        text = response.choices[0].message["content"]

    except:
        return [
            "Simple concept explanation",
            "Useful in real-world",
            "Easy to understand",
            "Widely used today",
            "Quote: Keep it simple 😄"
        ]

    lines = text.split("\n")

    points = []
    for line in lines:
        line = line.strip().replace("*", "")
        if len(line) > 3:
            points.append(line)

    return points[:5]