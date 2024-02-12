# Proof-of-concept for Concept-based Harmonization of Data Elements Across Health Data standards

## Python Support
Require Python 3.7 or later.

## Steps

1. Install dependencies. 
    ```
    pip install -r requirements.txt
    ```
2. Run `proof_of_concept.py`.

After running, the query results are stored in `query_output.txt`. 

## Folder content
The four folders respectively store: 

- `proof-of-concept/dummy_case.ttl`: the synthetic dataset to be queried for demonstration.
- `de-mappings`: 7 Turtle files (.ttl) storing the mappings between data elements in health data standards.
- `sssom`: 7 Excel files storing the SSSOM tables.
- `value-matching`: 2 Excels files storing the matching between categorical values.
- `proof-of-concept/sparql`: 7 SPARQL files for answering different use cases.
- `data`: 5 Turtle files (.ttl) storing synthetic data (complete).
