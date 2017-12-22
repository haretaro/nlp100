s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
ans  = {w[0] if i in [1,5,6,7,8,9,15,16,19] else w[:2] : i for i,w in enumerate(s.split(), 1)}
print(ans)
