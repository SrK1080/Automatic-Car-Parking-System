import numpy as np
import cv2


class Environment:
    def __init__(self, obstacles):
        self.margin = 5
        # coordinates are in [x,y] format
        self.car_length = 80
        self.car_width = 40
        self.color = (255, 0, 0)

        self.car_structure = np.array([[+self.car_length / 2, +self.car_width / 2],
                                       [+self.car_length / 2, -self.car_width / 2],
                                       [-self.car_length / 2, -self.car_width / 2],
                                       [-self.car_length / 2, +self.car_width / 2]],
                                      np.int32)

        self.background = np.ones((1000 + 20 * self.margin, 1000 + 20 * self.margin, 3))
        self.background[10:1000 + 20 * self.margin:10, :] = (0, 0, 0)
        self.background[:, 10:1000 + 20 * self.margin:10] = (0, 0, 0)
        self.render_obstacles(obstacles)

    def render_obstacles(self, obs):
        obstacles = np.concatenate([np.array([[0, i] for i in range(100 + 2 * self.margin)]),
                                    np.array([[100 + 2 * self.margin - 1, i] for i in range(100 + 2 * self.margin)]),
                                    np.array([[i, 0] for i in range(100 + 2 * self.margin)]),
                                    np.array([[i, 100 + 2 * self.margin - 1] for i in range(100 + 2 * self.margin)]),
                                    obs + np.array([self.margin, self.margin])]) * 10
        for ob in obstacles:
            self.background[ob[1]:ob[1] + 10, ob[0]:ob[0] + 10] = 0

    def render(self, x, y, psi):
        # x,y in 100 coordinates
        x = int(10 * x)
        y = int(10 * y)
        # x,y in 1000 coordinates
        # adding car body
        # initializing the rotate struct with base car state
        rotated_struct = self.rotate_car(self.car_structure, angle=psi)
        rotated_struct += np.array([x, y]) + np.array([10 * self.margin, 10 * self.margin])
        rendered = cv2.fillPoly(self.background.copy(), [rotated_struct], self.color)
        rendered = cv2.resize(np.flip(rendered, axis=0), (700, 700))
        return rendered

    def rotate_car(self, pts, angle=0):
        R = np.array([[np.cos(angle), -np.sin(angle)],
                      [np.sin(angle), np.cos(angle)]])
        return (R @ pts.T).T.astype(int)
