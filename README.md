## Entertainment Crossing

![Entertainment Crossing Welcome](readme-pics/welcome.png)

Entertainment Crossing is a single page web app built using Flask, jQuery, the Python library Beautiful Soup, and Google's Search API. Use it to discover what projects entertainers have worked on together, according to their IMDb pages. 

![Entertainment Crossing Welcome](readme-pics/results.png)

Once you clone this project, you will want to set up a [`virtual environment`](https://docs.python-guide.org/dev/virtualenvs/). I use `virtualenv` here, which, once installed, can be added to the project via the terminal using 

```
$ cd entertainmentCrossing
$ virtualenv venv
```

Your `venv` can then be activated with `$ . ./venv/bin/activate`. You should now see `$ (venv)` at the front of your command line. Now you can install all of this project's requirements into your environment by running `$ pip3 install -r requirements.txt`. You should see packages being Collected and Downloaded as needed (to see which packages exactly, take a look at the `requirements.txt` file found in the root directory of the project). 

Now, you have everything you need to run the project locally. Run `python3 run.py`, and your server should be ready to go! (You can ignore the warning, as we are not in production deployment.) Check out your localhost (you can copy-paste `http://127.0.0.1:5000/` from the terminal) in a browser and see how it looks! 
