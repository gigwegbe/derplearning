#!/usr/bin/env python3

from derp.scripts.clone import Clone

class CloneFixSpeed(Clone):

    def __init__(self, config, full_config):
        super(CloneFixSpeed, self).__init__(hw_config, sw_config)


    def plan(self, state):
        # Do not do anything if we do not have a loaded model
        if self.model is None:
            return 0.0, 0.0
        
        # Get the predictions of our model
        predictions = self.predict(state)

        # Speed is fixed based on state
        speed = state['offset_speed']

        # Steer is a simple weighted average of the previous speed and the current
        steer = float(predictions[0])
        
        return speed, steer