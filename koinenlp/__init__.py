#! /usr/bin/env python3
# -*- coding: utf-8 -*
#
# koine-nlp.py
# A library for common NLP tasks for Koine Greek
# (c) 2015, 2016 Nathan D. Smith <nathan@smithfam.info>
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


from __future__ import unicode_literals
import unicodedata

# List of stopwords obtained from Perseus Hopper source code and converted to
# UTF-8 with final sigmas.
# http://sourceforge.net/projects/perseus-hopper/
# Path: sgml/reading/properties/stoplists/greek.stop
stopwords = ["μή",
             "ἑαυτοῦ",
             "ἄν",
             "ἀλλ'",
             "ἀλλά",
             "ἄλλος",
             "ἀπό",
             "ἄρα",
             "αὐτός",
             "δ'",
             "δέ",
             "δή",
             "διά",
             "δαί",
             "δαίς",
             "ἔτι",
             "ἐγώ",
             "ἐκ",
             "ἐμός",
             "ἐν",
             "ἐπί",
             "εἰ",
             "εἰμί",
             "εἴμι",
             "εἰς",
             "γάρ",
             "γε",
             "ἡ",
             "ἤ",
             "καί",
             "κατά",
             "μέν",
             "μετά",
             "μή",
             "ὁ",
             "ὅδε",
             "ὅς",
             "ὅστις",
             "ὅτι",
             "οὕτως",
             "οὗτος",
             "οὔτε",
             "οὖν",
             "οὐδείς",
             "οἱ",
             "οὐ",
             "οὐδέ",
             "οὐκ",
             "περί",
             "πρός",
             "σύ",
             "σύν",
             "τά",
             "τε",
             "τήν",
             "τῆς",
             "τῇ",
             "τι",
             "τί",
             "τις",
             "τίς",
             "τό",
             "τοί",
             "τοιοῦτος",
             "τόν",
             "τούς",
             "τοῦ",
             "τῶν",
             "τῷ",
             "ὑμός",
             "ὑπέρ",
             "ὑπό",
             "ὡς",
             "ὦ",
             "ὥστε",
             "ἐάν",
             "παρά",
             "σός"]


def simplify_tag(tag):
    """Simplify the given tag, returning only the POS portion.

    This function may be given as the tag_mapping_function to the
    nltk.corpus.reader.TaggedCorpusReader (or similar) class. This allows the
    argument simplify_tags=True to be passed to tagged_* methods on corpora."""

    # Derived from examples here:
    # http://nltk.googlecode.com/svn/trunk/doc/api/nltk.tag.simplify-pysrc.html

    if '-' in tag:
        tag = tag.split('-')[0]
        return tag
    else:
        return tag


def strip_diacritics(text):
    """Return the given text string with Unicode diacritics removed."""

    # http://stackoverflow.com/a/518232
    decomposed_text = unicodedata.normalize('NFD', text)
    stripped_text = [char for char in decomposed_text if
                     unicodedata.category(char) != 'Mn']
    result_text = ''.join(stripped_text)
    return result_text


def unicode_normalize(text):
    """Return the given text normalized to Unicode NFKC."""

    normalized_text = unicodedata.normalize('NFKC', text)
    return normalized_text


def final_sigma(text):
    """Return the given text with final sigmas normalized to normal sigmas."""

    result_text = text.replace("\u03C2", "\u03C3")
    return result_text


def lowercase(text):
    """Return the given text in lowercase."""

    lowercase_text = text.lower()
    return lowercase_text


def remove_elision(text, diacritics=False):
    """Return the given text with all instances of elision removed.

    Pass diacritics=True if the input text contains diacritics. These
    must be removed for elisions can be detected and removed."""

    # All cases of elision derived from SBLGNT
    elisions = (
        ("αλλ’", "αλλα"),
        ("ανθ’", "αντι"),
        ("απ’", "απο"),
        ("αφ’", "απο"),
        ("δ’", "δε"),
        ("δι’", "δια"),
        ("επ’", "επι"),
        ("εφ’", "επι"),
        ("καθ’", "κατα"),
        ("κατ’", "κατα"),
        ("μεθ’", "μετα"),
        ("μετ’", "μετα"),
        ("μηδ’", "μηδε"),
        ("ουδ’", "ουδε"),
        ("παρ’", "παρα"),
        ("τουτ’", "τουτο"),
        ("υπ’", "υπο"),
        ("υφ’", "υπο")
        )

    if diacritics:
        text = strip_diacritics(text)
    # Standardize on the unicode elision character
    text = text.replace("'", "’")
    for orig, removed in elisions:
        text = text.replace(orig, removed)
    return text

# TODO assimilation - decide scope
# def remove_assimilation(text):
#    """Return the given text with all instances of assimilation normalized."""
#
#    pass


def remove_punctuation(text):
    """Return the given text with punctuation removed."""

    punctuation = [".", ",", ";", "·", "[", "]", "§"]

    for item in punctuation:
        text = text.replace(item, "")
    return text


def normalize(text):
    """Return the given text in a normalized form suitable for indexing.

    Namely, return after converting to lowercase, removing diacritics,
    converting final sigma to sigma, expanding elision to the full
    form and normalizing for unicode.

    """

    text = unicode_normalize(text)
    text = remove_punctuation(text)
    text = lowercase(text)
    text = final_sigma(text)
    text = strip_diacritics(text)
    text = remove_elision(text)
    # text = remove_assimilation(text)

    return text
