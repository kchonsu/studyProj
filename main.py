n = int(input())
parent = {'global': None}
var = {'global': []}
for i in range(n):
    cmd, namespace, arg = input().split()
    if cmd == 'add':
        if namespace in var:
            var[namespace] += [arg]
        if namespace not in var:
            var[namespace] = []
            var[namespace] += [arg]
    if cmd == 'create':
        if namespace in parent:
            parent[namespace] += [arg]
        if namespace not in parent:
            parent[namespace] = []
            parent[namespace] += [arg]
    if cmd == 'get':
        if arg in var[namespace]:
            print(namespace)
        if namespace in var:
            for k, v in parent.items():
                if k == [namespace]:
                    if k in var and arg in var[k]:
                        print(k)
                    else:
                        print('None')
print(parent)
print(var)