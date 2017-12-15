s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
ans = [len(w.strip(',').strip('.')) for w in s.split(' ')]
print(ans)
