import networkx as nx

def read_fastq(file):
    with open(file, "r") as filein:
        for line in filein:
            sequence = next(filein).strip()
            next(filein)
            next(filein)
            yield sequence


def cut_kmer(sequence, k):
    for i in range(len(sequence) - k + 1):
        yield sequence[i:i+k]


def build_kmer_dict(file, k):
    kmer_dict = {}
    for sequence in read_fastq(file):
        for kmer in cut_kmer(sequence, k):
            kmer_dict[kmer] = kmer_dict.get(kmer, 0) + 1
    return kmer_dict



def build_graph(kmer_dict):
    graph = nx.DiGraph()
    for kmer, weight in kmer_dict.items():
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph.add_edge(prefix, suffix, weight = weight)
    return graph

