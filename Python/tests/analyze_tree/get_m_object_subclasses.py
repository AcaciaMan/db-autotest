import os
import ast

def analyze(packagedir):
    l_m_object_sub = []
    for (dirpath, dirnames, filenames) in os.walk(packagedir):
        for filename in filenames:
            if not filename.endswith('.py'):
                continue

            filename = os.path.join(dirpath, filename)

            syntax_tree = ast.parse(open(filename).read(), filename)
            for node in ast.walk(syntax_tree):
                if type(node) == ast.ClassDef:
                    # if node is subclass of M_Object class
                    for x in node.bases:
                        if type(x) == ast.Name:
                            y: ast.Name = x
                            if y.id == 'M_Object':
                                l_m_object_sub.append((filename, node.name))
                                break 

    return l_m_object_sub

print(analyze(r'C:\work\GitHub\db-autotest\Python\src'))
