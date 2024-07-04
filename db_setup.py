from indexify import IndexifyClient, ExtractionGraph
client = IndexifyClient()



extraction_graph_spec = """
name: 'testdb'
extraction_policies:
   - extractor: 'tensorlake/chunk-extractor'
     name: 'chunker'
     input_params:
        chunk_size: 1000
        overlap: 100
   - extractor: 'tensorlake/minilm-l6'
     name: 'embeddings'
     content_source: 'chunker'
"""

extraction_graph = ExtractionGraph.from_yaml(extraction_graph_spec)
client.create_extraction_graph(extraction_graph)                                            
