# automatic-car-parking
#Checking
move_car - 
feasibility check - 
unit tests - 
mutant tests - 
black box - 
Different car sizes - 

Autopark.py takes the arguments and starts initiating different entities. Firstly, it initiates the ParkingLot() in which we define the walls and the cars parked and create an obstacle array with the coordinates of all walls and parked cars

Then we call generate_obstacles() method which generates the coordinates of the parked car using the input coordinates

Third that we initiate the Environment where we initialize the car length and car color and call render_obstacles() method to render the obstacles (walls and parked cars) in the grid.

Lastly we initialize the car which initialize the base state of the car which is car starting coordinates, angle of rotation and the length of tha car

Next we call the render() method of the Environment object in which we call the rotate_car function and fill the car coordinates with the given color and render it on the grid

Lastly we call the move_car function which calls determine_empty_spot() function which finds out the optimal parking spot and update_car_state() updates the final state of the car
