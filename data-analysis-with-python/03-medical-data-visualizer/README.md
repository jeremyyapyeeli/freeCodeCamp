## Project Instructions

In this project, you will visualize and make calculations from medical examination data using `matplotlib`, `seaborn`, and `pandas`. The dataset values were collected during medical examinations.

## Data Description
The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

Dataset: `medical_examination.csv`

|                    Feature                    |    Variable Type    |   Variable  |                    Value Type                    |
|:---------------------------------------------:|:-------------------:|:-----------:|:------------------------------------------------:|
|                      Age                      |  Objective Feature  |     `age`     |                    int (days)                    |
|                     Height                    |  Objective Feature  |    `height`   |                     int (cm)                     |
|                     Weight                    |  Objective Feature  |    `weight`   |                    float (kg)                    |
|                     Gender                    |  Objective Feature  |    `gender`   |                 categorical code                 |
|            Systolic blood pressure            | Examination Feature |    `ap_hi`    |                        int                       |
|            Diastolic blood pressure           | Examination Feature |    `ap_lo`    |                        int                       |
|                  Cholesterol                  | Examination Feature | `cholesterol` | 1: normal, 2: above normal, 3: well above normal |
|                    Glucose                    | Examination Feature |     `gluc`    | 1: normal, 2: above normal, 3: well above normal |
|                    Smoking                    |  Subjective Feature |    `smoke`    |                      binary                      |
|                 Alcohol intake                |  Subjective Feature |     `alco`    |                      binary                      |
|               Physical activity               |  Subjective Feature |    `active`   |                      binary                      |
| Presence or absence of cardiovascular disease |   Target Variable   |    `cardio`   |                      binary                      |

## Tasks

Use the data to complete the following tasks:

- Add an `overweight` column to the data.
  - To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters.
  - If that value is > 25 then the person is overweight. Use the value `0` for NOT overweight and the value `1` for overweight.
- Normalize the data by making 0 always good and 1 always bad.
  - If the value of `cholesterol` or `gluc` is `1`, make the value `0`. If the value is more than `1`, make the value `1`.
- Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot(). The dataset should be split by `cardio` so there is one chart for each cardio value. The chart should look like this:
![catplot](https://user-images.githubusercontent.com/88024785/229280506-1a5c9717-bbd6-412b-a349-28066df2fa99.png)
- Clean the data. Filter out the following patient segments that represent incorrect data:
  - diastolic pressure is higher than systolic (Keep the correct data with (df[`ap_lo`] <= df[`ap_hi`]))
  - height is less than the 2.5th percentile (Keep the correct data with (df[`height`] >= df[`height`].quantile(0.025)))
  - height is more than the 97.5th percentile
  - weight is less than the 2.5th percentile
  - weight is more than the 97.5th percentile
- Create a correlation matrix using the dataset.
  - Plot the correlation matrix using seaborn's `heatmap()`.
  - Mask the upper triangle.
  - The chart should look like this:
  ![heatmap](https://user-images.githubusercontent.com/88024785/229280765-01ee8b03-b08f-4b5c-a9df-dc56ce2cf268.png)


## Libraries Required

- Pandas
- Seaborn
- Matplotlin
- NumPy
