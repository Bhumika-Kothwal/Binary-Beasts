<!-- SETUP INSTRUCTUIONS -->
## Setup Instructions
### Installing the required python modules          
        
> Refreshing package index -
```sh
$ sudo apt update
```
> Installing ```opencv``` module -
```sh
$ sudo apt install python3-opencv
```
> Installing ```imutils``` module -
```sh
$ pip install imutils
```
> Installing ```flask``` module -
```sh
$ pip install flask
```
> Installing ```sounddevice``` module -
```sh
$ python3 -m pip install sounddevice
```
> Installing ```soundfile``` module -
```sh
$ sudo apt-get install -y python-soundfile
```
> Installing ```scipy```, ```numpy```, ```scikit-image``` module -
```sh
$ $ pip install numpy
$ pip install scipy
$ pip install scikit-image
```
> Installing ```dlib``` package- 
  * > Installing CMake, Boost, Boost.Python, and X11 can be accomplished easily with  apt-get: 
  ```sh
  $ sudo apt-get install build-essential cmake
  $ sudo apt-get install libgtk-3-dev
  $ sudo apt-get install libboost-all-dev
  ``` 
  * > Running the command below will download the dlib package from PyPI, automatically configure it via CMake, and then compile and install it on your system.
  ```sh
  $ pip install dlib
  ```
