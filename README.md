{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Road Trip Optimization\n",
    "\n",
    "Use a genetic algorithm to determine the optimal driving route between up to 70 points of interest. \n",
    "\n",
    "Visualize the optimal route in your web browser with Google Maps.\n",
    "\n",
    "<img src=\"images/east_2915_f76_results_map.png\" title=\"optimal route map\" height=\"750\" width=\"750\">\n",
    "\n",
    "Review in tabular form the driving distances and durations between each point of interest in the optimal route.\n",
    "\n",
    "<img src=\"images/east_2915_f76_results_distance_duration.png\" title=\"optimal route driving distances and durations\" height=\"750\" width=\"750\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Acknowledgements"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This project was made possible by [Randal S. Olson](http://www.randalolson.com/) and his notebook, [Computing the optimal road trip across the U.S.](https://github.com/rhiever/Data-Analysis-and-Machine-Learning-Projects/blob/master/optimal-road-trip/Computing%20the%20optimal%20road%20trip%20across%20the%20U.S..ipynb). All credit for the genetic algorithm code and the query Google Maps API code goes to him with a few adjustments made by me. See [data_collection.py](./src/data_collection.py) and [genetic_algorithm.py](./src/genetic_algorithm.py) for more details."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Getting Started"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Download the repository\n",
    "\n",
    "Click  `Clone or download`  and `Download as ZIP`. Once the download is complete, unzip the file and drag it onto your Desktop. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Setup a virtual environment\n",
    "\n",
    "The next step is to create a virtual environment on your computer. This environment will hold the Python version and packages necessary for road trip optimization. We can build the environment using the [Anaconda Distribution](https://www.anaconda.com/what-is-anaconda/), a popular Python data science platform for package management and deployment. If you already have Anaconda installed, move on to the next step. Otherwise, [download Anaconda here](https://www.anaconda.com/download/). \n",
    "\n",
    "To confirm Anaconda is installed correctly, open a terminal window and run:\n",
    "\n",
    "```python\n",
    "conda --version\n",
    "```\n",
    "\n",
    "You should see the installed version number, such as `conda 4.3.27`. If instead you see an error message, reference [Verifying that conda is installed](https://conda.io/docs/user-guide/tasks/manage-conda.html) in the conda documentation.\n",
    "\n",
    "With Anaconda correctly installed, you can use the `environment.yml` file to create a virtual environment on your computer. In the terminal, you need to navigate to the road-trip-optimization directory using the terminal command `cd <folder path>`. Once in the correct directory, run:\n",
    "\n",
    "```python\n",
    "conda env create -f environment.yml\n",
    "```\n",
    "\n",
    "You can now \"enter\" the new virtual environment using the following command:\n",
    "\n",
    "```python\n",
    "source activate road-trip\n",
    "```\n",
    "\n",
    "Verify the road-trip environment was installed correctly using:\n",
    "\n",
    "```python\n",
    "conda list\n",
    "```\n",
    "\n",
    "You should see a list of packages and package versions installed in your environment, such as `python    3.6.6` . If instead you see an error message, reference [Creating an environment from an environment.yml file](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) in the conda documentation."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### *Alternative approach : download necessary packages*\n",
    "\n",
    "You will need `Python 3.5` or greater along with the `pandas`, `googlemaps`, and `jupyter` packages."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Get a Google Maps API key\n",
    "You'll need a Google Maps API key in order to collect driving distance and duration information. Fortunately, these keys are available for free with a Google Account. To get an API key:\n",
    "\n",
    "1. Visit https://developers.google.com/console and log in with your Google Account\n",
    "2. Create a new project\n",
    "3. Enable the Distance Matrix API\n",
    "4. Create a new Server key\n",
    "5. Copy your new API key\n",
    "6. Open your favorite text editor and type:\n",
    "\n",
    "```\n",
    "# Enter your Google Maps API key\n",
    "GOOGLE_MAPS_API_KEY = \"Paste Your API Key Here\"\n",
    "```\n",
    "7. Ensure you pasted your API key between the \"\"s\n",
    "8. Save this file as `config.py` in the road-trip-optimization directory on your Desktop"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Run the program\n",
    "You are now ready to optimize your road trip!\n",
    "\n",
    "Go to the terminal window where you activated your road-trip-optimization environment and run:\n",
    "\n",
    "```\n",
    "jupyter notebook\n",
    "```\n",
    "\n",
    "A window should open in your web browser with what looks like your folder directory. If the window does not open automatically, copy/paste the URL in the terminal to your favorite web browser.\n",
    "\n",
    "Navigate through the folder structure to the `road-trip-optimization` directory on your Desktop. Open the `Road Trip Optimization.ipynb` file.\n",
    "\n",
    "Follow the instructions in the notebook. Press `Shift + Enter` to run the code in each cell.\n",
    "\n",
    "Congratulations you are now a road trip optimizing machine!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
