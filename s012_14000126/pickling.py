import pickle

#
# data = [
#     {
#         'key1': 1,
#         'key2': 2,
#         'key-name': 'akbar',
#     },
#     (1, 2, 3, 4),
#     'A String!'
# ]
#
#
# pickled = pickle.dumps(data)
# print('PICKLED:', pickled)  # ???
# # unpickled = pickle.loads(pickled)
# # print('UN-PICKLED:', unpickled)  # ???


with open('code', 'rb') as f:
    with open('code_pickle.txt', 'wb') as f2:
        pickle.dump(f.read(), f2)

with open('code_pickle.txt', 'rb') as f:
    exec(pickle.load(f))
