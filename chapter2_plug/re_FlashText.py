from flashtext import KeywordProcessor

# keywordProcessor = KeywordProcessor()
keywordProcessor = KeywordProcessor(case_sensitive=True)
keywordProcessor.add_keyword('Big Apple', 'New York')
keywordProcessor.add_keyword('Bay Area')

keywords_found = keywordProcessor.extract_keywords('I love big Apple and Bay Area.', span_info=True)
print(keywords_found)

keywords = keywordProcessor.get_all_keywords()
print(keywords)

keywordProcessor.add_keyword('New Delhi', 'NCR region')
new_sentence = keywordProcessor.replace_keywords('I love Big Apple and new Delhi.')
print(new_sentence)