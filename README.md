=======
# Tech-Monies

This repo contains file for expected salary of Tech Jobs


 Knowing what your value is in the job market prevents you from underselling yourself. A lot of people are being underpaid because they sold themselves short, especially people venturing into a new field. People going into tech are not an exception. The job market of techies is projected to grow exponentially and knowing your worth places you in an advantageous position

The project has been divided into tasks that involve:
Data Sourcing and Scrapping,
Data cleaning,
Model development, and 
Model deployment
    
   

# Data Scrapping

Current Status of Script:

### Output Columns
#### Main Columns:

| Information | Dataset Column | Available | Comment |
|---|---|---|---|
| Jobs title | `title` | ✅ | Posted Job Title |
| Description | `jobDesc` | ✅ | All details available in JD. Use `print` statement to get a formatted output |
| Salary | `salary` | ❌ | will be extracted from `salaryDesc` |
| Contract Type | `type` | ✅ | will be extracted from `salaryDesc` |
| Company Name | `company` | ✅ | - |
| Country | `country` | ❌ | will be extracted from `location` |
| State | `state` | ❌ | will be extracted from `location` |
| Years of Experience | `yearMinExp` | ❌ | will be extracted from `jobDesc` |
| Position | `level` | ❌ | will be extracted from `jobDesc` |
| Industry | `industry` | ❌ | will be extracted from `jobDesc` |
| Age Required | `ageCriteria` | ❌ | will be extracted from `jobDesc` |
| Skillset Required | `skills` | ❌ | will be extracted from `jobDesc` |
| Educational qualification | `eligibility` | ❌ | will be extracted from `jobDesc` | 
| Pay Frequency | `payFrequency` | ❌ | will be extracted from `jobDesc` |

---

There are some more columns available which are listed below.

#### Additional Columns:

| Information | Dataset Column | Available | Comment |
|---|---|---|---|
| Jobs ID | `jobID` | ✅ | - |
| Location | `location` | ✅ | One or more combination of city, state, country or pincode/zipcode |
| Salary Desc | `salaryDesc` | ✅ | One or more combination of salary (actual/estimated), job type, shift, etc. |
| JD link | `link` | ✅ | Link to actual Job Description provided by Indeed |
| Post Date | `postDate` | ✅ | Recency of Job Posting |
| Estimated by Indeed | `estimated` | ✅ | The salary is estimated by Indeed |

# Data Cleaning

The phase extract the needed features from the scrapped data.
| Information | Dataset Column |
|---|---|
| Jobs title | `title` |
| Salary | `salary` (both upper and lower) |
| Contract Type | `type` |
| Country | `country` |
| Years of Experience | `yearMinExp` |
| Position | `level` |
| Skillset Required | `skills` |
| Educational qualification | `eligibility` |
| Pay Frequency | `payFrequency` |


# Model Development

This phase includes the EDA and Modeling repo.

# Model Deployment
This phase include live page of the prediction for user use

The link to the live page 👉  https://ajmasih0309-tech-monies-predictionapp1-modelling-31dqnz.streamlitapp.com/
