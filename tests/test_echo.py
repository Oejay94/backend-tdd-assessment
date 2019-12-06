#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# Your test case class goes here


class TestEcho(unittest.TestCase):

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ['python', './echo.py', '-h'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open('./USAGE', 'r').read()

        self.assertEquals(stdout, usage)

    def test_parser(self):
        parser = echo.create_parser()
        args_list = ["-ult", "hello"]
        result = parser.parse_args(args_list)
        self.assertTrue(result.upper)
        self.assertTrue(result.lower)
        self.assertTrue(result.title)
        self.assertEqual(result.text, "hello")

    def test_upper(self):
        args_list = ["-u", "hello"]
        self.assertEqual(echo.main(args_list), "HELLO")

    def test_upper_long(self):
        args_list = ["--upper", "hello"]
        self.assertEqual(echo.main(args_list), "HELLO")

    def test_lower(self):
        args_list = ["-l", "HELLO"]
        self.assertEqual(echo.main(args_list), 'hello')

    def test_lower_long(self):
        args_list = ["--lower", "HELLO"]
        self.assertEqual(echo.main(args_list), "hello")

    def test_title(self):
        args_list = ["-t", "hello"]
        self.assertEqual(echo.main(args_list), "Hello")

    def test_title_long(self):
        args_list = ["--title", "hello"]
        self.assertEqual(echo.main(args_list), "Hello")

    def test_all(self):
        args_list = ["-tlu", "heLLo"]
        self.assertEqual(echo.main(args_list), "Hello")

    def test_none(self):
        args_list = ["piero"]
        self.assertEqual(echo.main(args_list), "piero")


if __name__ == '__main__':
    unittest.main()
