### Project Outline

This project aims to produce a set of IPython notebooks to support an Intermediate Python video class of approximately six hours duration. While the class will be commercial the publisher has agreed to the publication of the notebooks under a Creative Commons license allowing both commercial and non-commercial uses.

Since the project is running to tight timescales assistance in developing the content will be much appreciated.

__What Can I Do?__  
Most urgent at present is the review of the existing notebook content and suggestions for content -
particularly suggestions for what you'd like to see in the dauntingly long list of unstarted topics listed in `unstarted.txt`. Some portions of the outline may have to be cut anyway, as it looks like there is more than six hours material in it, so it will be good to have evidence of demand.

The notebooks vary in both style and length. Some contain only code. Some are heavily annotated as a preliminary video script. Currently the code is much more important than the annotations. Over time, though, the published notebooks will be increasingly annotated to increase their utility.

Those in the Portland area can sign up for in-person review sessions that focus on topics needing content and filling in gaps in participant's knowledge through interactive us of the IPython notebook. These notebooks will be shared with the participants after each session. [URL to follow]

Reviewers showing promise may be invited to become committers on the project, but at present we aren't set up to handle pull requests on this project, which is simply the contents of the latest nightly dump.

NOTE: This material will be released under a Collective Commons license, allowing free use for both commercial and non-commercial purposes.

#### Project Structure

You will find the following items in this project:

  * `outline.txt`, the indented and annotated table of contents
  * `unstarted.txt`, a list of unstarted topics
  * `nbstats.txt`, some statistics on the notebook content
  * A `notebooks` directory containing the most recently-released content
    * An `images` subdirectory containing graphical images used in notebooks

Any other files or directories you find in there are not yet a permanent part of the project structure.


### Running IPython Notebooks in the Cloud

First you need to have a Google account (which is also your Notebook Cloud Server account - it's an Appspot app) and an Amazon AWS account. None of this costs anything, and even if you aren't helping with the project this is a really easy way to access Python.

___Signing Up for Notebook Cloud Services___  
All the computing you need to evaluate these notebooks (and a whole bunch more!) can be accomplished with virtuals that qualify for Amazon's free-tier pricing. Free-tier remains free for the first twelve months, and it's unlikely anything you do will exceed the very generous limits. To sign up for an AWS account:

  * Visit the <a href="http://aws.amazon.com" target="_blank">Amazon AWS home page</a>
  * Click the “Sign Up” link
  * Enter an email address, select “I am a new user” and click “Sign in ..”

Once you have opened your account (there's the usual "please confirm" email with a link) you need to sign up with Notebook Cloud, a Google AppSpot application that uses AWS services on your behalf to create virtual machines running the IPython Notebook server on demand.

  * Visit the <a href="http://notebookcloud.appspot.com" target="_blank">notebook cloud</a> home page
  * Take a quick look at the simple documentation
  * Click "Log in with Google Account"
  * Once logged in, click the "Account Details" button,
    enter your AWS credentials (instructions how to get them are shown)
    and click "Save"

NOTE: you can password-protect all your notebooks by entering a password on this form. There is no mechanism to rerieve this password - you have been warned!

___Using the Notebook Cloud Service___  
You are now looking at the IPython Notebook Cloud server control window. For this purpose you only need to start the very smallest instance.

  * Click the "Micro" button to create a new Notebook Server

It will take a minute or two to create a new virtual machine. The Cloud server monitors the status of the virtual machine. Wait until it says "Serving" on the status line under the machine description, you are looking for something like

  __Instance id: i-706d2551    Type: t1.micro    Started: 01:04:36 ~ 2014-03-11__  
    __State__: Serving

Click on the word "serving" and a new window will open up with a notebook server showing an empty list of files. You can then drag Notebook (`.ipynb`) files into the (initially empty) files list, and an upload button appears. After uploading a notebook you can start it. Each notebook appears in its own browser window or tab.

After updating a notebook you can download a copy with the Notebook Server's "File | Download As ..." menu item. This allows you to download either a Python file (in which all the markdown text appears as comments) or a Notebook file that you can upload to another server if you want.

Your notebooks persist on the server between sessions. You can choose, though it's not necessary, to shut them down before closing or shutting down the Notebook Server.
When you are done, you might want to shut your Notebook Server down. There's no point leaving the clock ticking when it's not being used, but at the same time it costs hardly anything. I just don't like waste, you could be computing with those cycles. :)

In the Cloud Server window click the "Stop" button next to your chosen virtual. It takes a while (maybe up to a minute: what do you care, it's free, right?) to shut down a running virtual. The next time you visit your Notebook Cloud account (or even immediately!) you can restart it by clicking on its "Start" button.

The "Terminate" button removes the VM instance completely, destroying its file store (so better make sure that you have downloaded copies of all Notebooks you may want to keep before you terminate an instance).

___Reviewing the Course Content___  
Download the project (presumably you will simply clone the repository, but however). Upload them to your Notebook Cloud server and start them.

You can step through the notebook cell by cell using the SHIFT/Enter conbination. Alternatively you can select "Cell | Run All" from the notebook server menu and then scroll through the completed notebook to understand the results.

Take a look at `unstarted.txt` and let me know what you would like to see under any and all topics. To ensure suggestions do not simply get lost I would appreciate reviewers raising issues. A link to the tracker is included in all notebooks.
