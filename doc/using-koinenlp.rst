Using koine-nlp
===============

The ``normalize()`` function
++++++++++++++++++++++++++++

In the most basic mode of operation, koine-nlp is used to prepare
polytonic Greek text for indexing by normalizing. This done by means
of the omnibus ``normalize()`` function. Example Greek from the `SBLGNT
<http://sblgnt.com/>`_.

>>> import koinenlp
>>> koinenlp.normalize("καὶ ἡ σκοτία αὐτὸ οὐ κατέλαβεν.")
'και η σκοτια αυτο ου κατελαβεν'

Other Functions
+++++++++++++++

The ``normalize()`` function is just a chain of other functions in the
koinenlp module. You can use only certain parts if desirable. For
example, to remove all diacritics, or to remove instances of elision:

>>> koinenlp.strip_diacritics("οὗτος ἦν ἐν ἀρχῇ πρὸς τὸν θεόν.")
'ουτος ην εν αρχη προς τον θεον.'
>>> koinenlp.remove_elision("δι’ αὐτοῦ")
'δια αὐτοῦ'

See the API reference documentation for a full description of
available functions.

Stopwords
+++++++++

koine-nlp contains a list of stopwords which can be removed to keep
them out of the index.

.. note::

   The list of stopwords has not been normalized. You'll want apply
   the same normalizations to the stopwords list as to the text from
   which you are removing them.

>>> text = koinenlp.normalize("ὅσοι δὲ ἔλαβον αὐτόν")
>>> normal_stops = [koinenlp.normalize(word) for word in koinenlp.stopwords]
>>> ' '.join([word for word in text.split() if word not in normal_stops])
'οσοι ελαβον αυτον'
    
The ``simplify_tag()`` function
+++++++++++++++++++++++++++++++

When processing tagged corpora with `NLTK <http://www.nltk.org/>`_, it
is sometimes necessary to provide a function to split the simplified
tag (typically the part-of-speech) from the rest of the tag. The
provided ``simplify_tag()`` function splits based on the hyphen
character and can be passed to NLTK for this purpose.

>>> from nltk.corpus.reader import CategorizedTaggedCorpusReader
>>> lxx = CategorizedTaggedCorpusReader('lxxmorph-corpus/', '\d{2}\..*', encoding=u'utf8', tag_mapping_function=koinenlp.simplify_tag, cat_file='cats.txt')
