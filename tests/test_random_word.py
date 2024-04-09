from wonderwords import RandomWord, Defaults, NoWordsToChoseFrom

import pytest


class TestRandomWord:
    rw = RandomWord()

    def test_filter_default(self):
        """Test the filter method with default parameters"""
        data = self.rw.filter()
        assert isinstance(data, list) and len(data) == 8166

    def test_filter_starts_with(self):
        """Test the filter method with a custom starts_with parameter"""
        data = self.rw.filter(starts_with="mana")
        assert sorted(data) == sorted(
            ["manage", "manager", "management", "manacle", "manatee"]
        )

    def test_filter_ends_with(self):
        """Test the filter method with a custom ends_with parameter"""
        data = self.rw.filter(ends_with="ala")
        assert sorted(data) == sorted(["impala", "koala"])

    def test_filter_include_categories(self):
        """Test the filter method with a custom include_parts_of_speech
        parameter
        """
        data = self.rw.filter(include_categories=["adjective"])
        assert len(data) == 910

    def test_filter_include_categories_invalid(self):
        """Test the filter method with a custom include_parts_of_speech
        parameter that is invalid
        """
        with pytest.raises(ValueError):
            self.rw.filter(
                include_categories=["I am not a part of speech"]
            )

    def test_filter_word_min_length(self):
        """Test the filter method with a custom word_min_length parameter"""
        data = self.rw.filter(word_min_length=17)
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

    def test_filter_word_min_length_invalid(self):
        """Test the filter method with a custom word_min_length parameter which
        is not of the correct type (int)"""
        with pytest.raises(TypeError):
            self.rw.filter(word_min_length="INVALID")

    def test_filter_word_max_length(self):
        """Test the filter method with a custom word_max_length parameter"""
        data = self.rw.filter(word_max_length=2)
        assert sorted(data) == sorted(
            ["be", "ox", "go", "do", "ad", "TV", "id", "CD"]
        )

    def test_filter_word_max_length_invalid(self):
        """Test the filter method with a custom word_max_length parameter which
        is not of the correct type (int)"""
        with pytest.raises(TypeError):
            self.rw.filter(word_max_length=b"Invalid bytes :(")

    def test_filter_word_lengths_invalid(self):
        """Test the filter method where word_max_length is less than
        word_min_length (invalid)
        """
        with pytest.raises(ValueError):
            self.rw.filter(word_min_length=20, word_max_length=5)

    def test_filter_word_lengths_negative(self):
        """Test the filter method where word_min_length and word_max_length
        are invalid
        """
        data = self.rw.filter(word_min_length=-31, word_max_length=-10)
        assert isinstance(data, list)

    def test_filter_regex(self):
        """Test the regex functionality of the filter method"""
        data = self.rw.filter(regex=".*ea")
        assert sorted(data) == sorted(
            ["guinea", "sea", "tea", "idea", "plea", "area", "pea"]
        )

    def test_random_words(self):
        """Test the random_words method"""
        data = self.rw.random_words(4)
        assert isinstance(data, list) and len(data) == 4

    def test_random_words_not_enough(self):
        """Test the random_words method in which the query returns less results
        than expected
        """
        with pytest.raises(NoWordsToChoseFrom):
            self.rw.random_words(20, starts_with="ag")

    def test_random_words_not_enough_with_return_less_if_necessary(self):
        """Test the random_words method in which the query returns less results
        than expected but with the parameter return_less_if_necessary set to
        True
        """
        data = self.rw.random_words(
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

    def test_word(self):
        """Test the word method"""
        data = self.rw.word()
        assert isinstance(data, str)

    def test_custom_category_without_defaults(self):
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

    def test_custom_category_with_defaults(self):
        """Test a custom category using default values"""
        gen = RandomWord(my_verb=Defaults.VERBS)
        assert gen.word(starts_with="ab") == "abide"
