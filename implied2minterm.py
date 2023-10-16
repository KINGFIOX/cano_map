class ImpliedMintermGenerator:
    def __init__(self, text) -> None:
        self._minterms = []
        self._generate_minterms(text)

    def _generate_minterms(self, input_str):
        def backtrack(path, remaining_str):
            if not remaining_str:
                # Base case: Add the current path to the minterms list
                self._minterms.append(path)
                return

            current_char = remaining_str[0]

            if current_char == "1":
                backtrack(path + "1", remaining_str[1:])
            elif current_char == "0":
                backtrack(path + "0", remaining_str[1:])
            elif current_char == "-":
                # Branch for don't-care values
                backtrack(path + "1", remaining_str[1:])
                backtrack(path + "0", remaining_str[1:])

        backtrack("", input_str)

    def get_minterms(self):
        return self._minterms


if __name__ == "__main__":
    text = "1---"
    img = ImpliedMintermGenerator(text)
    arr = img.get_minterms()
    print(arr)
    print("hello world")
