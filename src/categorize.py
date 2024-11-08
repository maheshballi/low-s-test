# src/categorize.py
def organize_summaries(summaries, categories):
    """
    Organizes summaries into predefined categories based on topic.
    :param summaries: List of summaries.
    :param categories: Dictionary to store categorized summaries.
    :return: Dictionary of categorized summaries.
    """
    for summary in summaries:
        category = summary['category']
        categories[category].append(summary['text'])
    return categories
