from djitellopy import Tello
import djitellopy

tello = Tello()

tello.connect()

#Change these to change the ssid and password of the drone. Password has to be a min of 8 characters.
tello.set_wifi_credentials("evilDrone2", "droness425")

tello.end()
