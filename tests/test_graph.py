from main import GraphRekomendasi

def test_add_copurchase():
    graph = GraphRekomendasi()

    graph.add_copurchase("P001", "P002")

    assert "P001" in graph.adj

def test_rekomendasi():
    graph = GraphRekomendasi()

    graph.add_copurchase("P001", "P002")
    graph.add_copurchase("P002", "P003")

    hasil = graph.rekomendasi("P001")

    assert "P002" in hasil