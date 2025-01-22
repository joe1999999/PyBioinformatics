"""Problem

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID 
followed by a list of locations in the protein string where the motif can be found.

N-glycosylation motif is represented as N{P}[ST]{P}.
[XY] means "either X or Y" and {X} means "any amino acid except X.
"""


import re
import requests

def fetchProteinSequence(uniprot_id):
    """
    Fetch the protein sequence for a given UniProt ID.

    :param uniprot_id: UniProt Protein Database access ID
    :return: Protein sequence as a string
    """
    
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch data for UniProt ID {uniprot_id}")
    
    
    # Parse the FASTA format to extract the sequence
    fasta_data = response.text.splitlines()
    sequence = ''.join(line.strip() for line in fasta_data if not line.startswith('>'))
    return sequence

def findNglycosylationMotifs(sequence):
    """
    Find all locations of the N-glycosylation motif in the protein sequence.

    :param sequence: Protein sequence as a string
    :return: List of motif start positions (1-based indexing)
    """
    motif_pattern = r'(?=(N[^P][ST][^P]))'
    return [m.start() + 1 for m in re.finditer(motif_pattern, sequence)]

def analyzeProteins(uniprot_ids):
    """
    Analyze a list of UniProt IDs for the N-glycosylation motif.

    :param uniprot_ids: List of UniProt Protein Database access IDs
    :return: Dictionary mapping UniProt IDs to motif locations
    """
    results = {}
    for uniprot_id in uniprot_ids:
        try:
            sequence = fetchProteinSequence(uniprot_id)
            motif_locations = findNglycosylationMotifs(sequence)
            if motif_locations:
                for OLD_PROTEIN_ID, NEW_PROTEIN_ID in PROTEIN_IDS.items():
                    if NEW_PROTEIN_ID == uniprot_id:
                        results[OLD_PROTEIN_ID] = motif_locations
        except ValueError as e:
            print(e)
    return results

PROTEIN_IDS = {}

def parseIDs(fp):
        
        for oldId in fp:
            newId = oldId[:6]
            PROTEIN_IDS[oldId] = newId
        


with open("proteinIDs.txt") as fp:
    parseIDs(fp)
            



newids= []
for newId in PROTEIN_IDS.values():
    newids.append(newId)

results = analyzeProteins(newids)
for ogId, positions in results.items():
    print(ogId.rstrip("\n"))
    print(f"{" ".join(map(str, positions))}\n")

