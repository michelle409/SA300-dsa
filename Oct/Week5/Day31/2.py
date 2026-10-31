# Problem: Simplify Path
# Pattern: Stack - process path components
# Time: O(n) | Space: O(n)

def simplifyPath(path):
    parts = path.split('/')
    stack = []
    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(part)
    return '/' + '/'.join(stack)

print(simplifyPath("/home/"))           # "/home"
print(simplifyPath("/../"))             # "/"
print(simplifyPath("/home//foo/"))      # "/home/foo"
print(simplifyPath("/a/./b/../../c/"))  # "/c"