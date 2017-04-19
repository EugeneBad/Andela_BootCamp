def words(sentence):

    # Replacing newlines and tabs in the sentence with spaces.
    spaced_sentence = sentence.replace('\n', ' ').replace('\t', ' ')

    # Splitting the sentence at spaces.
    sentence_content = spaced_sentence.split(' ')
    content_count = {}

    for word in sentence_content:

        if len(word) > 0:  # Eliminating empty strings

            if word.isdigit():
                content_count[int(word)] = sentence_content.count(word)

            else:
                content_count[word] = sentence_content.count(word)

    return content_count
