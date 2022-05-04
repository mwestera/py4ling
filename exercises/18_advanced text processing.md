# Python for linguists


## 18. Advanced text processing

**18.1.** The first step for text processing is typically tokenization. Use web search to compile your own list of possible Python approaches to **tokenization**. Summarize your findings. (What were your search queries?)

**18.2.** Chances are you found the **spaCy** library, which we will use in the exercises of this section. From the spaCy website, extract an overview of the main functionalities offered by this library.

**18.3.** Which languages does spaCy (claim to) support? Would it be fair to complain that the field of Natural Language Processing (or Artificial Intelligence more generally) does not currently benefit everyone equally? Consider both arguments for and against the validity of this complaint.

**18.4.** What is meant by a 'pipeline' in natural language processing in general, and spaCy in particular? What is the role of a `Doc` object in spaCy?

- - - - - -
**Something to keep in mind:** A pivotal programmers' skill is translating your own problems into those which other people have likely had to solve before you. Concretely, this often means finding a relevant library and learning to use it, by browsing documentation, looking at the library's source code, and searching forums such as StackOverflow. This will also be necessary for the exercises in this section.
- - - - -

**18.5.** Use spaCy to process a number of example strings (for a spaCy-supported language of choice), and find a way to inspect its sentence segmentation. Can you construct examples that _trick_ spaCy into a faulty sentence segmentation (recall from the previous section what kinds of examples can trick the simple approach of splitting on punctuation)?

**18.6.** Find a way to inspect spaCy's word tokenization for a given string. Can you construct example strings that trick spaCy into a faulty word tokenization?

**18.7.** The spaCy word tokenizer is likely better than our own attempt in `text_utils.py`, but how much better? Can you think of a way to assess the quality of a word tokenizer _quantitatively_, by computing some kind of numerical score? Would this score be genre-dependent? Write down a possible approach, step-by-step (no programming required).

**18.8.** How does the spaCy tokenizer work, anyway? Have a look here for the basics: https://spacy.io/usage/linguistic-features#tokenization. Explain in your own words how it identifies the token _N.Y._ in the example, _She said: "Let's go to N.Y.!"_. (For a more detailed understanding, click on "Algorithm details: How spaCy's tokenizer works" and scroll down to the 11-step summary.)

**18.9.** The spaCy **source code** is freely available. Have a look at https://github.com/explosion/spaCy/blob/master/spacy/lang/en/tokenizer_exceptions.py, and scroll through it. Try to understand, if not the exact functioning, at least the relevance of the various portions of code it contains, and appreciate the amount of detail that goes into a library like spaCy, even for something as (seemingly) elementary as tokenization (and for just one language). (Perhaps interesting to note: in some places spaCy relies on regular expressions, e.g., here: https://github.com/explosion/spaCy/blob/master/spacy/lang/en/punctuation.py).

**18.10.** Write code to access, say, the third token of a spaCy `Doc`.

**18.11.** Write code to access, say, the third _sentence_ of a spaCy `Doc`. Since `Doc.sents` returns a generator, you need to collect its elements in a `list` before you can access them by index.

<br>**_Named entities, parts of speech, dependencies_**

**18.12.** Write a function `print_tokens` that takes a spacy-processed document as input, and prints all its tokens, one per line, each accompanied by its _lemma_ (i.e., standardized, inflectionless form), _part of speech_, _dependency_ and _head_, and its _named entity_ label. For instance, for the sentence 'Bob thinks Mary likes him', it should print (among other tokens) `Bob <Bob> (PROPN, nsubj of thinks) [PERSON]` and `likes <like> (VERB, ccomp of thinks) []`. Use this function to inspect spaCy's analysis for a number of simple sentences.

**18.13.** Write a function that takes a spaCy-processed document as input, and returns a `Counter` of all **parts of speech**. In a text of your choice, what are the most common parts of speech?

**18.14.** Write a function that takes a spaCy `Doc` object as input, and returns a Counter of all **named entity** types in the document. In a text of your choice, what are the most common named entity types? Do you expect this to differ between genres?

