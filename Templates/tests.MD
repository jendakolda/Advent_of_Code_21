# Test template
The following template uses pytest as a test runner. It’s prepared for three different tests, one each for the functions parse(), part1(), and part2():

    # test_aoc_template.py
    
    import pathlib
    import pytest
    import aoc_template as aoc
    
    PUZZLE_DIR = pathlib.Path(__file__).parent
    
    @pytest.fixture
    def example1():
        puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
        return aoc.parse(puzzle_input)
    
    @pytest.fixture
    def example2():
        puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
        return aoc.parse(puzzle_input)
    
    @pytest.mark.skip(reason="Not implemented")
    def test_parse_example1(example1):
        """Test that input is parsed properly"""
        assert example1 == ...
    
    @pytest.mark.skip(reason="Not implemented")
    def test_part1_example1(example1):
        """Test part 1 on example input"""
        assert aoc.part1(example1) == ...
    
    @pytest.mark.skip(reason="Not implemented")
    def test_part2_example2(example2):
        """Test part 2 on example input"""
        assert aoc.part2(example2) == ...
You’ll see an example of how you can use this template later. Until then, there are a few things you should note:

As indicated on line 1, you should name your pytest files with a test_ prefix.
Similarly, each test is implemented in a function named with a test_ prefix. You can see examples of these on lines 20, 25, and 30.
You should change the import on line 5 to import your solution code.
The template assumes that the example data are stored in files named example1.txt and example2.txt.
You should remove the skip marks on lines 19, 24, and 29 when you’re ready to start testing.
You’ll need to fill in the ellipses (...) on lines 22, 27, and 32 according to the example data and the corresponding solutions.
For example, if you were to adapt this template to the rewritten solution of the first part of the Day 1, 2020 puzzle from the previous section, then you’d need to create a file example1.txt with the following contents:

    1721
    979
    366
    299
    675
    1456
Next, you’d remove the skip marks for the first two tests and implement them as follows:

    def test_parse_example1(example1):
        """Test that input is parsed properly"""
        assert example1 == [1721, 979, 366, 299, 675, 1456]
    
    def test_part1_example1(example1):
        """Test part 1 on example input"""
        assert aoc.part1(example1) == 514579
Finally, you’d need to make sure that you’re importing your solution. If you used the filename aoc202001.py, then you should change line 5 to import aoc202001:

    import aoc202001 as aoc
    You would then run pytest to check your solution. If you implemented your solution correctly, then you’d see something like this:
    
    $ pytest
    ====================== test session starts =====================
    collected 3 items
    
    test_aoc202001.py ..s                                     [100%]
    ================= 2 passed, 1 skipped in 0.02s =================
Note the two dots (..) in front of the s. They represent two tests that passed. If the tests had failed, you’d see F instead of each dot, along with a detailed explanation of what went wrong.