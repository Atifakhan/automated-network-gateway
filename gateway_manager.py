import os
import subprocess

class GatewayManager:
    def __init__(self):
        pass

    @staticmethod
    def set_gateway(interface, gateway):
        """Set the gateway for the given interface."""
        command = f'netsh interface ip set address name="{interface}" gateway="{gateway}"'
        try:
            subprocess.run(command, check=True, shell=True)
            print(f'Successfully set gateway {gateway} for interface {interface}.')
        except subprocess.CalledProcessError as e:
            print(f'Error setting gateway: {e}')

    def switch_gateway(self, interface, new_gateway):
        """Switch to a new gateway for the given interface."""
        print(f'Switching gateway for {interface} to {new_gateway}...')
        self.set_gateway(interface, new_gateway)

# Example Usage
if __name__ == '__main__':
    gateway_manager = GatewayManager()
    gateway_manager.switch_gateway('Ethernet', '192.168.1.1')