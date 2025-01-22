import requests

def count_genbank_entries(genus, start_date, end_date):
    # Base URL for the NCBI Entrez API
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

    # Construct the query
    query = f'"{genus}"[Organism] AND ("{start_date}"[Publication Date] : "{end_date}"[Publication Date])'

    # Parameters for the API request
    params = {
        "db": "nucleotide",  # Database to search (nucleotide)
        "term": query,       # Query term
        "retmode": "json",   # Response format (JSON)
    }

    # Make the HTTP request to the NCBI API
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from NCBI. Status code: {response.status_code}")

    # Parse the JSON response
    data = response.json()

    # Extract the count of entries
    count = int(data.get("esearchresult", {}).get("count", 0))
    return count





# Example usage:
genus = "Paphiopedilum"
start_date = "2007/02/21"
end_date = "2010/11/11"
print(count_genbank_entries(genus, start_date, end_date))