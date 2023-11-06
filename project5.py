class CamelCaseConverter:
    def __init__(self, string):
        self.string = string

    def convert_to_camel_case(self):
        words = self.string.split()
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

    def convert(self):
        if self.string:
            return self.convert_to_camel_case()
        else:
            return self.string

input_string = "saya deni dari prodi sistem informasi ITG"
converter = CamelCaseConverter(input_string)
camel_case_output = converter.convert()
print("Input String: " + input_string)
print("CamelCase Output: " + camel_case_output)