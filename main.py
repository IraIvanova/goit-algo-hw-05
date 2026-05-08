from search_algorithms.kmp import kmp_search
from search_algorithms.boyer_moore import boyer_moore_search
from search_algorithms.rabin_karp import rabin_karp_search
import timeit


def read_file(filename, encoding="utf-8"):
    with open(filename, "r", encoding=encoding) as file:
        return file.read()


def test_algorithms(text, start_pattern, middle_pattern, end_pattern, fake_pattern):
    algorithms = {
        # "KMP": kmp_search,
        "Boyer-Moore": boyer_moore_search,
        "Rabin-Karp": rabin_karp_search,
    }

    patterns = {
        "start": start_pattern,
        "middle": middle_pattern,
        "end": end_pattern,
        "fake": fake_pattern,
    }

    results = {}

    for pattern_type, pattern in patterns.items():
        results[pattern_type] = {}

        for name, algorithm in algorithms.items():
            print(f"Testing {name} with {pattern_type} pattern...")
            execution_time = timeit.timeit(lambda: algorithm(text, pattern))

            results[pattern_type][name] = execution_time

    return results


def print_results(article_name, results):
    print(f"\nResults for {article_name}")
    print("-" * 50)

    for pattern_type, data in results.items():
        print(f"\nPattern type: {pattern_type}")

        for algorithm, execution_time in data.items():
            print(f"{algorithm}: {execution_time:.6f} sec")

        fastest = min(data, key=data.get)
        print(f"Fastest: {fastest}")


def main():
    print("Start analyzing...")
    # article_1 = read_file("texts/article1.txt", "cp1251")
    # print(article_1)
    article_2 = read_file("texts/article2.txt")
    #
    # results_1 = test_algorithms(
    #     article_1, "Вінницький", "запускаємо", "Вікіпедія", "кітпес"
    # )

    results_2 = test_algorithms(
        article_2,
        "Центральноукраїнський",
        "збалансованим",
        "implementation",
        "вигаданий_підрядок",
    )

    # print_results("Article 1", results_1)
    print_results("Article 2", results_2)


if __name__ == "__main__":
    main()
