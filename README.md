# Road Trip Optimization

Use a genetic algorithm to determine the optimal driving route between up to 70 points of interest.

Visualize the optimal route in your web browser with Google Maps.

<img src="images/east_2915_f76_results_map.png" title="optimal route map">

Review in tabular form the driving distances and durations between each point of interest in the optimal route.

<img src="images/east_2915_f76_results_distance_duration.png" title="optimal route driving distances and durations">

## Acknowledgements

This project was made possible by [Randal S. Olson](http://www.randalolson.com/) and his notebook, [Computing the optimal road trip across the US](https://github.com/rhiever/Data-Analysis-and-Machine-Learning-Projects/blob/master/optimal-road-trip/Computing%20the%20optimal%20road%20trip%20across%20the%20U.S..ipynb). All credit for the genetic algorithm code and the query Google Maps API code goes to him with a few adjustments made by me. See [data_collection.py](./src/data_collection.py) and [genetic_algorithm.py](./src/genetic_algorithm.py) for more details.

## Getting Started

### Download the repository

Click  `Clone or download`  and `Download ZIP`. Once the download is complete, unzip the file and drag it onto your desktop.

### Setup a virtual environment with Anaconda

The next step is to create a virtual environment on your computer. This environment holds the Python version and packages necessary for road trip optimization. We can build the environment using the [Anaconda Distribution](https://www.anaconda.com/what-is-anaconda/), a popular Python data science platform for package management and deployment. If you already have Anaconda installed, move on to the next step. Otherwise, [download Anaconda here](https://www.anaconda.com/download/).

To confirm Anaconda is installed correctly, [open a terminal window](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line) and run:

```
conda --version
```

You should see the installed version number, such as `conda 4.3.27`. If instead, you see an error message, reference [verifying that conda is installed](https://conda.io/docs/user-guide/tasks/manage-conda.html) in the conda documentation.

With Anaconda correctly installed, navigate in the terminal to the `road-trip-optimization-master` directory using the command:

```
cd Desktop/road-trip-optimization-master/
```

#### Option 1: Create environment from environment.yml file

Once in the correct directory, you can use the `environment.yml` file to create a virtual environment on your computer using the command:

```
conda env create -f environment.yml
```

This installs the necessary packages and may take some time to finish. Once the process is complete, run:

```
conda info --env
```

to list the virtual environments available on your computer with the active environment identified with an asterisk (*). You should see the new road-trip environment on this list.

Activate the `road-trip` virtual environment by running the following command:

```
source activate road-trip
```

Verify that the `road-trip` environment installed correctly using:

```
conda list
```

You should see a list of packages and package versions installed in your environment, including `googlemaps    2.5.1`, `jupyter    1.0.0`, `pandas    0.23.4`, and `python    3.6.6` . If instead, you see an error message, reference [creating an environment from an environment.yml file](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) in the conda documentation.

#### Option 2: Create an environment and install necessary packages

Once in the correct directory, you can create a `road-trip` virtual environment on your computer using the command:

```
conda create -n road-trip python=3.6.6 pandas=0.23.4 jupyter=1.0.0
```

When prompted to proceed, type `y` and hit `Enter`. This installs the correct version of Python along with the correct versions of the pandas and Jupyter packages into a newly created road-trip virtual environment. Note that each installation may take some time to finish.

Now activate the `road-trip` environment by running:

```
source activate road-trip
```

You need to install one additional package called googlemaps using conda-forge before you are ready to optimize a road trip. Install the `googlemaps` package using the following command:

```
conda install -c conda-forge googlemaps
```

When prompted to proceed, type `y` and hit `Enter`.

Verify your `road-trip` environment is set up correctly using:

```
conda list
```

You should see a list of installed packages and package versions including `googlemaps    2.5.1`, `jupyter    1.0.0`, `pandas    0.23.4`, and `python    3.6.6` . If instead, you see an error message, reference [installing packages](https://conda.io/docs/user-guide/tasks/manage-pkgs.html#installing-packages) in the conda documentation.

### *Alternative without Anaconda: Install necessary packages*

You need `Python 3.5` or greater along with the `pandas`, `googlemaps`, and `jupyter` packages to successfully run the road trip optimization program.

### Get a Google Maps API key

You need a [Google Maps API](https://cloud.google.com/maps-platform/) key to collect driving distance and duration information and to display a map showing the optimal road trip route. These keys are available with a Google Account. 

You must set up a billing account to use the Google Maps Platform. Fortunately, you get $200 in free usage every month. That is enough to optimize multiple road trips for free.  

1. Go to the [Google Cloud Platform Console](https://console.cloud.google.com/getting-started)
2. Click the `navigation menu` button (the three horizontal lines in the upper left-hand corner).
3. Select `Billing`.
4. Set up your billing account.

Now, let's create a `road-trip` project.

1. Click the `navigation menu` button (the three horizontal lines in the upper left-hand corner).
2. Select `Home`.
3. Click on the project drop-down in the top navigation bar.
4. Click `NEW PROJECT`.
5. Enter `road-trip` in the `Project name` field.
6. Click `Create`.

Now, let's enable the necessary APIs.

1. Click on the project drop-down in the top navigation bar.
2. Select the `road-trip` project.
3. Click the `navigation menu` button (the three horizontal lines in the upper left-hand corner).
4. Select `APIs & Services`.
5. Click `+ ENABLE APIS & SERVICES`.
6. Search for and select the `Maps JavaScript API`.
7. Click `ENABLE`.
8. Repeat steps 3-7 for the `Directions API` and the `Distance Matrix API`.

Finally, let's create an API key.

1. Click the `navigation menu` button (the three horizontal lines in the upper left-hand corner).
2. Select `APIs & Services > Credentials`.
3. Click `+ CREATE CREDENTIALS`.
4. Select `API key`.
5. Copy your API key.
6. Open your favorite text editor and type:

```
# Enter your Google Maps API key
GOOGLE_MAPS_API_KEY = "Paste Your API Key Here"
```

7. Ensure you pasted your API key between the " ".
8. Save this file as `config.py` in the `road-trip-optimization-master` directory on your desktop.

One last step! 

1. On your desktop, open the `road-trip-optimization-master` directory.
2. Right click on the `src/results_template.html` file and open it with your favorite text editor.
3. In line 31, find `YOUR_API_KEY` within the URL.
4. Highlight `YOUR_API_KEY` and press `command + V` to paste your Google API key. 
5. Save and close the file.

Success!

### Run the program

You are now ready to optimize your road trip!

Go to the terminal window where you activated your road-trip environment and run:

```
jupyter notebook
```

A window should open in your web browser with what looks like your folder directory. If the window does not open automatically, copy/paste the URL in the terminal into your favorite web browser.

Navigate through the folder structure to the `road-trip-optimization-master` directory on your desktop. Open the `Road Trip Optimization.ipynb` file. Follow the instructions in the notebook and press `Shift + Enter` to run the code in each cell.

Congratulations, you are now a road trip optimizing machine!

## Cleanup

### Road trip optimization notebook

When you finish using the `Road Trip Optimization.ipynb` notebook, go to `File > Save and Checkpoint` to save your progress and `File > Close and Halt` to close the notebook.

Exit the tab with the Jupyter folder directory in your web browser.

Go to the terminal window and press `Control + C` two times to shut down the notebook server.

### Road trip virtual environment

To deactivate the `road-trip` environment, run:

```
source deactivate road-trip
```

If you want to remove the `road-trip` virtual environment from your computer (this is optional), use the command:

```
conda env remove --name road-trip
```

When you are finished, exit the terminal with:

```
exit
```

and close the terminal window.

Cleanup complete!
