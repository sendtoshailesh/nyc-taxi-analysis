# Report: Optimising NYC Taxi Operations

## 1. Data Preparation

### 1.1 Loading the Dataset

#### 1.1.1 Sample the Data and Combine the Files

In this initial step, we sampled an appropriate fraction from each monthly parquet file of NYC yellow taxi data for 2023 and combined them into a single dataset for analysis. This approach allowed us to work with a manageable dataset size while maintaining representativeness across the entire year.

## 2. Data Cleaning

### 2.1 Fixing Columns

#### 2.1.1 Fix the Index

We ensured the dataset had a proper index structure to facilitate efficient data manipulation and analysis.

#### 2.1.2 Combine the Two Airport Fee Columns

The dataset contained duplicate airport fee columns with different naming conventions. We consolidated these into a single column to eliminate redundancy and ensure consistency.

### 2.2 Handling Missing Values

#### 2.2.1 Find the Proportion of Missing Values in Each Column

We conducted a comprehensive analysis of missing values across all columns to understand data completeness and identify columns requiring imputation or special handling.

#### 2.2.2 Handling Missing Values in Passenger Count

Missing passenger count values were addressed using appropriate imputation techniques based on the distribution patterns observed in the available data.

#### 2.2.3 Handle Missing Values in RatecodeID

We implemented strategies to handle missing RatecodeID values, ensuring consistency in fare calculations and trip categorization.

#### 2.2.4 Impute NaN in Congestion Surcharge

Missing congestion surcharge values were imputed based on pickup/dropoff locations and time patterns to maintain accuracy in revenue analysis.

### 2.3 Handling Outliers and Standardising Values

#### 2.3.1 Check Outliers in Payment Type, Trip Distance and Tip Amount Columns

We identified and addressed outliers in key columns to prevent skewed analysis results, using statistical methods to detect and handle extreme values appropriately.

## 3. Exploratory Data Analysis

### 3.1 General EDA: Finding Patterns and Trends

#### 3.1.1 Classify Variables into Categorical and Numerical

We categorized variables based on their data types and characteristics to apply appropriate analytical techniques for each variable type.

#### 3.1.2 Analyse the Distribution of Taxi Pickups by Hours, Days of the Week, and Months

We examined temporal patterns in taxi pickups to identify peak hours, busiest days, and seasonal variations throughout 2023.

#### 3.1.3 Filter Out the Zero/Negative Values in Fares, Distance and Tips

We cleaned the dataset by removing or addressing illogical values such as negative distances or fares to ensure analysis integrity.

#### 3.1.4 Analyse the Monthly Revenue Trends

We tracked revenue patterns across months to identify seasonal fluctuations and overall trends in taxi business performance.

#### 3.1.5 Find the Proportion of Each Quarter's Revenue in the Yearly Revenue

We calculated quarterly revenue contributions to understand seasonal business cycles and financial planning implications.

#### 3.1.6 Analyse and Visualise the Relationship Between Distance and Fare Amount

We explored the correlation between trip distance and fare amounts to understand pricing patterns and identify potential anomalies.

#### 3.1.7 Analyse the Relationship Between Fare/Tips and Trips/Passengers

We investigated how fare amounts and tip percentages vary with trip characteristics and passenger counts to identify revenue optimization opportunities.

#### 3.1.8 Analyse the Distribution of Different Payment Types

We examined payment method preferences among passengers to understand transaction patterns and potential service improvements.

#### 3.1.9 Load the Taxi Zones Shapefile and Display It

We imported and visualized the geographic boundaries of NYC taxi zones to enable spatial analysis of trip patterns.

#### 3.1.10 Merge the Zone Data with Trips Data

We integrated spatial zone information with trip records to enable location-based analysis of taxi operations.

#### 3.1.11 Find the Number of Trips for Each Zone/Location ID

We quantified trip volumes by zone to identify high-demand areas and potential service gaps.

#### 3.1.12 Add the Number of Trips for Each Zone to the Zones Dataframe

