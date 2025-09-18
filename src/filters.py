import cv2
import numpy as np


class Filters:
    # TODO: Image kernels
    Kernels = {
        "Original": np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=np.float32),
        "Blur": np.ones((3, 3), dtype=np.float32)/9,
        "Gaussian blur": np.array([[1/16, 1/8, 1/16], [1/8, 1/4, 1/8], [1/16, 1/8, 1/16]]),
        "Sharpen": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]),
        "Sobel (x)": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
        "Sobel (y)": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),
        "Edge detection": np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]),
        "Emboss": np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]),
    }

    def __init__(self, kernels=Kernels):
        self.kernels = kernels
        self.name = None
        # TODO: Implement internal variables

    def apply_filter(self, frame, filter_name) -> np.array:
        kernel = self.kernels[filter_name]
        return cv2.filter2D(frame, -1, kernel)

    def get_current_filter_name(self) -> str:
        if self.name is None:
            k_list = list(self.kernels.keys())
            self.name = k_list[0]
        return self.name

    def switch_next_filter(self):
        k_list = list(self.kernels.keys())
        current_idx = k_list.index(self.name)
        if current_idx+1 < len(k_list):
            self.name = k_list[current_idx+1]
        else:
            self.name = k_list[0]

    def switch_previous_filter(self):
        k_list = list(self.kernels.keys())
        current_idx = k_list.index(self.name)
        if current_idx-1 >= 0:
            self.name = k_list[current_idx-1]
        else:
            self.name = k_list[-1]
