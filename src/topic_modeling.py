from gensim import corpora
from gensim.models import LdaModel
from gensim.utils import simple_preprocess

def train_topic_model(texts, num_topics=4):
    """
    Trains an LDA topic model to identify main topics in text.
    :param texts: List of processed text segments.
    :param num_topics: Number of topics to extract.
    :return: LDA model and dictionary.
    """
    if not texts or all(len(text) == 0 for text in texts):
        print("Error: Texts is empty or has no valid terms.")
        return None, None

    # Convert text to word lists
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    
    # Check if the corpus is empty
    if not any(corpus):
        print("Error: Corpus is empty after processing texts.")
        return None, None

    # Train the LDA model
    lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, random_state=42)
    return dictionary, lda_model

def categorize_by_topic(text, lda_model, dictionary):
    """
    Categorizes text based on the most prominent topic using the LDA model.
    :param text: Processed text segment (tokenized).
    :param lda_model: Trained LDA model.
    :param dictionary: Dictionary used in the LDA model.
    :return: Topic category as a string.
    """
    bow = dictionary.doc2bow(simple_preprocess(text))
    topic_probs = lda_model[bow]
    if not topic_probs:
        return "Uncategorized"

    # Get the most likely topic
    main_topic = max(topic_probs, key=lambda x: x[1])[0]

    # Map topic indices to categories
    topic_mapping = {
        0: "Growth Prospects",
        1: "Key Business Changes",
        2: "Financial Metrics",
        3: "Market and Product Risks"
    }
    return topic_mapping.get(main_topic, "Uncategorized")