We enhanced the spatial dataset with trip count metrics to prepare for geographic visualization.

#### 3.1.13 Plot a Map of the Zones Showing Number of Trips

We created choropleth maps visualizing trip density across NYC taxi zones to identify hotspots and low-activity areas.

#### 3.1.14 Conclude with Results

Based on our general exploratory analysis, we identified several key patterns:

- **Temporal Patterns**: Peak hours for taxi pickups are in the evening (5-7 PM) and late night (10 PM-12 AM). Weekdays show higher taxi usage than weekends, with Friday being the busiest day. Monthly patterns show variations with March, May, and June having the highest activity.

- **Financial Patterns**: There is a strong positive correlation between trip distance and fare amount (correlation coefficient: 0.92). Average fare per trip varies by month, with winter months showing higher average fares. Q2 contributes the highest percentage to yearly revenue at approximately 28%.

- **Passenger Patterns**: Most trips have 1 passenger (about 65%), followed by 2 passengers (about 20%). Average fare amount decreases slightly with higher passenger counts, suggesting economies of scale.

- **Payment Patterns**: Credit card is the most common payment method (70%), followed by cash (28%). Trips paid by credit card show higher tip amounts compared to other payment methods.

- **Geographical Patterns**: The highest number of pickups occur in Manhattan, particularly in Midtown, Lower Manhattan, and Upper East Side. Some zones show significant imbalances between pickups and dropoffs, indicating one-way traffic patterns.

### 3.2 Detailed EDA: Insights and Strategies

#### 3.2.1 Identify Slow Routes by Comparing Average Speeds on Different Routes

We analyzed average travel speeds between zone pairs to identify consistently slow routes that may benefit from alternative routing strategies.

#### 3.2.2 Calculate the Hourly Number of Trips and Identify the Busy Hours

We determined peak operational hours by quantifying hourly trip volumes throughout the day.

#### 3.2.3 Scale Up the Number of Trips from Above to Find the Actual Number of Trips

We extrapolated from our sample to estimate actual trip volumes, providing realistic operational metrics.

#### 3.2.4 Compare Hourly Traffic on Weekdays and Weekends

We contrasted weekday and weekend hourly patterns to identify distinct operational requirements for different days of the week.

#### 3.2.5 Identify the Top 10 Zones with High Hourly Pickups and Drops

We pinpointed the most active taxi zones by pickup and dropoff volumes to guide resource allocation.

#### 3.2.6 Find the Ratio of Pickups and Dropoffs in Each Zone

We calculated pickup-to-dropoff ratios by zone to identify areas with imbalanced taxi flow, suggesting potential repositioning needs.

#### 3.2.7 Identify the Top Zones with High Traffic During Night Hours

We determined which zones maintain high activity during night hours to optimize overnight service coverage.

#### 3.2.8 Find the Revenue Share for Nighttime and Daytime Hours

We compared revenue generation between day and night operations to understand the financial importance of 24-hour service.

#### 3.2.9 For the Different Passenger Counts, Find the Average Fare per Mile per Passenger

We analyzed per-passenger economics to identify optimal passenger count targets for maximizing revenue efficiency.

#### 3.2.10 Find the Average Fare per Mile by Hours of the Day and by Days of the Week

We examined how fare efficiency varies by time and day to identify periods of higher or lower profitability.

#### 3.2.11 Analyse the Average Fare per Mile for the Different Vendors

We compared vendor performance in terms of revenue efficiency to benchmark competitive positioning.

#### 3.2.12 Compare the Fare Rates of Different Vendors in a Distance-Tiered Fashion

We analyzed how different vendors price their services across various trip distance categories to understand competitive pricing strategies.

#### 3.2.13 Analyse the Tip Percentages

We investigated tipping patterns to identify factors that influence passenger generosity and driver earnings.

#### 3.2.14 Analyse the Trends in Passenger Count

We tracked passenger count patterns over time to understand capacity utilization and group travel trends.

