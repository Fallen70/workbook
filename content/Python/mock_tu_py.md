Title: Pytest Cheat Sheat
Date: 2023-07-04 13:44
Category: Python
Lang: fr
Tags: pytest, mock

# Prérequis
 * pytest

# Créer un mock paramétrable

## Code pour le mock:

```python
import pytest

@pytest.fixture( name="mock_func" )
def fixture_mock_func()
	def _mock_func( param1, param2 ):
		returns = { 
			'test1' : { '10' : 'test1_with_value_10', '20': 'test1_with_value_20' },
			'test2' : { '30' : 'test2_with_value_30', '40': 'test2_with_value_40' },
		}
		return returns[param1][param2]
	return _mock_func
```

## Code pour le test:

### One mock patch
```python
from unittest import mock
from app.program import start

def test_with_function_a_mocked( mock_func ):
	mock_patch = "app.program.function_a"
	with mock.patch( mock_patch ) as mck:
		mck.side_effect = mock_func
		
		result = start("test1", "20" )
		
		assert result == "test1_with_value_20"
```

### Multiple mock patch
```python
	mock_patch_1 = "app.program.function_1"
	mock_patch_2 = "app.program.function_2"
	with mock.patch( mock_patch_1 ) as mck_1, \
    with mock.patch( mock_patch_2 ) as mck_2:
		mck_1.side_effect = mock_func_1
		mck_2.side_effect = mock_func_2
```

