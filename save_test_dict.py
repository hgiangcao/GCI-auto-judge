import numpy as np
key_encode = 1234
data = {
            "student_id": "Not connected!",
            "student_name": "Not connected",
            "task_1": -key_encode,
            "task_2": -key_encode,
            "task_3": -key_encode,
            "task_4": -key_encode,
        }

np.save("res.npy", data)

