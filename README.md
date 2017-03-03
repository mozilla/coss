# The Mezzanine Branch

Good name for a 4 hour costume drama, but this is actually the branch for building out a CoSS prototype for clubs based on the [Mezzanine CMS](http://mezzanine.jupo.org/).

## playing with the CMS on the web

This branch is deployed as web experiment over at https://mezzanine-cms-experiment.herokuapp.com/

## installing things locally

To get this to work:
- make sure you have python3 and git:
    - windows: git-scm.com and python.org, download the relevant installers
    - unix/linux: presumably you know how to get these
    - OSX: use homebrew, and remember to get `python3`, not `python`. Then follow the instructions if there are any.
- make sure you have `virtualenv`:
    - windows: `pip install virtualenv`
    - unix/linux: `sudo pip install virtualenv`
    - OSX: `sudo -H pip3 install virtualenv`
- clone this repository:
    - all OS: find a suitable directory in which you like to manage your git projects (like Documents/git/mozilla, ~/temp, whatever floats your boat) and then in that direcetory, run `git clone https://github.com/mozilla/coss` 
- cd into your local repository copy:
    - all OS: `cd coss`
- change your branch to the "mezzanine" branch:
    - all OS: `git checkout mezzanine`
- create a virtual environment; for consistency with other instructions, call this 'mezzanine':
    - all OS: `virtualenv mezzanine`
- this will create a virtual environment directory called "mezzanine". We then activate the virtual environment:
    - windows: `mezzanine\Scripts\Activate`
    - unix/linux/OSX: `source mezzanine/bin/activate`
    - to deactivate the virtual environment at any point:
        - windows: `mezzanine\Scripts\Deactivate`
        - unix/linus/OSX: simply type `deactivate`
- use pip to install all the base Mezzanine and dependencies nicely contained in your virtual environment dir:
    - all OS: `pip install -r requirements.txt`
- with Mezzanine installed, we can now fire up the `cmstest` instance:
- cd into the `cmstest` directory
- run `python manage.py runserver` (or, same as above, `manage runserver`)
- visit [http://127.0.0.1:8000](http://127.0.0.1:8000)

By default this uses a database that is local to your machine called `dev.db` with a pregenerated superuser called `admin` with the email address `admin@example.org` and password `admin`.
