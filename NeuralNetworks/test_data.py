X_test = []
y_test = []
for i in range(40):
    X_test.append([i % 2, i % 2])
    y_test.append(0 if i % 2 == 0 else 1)
    print(X_test)
    print(y_test)