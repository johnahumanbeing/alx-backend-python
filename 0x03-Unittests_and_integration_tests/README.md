# Project: 0x03. Unittests and Integration Tests

## About

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with

`$ python/python3 -m unittest path/to/test_file.py`

## Resources

#### Read or watch:

* [unittest — Unit testing framework]
* [unittest.mock — mock object library]
* [How to mock a readonly property with mock?]
* [parameterized]
* [Memoization]
## Tasks

| Task | File |
| ---- | ---- |
| 0. Parameterize a unit test | [test_utils.py](./test_utils.py) |
| 1. Parameterize a unit test | [test_utils.py](./test_utils.py) |
| 2. Mock HTTP calls | [test_utils.py](./test_utils.py) |
| 3. Parameterize and patch | [test_utils.py](./test_utils.py) |
| 4. Parameterize and patch as decorators | [test_client.py](./test_client.py) |
| 5. Mocking a property | [test_client.py](./test_client.py) |
| 6. More patching | [test_client.py](./test_client.py) |
| 7. Parameterize | [test_client.py](./test_client.py) |
| 8. Integration test: fixtures | [test_client.py](./test_client.py) |
| 9. Integration tests | [test_client.py](./test_client.py) |