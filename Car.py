import cv2
import numpy as np

global empty_spots
cars = {1: [[45, 20]], 2: [[65, 20]],
        3: [[35, 32]], 4: [[65, 32]],
        5: [[35, 44]], 6: [[65, 44]],
        7: [[35, 56]], 8: [[65, 56]],
        9: [[35, 68]], 10: [[65, 68]],
        11: [[35, 80]], 12: [[65, 80]]}


class Car:
    # Constructor to initialize the time, length, x xis, y axis and angle
    def __init__(self, x_0, y_0, psi_0, length):
        self.L = length
        self.x = x_0
        self.y = y_0
        self.psi = psi_0

    # This function will update the state of the car
    def update_car_state(self, x=0, y=0, psi=0):
        self.x = self.x + x
        self.y = self.y + y
        self.psi = psi

    # This function will calculate all the angles and acceleration needed to park the car
    # once the parking spot is found and is feasible
    def park(self, env):
        global empty_spots

        # to_park_x,to_park_y = get_parking_coordinates()

        # self.update_car_state(to_park_x,to_park_y,psi=np.deg2rad(90))

        if empty_spots[0] % 2:
            self.park_left(env)
        else:
            self.park_right(env)

    def park_left(self, env):

        self.update_car_state(y=5, psi=np.deg2rad(90))
        res = env.render(self.x, self.y, self.psi)
        cv2.imshow('environment', res)
        cv2.waitKey(100)

        self.update_car_state(x=-5, y=-5)
        res = env.render(self.x, self.y, np.deg2rad(45))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=-5, y=-5)
        res = env.render(self.x, self.y, np.deg2rad(45))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=-3, y=-3)
        res = env.render(self.x, self.y, np.deg2rad(45))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=-2, y=3)
        res = env.render(self.x, self.y, np.deg2rad(90))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        print("Parking complete")

    def park_right(self, env):
        self.update_car_state(y=5, psi=np.deg2rad(90))
        res = env.render(self.x, self.y, self.psi)
        cv2.imshow('environment', res)
        cv2.waitKey(100)

        self.update_car_state(x=5, y=-5)
        res = env.render(self.x, self.y, np.deg2rad(135))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=5, y=-5)
        res = env.render(self.x, self.y, np.deg2rad(135))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=3, y=-3)
        res = env.render(self.x, self.y, np.deg2rad(135))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=2, y=3)
        res = env.render(self.x, self.y, np.deg2rad(90))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        print("Parking complete")

    # Function to move car
    def move_car(self, env, parking):

        parking_environment = parking.get_cars()
        determine_empty_spot(parking_environment)
        print(parking_environment)
        to_park_x, to_park_y = get_parking_coordinates()
        to_park_y = to_park_y - 12
        for i in range(5):
            self.update_car_state(y=to_park_y / 5 + 3.5, psi=np.deg2rad(90))
            res = env.render(self.x, self.y, self.psi)
            cv2.imshow('environment', res)
            # self.x = i
            cv2.waitKey(100)
        self.park(env)


def get_parking_coordinates():
    global empty_spots

    if empty_spots[0] != len(cars):
        if empty_spots[0] % 2:
            coord = cars.get(empty_spots[0] + 2)
        else:
            coord = cars.get(empty_spots[0] + 1)

        x, y = coord[0]
        print(x, y)
        return x - 12, y - 12
    else:
        pass


def determine_empty_spot(parking_environment):
    global empty_spots
    empty_spots = []
    for i in range(1, len(parking_environment)):
        if i not in parking_environment:
            empty_spots.append(i)
    print(empty_spots)

    return empty_spots
