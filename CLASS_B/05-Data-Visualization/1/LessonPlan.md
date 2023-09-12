## 5.1: Introduction to Matplotlib

### Overview

Today's class will introduce the students to the basics of [Matplotlib](http://Matplotlib.org/), one of the most popular Python plotting libraries in use today. This lesson plan focuses on how to import the Matplotlib library and use its core PyPlot module to design and customize line, bar, and pie charts as well as scatter plots. Today will also serve as a refresher of data visualizations, which were introduced in Unit 1.

### Class Objectives

* By the end of today's class, the students will be able to:

* Use Matplotlib's PyPlot interface.

* Create line, bar, and pie charts as well as scatter plots.

* Change the appearance of their plots.

* Identify basic plot configuration options, such as `xlim` and `ylim`.

---

### Instructor Notes

In this module, we introduce the `matplotlib` library. This curriculum has been tested with Python 3.10, but updates to packages and variances in student machines can still cause conflicts to occur. If a student has an error that you believe to be related to Python 3.10, at your discretion you can instruct them to create a new environment using a different Python version. If you believe that an update has introduced a bug at a curriculum level, attempt to find a suitable workaround for the moment and submit a report using the Boot Camp Feedback Form.

An important note on potential errors that the Matplotlib library can cause:

* `%matplotlib notebook` is used in multiple activities. It not only makes a plot interactive, but it also allows it to be updated after the initial plot. If students encounter any weirdness during the activities, check that they are using this line before importing the plotting libraries.

The solutions to most of today's activities are fairly simple. For each exercise, present the expected output, briefly discuss the code used to generate it, and share the final image&mdash; but withhold the example code until the activity review.

