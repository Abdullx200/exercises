import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize('string',
[
'Ik spreeek (lol)', 
'Eten is (lol)'
'nah man ( ksi) allow it (tobi)',
"()))()(("
]
)

def test_matching_parentheses_True(string):
    assert matching_parentheses(string), f'{string} is giving true'


@pytest.mark.parametrize('string',
[
'bruh (brudah,',
'you do be ) bussin',
'(()()))',
"()))()"
]
)

def test_matching_parentheses_False(string):
    assert not matching_parentheses(string), f'{string} is giving false'
