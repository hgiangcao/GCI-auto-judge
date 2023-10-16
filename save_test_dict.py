import numpy as np

data = {
            "student_id": "Not connected!",
            "student_name": "Not connected",
            "task_1": 0,
            "task_2": 0,
            "task_3": 0,
            "task_4": 0,
        }

np.save("res.npy", data)

