import os
import AzureTextSummary


def text_summarization():
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import (TextAnalyticsClient,ExtractSummaryAction)

    endpoint = os.environ["AZURE_TEXT_ANALYTICS_ENDPOINT"]
    key = os.environ["AZURE_TEXT_ANALYTICS_KEY"]

    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )

    document = [
        "Document text of What you want to be summarized"
    ]

    poller = text_analytics_client.begin_analyze_actions(
        document,
        actions=[
            ExtractSummaryAction(),
        ],
    )

    document_results = poller.result()
    for result in document_results:
        extract_summary_result = result[0]  # first document, first result
        print("Summary extracted: \n{}".format(" ".join([sentence.text for sentence in extract_summary_result.sentences])))


if __name__ == "__main__":
    text_summarization()