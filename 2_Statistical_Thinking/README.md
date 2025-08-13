# Statistical Thinking in Data Science

## Statistics

### Overview

Statistics forms the foundation of data science, equipping practitioners with mathematical tools to collect, analyze, interpret, and present data. These tools enable data scientists to extract insights, make predictions, and support decision-making through data-driven approaches.

### Key Concepts

1. **Descriptive Statistics**: Summarizes and explores the main characteristics of datasets.

   - Data summarization
   - Measures of central tendency (mean, median, mode)
   - Measures of variability (range, variance, standard deviation)

2. **Inferential Statistics**: Facilitates predictions or generalizations about populations based on sample data.
   - Drawing inferences from samples
   - Hypothesis testing
   - Confidence intervals
   - Regression analysis and correlation

## Data

### Data Types

Data can be classified as:

- **Nominal**: Categorical data without inherent order (e.g., colors, names, gender).
- **Ordinal**: Categorical data with a defined order but unequal intervals (e.g., rankings, ratings).
- **Interval**: Numerical data with equal intervals but no true zero (e.g., temperature).
- **Ratio**: Numerical data with equal intervals and a true zero (e.g., height, weight).

### Key Terms

1. **Population**: The complete set of individuals or items of interest.

2. **Sample**: A subset of the population selected for analysis.

3. **Distribution**: Describes how values are spread within a dataset.

   ![Distribution Example](./img/1.png)

   ![Normal Distribution Example](./img/2.png)

4. **Central Tendency**: Represents the center or typical value of a dataset.

   - **Mean** (μ): The average value.

     - **Population Mean**:

       ![Population Mean Formula](./img/f_1_1.png)

       where:

       - Σ = sum of all values in the population
       - Xi = each value in the population
       - N = total number of values

     - **Sample Mean** (x-bar):

       ![Sample Mean Formula](./img/f_1_2.png)

       where:

       - Σ = sum of all values in the sample
       - Xi = each value in the sample
       - n = total number of values

   - **Median**: The middle value in an ordered dataset.

     | Students   | 1   | 2   | 3   | 4   | 5   | 6                                                          | 7   | 8   | 9   | 10  | 11  |
     | ---------- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- |
     | **Grades** | 72  | 75  | 78  | 80  | 82  | <span style="color: #ffd700; font-weight: bold;">85</span> | 88  | 90  | 92  | 94  | 96  |

     - The **median** is **85** (the 6th value).

   - **Mode**: The value(s) that occur most frequently.

     | Students   | 1   | 2   | 3   | 4   | 5                                                          | 6                                                          | 7   | 8   | 9   | 10  | 11  |
     | ---------- | --- | --- | --- | --- | ---------------------------------------------------------- | ---------------------------------------------------------- | --- | --- | --- | --- | --- |
     | **Grades** | 72  | 75  | 78  | 80  | <span style="color: #ffd700; font-weight: bold;">82</span> | <span style="color: #ffd700; font-weight: bold;">82</span> | 85  | 88  | 90  | 92  | 94  |

     - The **mode** is **82** (appears twice).

5. **Standard Deviation**: Measures the spread of data around the mean.

   - Low standard deviation: values are close to the mean.
   - High standard deviation: values are more dispersed.

   - **Population Standard Deviation**:

     ![Population Standard Deviation Formula](./img/f_2.png)

     where:

     - Σ = sum of squared deviations from the mean
     - Xi = each value in the population
     - μ = population mean
     - N = total number of values

   - **Sample Standard Deviation**:

     ![Sample Standard Deviation Formula](./img/f_3.png)

     where:

     - Σ = sum of squared deviations from the mean
     - Xi = each value in the sample
     - μ = sample mean
     - n = total number of values

   #### Empirical Rule

   The **Empirical Rule** (68-95-99.7 Rule) for normal distributions states:

   - **68%** of data falls within **1 standard deviation**
   - **95%** within **2 standard deviations**
   - **99.7%** within **3 standard deviations**

   ![Empirical Rule Illustration](./img/3.png)

   This rule helps estimate data spread and identify outliers.

6. **Variance**: The average squared deviation from the mean.

   - Low variance: values are close to the mean.
   - High variance: values are more spread out.

   - **Population Variance**:

     ![Population Variance Formula](./img/f_4_1.png)

     where:

     - Σ = sum of squared deviations from the mean
     - Xi = each value in the population
     - μ = population mean
     - N = total number of values

   - **Sample Variance**:

     ![Sample Variance Formula](./img/f_4_2.png)

     where:

     - Σ = sum of squared deviations from the mean
     - Xi = each value in the sample
     - μ = sample mean
     - n = total number of values

7. **Z-Score**: Indicates how many standard deviations a value is from the mean.

   - Z = 0: at the mean
   - Z > 0: above the mean
   - Z < 0: below the mean

   - **Population Z-Score**:

     ![Population Z-Score Formula](./img/f_5_1.png)

     where:

     - X = each value in the population
     - μ = population mean
     - N = total number of values in population

   - **Sample Z-Score**:

     ![Sample Z-Score Formula](./img/f_5_2.png)

     where:

     - X = each value in the sample
     - μ = sample mean
     - s = total number of values in sample

8. **Covariance**: Measures how two variables change together (direction, not strength).

   - Positive: variables increase together.
   - Negative: one increases as the other decreases.

   - **Population Covariance**:

     ![Population Covariance Formula](./img/f_6.png)

     where:

     - Σ = sum of products of deviations from the mean
     - Xi = each value in the population
     - x-bar = population mean
     - n = total number of values in population

   - **Sample Covariance**:

     ![Sample Covariance Formula](./img/f_7.png)

     where:

     - Σ = sum of products of deviations from the mean
     - Xi = each value in the sample
     - x-bar = sample mean
     - n = total number of values in sample

9. **Correlation**: Quantifies the strength and direction of a linear relationship.

   - Positive: variables increase together.
   - Negative: one increases as the other decreases.
   - Zero: no linear relationship.

   - **Pearson r Formula**:

     ![Pearson r Formula](./img/f_8.png)
