# Code review dashboard

A dashboard to see the status of all opened pull requests. It is configurable and extensible so you can customize the information that is shown for each pull request.

* **Need More Work** build is failing or the CI build has not completed yet.
* **CircleCI Happy** CircleCI build passes but the pull requests have not been approved yet.
* **Approved!** pull requests have been approved by a reviewer.

It also shows in red the pull requests that have been without activity in the configured days, and shows in green the pull requests where the current user has participated.

## Configuration

The dashboard is configured in the `config.py` file. Feel free to edit and adapt it to your needs.

## Running as a Docker container (recommended)

If you prefer to run the dashboard as a Docker container, you just have to build the image and
run the container as follows:

    # Build the Docker image (only the first time)
    docker build -t tetrate/code-review-dashboard .

    # Run the container
    docker run -d -p 80:8080 \
        -e CLIENT_ID=<client id> \
        -e CLIENT_SECRET=<client secret> \
        -e SECRET_KEY=<secret key> \
        tetrate/code-review-dashboard

### Deploying to Kubernetes

The `deployment` folder contains the Kubernetes deployment and service files. You just need to edit the `deployment/config.yml`
and add the values for the client id and secret variables. Then you can just `kubectl apply` all files and you're done.

## Running without Docker

The dashboard uses [Flask](http://flask.pocoo.org/docs/) and [Requests](http://python-requests.org).
You can install them using [Pip](http://www.pip-installer.org) as follows:

    pip install Flask requests

If you don't have *pip* installed, you can install it following the instructions found in the site. It can
be installed in a virtualenv or in the core system. Here is how you can install it in your system. Installing
it into a virtualenv should be the same, once it has been activated:

    # Install setuptools
    wget https://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg#md5=fe1f997bc722265116870bc7919059ea
    sudo sh sh setuptools-0.6c9-py2.4.egg

    # Install pip
    curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    sudo python get-pip.py

Once you have installed the requirements you can run the dashboard as follows:

    python application.py
