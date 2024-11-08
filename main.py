from src.pdf_processing import extract_text_from_pdf, clean_text
from src.text_segmentation import segment_text_by_speaker
from src.summarization import summarize_text
from src.topic_modeling import train_topic_model, categorize_by_topic
from src.categorize import organize_summaries
from src.visualization import plot_revenue_trends  # Optional

def main():
    # Step 1: Extract and clean text
    pdf_path = "data/SJS Transcript Call.pdf"
    raw_text = extract_text_from_pdf(pdf_path)
    cleaned_text = clean_text(raw_text)
    
    # Check that text extraction and cleaning worked
    print("Extracted Text (first 500 chars):", raw_text[:500])
    print("Cleaned Text (first 500 chars):", cleaned_text[:500])
    
    # Step 2: Segment the text
    segments = segment_text_by_speaker(cleaned_text)
    
    # Check that segmentation worked
    print("Segments (first 3):", segments[:3])
    
    # Step 3: Summarize each segment, skipping empty or irrelevant ones
    summaries = []
    for segment in segments:
        if len(segment) > 30:  # Only process meaningful segments
            summary_text = summarize_text(segment)
            summaries.append({'text': summary_text, 'category': None})

    # Check that summarization produced meaningful results
    print("Summaries (first 3):", summaries[:3])
    
    # Step 4: Prepare texts for topic modeling
    from gensim.utils import simple_preprocess
    texts = [simple_preprocess(summary['text']) for summary in summaries if summary['text']]
    
    # Ensure texts are not empty before proceeding to topic modeling
    if texts and any(len(text) > 0 for text in texts):
        dictionary, lda_model = train_topic_model(texts)
        
        # Check if LDA model was successfully created
        if lda_model:
            # Step 5: Categorize summaries based on topics
            categories = {
                "Growth Prospects": [],
                "Key Business Changes": [],
                "Financial Metrics": [],
                "Market and Product Risks": []
            }
            
            for summary in summaries:
                category = categorize_by_topic(summary['text'], lda_model, dictionary)
                summary['category'] = category

            # Step 6: Organize and display categorized summaries
            structured_summary = organize_summaries(summaries, categories)
            for key, value in structured_summary.items():
                print(f"\n{key}:")
                for v in value:
                    print(f" - {v}")
        else:
            print("LDA model could not be created due to an empty corpus.")
    else:
        print("No valid texts found for LDA topic modeling.")

    # Optional: Visualize financial metrics (replace with real data if available)
    quarters = ["Q1 FY23", "Q2 FY23", "Q3 FY23", "Q1 FY24"]
    revenue = [1000, 1200, 1300, 1400]  # Replace with actual values if available
    plot_revenue_trends(quarters, revenue)

if __name__ == "__main__":
    main()
