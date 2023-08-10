import spacy

# Load the larger language model
nlp_md = spacy.load('en_core_web_md')

# Load the smaller language model
nlp_sm = spacy.load('en_core_web_sm')

# Define the text examples
cat_text = "The cat sits on the windowsill."
monkey_text = "The monkey swings from tree to tree."
banana_text = "The banana is ripe and yellow."

# Process the texts with the larger model
cat_doc_md = nlp_md(cat_text)
monkey_doc_md = nlp_md(monkey_text)
banana_doc_md = nlp_md(banana_text)

# Process the texts with the smaller model
cat_doc_sm = nlp_sm(cat_text)
monkey_doc_sm = nlp_sm(monkey_text)
banana_doc_sm = nlp_sm(banana_text)

# Calculate similarity between cat and monkey
cat_monkey_similarity_md = cat_doc_md.similarity(monkey_doc_md)
cat_monkey_similarity_sm = cat_doc_sm.similarity(monkey_doc_sm)

# Calculate similarity between cat and banana
cat_banana_similarity_md = cat_doc_md.similarity(banana_doc_md)
cat_banana_similarity_sm = cat_doc_sm.similarity(banana_doc_sm)

# Calculate similarity between monkey and banana
monkey_banana_similarity_md = monkey_doc_md.similarity(banana_doc_md)
monkey_banana_similarity_sm = monkey_doc_sm.similarity(banana_doc_sm)

# Print similarities
print("Similarities using 'en_core_web_md':")
print("Cat-Monkey:", cat_monkey_similarity_md)
print("Cat-Banana:", cat_banana_similarity_md)
print("Monkey-Banana:", monkey_banana_similarity_md)

print("\nSimilarities using 'en_core_web_sm':")
print("Cat-Monkey:", cat_monkey_similarity_sm)
print("Cat-Banana:", cat_banana_similarity_sm)
print("Monkey-Banana:", monkey_banana_similarity_sm)

"""$submit_date = $_POST['date']; if (strtotime(submit_date)<time()){
    echo"date soumise est incorrect";} else{
        echo"the date is correct continue le payement";
    }"""
