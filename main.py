import random

class Section:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Document:
    def __init__(self, id, section_id, title, size):
        self.id = id
        self.section_id = section_id
        self.title = title
        self.size = size

class DocSection:
    def __init__(self, section_id, doc_id):
        self.section_id = section_id
        self.document_id = doc_id


sections = [Section(i, f"Раздел {i}") for i in range(1, 5)]
sections.append(Section(5, "белиберда без слова на  Р"))

documents = [Document(i,random.randint(1, 5), f"Документ {i}", random.randint(100,900)) for i in range(1,8)]

DocSections = [DocSection(random.randint(1,5), random.randint(1,7)) for i in range(8)]

def task1(documents, sections):
    result = []
    for section in sorted(sections, key = lambda s: s.name):
        docs = sorted([doc for doc in documents if doc.section_id == section.id], key=lambda doc: doc.id)
        result.append((section.name, [doc.title for doc in docs]))
    return result

def task2(documents,sections):
    result = []
    for section in sections:
        docs = [doc for doc in documents if doc.section_id == section.id]
        docSum = sum(doc.size for doc in docs)
        result.append((section.name, docSum))
    result = sorted(result, key=lambda section: section[1], reverse=True)
    return result

def task3(documents,sections, DocSections):
    print("Задание 3: Разделы, содержащие слово 'раздел', и документы в них:")
    section_dict = {}
    for docSec in DocSections:
        if docSec.section_id not in section_dict:
            section_dict[docSec.section_id] = [docSec.document_id]
        else:
            section_dict[docSec.section_id].append(docSec.document_id)

    for section in sections:
        if section.id in section_dict and "раздел" in section.name.lower():
            print(f"{section.name}:")
            for doc in documents:
                if doc.id in section_dict[section.id]:
                    print(f"\t{doc.title}")




def main():
    result1 = task1(documents, sections)
    print("Задание 1: Выведите список всех связанных разделов и документов, отсортированных по разделам, сортировка по документам произвольная")
    for cort in result1:
        print(cort[0] + ':')
        for doc in cort[1]:
            print('\t' + doc + ',')

    result2 = task2(documents, sections)
    print("Задание 2: Выведите список разделов с суммарным размером документов в каждом разделе, отсортированный по суммарному размеру.")
    for cort in result2:
        print(cort[0] + ':')
        print('\t' + str(cort[1]))

    task3(documents, sections, DocSections)


if __name__ == "__main__":
    main()
