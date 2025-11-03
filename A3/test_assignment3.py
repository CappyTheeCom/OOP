import unittest 
import numpy.testing as np
import matplotlib.patches as mpatches
from Assignment3 import AustralianUser, AustralianFoodBase, GraphSave, UserInformation


class BaseSetup(unittest.TestCase):
    def setUp(self):
        self.male = AustralianFoodBase(53,"M",175,70,2,5,7,4,3)
        self.female = AustralianFoodBase(35,"F",165,63,1.5,3,2,4,1)
        self.child = AustralianFoodBase(15,"F",165,55,2,4,5,2,3)


class TestAustralianUser(BaseSetup):

    def test_bmi(self):
        self.assertAlmostEqual(self.male.get_userBmi, 22.86)
        self.assertAlmostEqual(self.female.get_userBmi, 23.14)
        self.assertAlmostEqual(self.child.get_userBmi, 20.2)


class TestAustralianFoodBase(BaseSetup):

    
    def test_array(self):
        base_data = self.male.__basePlot()
        user_data = self.male.__userPlot()


        expected_base = np([3,2.5,6,6,2])
        expected_user = np([2,5,7,4,3])

        np.assert_array_almost_equal(expected_base,base_data)
        np.assert_array_almost_equal(expected_user,user_data)


    def test_line(self):
        figure = self.male.plotFoodIntakeLine()
        ax = figure.axes[0]
        line = ax.get_lines()

        base_y = line[0].get_ydata()
        user_y = line[1].get_ydata()

        user_data = np.array([2, 5, 7, 4, 3])
        base_data = self.basePlot()

        np.assert_array_almost_equal(base_y, base_data)
        np.assert_array_almost_equal(user_y, user_data)




    def test_barplot(self):
        figure = self.male.plotFoodIntakeBar()
        ax = figure.axes[0]

        bars = [patch for patch in ax.patches if isinstance(patch, mpatches.Rectangle)]

        bar_heights = [bar.get_height() for bar in bars]

        expected_base = [3, 2.5, 6, 6, 2]
        expected_user = [2, 5, 7, 4, 3]

        # Bars are grouped side-by-side, so even index bars are base, odd index bars are user data (adjust if needed)
        base_heights = bar_heights[0::2]
        user_heights = bar_heights[1::2]
        np.assert_array_almost_equal(base_heights, expected_base)
        np.assert_array_almost_equal(user_heights, expected_user)




    def test_pie(self):
        figure = self.male.plotFoodIntakePie()
        axes = figure.axes

        # Access both pie charts (recommended intake and user intake)
        pie1 = axes[0]
        pie2 = axes[1]

        # The wedges in a pie are stored as patches
        wedges1 = pie1.patches
        wedges2 = pie2.patches

        # Extract sizes (values) from the pie chart wedges
        sizes1 = [wedge.r for wedge in wedges1]  # radius is same; so instead, get fraction from theta1-theta2
        sizes1 = [wedge.theta2 - wedge.theta1 for wedge in wedges1]

        sizes2 = [wedge.theta2 - wedge.theta1 for wedge in wedges2]

        # Normalize sizes back to sum to 1 to compare proportions
        norm1 = [size / sum(sizes1) for size in sizes1]
        norm2 = [size / sum(sizes2) for size in sizes2]

        # Expected proportions (base data and user data normalized)
        base = [3, 2.5, 6, 6, 2]
        user = [2, 5, 7, 4, 3]

        base_prop = [x / sum(base) for x in base]
        user_prop = [x / sum(user) for x in user]

        # Use numpy testing for approximate equality
    
        np.assert_almost_equal(norm1, base_prop, decimal=2)
        np.assert_almost_equal(norm2, user_prop, decimal=2)

    
    def test_scatterplot(self):
        figure = self.male.plotFoodIntakeScatter()
        ax = figure.axes[0]

        # Scatter points are in ax.collections (each scatter plot is a PathCollection)
        collections = ax.collections
        # There should be two scatter plots: recommended intake and user intake
        scatter1 = collections[0]
        scatter2 = collections[1]

        # Get the offsets (x,y coordinates) of scatter points
        xy1 = scatter1.get_offsets().data
        xy2 = scatter2.get_offsets().data

        # Expected x values (food labels as numbers), convert food labels to positions if needed
        expected_x = np.arange(5)  # Assuming indices 0 to 4 for 5 food types

        # Expected y values for recommended intake and user intake
        expected_y1 = np.array([3, 2.5, 6, 6, 2])
        expected_y2 = np.array([2, 5, 7, 4, 3])

        # Assert x-coordinates are as expected
        np.assert_array_equal(xy1[:, 0], expected_x)
        np.assert_array_equal(xy2[:, 0], expected_x)

        # Assert y-coordinates match the expected daily servings
        np.assert_array_almost_equal(xy1[:, 1], expected_y1)
        np.assert_array_almost_equal(xy2[:, 1], expected_y2)


    def test_bmi_plot(self):
        figure = self.male.plotFoodIntakeBMI()
        ax = figure.axes[0]

        # Check if there's an axvline corresponding to user's BMI
        lines = ax.get_lines()
        # There should be a vertical line for user BMI (typically one line here)
        user_bmi_lines = [line for line in lines if line.get_label().startswith("Your bmi")]

        # Assert that user bmi line exists
        self.assertTrue(len(user_bmi_lines) == 1)

        # Verify the x-position of the vertical line matches user's BMI approximately
        user_bmi_line = user_bmi_lines[0]
        user_bmi_x = user_bmi_line.get_xdata()[0]  # Vertical line's x position

        expected_bmi = self.male.get_userBmi

        # Floating point approximate equality
        self.assertAlmostEqual(user_bmi_x, expected_bmi, places=2)

        # Optionally, check the bar ranges labels
        bars = [bar for bar in ax.containers[0]] if ax.containers else []
        self.assertTrue(len(bars) > 0)  # Bars representing the BMI ranges exist






if __name__ == "__main__":
    unittest.main()