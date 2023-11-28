class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split(' ')

        output = []
        for x in range(0,len(split)):

            y = split.pop(-1)
            if y.strip() != '':
                output.append(y)

        return ' '.join(output)
