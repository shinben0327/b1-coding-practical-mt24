class ControllerPD:
    def __init__(self, kp, kd):
        self.kp = kp  # Proportional gain
        self.kd = kd  # Derivative gain
        self.prev_error = 0  # Error at the previous time step, initialized to 0

    def compute_control_action(self, error):
        control_action = self.kp * error + self.kd * (error - self.prev_error)
        self.prev_error = error
        return control_action
