import pickle

my_list = [(((0.0, 0.0, 0.0), (1000.0, 0.0, 0.0), (0.0, 2.0, 0.0), (1000.0, 2.0, \
0.0), (0.0, 0.0, 1000.0), (1000.0, 0.0, 1000.0), (0.0, 2.0, 1000.0), \
(1000.0, 2.0, 1000.0)), ((0, 2, 3, 1), (4, 6, 7, 5), (1, 3, 7, 5), (4, 6, \
2, 0), (2, 6, 7, 3), (4, 0, 1, 5)), ((255, 0, 0), (255, 128, 0), (255, 255, 0), \
(255, 255, 255), (0, 0, 255), (0, 255, 0)))]


fileName = "py_list_file"
fileObject = open(fileName,'wb')
pickle.dump(my_list,fileObject)   
fileObject.close()

with open('py_list_file.pkl', 'wb') as f:
    pickle.dump(my_list, f)

with open('py_list_file.pkl', 'rb') as f:
    loaded_list = pickle.load(f)

print('Using pickle:')
print(loaded_list)