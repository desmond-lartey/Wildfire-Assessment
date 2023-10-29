# Wildfire Assessment in Africa

![Wildfire Assessment Cover Photo](https://live.staticflickr.com/65535/51897707965_b7d8183592_b.jpg)

## About

The **International Programs Office of the United States Forest Service** is undertaking a comprehensive assessment of the wildland fire situation across Africa. With the increasing demand for wildland fire-related programming worldwide, it's crucial to recognize that Africa is home to the highest proportion of fire-prone ecosystems globally. These assessments aim to provide a holistic understanding of fire on the landscape, its impacts, and the trade-offs of management actions.

**[Check the Application version of the assessment here](https://wildfire-assessment.streamlit.app/)**


## Assessment Approach

The assessments will follow the **Integrated Fire Management (IFM)** approach. This approach:

- Recognizes fire as a natural and necessary ecological process in many ecosystems.
- Emphasizes the integration of various strategies and tools for effective fire management.
- Aims to minimize negative impacts while promoting positive impacts, such as ecological health and community safety.
- Categorizes IFM activities into five groups: Review and Analysis, Risk Reduction, Readiness, Response, and Recovery.


## Web Application Documentation

### Overview
The web application provides a visual analysis interface for the South Africa Wildland Fire Survey data. Users can explore the data based on different categories, questions, demographics, and chart types to gain in-depth insights into the survey responses.

### How to Use
1. **Category Selection**: On the sidebar, choose a category from the available options (e.g., Review and Analysis, Risk Reduction, etc.).
2. **Question Selection**: Based on the chosen category, select the question you want to analyze.
3. **Analysis Type**: Choose between 'correlation' to analyze the relationship between two questions or 'comparative' to analyze one question across a demographic.
   - If 'correlation' is chosen, a second question must be selected.
4. **Demographic**: Select the demographic (e.g., Race, Gender, Province, Occupation) for which you want the analysis.
5. **Chart Type**: Choose the type of chart to visualize the data (heatmap, bar, pie, or line).
6. Click the **Plot** button to visualize the data based on your selections. The `Plot` button in the sidebar, when clicked, calls the `plot_analysis` function, executing the visualization based on the user's input selections.


### Key Decisions & Algorithms
- **Data Loading**: The dataset is loaded from the provided Excel file.
- **Data Filtering**: Depending on user choices, the data is filtered to match the selected category, question(s), and demographic.
- **Correlation Analysis**: If the user chooses the correlation analysis type:
  - Data for two selected questions is merged based on 'Respondent ID'.
  - A heatmap is generated using a crosstabulation of the responses, showing how they correlate.
- **Comparative Analysis**: If the user chooses the comparative analysis type:
  - The selected question's responses are grouped by the chosen demographic.
  - A bar, pie, or line chart is generated based on the user's choice to represent the distribution of responses across the demographic.

### Data Analysis and Visualizatio
- The `plot_analysis` function is defined to handle the plotting based on user selections. 
  - For a correlation analysis, data for the two selected questions is merged based on the 'Respondent ID'. A heatmap visualizes the correlation between the two questions using a crosstabulation.
  - For a comparative analysis, data for the selected question is grouped by the selected demographic. Depending on the chosen chart type (bar, pie, or line), the relevant visualization is displayed.

### Contact & Further Information
For additional details or feedback on the application, refer to the provided contact links on the sidebar, including GitHub, Twitter, and LinkedIn. A direct link to the detailed [assessment publication](https://github.com/desmond-lartey/Wildfire-Assessment/blob/Fires/README.md) is also available for deeper insights.

## Key Findings

- Africa has the highest portion of fire-prone ecosystems in the world.
- Climate change is leading to warmer, drier conditions.
- Satellite measurements show that Africa accounts for approximately 67% of the global annual burned area.
- The impacts of these fires can be both positive and negative, affecting ecological, economic, and socio-cultural perspectives.
  
## Detailed Survey Results from South Africa (5Rs)

### Review and Analysis
- **58%** of respondents either "somewhat agree" or "strongly agree" that wildland fires have significant unwanted effects in their communities.
- In the Western Cape province, **11 out of 19 respondents** "strongly agree" regarding the unwanted impacts of wildland fires, suggesting heightened concerns in this region.
- **Demographic Insight**: Black respondents were particularly concerned about the unwanted effects of wildland fires, with 46% expressing agreement. This could reflect direct experiences or heightened awareness within this demographic.
- **Gender-based Observation**: Male respondents were more likely to "strongly agree" about the unwanted effects of wildland fires compared to their female counterparts. This might suggest that males in the survey sample have had more direct encounters or negative experiences with wildfires.

### Risk Reduction
- When considering human-originated wildfires, **arson** is highlighted by 17 respondents as a leading cause, followed closely by **negligence** (7 mentions).
- For intentionally set fires, **arson** stands out as the primary motive, cited by **41 respondents**. Other motivations include **grazing** (16 mentions) and **fuel management** (11 mentions).
- **Gender-based Observation**: Female respondents particularly highlighted "arson" as a significant concern behind intentionally set fires. This could be indicative of safety concerns or experiences that females associate with intentionally set fires.

### Readiness
- There's a diverse perception regarding personnel readiness: **29% "somewhat agree"**, but **23% "strongly disagree"** about having enough personnel to deal with wildland fires.
- **Western Cape** stands out with **7 out of 19 respondents** "strongly disagreeing" about personnel readiness, pointing to localized concerns.
- In terms of brigade training, **42 respondents "somewhat agree"** and **33 "strongly agree"** that wildland fire suppression brigades are professionally trained and equipped.
- **Demographic Insight**: It's notable that Black and Coloured respondents were more likely to "strongly agree" about the brigade's preparedness compared to White respondents. This could reflect differing perceptions based on community-level engagements or experiences with brigade responses.

### Response
- **36 respondents "strongly agree"** and an equal number "somewhat agree" that a Formal Incident Command System is used in their communities, indicating a structured response mechanism.
- However, there are regional disparities: **Western Cape** has **8 out of 19 respondents** "strongly agreeing", while provinces like **Eastern Cape** and **Gauteng** show mixed perceptions.
- **75 respondents** either "strongly agree" or "somewhat agree" that firefighters are adequately equipped, but **17 respondents** express concerns about the quality or availability of equipment.
- **Gender-based Observation**: Female respondents were slightly more optimistic about the provision of equipment to firefighters compared to males. This optimism might stem from fewer direct encounters with inadequacies or a general positive perception of local firefighting efforts.

### Recovery
- **42 respondents** either "somewhat agree" or "strongly agree" that there are restoration guidelines for ecosystems affected by wildland fires. However, **32 respondents** have concerns, either "somewhat disagreeing" or "strongly disagreeing".
- Regional data suggests potential disparities in recovery efforts. For instance, in the **Western Cape**, perceptions are mixed regarding support programs and restoration guidelines after damaging wildfires.
- **Gender-based Observation**: In the aftermath of fires, Male respondents were more likely to "strongly disagree" about the existence of effective recovery programs compared to females. This could indicate that males in the sample might have had more direct experiences with post-fire landscapes or recovery efforts and found them lacking.

## Contact Information

For more details, you can contact:

- **Louis Fleming**  
  *Program Specialist*  
  [louis.fleming@usda.gov](mailto:louis.fleming@usda.gov)

- **Beth Hahn**  
  *Southern Africa Program Manager*  
  [beth.hahn@usda.gov](mailto:beth.hahn@usda.gov)

- **Tim Murphy**  
  *Africa Disaster Management Specialist*  
  [timmurphy5000@gmail.com](mailto:timmurphy5000@gmail.com)

- **David Flores, PhD**  
  *Forest Service Rocky Mountain Research Station*  
  [david.flores2@usda.gov](mailto:david.flores2@usda.gov)


## Additional Information

The International Programs Office of the U.S. Forest Service has been providing natural resource management technical assistance in Africa for over 20 years. They have strong partnerships in 32 countries and offer various fire prevention and response activities.

## Activities Include:

- National Incident Management System (NIMS)/Incident Command System (ICS) training
- ICS position specific training
- Basic and Advanced Wildland Firefighter training
- And many more...

## Current Initiatives

- **Dem. Republic of Congo**: Fire Prevention & Response Training
- **South Africa**: Formation of the South African ICS Working Team
- **Botswana**: Training & Application of NIMS
- **Madagascar**: Wildland Firefighting Training & Equipment Support
- **Angola**: Wildland Fire Assessment
- **Ethiopia**: NIMS and ICS Training

---

_This assessment is brought to you by the **International Programs Office** of the **U.S. Forest Service**._

