def main():
    try:
        text = input().strip()
    except EOFError:
        return

    if not text:
        return

    # پاکسازی ورودی
    cleaned_text = "".join(ch if ch.isalnum() or ch.isspace() else " " for ch in text)
    words = cleaned_text.split()
    word_count = len(words)

    # شمارش حروف یکتا
    letters = [ch.lower() for ch in cleaned_text if ch.isalpha()]
    unique_letter_count = len(set(letters))

    # شمارش پرتکرارترین کلمه
    word_freq = {}
    for word in words:
        word_lower = word.lower()
        for char in word_lower:
            if not char.isalpha():
                word_lower = word_lower.replace(char, "")
        word_freq[word_lower] = word_freq.get(word_lower, 0) + 1

    max_freq = max(word_freq.values()) if word_freq else 0
    most_frequent_words = [word for word, freq in word_freq.items() if freq == max_freq]

    print(word_count)
    print(unique_letter_count)
    print(" ".join(sorted(most_frequent_words)))


if __name__ == "__main__":
    main()
