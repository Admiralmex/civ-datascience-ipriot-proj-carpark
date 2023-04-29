# General Tips and Tricks

Provides advice and tips on common issues. Regularly updated.

## Module import errors when testing

While common, having tests and source in sibling folders can cause confusing problems.

### Assign a category to a folder in the Project tool window

1. Open the **Project** tool window (for example **View | Tool Windows | Project**).

2. Select the folder that you want to assign to a certain category.

3. Right-click it and select the desired category from Mark Directory As menu. Specifically:
   a. Mark `smartpark/` as **Sources Root**
   b. Mark `tests/` as **Test Sources Root**  

From [jetbrains](https://www.jetbrains.com/help/pycharm/configuring-project-structure.html#mark-dir-project-view)

### General solution

A known weakness of Python is how it manages imports. It is not at all intuitive (but it is not something you have to set up that often). Here's some interesting, if advanced, reading on the subject:
[Relative imports for the billionth time](https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time)