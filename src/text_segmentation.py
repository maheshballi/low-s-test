# src/text_segmentation.py
import re

def segment_text_by_speaker(text):
    """
    Splits text into segments based on speaker names and excludes non-informative sections.
    :param text: Cleaned text from PDF.
    :return: List of text segments, each representing a speaker's section.
    """
    # Split text by common speaker patterns (e.g., names and roles)
    segments = re.split(r"(Mr\.|Ms\.|Moderator|Analyst):", text)

    # Combine segments and filter out non-informative or very short segments
    combined_segments = []
    for i in range(1, len(segments) - 1, 2):
        segment = " ".join([segments[i], segments[i+1]]).strip()
        if len(segment) > 30:  # Only keep meaningful segments
            combined_segments.append(segment)
    
    return combined_segments
