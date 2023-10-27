import numpy as np
key_encode = 1234
blank_data = {
            "test_name": "Exercises-2",
            "student_id": "Not connected!",
            "student_name": "Not connected",
            "task_1": -key_encode-1,
            "task_2": -key_encode-1,
            "task_3": -key_encode-1,
            "task_4": -key_encode-1,
        }
np.save("lib/res.npy", blank_data)


blank_user_answer = {
            "task_1_user_answer": None,
            "task_2_user_answer": None,
            "task_3_user_answer": None,
            "task_4_user_answer": None,
        }

np.save("lib/user_answer.npy", blank_user_answer)