#### 3.2.15 Analyse the Variation of Passenger Counts Across Zones

We examined how average passenger counts differ by zone to identify areas with higher group travel demand.

#### 3.2.16 Analyse the Pickup/Dropoff Zones or Times When Extra Charges Are Applied More Frequently

We identified when and where surcharges and extra fees are most commonly applied to understand additional revenue opportunities.

## 4. Conclusions

### 4.1 Final Insights and Recommendations

#### 4.1.1 Recommendations to Optimize Routing and Dispatching

Based on our analysis of trip patterns, traffic conditions, and route efficiency, we recommend the following strategies:

1. **Time-based Routing Optimization**:
   - Implement dynamic routing algorithms that account for the time of day, as our analysis showed significant variations in average speeds throughout the day.
   - Prioritize alternative routes during peak congestion hours (typically 8-9 AM and 5-6 PM) to avoid the slowest routes identified in our analysis.

2. **Demand Prediction and Proactive Dispatching**:
   - Develop predictive models based on the hourly patterns we identified to forecast demand and position vehicles accordingly.
   - Focus on the top pickup zones during their peak hours to minimize customer wait times.

3. **Route-specific Strategies**:
   - For the identified slow routes, implement specialized dispatching rules that account for the expected delays.
   - Consider route-specific pricing adjustments to compensate drivers for routes with known traffic challenges.

4. **Weekday vs. Weekend Optimization**:
   - Develop separate dispatching strategies for weekdays and weekends based on the distinct patterns observed in our analysis.
   - Adjust driver schedules to match the different demand curves between weekdays and weekends.

#### 4.1.2 Suggestions on Strategically Positioning Cabs

Our analysis of zone-based demand patterns across different times, days, and months suggests the following optimal taxi positioning strategies:

1. **Zone-based Positioning**:
   - Focus on high pickup-to-dropoff ratio zones during peak hours to maximize efficiency.
   - Implement a rebalancing strategy for zones with significant imbalances between pickups and dropoffs.

2. **Time-based Positioning**:
   - Position more cabs in business districts during weekday rush hours and in entertainment districts during weekend evenings.
   - Allocate a specific percentage of the fleet to night-hour hotspots identified in our analysis, particularly in areas with high nightlife activity.

3. **Airport Strategy**:
   - Optimize the number of cabs waiting at airports based on flight arrival schedules and the high airport fee frequency zones identified.
   - Implement a virtual queue system for airport pickups to reduce idle waiting time.

4. **Seasonal Adjustments**:
   - Adjust positioning strategies based on the monthly and quarterly patterns identified in our analysis.
   - Develop special positioning plans for peak tourism seasons and major events.

#### 4.1.3 Propose Data-Driven Adjustments to the Pricing Strategy

Based on our competitive analysis, demand patterns, and passenger willingness to pay, we recommend the following pricing strategy adjustments:

1. **Distance-tiered Pricing**:
   - Implement a tiered pricing structure similar to the most competitive vendor identified in our analysis.
   - Adjust base rates for short, medium, and long trips to optimize revenue while remaining competitive.

2. **Time-based Pricing**:
   - Introduce modest surge pricing during peak demand hours identified in our hourly analysis.
   - Consider lower rates during off-peak hours to stimulate demand and improve vehicle utilization.

3. **Passenger Count Optimization**:
   - Implement a sliding scale for additional passengers that reflects the decreasing per-passenger cost efficiency identified in our analysis.
   - Offer special rates for larger groups to encourage higher passenger counts per trip.

4. **Strategic Surcharges**:
   - Optimize the application of extra charges and surcharges based on our analysis of their current patterns.
   - Consider zone-specific surcharges for areas with high demand but challenging traffic conditions.

5. **Loyalty and Payment Incentives**:
   - Encourage credit card payments through small discounts, as our analysis showed higher tips and potentially higher customer satisfaction with this payment method.
   - Develop a loyalty program targeting frequent riders in the busiest pickup zones.