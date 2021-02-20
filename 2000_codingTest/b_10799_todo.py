K = list(input())
st = []
result = 0

for i in range(len(K)):
    if K[i] == '(':
        st.append(K[i])
    else:
        if K[i-1] == '(':
            st.pop()
            result += len(st)
        else:
            st.pop()
            result += 1

print(result)
