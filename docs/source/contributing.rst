.. _topic_contributing:

========================================
Contributing to Sniffpy
========================================
Thank you for deciding to contribute to Sniffpy. We welcome contributors of all
levels of expertise and are willing to provide guidance when needed. This
document outlines the steps to take to contribute and some general guidelines
and rules about the project. 

* `Setting up the development environment`_
* `Contributing with code`_
* `Contributing with documentation`_
  


.. warning:: Sniffpy uses Git and Github extensively. Troughout, we will assume
	     that you are familiar with these tools. However, if you are not
	     not or there are concepts you need a
	     refresher for, `this guide <https://git-scm.com/book/en/v2>`_ is an
	     excellent resource. 

-------------------------------------------	     
Setting up the development environment
-------------------------------------------	     

Regardless of whether you are contributing to code or documentation you need to
set up an environment in you computer. If you know how to do this you can skip
this section.

^^^^^^^^^^^^^^^^
Getting the code
^^^^^^^^^^^^^^^^

Our project is stored on Github and thus requires you to have an account on the
site to work on it. Once you have done this go to our `repository
<https://github.com/codeprentice-org/snifpy>`_ and fork it (there should be a
button on the top right of the page that allows you to do this.)

Once the repository is forked you need to get a copy of it in your computer.
There are various ways of doing this. One such way is to navigate from your
terminal to the folder you'd like the project to be in and type: ::
  
    git clone https://github.com/<YOUR-USERNAME>/sniffpy.git
    
Doing this should create a directory on your computer with the project inside of it.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Creating a virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To work on the code you will need to use a virtual environment.
If you are a Mac(OS X) or Linux user you can do this easily by going inside of
the project folder from your terminal and typing: ::

  make virtualenv

This will create a virtual environment and will install the required
dependencies inside of it. If you are a Windows user you will need to first
install GNU make. We recommend that to do this you install the
package manager `Chocolatey <https://chocolatey.org/install>`_ and then from the
command line or powershell run: ::
  
  choco install make

If evertying is working properly you should be able to use the make commands
from now on. After installing GNU make simply follow the instructions for Mac
and Linux. 

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Using your virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To use your virtual environment you should go the root directory and from the
command line type ::
  
  source venv/bin/activate

if you are using Mac or Linux, or::

  . \venv\Scripts\activate

if you are using Windows.
To leave your virtual environment type::

  deactivate
  
Remember to always use your virtual environment when testing or modifying
documents or code.

.. note:: If you want to learn more about virtual environments you can read the
	  `official documentation
	  <https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>`_


-----------------------
Contributing with code
-----------------------
To make changes to your repository create a new branch.
**NEVER** user the Master branch. A new branch can be easily created by going
inside of the project directory and issuing the command::
  
  git checkout -b <BRANCH-NAME>

where ``<BRANCH-NAME>`` should be replaced by some name reflective of the changes you
will make to the codebase. This command will create a new branch and place you
inside of it. After this point you can start editing your code.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Important coding standards and Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
There are a couple of standards that you should keep in mind when contributing
and which are neccesary for any code sumbission to be accepted.

* **PEP8**: All the code that you write should follow the PEP8 style guide.
  To make sure that you comply with this standard you should run ::
    
    make checkstyle

  from the code root directory. Running ``make checkstyle`` should return no error.
  Code that doesn't apply PEP8 **won't** be  incorparated in the repo. If you
  are not familiar with PEP8 you can read  about it in `PEP 8
  <https://pep8.org>`_.

* **Python annotations**: As a general rule every function should be annotated. The
  objective of annotations is to make your code more readable to other people.
  If you are not familiar with annotations in python you can read about them in
  `PEP484 <https://www.python.org/dev/peps/pep-0484/>`_ or `here
  <https://realpython.com/lessons/annotations/>`_ for a friendlier
  introduction.

* **Docstrings and Documentation**: Any class, function, etc that is part of the public API should
  have a docstring. Moreover, this docstring should follow the `Sphinx format
  <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html>`_. Additionally,
  any feature that is implemented should have proper documentation to accompany
  it as described in `contributing with documentation`_

* **Tests**: Any function or feature implemented should have tests that verify
  the behaviour is as described. Similarly, any issue that is solved should have
  a test to verify that it indeed has been solved. This project uses pytests for
  testing. The tests that you write should be placed in the ``\tests`` folder in
  an appropiate file and should adhere to the conventions in
  pytests. If you are not familiar with the library you can use the official
  `pytest documentation <https://docs.pytest.org/en/stable/contents.html>`_ to
  get familiar with it. Before, any pull-request you should run the command ::

    make tests

  from the root directory to make sure that all the tests pass. Only code where
  all the tests pass will be accepted. Nevertheless, don't hesitate to ask for
  help from the mantainers when needed.


  
^^^^^^^^^^^^^^^^^^^^^^
Making a Pull Request
^^^^^^^^^^^^^^^^^^^^^^
Once you have fixed the issue and have committed all your changes you should
run::
  
  make push

from the root of the project directory.
This will run all the tests and will check that your code follows the PEP8
guidelines. Fix the problems in your code and re-run ``make push`` till all
tests pass. Once all the tests pass run the command ::
  
  git push

and then direct yourself to your forked copy of the repo on GitHub. From there you will be
able to make a pull request with your changes. 


--------------------------------
Contributing with documentation
--------------------------------




