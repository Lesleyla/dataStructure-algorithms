def minRemoveToMakeValid(self, s: str) -> str:
    idx_to_remove = set()
    stack = []
    for i, c in enumerate(s):
        if c not in "()":
            continue
        if c == "(":
            stack.append(i)
        elif not stack:#c == ) but no ( former: means have to remove this )
            idx_to_remove.add(i)
        else:#is a ()
            stack.pop()
    #if there's remaining "(" in the stack:
    idx_to_remove = idx_to_remove.union(set(stack))
    res = []
    for i, c in enumerate(s):
        if i not in idx_to_remove:
            res.append(c)
    return "".join(res)

#time complexity: O(N) [iterate over the array twice]
#space complexity: O(N) [use extra space: stack and idx array]