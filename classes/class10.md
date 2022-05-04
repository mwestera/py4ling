# Python for Linguists

## Class 10
1. Mini-exam 9 + discussion
2. Admin: homework time? (12 hours); exam info (open-book/laptop; some pen-and-paper, some computer coding); looking ahead
3. Homework discussion: Sec. 15 (read/write), 16 (sort/count), 17-17.37 (regex)

--- break ---

4. Finish similarity adventure (gensim)
5. Intro NLP pipeline
6. Homework for next time: 17.38-end, 18-18.30 (spaCy)
------

## Similarity adventure notes
- Recap of basic idea.
- Dimensionality reduction.
    1. reduce dimensionality of the space of vectors / of the cooccurrence matrix
    2. while trying to maintain as much of the spatial structure as possible
    3. consequence: only the 'less important' dimensions get reduced (simplification)
       1. variation among the 'less important' dimensions == noise from your data
       2. hence dimensionality reduction allows generalization
    4. resulting dimensions are the more important ones; more like 'semantic primitives' 
       1. e.g., alive vs dead; artefact vs. natural; concrete vs. abstract
- Library: Gensim.
- State of the art?
  - vectors: embeddings
  - after the first neural network distributional semantics revolution (Word2Vec)...
  - ...now we have _contextualized embeddings_ (ELMo & BERT).

## NLP pipeline (with spaCy)

#### spaCy pipeline:

![spacy_pipeline.png](slides/spacy_pipeline.png)

#### spaCy architecture:

![spacy_architecture.png](slides/spacy_architecture.png)
