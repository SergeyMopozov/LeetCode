
class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result = []
        buffer = []
        for c in s:
            if c != '#':
                buffer.append(c)
            else:

                if len(buffer) > 2:
                    for b in buffer[:-2]:
                        result.append(alphabet[int(b)-1])

                    result.append(alphabet[int(''.join(buffer[-2:]))-1])
                    buffer = []
                else:
                    result.append(alphabet[int(''.join(buffer))-1])
                    buffer = []

        for b in buffer:
            result.append(alphabet[int(b)-1])

        return ''.join(result)


sol = Solution()
s = "1326#"
print(sol.freqAlphabets(s))

