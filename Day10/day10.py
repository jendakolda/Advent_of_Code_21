opening = ('([{<')
closing = (')]}>')
pairs = ('()', '[]', '{}', '<>')
err_scoring = {')': 3, ']': 57, '}': 1197, '>': 25137}


with open('day10_input.txt', 'r', encoding='utf-8') as f:
    chunks = f.read().split('\n')

err_score = 0
all_scores = []

for chunk in chunks:
    try:
        stack = []
        for i in chunk:
            if i in opening:
                stack.append(i)
            elif i in closing and stack[-1] + i in pairs:
                stack.pop()
            else:
                err_score += err_scoring[i]
                raise StopIteration()
        ok_score = 0
        for j in reversed(stack):
            ok_score *= 5
            match j:
                case '(':
                    ok_score += 1
                case '[':
                    ok_score += 2
                case '{':
                    ok_score += 3
                case '<':
                    ok_score += 4
        all_scores.append(ok_score)
    except StopIteration:
        pass
all_scores.sort()

print('Part A:', err_score)
print('Part B:', all_scores[len(all_scores) // 2])




