from wonderwords import RandomSentence


DEFAULT_NOUNS = ["cat", "mouse"]
DEFAULT_VERBS = ["chase", "play"]
PRESENT_TENSE = ["chases", "plays"]
DEFAULT_ADJECTIVES = ["grey", "furry"]


class TestRandomSentence:
    rs = RandomSentence(
        nouns=DEFAULT_NOUNS,
        verbs=DEFAULT_VERBS,
        adjectives=DEFAULT_ADJECTIVES
    )

    def test_default_configuration(self):
        """Test the default configuration of RandomSentence"""
        gen = RandomSentence()
        data = gen.bare_bone_sentence().split()
        assert len(data) == 3

    def test_semi_default_configuration(self):
        """Test some custom parameters with RandomSentence"""
        gen = RandomSentence(nouns=["human"])
        data = gen.bare_bone_sentence().split()
        assert len(data) == 3 and data[1] == "human"

    def test_bare_bone_sentence(self):
        """Test the bare_bone_sentence method"""
        data = self.rs.bare_bone_sentence().split()
        assert (
            data[0] == "The"
            and data[1] in DEFAULT_NOUNS
            and data[2][:-1] in PRESENT_TENSE
            and data[2].endswith(".")
        )

    def test_simple_sentence(self):
        """Test the simple_sentence method"""
        data = self.rs.simple_sentence().split()
        assert (
            data[0] == "The"
            and data[1] in DEFAULT_NOUNS
            and data[2] in PRESENT_TENSE
            and data[3][:-1] in DEFAULT_NOUNS
            and data[3].endswith(".")
        )

    def test_bare_bone_with_adjective(self):
        """Test the bare_bone_with_adjective method"""
        data = self.rs.bare_bone_with_adjective().split()
        assert (
            data[0] == "The"
            and data[1] in DEFAULT_ADJECTIVES
            and data[2] in DEFAULT_NOUNS
            and data[3][:-1] in PRESENT_TENSE
            and data[3].endswith(".")
        )

    def test_sentence(self):
        """Test the sentence method"""
        data = self.rs.sentence().split()
        assert (
            data[0] == "The"
            and data[1] in DEFAULT_ADJECTIVES
            and data[2] in DEFAULT_NOUNS
            and data[3] in PRESENT_TENSE
            and data[4][:-1] in DEFAULT_NOUNS
            and data[4].endswith(".")
        )
