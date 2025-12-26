from main import task1, task2, task3, Section, Document, DocSection

sections = [Section(i, f"Раздел {i}") for i in range(1, 5)]
sections.append(Section(5, "белиберда без слова на  Р"))

documents = [
    Document(1, 1, "Документ 1", 100),
    Document(2, 1, "Документ 2", 200),
    Document(3, 2, "Документ 3", 300),
    Document(4, 3, "Документ 4", 400),
]

doc_sections = [
    DocSection(1, 1),
    DocSection(1, 2),
    DocSection(2, 3),
    DocSection(3, 4),
]

def test_task1():
    result = task1(documents, sections)
    assert result[0][0] == "Раздел 1"
    assert result[0][1] == ["Документ 1", "Документ 2"]

def test_task2():
    result = task2(documents, sections)
    assert result[0] == ("Раздел 3", 400)

def test_task3():
    result = task3(documents, sections, doc_sections)
    assert ("белиберда без слова на Р", []) not in result
