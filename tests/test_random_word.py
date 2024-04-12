from wonderwords import RandomWord, Defaults, NoWordsToChooseFrom, is_profanity, filter_profanity
from random import Random

import pytest


class TestIsProfanity:
    def test_no_profanity(self):
        assert not is_profanity("apple")

    def test_profanity(self):
        assert is_profanity("  piSS ")


class TestFilterProfanity:
    def test_no_profanity(self):
        words = ["hello", "world", "assassin", "CraZy"]
        output = list(filter_profanity(words))
        assert output == words

    def test_profanity(self):
        words = {"hello", "a55", "world", " aSS  ", "hi", "pIsS "}
        output = set(filter_profanity(words))
        assert output == {"hello", "world", "hi"}


@pytest.mark.parametrize("gen", [RandomWord(enhanced_prefixes=True), RandomWord(enhanced_prefixes=False)])
class TestRandomWord:
    def test_filter_default(self, gen):
        """Test the filter method with default parameters"""
        data = gen.filter()
        assert isinstance(data, list) and len(data) == 8166

    def test_filter_sorting(self, gen):
        """Test that the filter method returns a sorted list."""
        gen = RandomWord(words=["november", "uniform", "alpha", "delta", "bravo"])
        assert gen.filter() == ["alpha", "bravo", "delta", "november", "uniform"]

    def test_filter_starts_with(self, gen):
        """Test the filter method with a custom starts_with parameter"""
        data = gen.filter(starts_with="mana")
        assert sorted(data) == sorted(
            ["manage", "manager", "management", "manacle", "manatee"]
        )

    def test_filter_ends_with(self, gen):
        """Test the filter method with a custom ends_with parameter"""
        data = gen.filter(ends_with="ala")
        assert sorted(data) == sorted(["impala", "koala"])

    def test_filter_include_categories(self, gen):
        """Test the filter method with a custom include_parts_of_speech
        parameter
        """
        data = gen.filter(include_categories=["adjective"])
        assert len(data) == 910

    def test_filter_include_categories_invalid(self, gen):
        """Test the filter method with a custom include_parts_of_speech
        parameter that is invalid
        """
        with pytest.raises(ValueError):
            gen.filter(
                include_categories=["I am not a part of speech"]
            )

    def test_filter_word_min_length(self, gen):
        """Test the filter method with a custom word_min_length parameter"""
        data = gen.filter(word_min_length=17)
        assert sorted(data) == sorted(
            [
                "rehospitalisation",
                "electrocardiogram",
                "industrialisation",
                "great-grandfather",
                "rehospitalization",
                "misrepresentation",
                "cross-contamination",
                "revascularisation",
                "revascularization",
                "great-grandmother",
                "industrialization",
            ]
        )

    def test_filter_word_min_length_invalid(self, gen):
        """Test the filter method with a custom word_min_length parameter which
        is not of the correct type (int)"""
        with pytest.raises(TypeError):
            gen.filter(word_min_length="INVALID")

    def test_filter_word_max_length(self, gen):
        """Test the filter method with a custom word_max_length parameter"""
        data = gen.filter(word_max_length=2)
        assert sorted(data) == sorted(
            ["be", "ox", "go", "do", "ad", "TV", "id", "CD"]
        )

    def test_filter_word_max_length_invalid(self, gen):
        """Test the filter method with a custom word_max_length parameter which
        is not of the correct type (int)"""
        with pytest.raises(TypeError):
            gen.filter(word_max_length=b"Invalid bytes :(")

    def test_filter_word_lengths_invalid(self, gen):
        """Test the filter method where word_max_length is less than
        word_min_length (invalid)
        """
        with pytest.raises(ValueError):
            gen.filter(word_min_length=20, word_max_length=5)

    def test_filter_word_lengths_negative(self, gen):
        """Test the filter method where word_min_length and word_max_length
        are invalid
        """
        data = gen.filter(word_min_length=-31, word_max_length=-10)
        assert isinstance(data, list)

    def test_filter_regex(self, gen):
        """Test the regex functionality of the filter method"""
        data = gen.filter(regex=".*ea")
        assert sorted(data) == sorted(
            ["guinea", "sea", "tea", "idea", "plea", "area", "pea"]
        )

    def test_exclude_with_spaces(self, gen):
        """Test exclude_with_spaces parameter."""
        rw = RandomWord(words=["apple", "contact lens", "car", "dump truck"])
        assert sorted(rw.filter(exclude_with_spaces=True)) == ["apple", "car"]

    def test_random_words(self, gen):
        """Test the random_words method"""
        data = gen.random_words(4)
        assert isinstance(data, list) and len(data) == 4

    def test_random_words_not_enough(self, gen):
        """Test the random_words method in which the query returns less results
        than expected
        """
        with pytest.raises(NoWordsToChooseFrom):
            gen.random_words(20, starts_with="ag")

    def test_random_words_not_enough_with_return_less_if_necessary(self, gen):
        """Test the random_words method in which the query returns less results
        than expected but with the parameter return_less_if_necessary set to
        True
        """
        data = gen.random_words(
            20,
            starts_with="ag",
            return_less_if_necessary=True
        )
        assert sorted(data) == sorted(
            [
                "age",
                "agree",
                "agent",
                "aglet",
                "aggradation",
                "aggression",
                "agony",
                "agreeable",
                "agenda",
                "agriculture",
                "aggressive",
                "agency",
                "agonizing",
                "agreement",
            ]
        )

    def test_random_words_enough_with_return_less_if_necessary(self, gen):
        """Test to see if setting return_less_if_necessary doesn't do anything if there are enough words."""
        data_1 = gen.random_words(5, starts_with="mo", return_less_if_necessary=True)
        data_2 = gen.random_words(5, starts_with="mo", return_less_if_necessary=False)
        assert len(data_1) == len(data_2) == 5

    def test_word(self, gen):
        """Test the word method"""
        data = gen.word()
        assert isinstance(data, str)

    def test_custom_category_without_defaults(self, gen):
        """Test a custom category without using default values"""
        names = ["Bob", "Billy", "Anne", "Max"]
        foods = ["soup", "noodles", "cake", "rice"]
        gen = RandomWord(
            name=names,
            food=foods,
        )
        first_word = gen.word()
        assert (
            (first_word in names or first_word in foods)
            and (gen.word(include_categories=["food"]) in foods)
        )

    def test_custom_category_with_defaults(self, gen):
        """Test a custom category using default values"""
        gen = RandomWord(my_verb=Defaults.VERBS)
        assert gen.word(starts_with="ab") == "abide"

    def test_custom_category_with_mixing(self, gen):
        """Test custom categories mixed with default categories."""
        proper_nouns = ["Austin", "Seattle", "New York"]
        gen = RandomWord(proper_nouns=proper_nouns, common_nouns=Defaults.NOUNS)
        assert set(gen.filter(regex="[Ss]eat.*")) == {"Seattle", "seat"}

    def test_custom_generator_determinism(self, gen):
        """Test a custom random generator and ensure that seeded output is deterministic."""
        gen = RandomWord(rng=Random(10))
        # Should return the same thing in all supported versions of CPython. Will need to update this test if the random
        # implementation is ever changed.
        assert gen.word() == "mortal"
