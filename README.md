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
- with the virtual environment activated, use pip to install all the base Mezzanine and dependencies nicely contained in your virtual environment dir:
    - all OS: `pip install --require-hashes --no-deps -r requirements.txt`
- rename `.env-dist` file to `.env`. There you can override config entries to your local environment.
- with Mezzanine installed, bootstrap a database and superuser:
	- run `python manage.py migrate`
	- create a superuser by running `python manage.py createsuperuser` and filling in sensible values
	- create the pool of static assets for `whitenoise` to host, using `python manage.py collectstatic`

## Running Mezzanine

we can now fire up the Mezzanine instance
- run `python manage.py runserver` (or, same as above, `manage runserver`)
- visit [http://127.0.0.1:8000](http://127.0.0.1:8000)

## For dev work, make sure Mezzanine knows it's on localhost

On a first time run, before you do anything else, navigate to [the "sites" configuration](http://127.0.0.1:8000/admin/sites/site/) for Mezzanine, and change the entry listed from "example.com" to "127.0.0.1:8000" as both the `Domain name` and `Display name`.

## Adding apps

To add a new app to the collection of apps, use `python manage.py startapp AppNameHere` with the obvious substitution of the actual app name you need for the `AppNameHere` string.

There are two apps currently defined, in addition to the general prepackaged Mezzanine app hidden away deep in a pip dependency:

- "`./network`" for stubbing out pages and functionality relating to the Mozilla Network project.
- "`./clubs`" for stubbing out pages and functionality relating to CoSS clubs work.

### Templates, images, css, etc.

Templates are automatically resolved based on model name. For instance, the `club` app defines a model `class Club(Page)`, that is: a model called `Club` that extends Mezzanine's `Page` concept. As such, is associated template that gets used to render the model in the browser is `./templates/pages/club.html`. If we had a model called `Elephant` that implemented a Mezzanine `Page` then its associated template would be `./templates/pages/elephant.html`, and if we had a model called `Orange` that implemented a Mezzanine `Blog` then its associated template would be `./templates/blog/orange.html`.

Static assets that are used in templates such as CSS, images, scripts, etc. go in each app's `static` directory. As such, the club app has two directories:

- `./club/static/img/`
- `./club/static/css/`

In order to have templates use this data, you need to run `python manage collectstatic`, which copies all static assets declared in each app, and copies them over into a master root `./static` dir, which is then used by Mezzanine (technically: whitenoise, a static server that can be used with Django) when rendering CMS content.
