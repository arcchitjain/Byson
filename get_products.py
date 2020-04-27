import csv
import requests
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from typing import List
from pathlib import Path


data_path = Path(__file__).parent / "data"


class CategoryHierarchy:
    """Hierarchy of categories."""

    def __init__(self, file=data_path / "openfoodfacts.categories.edges.txt"):

        self._edges = defaultdict(list)
        self._graph = nx.DiGraph()
        with open(file) as f:
            reader = csv.reader(f, quotechar='"', quoting=csv.QUOTE_ALL)
            for parent, child in reader:
                parent = self.parse_name(parent)
                child = self.parse_name(child)
                self._edges[child].append(parent)
                self._graph.add_edge(child, parent)

    def get_ancestor_paths(self, category):
        category = self.parse_name(category)
        paths = list()
        queue = [(category,)]
        while len(queue) > 0:
            path = queue.pop()
            if path[-1] in self._edges:
                for parent in self._edges[path[-1]]:
                    queue.append((*path, parent))
            else:
                paths.append(path)
        return paths

    def get_ancestor_graph(self, categories):
        """Get ancestor graph from a set of categories.
        
        Args:
            cut: Whether to create a fine-grained hierarchy by
                cutting the graph.

        """
        categories = [self.parse_name(c) for c in categories]
        ancestors = list()
        for c in categories:
            try:
                ancestors.append(nx.descendants(self._graph, c))
            except:
                pass
        # ancestors = set.union(*[nx.descendants(self._graph, c) for c in categories])
        ancestors = set.union(*ancestors)
        return nx.subgraph(self._graph, ancestors)

    def get_categories(self, categories):
        pass

    @classmethod
    def parse_name(cls, name):
        # remove language tag
        if name[2] == ":":
            name = name[3:]
        # lower
        return name.replace(" ", "-").lower()


class OFFProduct:
    """Wrapper around openfoodfacts product."""

    def __init__(self, barcode):
        result = requests.get(
            "https://world.openfoodfacts.org/api/v0/product/{}.json".format(barcode)
        )
        result.raise_for_status()
        self._raw = result.json()["product"]

    def categories(self) -> List[str]:
        return self._raw["categories_tags"]
    
    def __str__(self):
        return self._raw["product_name"]
    
    def images(self):
        return self._raw["image_front_url"]
    
    def quantity(self):
        for p in self._raw:
            if 'quantity' in p:
                print(p)
        return self._raw["quantity"]


class ProductCollection:
    """Generate hierarchy for a specific set of products."""

    def __init__(self, products: List[OFFProduct]):
        self._products = products
        self._hierarchy = CategoryHierarchy()

    def full_hierarchy(self):

        graphs = list()
        edges = list()
        for p in self._products:
            categories = p.categories()
            graphs.append(self._hierarchy.get_ancestor_graph(categories))
            for c in categories:
                edges.append((str(p), c))
        
        graph = nx.compose_all(graphs)
        for edge in edges:
            graph.add_edge(*edge)

        node_map = list()
        for node in graph:
            is_product = False
            for p in self._products:
                if node == str(p):
                    is_product = True
                    break
            if is_product:
                node_map.append('red')
            else:
                node_map.append('blue')

        plt.figure(figsize=(20, 20))
        nx.draw(graph, with_labels=True, node_color=node_map)
        plt.show()

    @classmethod
    def from_barcodes(cls, barcodes):
        return cls([OFFProduct(barcode) for barcode in barcodes])


if __name__ == "__main__":

    pc = ProductCollection.from_barcodes(
        ["5015552555132", "5449000000996", "5449000011527", "1200101499102"]
    )

    pc.full_hierarchy()

    for p in pc._products:
        print(str(p))
        print("Quantity:", p.quantity())
        print("Front image", p.images())
        print()