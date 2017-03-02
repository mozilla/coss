# The Mezzanine Branch

Good name for a 4 hour costume drama, but this is actually the branch for building out a CoSS prototype for clubs based on the [Mezzanine CMS](http://mezzanine.jupo.org/).

To get this to work:
- make sure you have python3 and git:
    - windows: git-scm.com and python.org, download the relevant installers
    - unix/linux: presumably you know how to get these
    - OSX: use homebrew, and remember to get `python3`, not `python`. Then follow the instructions if there are any.
- make sure you have `virtualenv`:
    - windows: `pip install virtualenv`
    - unix/linux: `sudo pip install virtualenv`
    - OSX: `sudo -H pip3 install virtualenv`
- clone the repo.
- cd into the local coss directory.
- change branch to the "mezzanine" branch.
- create a virtual environment; for consistency with other instructions, call this 'mezzanine':
    - windows: `virtualenv mezzanine`
    - unix/linux: `virtualenv -p /usr/bin/python3 mezzanine`
    - OSX:  `virtualenv -p /usr/local/bin/python3 mezzanine`
- activate the virtual environment:
    - windows: `mezzanine\Scripts\Activate`
    - unix/linux/OSX: `source mezzanine/bin/activate`
- use pip to install all the base Mezzanine and dependencies:
    - windows: `pip install -r requirements.txt`
    - unix/linux: probably the same command
    - OSX: `pip3 install -r requirements.txt` **note the pip3 command**
- with Mezzanine installed, set up a Mezzanine instance called `cmstest`:
    - all OS: `mezzanine-project cmtest`
- cd into the `cmstest` directory
- run `python manage.py createdb` (or if you bound python to your environment, `manage createdb`)
- run `python manage.py runserver` (or, same as above, `manage runserver`)
- visit [http://127.0.0.1:8000](http://127.0.0.1:8000)
