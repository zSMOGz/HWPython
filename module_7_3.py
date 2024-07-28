class WordsFinder:
    def __init__(self,
                 *file_names: str):
        self.file_names = file_names

    def get_all_words(self):
        removable_substring = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {}
        words = []

        for file_name in self.file_names:
            with open(file_name, "r", encoding='utf-8') as file:
                words.clear()

                for line in file:
                    for substring in removable_substring:
                        line.replace(substring, '')

                    for word in line.split(' '):
                        words.append(word)

                all_words[file_name] = words

        return all_words

    def find(self, finding_word: str):
        all_words = self.get_all_words()
        find_words = {}

        for file, words in all_words.items():
            index = 0
            for word in words:
                index += 1
                if word.find(finding_word.lower()) >= 0:
                    find_words[file] = index
                    break
            find_words[file] = index

        return find_words

    def count(self, search_word: str):
        all_words = self.get_all_words()
        find_words = {}
        search_word = search_word.lower()

        for file, words in all_words.items():
            count_finding_words = 0

            for word in words:
                count_finding_words += word.lower().count(search_word)

            if count_finding_words > 0:
                find_words[file] = count_finding_words

        return find_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
