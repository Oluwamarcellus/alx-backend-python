#!/usr/bin/env python3
"""
to_kv module
"""
from typing import Union


def to_kv(k: str, v: (int | float)) -> tuple[str, Union[(int, float)]]:
    """
    a type-annotated function to_kv that takes a string k and an
    int OR float v as arguments and returns a tuple
    """
    return (k, v)
