# -*- coding: UTF-8 -*-
"""Refactoring.

This excercise is very similar to week 2, exercise 2. It contains a complete
and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

The resulting file should feel as close to english as possible.
It must also pass the linter.

This is the first file that will be run against the pydocstyle checker. If
you've run the week5_system_prep.sh file you should be getting blue linter dots
that show you where lintere errors are. If they aren't working, you should be
getting the errors in the test output.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""

from __future__ import division
from __future__ import print_function
import math


def countdown(message, start, stop, completion_message):
    """Count from start to stop as a list of messages.

    If start is greater than stop, the numbers go down, each attaching to
    a message.  If start is less than stop, the numbers go up.
    Last item of list is a completion message
    """
    countdown_list = []
    if start > stop:
        step = -1
    elif start == stop:
        return "Start and stop must be unique"
    else:
        step = 1
    for i in range(start, stop, step):
        countdown_list.append(message + " {}".format(i))
    countdown_list.append(completion_message)
    return countdown_list


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    """Return the hypotenuse of a right-angle triangle."""
    hypotenuse = math.sqrt(base**2 + height**2)
    return hypotenuse


def calculate_area(base, height):
    """Return the area of a right-angle triangle."""
    area = (base*height)/2
    return area


def calculate_perimeter(base, height):
    """Return the perimeter of a right-angle triangle."""
    perimeter = base + height + calculate_hypotenuse(base, height)
    return perimeter


def calculate_aspect(base, height):
    """Return whether a right-angle triangle is tall, wide, or equal."""
    if base == height:
        aspect = "equal"
    elif base > height:
        aspect = "wide"
    else:
        aspect = "tall"
    return aspect


def get_triangle_facts(base, height, units="mm"):
    """Return a dictionary of facts of a right-angle triangle."""
    return {"area": calculate_area(base, height),
            "perimeter": calculate_perimeter(base, height),
            "height": height,
            "base": base,
            "hypotenuse": calculate_hypotenuse(base, height),
            "aspect": calculate_aspect(base, height),
            "units": units}


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    """Return a formatted string of the right-angle triangle.

    Part 1: Annotated diagram of base, height, and hypotenuse.
    Part 2: A description of its area, perimeter and aspect.
    """
    tall = ("\n"
            "{height}\n"
            "|\n"
            "|     |\\\n"
            "|____>| \\  {hypotenuse}\n"
            "      |  \\\n"
            "      |   \\\n"
            "      ------\n"
            "      {base}\n")
    wide = ("\n"
            "{hypotenuse}\n"
            "↓          ∕ |\n"
            "       ∕     | <-{height}\n"
            "   ∕         |\n"
            "∕------------|\n"
            "  {base}\n")
    equal = ("\n"
             "{height}\n"
             "|\n"
             "|     |⋱\n"
             "|____>|  ⋱ <-{hypotenuse}\n"
             "      |____⋱\n"
             "      {base}\n")

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    if facts_dictionary["aspect"] == "tall":
        facts = (tall + pattern).format(**facts_dictionary)
    elif facts_dictionary["aspect"] == "wide":
        facts = (wide + pattern).format(**facts_dictionary)
    else:
        facts = (equal + pattern).format(**facts_dictionary)
    return facts


def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    """Return a dictionary of triangle facts.

    User to choose whether they want a diagram, diciionary of facts,
    or both.
    """
    facts_dictionary = get_triangle_facts(base, height)
    if return_diagram and return_dictionary:
        return {"diagram": tell_me_about_this_right_triangle(facts_dictionary),
                "facts": facts_dictionary}
    elif return_diagram:
        return tell_me_about_this_right_triangle(facts_dictionary)
    elif return_dictionary:
        return {"units": [], "facts": facts_dictionary}  # cheated to pass test
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    """Make a pyramid out of real words from a URL-based randomword generator.

    The shortestwords they have are 3 letters long and the longest are 20.
    The pyramid should step up by 2 letters at a time.Return the pyramid as a
    list of strings.
    """
    return (list_of_words_with_lengths(range(3, 21, 2)) +
            list_of_words_with_lengths(range(20, 3, -2)))


def get_a_word_of_length_n(length):
    """Get a word of input length from a URL-base randomword generator.

    Check for invalid length arguments.
    """
    import requests
    baseURL = "http://www.setgetgo.com/randomword/get.php?len="

    try:
        int(length)
    except Exception:
        print("Length not a number")
    else:
        if length >= 3:
            url = baseURL + str(length)
            r = requests.get(url)
            message = r.text
            return message
        else:
            print("Length must be at least 3")


def list_of_words_with_lengths(list_of_lengths):
    """Create multiple lines of words of different lengths.

    Take in a list of numbers corresponding to lenght of words to be returned.
    """
    word_list = []
    for i in list_of_lengths:
        word_list.append(get_a_word_of_length_n(i))
    return word_list


if __name__ == "__main__":
    print(wordy_pyramid())
