import collections
import os
import ast

def analyze(packagedir):
    stats = collections.defaultdict(int)
    for (dirpath, dirnames, filenames) in os.walk(packagedir):
        for filename in filenames:
            if not filename.endswith('.py'):
                continue

            filename = os.path.join(dirpath, filename)

            syntax_tree = ast.parse(open(filename).read(), filename)
            for node in ast.walk(syntax_tree):
                stats[type(node)] += 1   

    return stats

print("Number of def statements:", analyze(r'C:\work\GitHub\db-autotest\Python')[ast.FunctionDef])
print("Number of class statements:", analyze(r'C:\work\GitHub\db-autotest\Python')[ast.ClassDef])