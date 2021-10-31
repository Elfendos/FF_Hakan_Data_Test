from google.cloud import bigquery
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "firefly-330213-020d47a3ecdb.json"
client = bigquery.Client()


def query_helper(QUERY):
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish
    array = []
    for row in rows:
        array.append(row)
    return array
