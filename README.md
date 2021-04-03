Some notes 
- The action vector consits of 4 values between -1 and 1
- They control the force applied to the hip and knee of both legs [hip1, knee1, hip2, knee2]

- The observation vector (the state of the robot) is made up of 24 values. 
The last 10 are lidar readings, which make more sense in some of the more complicated environments. Here, we'll just focus on the first 14. These are a smattering of angle and velocity values, but fortunately we don't care all that much since we're going to let evolution do the work. 