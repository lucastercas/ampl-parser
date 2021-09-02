# coding=utf-8
import os

from ampl_parser import AMPLParser


def init_parser(filename: str) -> AMPLParser:
    new_parser = AMPLParser()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    new_parser.match(f"{dir_path}/data/{filename}.mod")
    return new_parser


def test_is_reading_model():
    new_parser = AMPLParser()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    new_parser.read_model(f"{dir_path}/data/refinaria.mod")
    with open(f"{os.path.dirname(__file__)}/data/refinaria.mod") as f:
        expected_content = f.read()
    assert new_parser.model_content == expected_content


def test_should_have_right_number_of_estructures_parsing_var():
    new_parser: AMPLParser = init_parser("only_var")
    assert len(new_parser.model_parsed.children) == 1
    assert len(new_parser.model_parsed.children[0].children) == 2


def test_should_have_right_number_of_estructures_parsing_objectives():
    new_parser: AMPLParser = init_parser("only_objective")
    assert len(new_parser.model_parsed.children) == 1
    assert len(new_parser.model_parsed.children[0].children) == 4


def test_should_have_right_number_of_estructures_parsing_constraints():
    new_parser: AMPLParser = init_parser("only_constraints")
    assert len(new_parser.model_parsed.children) == 1
    assert len(new_parser.model_parsed.children[0].children) == 2
