import unittest
from yml import decode_yaml_file, decode_yaml_content


class TestYamlContent(unittest.TestCase):

    def test_decode_yaml_content(self):
        x = {"hello": "world"}
        y = 'hello: world'
        self.assertEqual(x, decode_yaml_content(y))

    def test_decode_yaml_content_not_empty(self):
        x = ''
        y = 'hello: world'
        self.assertNotEqual(x, decode_yaml_content(y))

    def test_decode_yaml_content_error_int_param(self):
        y = 0
        self.assertRaises(
            TypeError,
            decode_yaml_content(y))

    @unittest.skip('Temporarily skipped')
    def test_decode_yaml_content_error_float_param(self):
        y = 0.0
        with self.assertRaises(TypeError):
            decode_yaml_content(y)


class TestYamlFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.yaml_path = "test.yaml"
        cls.yaml_content = """name: 'my_name'
date: 2017-10-01
metrics:
    percentage:
    value: 87
    trend: stable"""
        with open(cls.yaml_path, "w", encoding="utf-8") as a_file:
            a_file.write(cls.yaml_content)

    @classmethod
    def tearDownClass(cls):
        import os
        os.remove(cls.yaml_path)

    def test_decode_yaml_file(self):
        self.assertEqual(decode_yaml_content(self.yaml_content), decode_yaml_file(self.yaml_path))


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTests([TestYamlContent(), TestYamlFile()])
    suite = unittest.makeSuite('testYaml')
    suite.addTests([TestYamlContent(), TestYamlFile()])
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    print('Errors: ', result.errors)
    print('\nFailures: ', result.failures)
    print('\nSkipped Tests: ', result.skipped)
    print('\nNo. of Tests: ', result.testsRun)
    print('\nSuccess? ', result.wasSuccessful())
