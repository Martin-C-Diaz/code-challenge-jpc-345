from utils import parse_and_transform

if __name__ == "__main__":
    example_sentences = [
        "Smooth",
        "Space separated",
        "Dash-separated",
        "Number2separated",
        ["hi", "how", "are", "you"],
        245,
        None,
    ]

    for example in example_sentences:
        print(parse_and_transform(example))
