import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        numpy_list = np.array(list)
        splited = np.array(np.split(numpy_list, 3))
        abc = splited.sum(axis=0)
        print(abc)
        calculations = np.array({'mean': [splited.mean(axis=0).tolist(), splited.mean(axis=1).tolist(), np.mean(numpy_list)],
                                 'variance': [splited.var(axis=0).tolist(), splited.var(axis=1).tolist(), np.var(numpy_list)],
                                 'standard deviation': [splited.std(axis=0).tolist(), splited.std(axis=1).tolist(), np.std(numpy_list)],
                                 'max': [splited.max(axis=0).tolist(), splited.max(axis=1).tolist(), np.max(numpy_list)],
                                 'min': [splited.min(axis=0).tolist(), splited.min(axis=1).tolist(), np.min(numpy_list)],
                                 'sum': [splited.sum(axis=0).tolist(), splited.sum(axis=1).tolist(), np.sum(numpy_list)]
                                 })
    return calculations