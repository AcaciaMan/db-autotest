import os
import ast

def split_path(path):
    parts = []
    while True:
        path, folder = os.path.split(path)
        if folder:
            parts.append(folder)
        else:
            if path:
                parts.append(path)
            break
    parts.reverse()
    return parts


def analyze(packagedir):
    l_m_object_sub = {}
    f_m_generated_entity = None
    packages = {}
    package_name = None
    for (dirpath, dirnames, filenames) in os.walk(packagedir):
        head, tail = os.path.split(dirpath)

        if head == packagedir:
            packages[dirpath] = tail

        if head in packages:
            package_name = packages[head]

        for filename in filenames:
            if not filename.endswith('.py'):
                continue

            filename = os.path.join(dirpath, filename)

            syntax_tree = ast.parse(open(filename).read(), filename)
            for node in ast.walk(syntax_tree):
                if type(node) == ast.ClassDef:
                    if node.name == 'M_GeneratedEntityDict':
                        f_m_generated_entity=filename
                    d={}
                    d['IS_M_TABLE']=0
                    d['IS_META_DB']=0
                    # if node is subclass of M_Object class
                    for x in node.decorator_list:
                        if type(x) == ast.Name:
                            y: ast.Name = x
                            if y.id == 'M_Object_Decorator':
                                d['M_PACKAGE']=package_name
                                # remove package dir
                                # split path
                                # join back with '.'
                                removed_begining_and_py = filename[len(packagedir):-3]
                                d['M_FILE']='.'.join(split_path(removed_begining_and_py)[1:])
                                d['M_CLASS']=node.name
                                d['M_PARENT']=None
                                if (len(node.bases)>0):
                                    if type(node.bases[0]) == ast.Name:
                                        if node.bases[0].id != 'M_Object':
                                            d['M_PARENT']=node.bases[0].id

                            elif y.id == 'M_Table_Decorator':
                                d['IS_M_TABLE']=1

                            elif y.id == 'M_Meta_DB_Decorator':
                                d['IS_META_DB']=1

                    if len(d.keys())>2:
                        l_m_object_sub[node.name]=d
                            

    return (l_m_object_sub, f_m_generated_entity)

dirpath = r'C:/work/GitHub/db-autotest/Python/src'
# directories = split_path(dirpath)
# print(directories)
print(analyze(dirpath))
