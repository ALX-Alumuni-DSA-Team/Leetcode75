from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        solution = []
        current = ""
        count = 0
        for char in chars:
            if char and char != current:
                if current and count > 1:
                    solution.extend(str(count))
                solution.append(char)
                current = char
                count = 1
            elif not char:
                current = char
            else:
                count += 1
        if count > 1:
            solution.extend(str(count))
        chars.clear()
        chars.extend(solution)
        return len(solution)