**18.15.** Read the spaCy documentation about **dependency parses** (https://spacy.io/usage/linguistic-features#dependency-parse). Dependency structure is a framework for syntax that tends to be a bit friendlier toward cross-linguistic generalization and computational applications than _constituency structure_ (the type of syntax you are likely familiar with). Describe in your own words how dependency structure relates to (and differs from) constituency structure.

**18.16.** As a warming-up with dependency parses, use your `print_tokens` function from earlier to inspect the dependency structure of various simple syntactic structures. Try to draw the corresponding dependency trees on a piece of paper.

**18.17.** The root of the dependency tree for a given sentence (or other constituent, e.g., a noun phrase) is accessible with `.root`. Use it to print the root (typically the main verb) of an example sentence. Note that this requires that you access a _sentence_ in the `Doc`, using the `.sents` attribute. Why is there no `.root` attribute on a `Doc` object?

**18.18.** Because of the foregoing, you may find it convenient (for testing some code on a single sentence) to have a function `spacy_sent` that takes a single sentence (as a string), applies spaCy to it, and returns spaCy's analysis of that single sentence directly (instead of the `Doc` object containing it). Define such a function.

- - - - - -
**Something to keep in mind:** In general when programming, but especially when learning to use a new library, it is crucial to keep in mind _what type of object are you working with?_ A string? A spacy `Doc`? A spacy `Span`, such as a sentence? A single token? And also: _what type of object do you need_, in order to solve the task? Different objects offer different methods. Don't hold back on inserting `print(type(...))` statements frequently (during development and debugging) to check what you are dealing with.
- - - - -

**18.19.** Write a function `get_verb_frame` that takes a single spaCy-processed sentence as input and returns a tuple of the main verb with its direct `nsubj` and `dobj` descendants, if present (this is a simplification of all possible verb frames, of course). Note that for sentences with multiple verbs, e.g., 'John noticed that Mary was sad.', only the arguments of the main verb (in this case 'noticed') should be returned.

**18.20.** Consider the function below, and note that it _calls itself_, i.e., it is a **recursive definition**. For a given `sentence` for which you drew a dependency tree earlier (based on the info from `print_tokens`), try to predict the exact order in which that sentence's tokens would get printed by `print_dependency_tree(sentence.root)`. Then test your prediction and verify your understanding. (How come the function calling itself does not result in an infinite loop?)

```python
def print_dependency_tree(token):
    print(f'{token.dep_}: {token.text}')
    for child in token.children:
        print_dependency_tree(child)
```


**18.21.** For increased readability, modify the above function in such a way that each printed token is indented (i.e., prefixed with whitespace) one level further than its parent.

**18.22.** What are _noun chunks_ in spaCy? For some (sufficiently diverse) spaCy `doc`, iterate over the `doc.noun_chunks` and print them. Are pronouns noun chunks? Proper names, including bigrams like 'Sherlock Holmes'? Quantifiers? Can one noun chunk be nested inside another? Can you iterate over the individual tokens of a noun chunk?

**18.23.** Noun chunks, even single-word chunks, lack any part of speech or dependency information (e.g., `chunk.pos_` or `chunk.dep_` don't work). Do you understand why? But noun chunks (or any span of tokens for that matter) do have a `.root` attribute. Can you use this to check whether, e.g., a noun chunk is a grammatical subject?

**18.24.** For some spaCy-supported language, find out _by considering only pronouns_ whether women are referenced more or less frequently than men in a text of your choice. (For which types of text might this be a societally relevant inquiry?)

**18.25.** In the same text, again by considering only pronouns, do women occur more often (than one would expect based on overall frequency) as objects than as subjects, compared to men?

**18.26.** What would be needed to extend the preceding gender analysis to take also proper names into account? And what about common nouns, in phrases such as 'a fireman' and 'the queen'? (No programming required.)

**18.27.** For a text of a (spaCy-supported) language of your choice, write a program to determine which aspectual structure is more common: progressive ('be <verb>+ing' in English) or perfect ('have <verb>+ed').

**18.28.** If you haven't already, check the spaCy documentation about **morphology** (https://spacy.io/usage/linguistic-features#morphology) and enrich your `print_tokens` function from earlier, to print also the `morph` feature of each token. Use it to inspect some progressive and perfect example sentences. Can you use `morph` to improve your solution to the previous exercise?

**18.29.** Write a function `get_path_to_root` that takes a spaCy-processed sentence (not a full `doc`, which does not have a _root_) and a token from that sentence, and returns the dependency path from that token back to the sentence's root. It should return the path as a list of tokens, the first being the start token and the last being the root. This function will likely be useful for the mini-adventure below.

**18.30.** Write a function that takes a spaCy-processed `Doc` as input and returns all _embedded clauses_ (e.g., the italicized parts of 'John knows _that Mary is old_', 'John wonders _if Mary likes him_'). As before, first apply `print_tokens` to a couple of relevant examples, to know what you need to be looking for. (Another tip: for a given token `tok`, use `list(tok.subtree)` to obtain the subtree headed by that token.) Do the results of your function include reported speech (e.g. '_I'm not happy_ he said')? Infinitival complements (e.g., 'I love _to go running with my boyfriend_')?

- - - - - -
**Something to keep in mind:** SpaCy is a powerful and versatile computational tool for linguists, and more so than this section can show. In case you want to learn more, besides browsing the documentation, be sure to check also the free, online spaCy course: https://course.spacy.io/ .
- - - - -

<br>**_Mini-adventure: Question classification_**

_Questions are a window into our soul, but are also often weaponized for rhetorical gain. In this mini-adventure you will create a computational window on questions. It could be very interesting, in future work, to compare the use of questions across genres, e.g., in genuine vs. disinformation tweets, in left-wing vs. right-wing media, in sarcastic vs. serious comments, or in political debates vs. the news._

**18.31.** In Section 17 you used regular expressions to extract _questions_ from a text (namely: sentences ending in a question mark), and you categorized these questions by their **wh-word** (if any). Review your solution there and some of its likely shortcomings (no offense), and consider how spaCy might help.

**18.32.** Define an auxiliary function `extract_wh_word` that takes a spaCy analysis for a given question, and loops through its tokens to find the question's wh-word (if any). Some complexities it should handle (start simple, then try to solve these one at a time):
 - The wh-word is not necessarily the first token in a sentence (e.g., 'And what product did you buy?', 'And you bought what?', 'You went where?'). 
 - Conversely, not every wh-word makes for a wh-question (e.g., 'What John did was bad?', 'Did you like what you bought?', 'Did you see who called?'); these do _not_ count as wh-words (for our purposes). 
 - For an extra challenge, try to handle multiple-wh questions ('Who bought what?'), representing their category by a _tuple_ of wh-words.

 As a starting point, compile a list of challenging questions (e.g., the examples above) and use spaCy and `print_tokens` to inspect their linguistic features, to hopefully come up with plausible rules for detecting genuine wh-words (i.e., ones that make it a wh-question, see above). (Hint 1: Your earlier function `get_path_to_root` may be useful here. Hint 2: spaCy itself can make mistakes, just accept this as a source of error and don't spend too much effort on trying to correct or bypass spaCy.)

**18.33.** Write another auxiliary function, this time for categorizing **non-wh-questions** in a meaningful way. In particular: 
 - Distinguish _interrogative_ non-wh-questions (e.g., 'Did you run?') from so-called _rising declaratives_ (declarative syntax but used as a question, typically indicated by rising intonation, e.g., 'You arrived yesterday?'). 
 - Depending on your source text, you may also encounter many _elliptical questions_, where, e.g., the auxiliary is omitted ('You arrive yesterday?', the tenselessness indicating missing auxiliary 'Did...') or even the main verb (e.g., 'That guy?', meaning 'Is that guy the famous artist you mentioned?'). Assign such verb-elliptical, non-wh-questions to a separate category.

**18.34.** Combine both auxiliary functions into one that takes a question (as a string) and returns its category (or categories), represented as a (tuple of) short string(s) (e.g., the question's wh-word(s) `.lemma_`, or a label like 'DECL' for rising declaratives, etc.).

**18.35.** Apply your categorization function to questions extracted from a text (in a spaCy-supported language of choice), and manually go through the assigned categories. Refine your system where needed (and possible), and in the end inspect a random sample to assess the **accuracy** of your system: What proportion of questions is correctly categorized? Which of your categories is the most heterogeneous, hence, could benefit from a further subdivision?

- - - - - -
**Something to keep in mind:** Whenever you automate part of your linguistic analysis, you must assess its quality. This is typically done by comparing the system's outputs to an expert-annotated **gold standard**. _Accuracy_, or the proportion of responses that are correct, is one metric for quantifying quality. Other common metrics are per-category _precision_ (% of responses of a category X that are correct) and _recall_ (% of actual category X items that are detected).
- - - - -

**18.36.** _(Optional)_ Count the categories assigned to the questions you extracted from a text, and create a _barplot_ of the counts, one bar for each question category. A suitable web query could be 'Python barplot from Counter'.

**18.37.** _(Optional)_ Different wh-words can be used to ask the same type of question, e.g., 'How come', 'Why' and 'For what reason' can all ask for a purpose, and would ideally be given the same category. Conversely, the same wh-word can be used to ask very different types of question, e.g., 'How' in 'How come' vs. 'How many', which should arguably be assigned to distinct categories. Improving your categorization to take this into account would be a substantial but interesting exercise.

**18.38.** _(Optional)_ No further programming, but a brainstorm exercise: How might we collect and categorize so-called 'indirect questions' too, such as _I wonder who failed syntax_, which can be used to 'indirectly' pose the question _Who failed syntax?_. Do you think this could be reliably done? What are some difficulties you anticipate? (You could use your results from exercise 18.26 as data for exploring this issue.)