* This will encourage the students to develop the habit of exploring the Matplotlib documentation. Reading [examples](http://Matplotlib.org/examples/index.html) is an important part of the process for developing plots with the library, so it’s important that students get accustomed to this workflow.

---

### Class Slides

The slides for this lesson can be viewed on Google Drive here: [Lesson 5.1 Slides](https://docs.google.com/presentation/d/1HACyjjB7UnM3kx-hAuhezMkL4LTqB7weE56BbosdLig/edit?usp=sharing).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit).

**Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

---

### Time Tracker

| Start Time | Number | Activity                                           | Duration |
| ---------- | ------ | -------------------------------------------------- | -------- |
| 6:30 PM    | 1      | Instructor Do: Introduction to Class               | 0:05     |
| 6:35 PM    | 2      | Instructor Do: Introduction to Matplotlib          | 0:10     |
| 6:45 PM    | 3      | Students Do: New Jersey Weather Line Plots         | 0:15     |
| 7:00 PM    | 4      | Review: New Jersey Weather Line Plots              | 0:05     |
| 7:05 PM    | 5      | Instructor Do: Configuring Line Plots              | 0:05     |
| 7:10 PM    | 6      | Students Do: Legendary Temperature                 | 0:15     |
| 7:25 PM    | 7      | Review: Legendary Temperature                      | 0:05     |
| 7:30 PM    | 8      | Instructor Do: Aesthetics                          | 0:05     |
| 7:35 PM    | 9      | Students Do: Coaster Speed: Styling Line Plots     | 0:10     |
| 7:45 PM    | 10     | Review: Coaster Speed - Styling Line Plots         | 0:05     |
| 7:50 PM    | 11     | BREAK                                              | 0:15     |
| 8:05 PM    | 12     | Instructor Do: Different Plots                     | 0:05     |
| 8:10 PM    | 13     | Instructor Do: Bar Charts                          | 0:05     |
| 8:15 PM    | 14     | Students Do: Cars Bar Chart                        | 0:10     |
| 8:25 PM    | 15     | Review: Cars Bar Chart                             | 0:05     |
| 8:30 PM    | 16     | Instructor Do: Pie Charts                          | 0:05     |
| 8:35 PM    | 17     | Students Do: Pies Pie Chart                        | 0:10     |
| 8:45 PM    | 18     | Review: Pies Pie Chart                             | 0:05     |
| 8:50 PM    | 19     | Instructor Do: Scatter Plots                       | 0:05     |
| 8:55 PM    | 20     | Students Do: Scatter Py                            | 0:10     |
| 9:05 PM    | 21     | Review Scatter Py                                  | 0:05     |
| 9:10 PM    | 22     | Students Do: Average Rainfall with Pandas          | 0:15     |
| 9:25 PM    | 23     | Review: Average Rainfall with Pandas               | 0:05     |
| 9:30 PM    |        | END                                                |          |

---

### 1. Instructor Do: Introduction to Class (5 min)

Open the slideshow as you cover the following talking points:

* This week, we will be learning how to plot and analyze our datasets using Python.

* Today's class will introduce students to Matplotlib, one of the most popular Python charting libraries in use today.

* In particular, we will familiarize ourselves with the basics of a module named PyPlot, which we can use to quickly create simple charts.

---

### 2. Instructor Do: Introduction to Matplotlib (10 min)

**Corresponding Activity:** [01-Ins_BasicLineGraphs](Activities/01-Ins_BasicLineGraphs/)

Use the next few slides to accompany the beginning of this demonstration.

Open and run the solved exponential chart file in Jupyter Notebook, and describe how PyPlot can be used to create an exponential line plot. Make sure to cover the following talking points:

* For many of our Python activities, we will generate our data using the NumPy library. The NumPy library contains many built-in methods to generate and manipulate simple or complex data types.

* `np.arange(start, end, step)` creates a NumPy array of numbers from `start` to `end`, where each number in the array is a `step` away from the next one.

* A NumPy array is similar to a Python list, but they are not the same thing. A Python list can contain elements of various data types. In contrast, a NumPy array must contain only a single data type, which allows for faster computation and more efficient storage.

* The `e_x` list is created by using a list comprehension, which allows lists to be created using mathematical formulas. For example, the list comprehension in this example takes values from the `x_axis` list one at a time, finds the exponent, and stores the response within a list, as captured in the following image:

    ![NumPy and List Comprehensions.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-01-IntroToMatPlot_Lists.png)

* Matplotlib allows users to generate plots by setting one list or array as the x-axis and another as the y-axis. It’s as simple as calling `plt.plot()`, passing those 2 lists through as parameters, and then calling `plt.show()` to print the chart to the screen.

* Matplotlib handles the details of printing charts to the screen, but the programmer has full control over each stage of the drawing process if necessary. By using `plt.xlabel()` and `plt.ylabel()`, for example, users can easily add axis titles to their charts, as captured in the following image:

    ![Drawing a Line Chart.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-01-IntroToMatPlot_MakeChart.png)

Open and run the solved sin and cos file in Jupyter Notebook, and describe how PyPlot can be used to create a plot with multiple lines. Make sure to cover the following talking points:

* `np.arange()`, `np.sin()`, and `np.cos()` are all being used to create the lists for the application's charts.

* To chart multiple lines on the same chart, simply call `plt.plot()` two times and provide PyPlot with different values, as captured in the following image:

    ![Sin and Cos.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-01-IntroToMatPlot_SinCos.png)

* Although this plot is very simple, it introduces all of the key tools for building more visually interesting plots in the future.

Remind the students that data visualizations have value beyond aesthetics. Trends and insights buried within complex datasets are often clearest when the data is visualized in some way.

Open the [Bay Area Weather blog post](https://ermlab.com/en/blog/data-science/pandas-weather-data-visualization-tutorial/), or just the [image](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-01-temperature.png), and point out that the trend that each city follows is clear in the graphic but may _not_ be obvious in a table.

The following image captures the mean temperature trend (Fahrenheit) in Bay Area cities.

    ![Bay Area Weather screenshot.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-01-temperature.png)

---

### 3. Students Do: New Jersey Weather Line Plots (15 min)

**Corresponding Activity:** [02-Stu_NJTemp-LinePlots](Activities/02-Stu_NJTemp-LinePlots/)

Send the unsolved file and the instructions to students.

In this activity, the students will create a series of line plots using temperature data from New Jersey.

Open solved file in Jupyter notebook and run and discuss the output to give the students an idea of the application’s end results.

You may choose to continue the slideshow to accompany this activity.

---

### 4. Review: New Jersey Weather Line Plots (5 min)

**Corresponding Activity:** [02-Stu_NJTemp-LinePlots](Activities/02-Stu_NJTemp-LinePlots/)

Open the solved file within the Jupyter notebook, and go through the code line by line with the class, answering whatever questions they may have.

* A list of numbers ranging from 1 to 12 is created using `np.arange(1,13,1)`. The parameters passed tell NumPy to start at 1 and finish before 13, and that each value should be 1 greater than the last.

* To create the Fahrenheit chart, pass the `x_axis` and `points` lists into `plt.plot()` and then run `plt.show()`, as captured in the following image:

    ![Fahrenheit Plot.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-02-NJTemp_Fahrenheit.png)

* To convert the values within the points list to Celsius, use a list comprehension where each value in the initial list is passed through the formula (F – 32) * 0.56, as captured in the following image:

    ![Celsius Plot](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-02-NJTemp_Celsius.png)

* To include both lines on a single chart, simply run the code for drawing both of the charts within the same cell, and then use the `plt.show()` method.

---

### 5. Instructor Do: Configuring Line Plots (5 min)

**Corresponding Activity:** [03-Ins_ConfiguringLinePlots](Activities/03-Ins_ConfiguringLinePlots/)

Use the next few slides to accompany the beginning of this demonstration as you cover the following talking points:

* Matplotlib's basic line plots are rather bland.

* Matplotlib offers considerable control over the details of our plots' appearances.

* The easiest way to change how things look in Matplotlib is to use **keyword arguments** to configure the behavior of `plot`.

Send out the updated sine and cosine example, and open the code within Jupyter Notebook. Explain the following:

* Although not very different aesthetically, this new version of the sin/cos plot does introduce some additional components.

* `plt.hlines()` is used to draw a horizontal line. This method takes in 3 parameters: the _y_ value across which the line will be drawn, the _x_ value where the line will start, and the _x_ value where the line will end.

* The transparency of the horizontal line can also be set using the `alpha=` keyword and passing a number between 0 and 1, as captured in the following image. This setting is possible with most Matplotlib plotting functions.

    ![Horizontal Line.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-03-LineConfiguration_HLines.png)

Direct attention to the lines being drawn, and stored in the variables `sin_handle,` and `cos_handle,` and explain:

* `pyplot.plot` returns a list of the lines that were added to the plot.

* This bit of code is using argument unpacking to select only the first line from that list of lines.

* So, calling the `sine_handle` is a reference to the line's object.

* `plt.plot()` can take in more parameters than just the **x** and **y** values for the line being charted. For example, the markers for a plot can be set using `marker=`, the color of a plot can be set using `color=`, and the label for a line can be set using `label=`, as captured in the following image:

    ![Tupled Plots.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-03-LineConfiguration_Tupled.png)

* The `plt.legend()` method allows the user to create a legend for their chart. The `loc` argument is used to set the location of the legend on the chart.

* Although the `plt.show()` command hasn’t changed, a new line called `plt.savefig()` has been added, which will save a version of the chart to an external file. Simply pass the desired file path as a parameter to save the image, as captured in the following image:

    ![Adding Legends.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-03-LineConfiguration_Legend.png)

Explain that the different [markers](http://Matplotlib.org/api/markers_api.html) and [colors](http://Matplotlib.org/api/colors_api.html) are available in the documentation, which the students are encouraged to peruse when building their plots.

---

### 6. Students Do: Legendary Temperature (15 min)

**Corresponding Activity:** [04-Stu_LegendaryTemperature](Activities/04-Stu_LegendaryTemperature/)

Send the unsolved file and the README to the students and go over the instructions.

* In this activity, the students will edit the line plots they created earlier so that these charts are more visually interesting.

Encourage the students to play with additional configuration options beyond those specified in the activity. Send out links to the Matplotlib API so that the students can play around with the library when they finish the activity.

You may choose to use the next few slides to accompany this activity. Otherwise, show and describe to the students the chart that they will be attempting to create, which is captured in the following image:

![avg_temp.png](Activities/04-Stu_LegendaryTemperature/Images/avg_temp.png)

---

### 7. Review: Legendary Temperature (5 min)

**Corresponding Activity:** [04-Stu_LegendaryTemperature](Activities/04-Stu_LegendaryTemperature/)

Open the solved file within Jupyter Notebook, and go through the code line by line with the class, answering whatever questions they may have. Make sure to cover the following talking points:

* Both `fahrenheit` and `celsius` are followed by commas to set them as tuples. This is crucial because `plt.legend()` expects to receive tuples within its `handles` parameter and would otherwise return an error.

* The `loc` parameter of `plt.legend()` has been set to "best" within this application. This allows Matplotlib to decide where to place the legend so that it does not get in the way.

```python
# Create a handle for each plot
fahrenheit, = plt.plot(x_axis, points_F, marker="+",color="blue", linewidth=1, label="Fahrenheit")
celsius, = plt.plot(x_axis, points_C, marker="s", color="Red", linewidth=1, label="Celsius")
```

```python
# Set our legend to where the chart thinks is best
plt.legend(handles=[fahrenheit, celsius], loc="best")
```

Check with the class to see what interesting formatting options they uncovered during this activity, and ask a few students to explain their code to the class.

---

### 8. Instructor Do: Aesthetics (5 min)

**Corresponding Activity:** [05-Ins_Aesthetics](Activities/05-Ins_Aesthetics/)

Continue the slideshow during the beginning of this demonstration while covering the following talking points:

* The best plots, like the best code, are easy to read. Emphasize that data visualizations do not need to be artistic; they need to be easy to understand.

* Some ways to improve readability include:

    * Adding labels to the x-axis

    * Adding labels to the y-axis

    * Adding titles to plots

    * Limiting the extent of the plot to bound the plot's data points

* On a case-by-case basis, adding grids can also be helpful.

* Adding labels ensures that the graphic remains honest and easy to understand, even in cases where the visualization is complicated, such as with [Sankey diagrams](https://en.wikipedia.org/wiki/Sankey_diagram).

* Limiting the extent of the plot maximizes the [data-to-ink ratio](https://infovis-wiki.net/wiki/Data-Ink_Ratio) and constrains the plot so it displays only relevant information.

Open the aesthetics [output](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-05-Aesthetics_Output.png). Explain the following:

* This plot is not yet very visually interesting but is more readable than the previous plots as a result of the labels and changes being made to the x-axis.

* `plt.xlabel()`, `plt.ylabel()`, and `plt.title()` are fairly self-explanatory. Simply pass a string into them as a parameter, and the labels and title will be drawn onto the chart.

* `plt.xlim()` and `plt.ylim()` are used to set where the axes for the chart should begin and end. By default, Matplotlib creates charts with lots of empty space, which we can address with these methods.

* `plt.grid()` is also fairly self-explanatory: it adds gridlines to the chart, as captured in the following image:

    ![An updated sine and cosine plot.](Activities/05-Ins_Aesthetics/Images/sin_cos_with_markers.png)

---

### 9. Students Do: Coaster Speed: Styling Line Plots (10 min)

**Corresponding Activity:** [06-Stu_RollerCoaster-StylingLinePlots](Activities/06-Stu_RollerCoaster-StylingLinePlots/)

Send out the unsolved file and the README to students.

In this activity, the students will create a line chart that graphs the speed of a roller coaster over time. They will then style the chart and add some aesthetics to it.

You may choose to utlize the next few slides to accompany this activity. Otherwise, show and describe to the students the chart that they will be attempting to create, which is captured in the following image:

![Coaster Speed Chart](Activities/06-Stu_RollerCoaster-StylingLinePlots/Images/CoasterSpeed.png)

### 10. Review: Coaster Speed - Styling Line Plots (5 min)

**Corresponding Activity:** [06-Stu_RollerCoaster-StylingLinePlots](Activities/06-Stu_RollerCoaster-StylingLinePlots/)

Open the solved file within Jupyter Notebook and share the notebook file with students. Go through the code line by line with the class, answering whatever questions they may have.

Cover the following talking points as you go:

* `plt.title()`, `plt.xlabel()`, and `plt.ylabel()` are used to set the title and axis labels.

* `plt.xlim()` and `plt.ylim()` are set so that there is as little empty space as possible on the chart while still retaining its readability.

* The following images capture the code for this activity:

    ![Coaster Code.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-06-CoasterSpeed_Code_1.png)

    ![Coaster Code.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-06-CoasterSpeed_Code_2.png)

---

### 11. BREAK (15 min)

---

### 12. Instructor Do: Different Plots (5 min)

Continue the slideshow while covering the following talking points:

* Matplotlib provides a simple interface for producing more than just line plots.

* The most common charts that students will generate are line charts, bar charts, pie charts, and scatter plots.

* **Bar charts** are useful for comparing different entities.

* **Pie charts** are suitable for displaying parts of a whole&mdash;in particular, the amount each constituent contributes to a complete dataset.

* **Scatter plots** are good for displaying where points fall with respect to 2 factors.

* It's important to choose the right plot for a given dataset; the wrong choice can make a graphic less readable&mdash;or even misleading.

* Some data might lend itself to different plots; for example, it’s better to display some data in a bar chart, while other data is better off in a pie chart.

---

### 13. Instructor Do: Bar Charts (5 min)

**Corresponding Activity:** [07-Ins_BarCharts](Activities/07-Ins_BarCharts/)

Use the next few slides to cover the following talking points:

* Bar charts are particularly useful when trying to visualize data that has been counted or a single variable that has been measured multiple times.

    * Data that comes from a single variable is called **univariate**.

    * For example, the amount of rainfall per month for a given location or the results of a poll containing multiple categories could be visualized effectively using a bar chart.

* Bar charts are not very useful when comparing **bivariate** data, or data that compares two different variables.

    * For example, a dataset that compares the number of ice cream bars sold versus daily temperature would not be visualized well using a bar chart.

Ask the students to think of a few other examples of univariate datasets that would be visualized well with bar charts.

Open the solved file in Jupyter Notebook. Cover the following talking points:

* When dealing with bar charts, it is necessary to provide the heights of each bar within an array.

* The x-axis will also be an array whose length must equal that of the list of heights.

* Instead of using `plt.plot()`, bar charts are drawn using `plt.bar()`.

* The `align` parameter for `plt.bar()` centers the data on each tick, as captured in the following image:

    ![Axes and Plotting.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-07-BarCharts_Plot.png)

* Another aesthetic challenge with bar charts is aligning the tick locations on the x-axis and providing textual, rather than numeric, labels.

* The `tick_locations` list created within this application places a tick for each value in the `x_axis`, as captured in the following image:

    ![Ticks.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-07-BarCharts_Ticks.png)

* `plt.xlim()` and `plt.ylim()` are set so that there is some space between the bars and the edge of the chart. This makes the chart look better aesthetically.

---

### 14. Students Do: Cars Bar Chart (10 min)

**Corresponding Activity:** [08-Stu_PyBars](Activities/08-Stu_PyBars/)

Send the unsolved file and the README to the students and go over the instructions.

In this activity, the students will create a bar chart that visualizes the density of commuting cars per 1,000 population aged 16 and over in major U.S. cities.

You may choose to use the slideshow to accompany this activity. Otherwise, show and describe to the students the chart that they will be attempting to create, which is captured in the following image:

![PyBars Output.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-08-PyBars_Output.png)

---

### 15. Review: Cars Bar Chart (5 min)

**Corresponding Activity:** [08-Stu_PyBars](Activities/08-Stu_PyBars/)

Open the solved file within the Jupyter notebook, and go through the code line by line with the class, answering whatever questions they may have.

Pay particular attention to the ticks set for the bar chart.

Explain that `plt.xlim()` is set to go from -0.75 to the length of the x-axis minus 0.25 so that there is a degree of space between the leftmost bar and the edge of the chart.

    ```python
    # Create a bar chart based on the above data
    plt.bar(x_axis, cars_in_cities, color="b", align="center")

    # Create the ticks for our bar chart's x axis
    tick_locations = [value for value in x_axis]
    plt.xticks(tick_locations, cities)

    # Set the limits of the x axis
    plt.xlim(-0.75, len(x_axis)-0.25)

    # Set the limits of the y axis
    plt.ylim(0, max(cars_in_cities)+10)
    ```

Explain that the process for tweaking aesthetic parameters can be time-consuming, so we always want to save the Python code that we use to generate figures. A notebook or script makes it easier to recreate plots in the future.

Data Source:

* [2019 ACS 1-Year Estimates, DEMOGRAPHIC AND HOUSING ESTIMATES](https://data.census.gov/cedsci/table?q=population%20of%20san%20francisco%20city%202019&t=001%20-%20Total%20population&g=1600000US0667000,2255000,3137000,3915000,4055000,4261000,5553000&tid=ACSDP1Y2019.DP05)

* [2019 ACS 1-Year Estimates, AGGREGATE NUMBER OF VEHICLES (CAR, TRUCK, OR VAN) USED IN COMMUTING BY WORKERS 16 YEARS AND OVER BY SEX](https://data.census.gov/cedsci/table?q=cars%20in%20cities&t=Populations%20and%20People&g=1600000US0667000,2255000,3137000,3915000,4055000,4261000,5553000_310XX00US14500&tid=ACSDT1Y2019.B08015)

---

### 16. Instructor Do: Pie Charts (5 min)

**Corresponding Activity:** [09-Ins_PieCharts](Activities/09-Ins_PieCharts/)

Use the next few slides to cover the following talking points:

* Pie charts are particularly useful when trying to visualize percentage, fractional, or proportional data.

    * Essentially, pie charts are great at visualizing "piece of the pie" data.

    * For example, the proportion of Democratic voters versus Republicans versus independents would be effectively visualized using a pie chart.

    * The fewer the number of categories, the greater the effectiveness of the pie chart.

    * Pie charts are less effective with datasets that have more than approximately 10 categories. Similar to bar charts, pie charts are only effective at describing univariate data.

    * When there are too many categories, pie charts become too busy and lose their effectiveness.

* Due to overlapping functionality, bar charts can also be used to visualize the same data used to generate a pie chart.

    * However, pie charts can be far more dramatic and effective at demonstrating a fractional relationship.

    * When in doubt, it is always safer to use a bar chart visualization rather than overcrowding a pie chart.

Ask the students to think of a few other examples of univariate datasets that would be visualized well with pie charts.

Open the solved file and cover the following talking points:

* The sizes of each wedge are passed into `plt.pie()` as an array. Lists containing the labels for each wedge and the colors for each wedge are also passed in.

* The pie chart allows the user to choose a wedge to "explode," using the `explode` option. This will separate one wedge from the rest so that it is easier to examine.

* Inside of the `plt.pie()` method, a parameter of `autopc="%1.1%%"` is being passed. This will automatically convert the values we pass into percentages with one decimal place.

* The following image captures the code for this demonstration:

```python
# Add labels for the sections of our pie chart
labels = ["Humans", "Smurfs", "Hobbits", "Ninjas"]

# Add the values of each section of the pie chart
sizes = [220, 95, 80, 100]

# Add the colors of each section of the pie chart
colors = ["red", "orange", "lightcoral", "lightskyblue"]

# Tell Matplotlib to separate the "Humans" section from the others
explode = (0.1, 0, 0, 0)

# Create the pie chart based upon the values above
# Automatically find the percentages of each part of the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
```

Matplotlib does not constrain pie charts to be circular&mdash;by default, they will be ovals if the window the plot lives in is not a square. Passing in `plt.axis("equal")` will make the plot circular, as in the following image:

![Pie Axis.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-09-pie02.png)

Explain that there are additional configuration options for improving the appearance of Matplotlib's pie charts, should students desire to learn more.

---

### 17. Students Do: Pies Pie Chart (10 min)

**Corresponding Activity:** [10-Stu_PyPies](Activities/10-Stu_PyPies/)

Send the unsolved file and the README to the students and go over the instructions.

In this activity, the students will create a pie chart that visualizes pie flavor preferences in the United States.

You may choose to use the slideshow to accompany this activity. Otherwise, show and describe to the students the chart that they will be attempting to create, which is captured in the following image:

  ![PyPies Output.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-10-PyPies_Output.png)

---

### 18. Review: Pies Pie Chart (5 min)

**Corresponding Activity:** [10-Stu_PyPies](Activities/10-Stu_PyPies/)

Open the solved file in the Jupyter notebook, and go through the code line by line with the class, answering whatever questions they may have. Cover the following talking points:

* One thing that makes this activity challenging is knowing what colors are available. Share the following link with students, so they can find a [list of colors](https://matplotlib.org/stable/gallery/color/named_colors.html).

* Pie charts are easy to make because editing a chart only requires editing the values, as captured in the following image. Otherwise, the styling and aesthetics are fairly uniform across charts.

    ![Py Pies Plotting.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-10-PyPies_Plotting.png)

---

### 19. Instructor Do: Scatter Plots (5 min)

**Corresponding Activity:** [11-Ins_ScatterPlots](Activities/11-Ins_ScatterPlots/)

Using the slideshow, cover the following talking points:

* Scatter plots are extremely useful when visualizing **bivariate** data, or data that relates two variables.

    * Any data that we can plot on the x- and y-axis from two lists is considered bivariate data.

    * We can describe bivariate data as “something versus something else.”

    * For example, if we were to plot the amount of ice cream sold per day versus daily temperature, this bivariate data would be best visualized using a scatter plot.

* Scatter plots are one of the cleanest and most effective charts for visualizing large datasets, or those with 500 values or more.

* Scatter plots are frequently used to visualize clusters in a dataset.

* Scatter plots are not great for visualizing continuous measurements.

    * The most common continuous data is data measured over time, or **time series** data.

* When data is continuous, we often want to be able to interpolate between measurements. In this case, scatter plots may not be as effective as line plots.

    * This is especially true if the dataset is small&mdash;the smaller the dataset, the more likely the audience will want to read between the data points.

* In most cases, datasets will be large enough to effectively use scatter plots.

Finally, open the solved file and cover the following talking points:

* This plot uses random data just so the class can avoid cluttering the example with Pandas cleanup&mdash;later activities will provide more realistic context.

* Generating scatter plots requires the simplest set of methods of all the charts we’ve covered so far. Simply take in two sets of data and pass them into `plt.scatter()`.

* The code can change the size of each dot by passing the `s=<LIST>` parameter. In this case, the values stored within `x_axis` will determine the size of a dot.

* The following image captures the code for this demonstration:

    ![Scatter Plots.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-11-scatter.png)

---

### 20. Students Do: Scatter Py (10 min)

**Corresponding Activity:** [12-Stu_ScatterPy](Activities/12-Stu_ScatterPy/)

Send the unsolved file and the README to students and go over the instructions.

In this activity, the students will create a scatter plot that visualizes ice cream sales in comparison to temperature increases.

You may choose to use the slideshow to accompany this activity. Otherwise, show and describe to the students the chart that they will be attempting to create, which is captured in the following image:

  ![PyScatter Output.](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-12-ScatterPy_Output.png)

---

### 21. Review Scatter Py (5 min)

**Corresponding Activity:** [12-Stu_ScatterPy](Activities/12-Stu_ScatterPy/)

Open the solved file within the Jupyter notebook, and go through the code line by line with the class, answering whatever questions they may have. Be sure to point out the following:

* To make the scatter plot easier to read, we customize the color and border of the markers using the `facecolors` and `edgecolors` arguments.

    * If the students are curious about the different color and shape options, direct them to the [`matplotlib` quick start documentation](https://matplotlib.org/3.7.1/tutorials/introductory/quick_start.html).

* Often, with scatter plot data, values will be tightly clustered, or there will be large ranges of white space between values. It is a good idea to set the `plt.xlim()` and `plt.ylim()` functions to ensure that our figures are clear and readable.

---

### 22. Students Do: Average Rainfall with Pandas (15 min)

**Corresponding Activity:** [13-Stu_AvgRain-BarChartsWithPandas](Activities/13-Stu_AvgRain-BarChartsWithPandas/)

Send the unsolved file and the README to students and go over the instructions.

In this activity, the students will import data from a CSV file to create a bar chart that plots the average rainfall in different states. Students will need to think outside the box and try using Pandas alongside Matplotlib.

You may choose to use the slideshow to accompany this activity. Otherwise, show and describe to the students the chart that they will be attempting to create, which is captured in the following image:

  ![Average Rain Output](https://static.bc-edx.com/data/dl-1-2/m5/lessons/1/img/5-1-13-AverageRain_Output.png)

Data Source: M. Palecki, I. Durre, J. Lawrimore, and S. Applequist, 2021: U.S. Annual/Seasonal Climate Normals (2006-2020) [National Centers for Environmental Information, National Oceanic and Atmospheric Administration](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc%3AC01623/html). N.B. This data was downloaded, combined, reduced, and calculated in Pandas.

---

### 23. Review: Average Rainfall with Pandas (5 min)

**Corresponding Activity:** [13-Stu_AvgRain-BarChartsWithPandas](Activities/13-Stu_AvgRain-BarChartsWithPandas/)

Open the solved file within the Jupyter notebook, and go through the code line by line with the class, answering whatever questions they may have.

Point out to the students that this figure is very busy. A bar plot of this size may be good for exploratory analysis, but it won’t be appropriate for presentation or reporting.

Explain that in data analytics, it is very important to create figures that truthfully summarize the data. However, if a figure takes too long to understand, it will lose its effectiveness.

Explain that as we progress further into the course, we will learn methods to identify trends and calculate statistics on larger datasets. This will enable us to create more powerful tables and figures that tell the same story without the visual clutter.

---

### End Class

___

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
